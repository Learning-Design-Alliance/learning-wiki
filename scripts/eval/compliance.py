"""
compliance.py — robots.txt enforcement + per-domain rate limiting for the
article-fetching layer, so a "10 articles" smoke test and a future
thousand-article batch behave identically with respect to each site's stated
crawling rules instead of the limit only being "whatever the code happens to
do today."

This does NOT replace reading each source's terms of use — robots.txt only
covers automated-access mechanics (which paths, how fast), not licensing or
"which retrieval channel is actually sanctioned" (e.g. NCBI restricts
automated PMC retrieval to specific APIs regardless of what robots.txt
allows). See eval/SOURCES.md for the per-source policy notes that motivated
the choices here (why PMC goes through the BioC API instead of scraping
article HTML, why arXiv bulk work should move to S3 instead of this module).
"""

import os
import time
import warnings
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

CONTACT_EMAIL = os.environ.get("EVAL_HARNESS_CONTACT_EMAIL", "")
if not CONTACT_EMAIL:
    warnings.warn(
        "EVAL_HARNESS_CONTACT_EMAIL is not set. Several sources (e.g. NCBI's usage "
        "guidelines) ask automated clients to identify a contact email so they can "
        "reach you before blocking your IP if something goes wrong. Set it before a "
        "real batch run.",
        stacklevel=2,
    )

USER_AGENT = (
    f"learning-design-wiki-eval-harness/1.0 "
    f"(research corpus fetch; contact: {CONTACT_EMAIL or 'unset - see EVAL_HARNESS_CONTACT_EMAIL'})"
)

# Conservative floors applied even when a site's robots.txt doesn't specify a
# Crawl-delay, sourced from each site's published API/usage guidance rather
# than the (often silent) robots.txt alone:
#   - arxiv.org: robots.txt itself specifies Crawl-delay: 15 for all agents.
#   - www.ncbi.nlm.nih.gov: E-utilities/BioC guidance caps anonymous use at
#     3 req/s (~0.34s apart); we're well under that at one article at a time,
#     but keep a courteous floor above the bare minimum.
#   - eric.ed.gov / files.eric.ed.gov: no published rate-limit guidance found;
#     use a conservative default rather than assuming unlimited.
DEFAULT_MIN_DELAY = {
    "arxiv.org": 15.0,
    "export.arxiv.org": 15.0,
    "www.ncbi.nlm.nih.gov": 1.0,
    "eutils.ncbi.nlm.nih.gov": 1.0,
    "eric.ed.gov": 2.0,
    "files.eric.ed.gov": 2.0,
}
FALLBACK_MIN_DELAY = 3.0  # any domain not listed above

# Hosts where robots.txt is a generic "don't crawl this like a website"
# backend default rather than a statement about API authorization, but where
# the SAME organization separately publishes usage terms that explicitly
# sanction the exact automated retrieval this harness does. robots.txt
# governs crawler mechanics (which HTML paths, how fast); it doesn't get the
# final word over a documented, narrower API policy for a non-HTML endpoint
# it wasn't written to address. Only add a host here with a citation you can
# point to — never as a way to route around a robots.txt disallow whose
# target genuinely doesn't want automated access.
#
#   eutils.ncbi.nlm.nih.gov: fetching its own robots.txt returns
#     "# robots.txt - robot exclusion file - back-end server version - no
#     robots!" followed by a blanket `Disallow: /` for all agents — i.e. "there
#     is nothing here for a crawler to index," not "our API is off-limits."
#     NCBI's own usage guidelines state E-Utilities is one of the sanctioned
#     automated-retrieval channels for PMC content (see eval/SOURCES.md,
#     which already notes this exact tension for the sibling BioC endpoint:
#     "independent of what robots.txt says"). Rate limiting below still
#     applies in full — this override only concerns the allow/disallow check.
#
#   api.ies.ed.gov (ERIC's official API host): fetching /robots.txt returns
#     HTTP 403 with the body {"message":"Missing Authentication Token"} — the
#     standard AWS API Gateway response for a path that doesn't match any
#     configured route, i.e. this host has no real robots.txt at all, just an
#     infrastructure artifact for an unmapped path. Python's robotparser
#     treats any 403 as "disallow everything for everyone," which is a false
#     signal here, not a published policy. ERIC's own API documentation
#     (see eval/SOURCES.md) names this exact host/endpoint as the first-party
#     sanctioned channel for automated ERIC search. Rate limiting below still
#     applies in full — this override only concerns the allow/disallow check.
API_TERMS_OVERRIDE = {
    "eutils.ncbi.nlm.nih.gov",
    "api.ies.ed.gov",
}

_robots_cache: dict = {}
_last_request_at: dict = {}


class ComplianceError(RuntimeError):
    pass


def _domain(url: str) -> str:
    return urlparse(url).netloc


def _get_robot_parser(url: str) -> "tuple[RobotFileParser | None, bool]":
    """Returns (parser, verified). verified=False means robots.txt could not be
    fetched/parsed — caller should proceed cautiously rather than treat that as
    an explicit allow."""
    origin = f"{urlparse(url).scheme}://{_domain(url)}"
    if origin in _robots_cache:
        return _robots_cache[origin]

    rp = RobotFileParser()
    rp.set_url(origin + "/robots.txt")
    try:
        rp.read()
        result = (rp, True)
    except Exception as e:  # noqa: BLE001 - any network/parse failure, by design
        warnings.warn(f"Could not fetch/parse robots.txt for {origin} ({e}) — "
                       f"proceeding without a verified robots.txt for this domain.")
        result = (None, False)

    _robots_cache[origin] = result
    return result


def check_allowed(url: str) -> None:
    """Raise ComplianceError if this domain's robots.txt explicitly disallows
    fetching `url` for our user agent. Silent (not an error) if robots.txt is
    unreachable — that's a warning, not proof of disallowal. Hosts in
    API_TERMS_OVERRIDE skip the robots.txt check entirely (see that dict's
    comment) but still go through wait_for_rate_limit() via guard()."""
    if _domain(url) in API_TERMS_OVERRIDE:
        return
    rp, verified = _get_robot_parser(url)
    if verified and not rp.can_fetch(USER_AGENT, url):
        raise ComplianceError(
            f"robots.txt for {_domain(url)} disallows fetching {url} for our user agent. "
            f"Do not route around this — use that source's official API/bulk-data channel "
            f"instead (see eval/SOURCES.md)."
        )


def wait_for_rate_limit(url: str) -> None:
    """Block until it's been long enough since the last request to this domain,
    per the larger of (a) robots.txt's own Crawl-delay, if published, or
    (b) our conservative per-domain floor above."""
    domain = _domain(url)
    rp, verified = _get_robot_parser(url)

    min_delay = DEFAULT_MIN_DELAY.get(domain, FALLBACK_MIN_DELAY)
    if verified:
        robots_delay = rp.crawl_delay(USER_AGENT)
        if robots_delay is not None:
            min_delay = max(min_delay, float(robots_delay))

    last = _last_request_at.get(domain)
    if last is not None:
        elapsed = time.monotonic() - last
        remaining = min_delay - elapsed
        if remaining > 0:
            time.sleep(remaining)

    _last_request_at[domain] = time.monotonic()


def guard(url: str) -> None:
    """Call before every request in fetch_article.py: enforces robots.txt and
    rate limiting together in the right order (rate-limit even the check
    itself, since it's a request to the same server)."""
    wait_for_rate_limit(url)
    check_allowed(url)
