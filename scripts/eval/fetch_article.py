"""
fetch_article.py — Fetch and cache full text for the eval corpus (arXiv / ERIC / PMC).

Every request goes through compliance.guard() first (robots.txt + per-domain
rate limiting) — see eval/SOURCES.md for why each source is fetched the way
it is (e.g. PMC via the PMC Article Datasets on AWS, see pmc_aws.py, rather
than scraping article HTML, which NCBI's usage guidelines don't list as a
sanctioned automated-retrieval path).

Text is cached to eval/corpus/cache/<id>.txt so repeated harness runs (and reruns
against new models) don't re-download or re-parse PDFs. Delete a cache file (or
pass --refresh-cache to eval_harness.py) to force a re-fetch.
"""

import io
import sys
import time
from pathlib import Path

import requests

from . import compliance, pmc_aws

EVAL_ROOT = Path(__file__).parent.parent.parent / "eval"
CACHE_DIR = EVAL_ROOT / "corpus" / "cache"

TIMEOUT = 60
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 5  # seconds; doubled each attempt if the server gives no Retry-After


class FetchError(RuntimeError):
    pass


def _get(url: str) -> requests.Response:
    """A bounded, Retry-After-respecting retry on 429/503 — not a hammer,
    just enough to survive a transient rate hiccup. Empirically justified,
    not speculative: a live PMC fetch hit 429 from www.ncbi.nlm.nih.gov while
    this harness was well under NCBI's documented 3 req/s ceiling, most
    likely because their server-side limiting pools traffic by IP across all
    of *.ncbi.nlm.nih.gov rather than per-subdomain the way compliance.py's
    own bookkeeping does. compliance.guard() re-runs on every attempt, so a
    retry still respects our own rate floor on top of any explicit backoff."""
    for attempt in range(MAX_RETRIES + 1):
        compliance.guard(url)
        resp = requests.get(url, headers={"User-Agent": compliance.USER_AGENT}, timeout=TIMEOUT)
        if resp.status_code in (429, 503) and attempt < MAX_RETRIES:
            retry_after = resp.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else RETRY_BACKOFF_BASE * (2 ** attempt)
            except ValueError:
                delay = RETRY_BACKOFF_BASE * (2 ** attempt)
            print(f"  [WARN] {resp.status_code} from {url}, retrying in {delay:.0f}s "
                  f"(attempt {attempt + 1}/{MAX_RETRIES})...", file=sys.stderr)
            time.sleep(delay)
            continue
        resp.raise_for_status()
        return resp


def _pdftotext_page(content: bytes, n: int) -> str:
    """One page through poppler's pdftotext, for a page pypdf cannot read (a malformed font
    descriptor, say). Empty when pdftotext is not installed or also fails."""
    import shutil
    import subprocess
    import tempfile
    if not shutil.which("pdftotext"):
        return ""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(content)
        f.flush()
        r = subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout", f.name, "-"],
                           capture_output=True, text=True, timeout=60)
    return r.stdout if r.returncode == 0 else ""


def _extract_pdf_text(content: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        raise FetchError("pypdf not installed. Run: pip install -r requirements-eval.txt")
    reader = PdfReader(io.BytesIO(content))
    pages = []
    for n, page in enumerate(reader.pages, 1):
        try:
            pages.append(page.extract_text() or "")
        except Exception:  # noqa: BLE001 - one malformed font or stream must not lose the whole paper
            pages.append(_pdftotext_page(content, n))
    text = "\n\n".join(pages)
    if len(text.strip()) < 500:
        raise FetchError("Extracted PDF text is suspiciously short (<500 chars) — "
                          "likely a scanned/image PDF that needs OCR.")
    return text


def _extract_docx_text(content: bytes) -> str:
    """The text of a Word document, which some repositories hold as the open copy. Read as
    a web page it was cached as zip bytes, and the model rejected the paper as out of scope
    (Noetel et al. 2021, batch 71)."""
    import re as _re
    import zipfile
    try:
        xml = zipfile.ZipFile(io.BytesIO(content)).read("word/document.xml").decode("utf-8", "replace")
    except (zipfile.BadZipFile, KeyError):
        raise FetchError("a zip file that is not a Word document")
    xml = _re.sub(r"</w:p>", "\n", xml)
    text = _re.sub(r"<[^>]+>", "", xml)
    import html as _html
    text = _html.unescape(text)
    if len(text.strip()) < 500:
        raise FetchError("Word document text is suspiciously short (<500 chars)")
    return text


def _extract_html_text(html: str) -> str:
    """The readable text of a report or article page: <main>/<article> when the page
    has one, else <body>, with scripts, styles, navigation, headers and footers
    dropped. A page whose text is short is a landing page, not the work, and fails
    like a scanned PDF does, so the run records it rather than extracting from a menu."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "nav", "header", "footer", "form", "aside"]):
        tag.decompose()
    root = soup.find("main") or soup.find("article") or soup.body or soup
    text = "\n".join(l.strip() for l in root.get_text("\n").splitlines() if l.strip())
    if len(text) < 1500:
        raise FetchError("Extracted page text is short (<1500 chars): a landing or index page, "
                         "or one rendered by JavaScript, not the work itself.")
    return text


def _report_pdf_link(html: str, base: str) -> "str | None":
    """The link to the work's own PDF on a landing page, when it has one: a report page
    (WWC, CREDO, Campbell, an OJS journal's article page) is usually a summary with the
    full text one link away. Prefers links whose text or address says download, full
    text, report or PDF; never a link to another site's PDF that is not the work."""
    from urllib.parse import urljoin, urlparse
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    host = urlparse(base).netloc
    best, best_score = None, 0
    for a in soup.find_all("a", href=True):
        href = urljoin(base, a["href"])
        label = (a.get_text(" ") + " " + " ".join(a.get("class") or [])).lower()
        low = href.lower()
        if not (low.split("?")[0].endswith(".pdf") or "/download/" in low or "pdf" in label
                or "/article/download/" in low):
            continue
        score = 1
        score += 3 if any(w in label for w in ("full report", "download", "full text", "pdf", "read the report")) else 0
        score += 2 if urlparse(href).netloc == host or not urlparse(href).netloc else 0
        score -= 3 if any(w in low for w in ("appendix", "brief", "summary", "snapshot", "infographic")) else 0
        if score > best_score:
            best, best_score = href, score
    return best


_DSPACE_ITEM_RE = __import__("re").compile(r"^(https?://[^/]+)/items/([0-9a-f-]{36})/?$")


def _fetch_dspace_item(fetch_url: str) -> "str | None":
    """A DSpace 7 item page (Digital Promise's repository holds ~280 hub entries) is an
    Angular shell with no text in its HTML. DSpace's REST API, which robots.txt does not
    refuse, lists the item's bundles: the ORIGINAL bundle holds the deposited work, and
    its first PDF is read as an article. Returns None for any other URL, or for an item
    with no PDF in ORIGINAL, so the ordinary web fetch runs instead."""
    m = _DSPACE_ITEM_RE.match(fetch_url)
    if not m:
        return None
    origin, uuid = m.groups()
    try:
        bundles = _get(f"{origin}/server/api/core/items/{uuid}/bundles").json()["_embedded"]["bundles"]
    except (FetchError, requests.RequestException, ValueError, KeyError):
        return None
    for b in bundles:
        if b.get("name") != "ORIGINAL":
            continue
        streams = _get(b["_links"]["bitstreams"]["href"]).json()["_embedded"]["bitstreams"]
        for bs in streams:
            r = _get(f"{origin}/server/api/core/bitstreams/{bs['uuid']}/content")
            if "pdf" in r.headers.get("Content-Type", "").lower() or r.content[:5] == b"%PDF-":
                return _extract_pdf_text(r.content)
    return None


def _fetch_web(fetch_url: str) -> str:
    """A report or article on the publisher's own site (the curated lists in
    scripts/eval/source_lists.py: WWC, Evidence for ESSA, Mathematica, Brookings, ...).
    PDF or HTML, decided by what the server sends. An HTML landing page that links
    the work's PDF is followed to it; otherwise the page's own text is the work, if it
    is long enough to be one. robots.txt and the per-domain rate floor apply through
    compliance.guard, as for every other source."""
    dspace = _fetch_dspace_item(fetch_url)
    if dspace:
        return dspace
    resp = _get(fetch_url)
    ctype = resp.headers.get("Content-Type", "").lower()
    if "pdf" in ctype or resp.content[:5] == b"%PDF-":
        return _extract_pdf_text(resp.content)
    if resp.content[:2] == b"PK":
        return _extract_docx_text(resp.content)
    if b"\0" in resp.content[:2000]:
        raise FetchError(f"{fetch_url} sent a binary file that is neither PDF nor Word ({ctype or 'no type'})")
    pdf = _report_pdf_link(resp.text, resp.url)
    if pdf:
        try:
            r2 = _get(pdf)
            if "pdf" in r2.headers.get("Content-Type", "").lower() or r2.content[:5] == b"%PDF-":
                return _extract_pdf_text(r2.content)
        except (FetchError, requests.RequestException, compliance.ComplianceError):
            pass   # fall back to the page itself
    return _extract_html_text(resp.text)


def _fetch_pmc_via_aws(entry: dict) -> str:
    """Fetches full text via the PMC Article Datasets on AWS (pmc_aws.py)
    instead of the old BioC-PMC API — see that module's docstring. Uses the
    same `is_pmc_openaccess` ground truth discover_articles.search_pmc() now
    checks before adding a manifest entry, so a 404/empty-body surprise here
    should be rare — but a manifest entry can come from a hand-curated
    source (the original 10-article benchmark) that never went through that
    check, so this still verifies rather than assuming. Don't fall back to
    scraping the HTML page for a miss; swap the manifest entry instead."""
    pmcid = entry.get("pmcid") or entry["id"]
    aws_meta = pmc_aws.fetch_metadata(pmcid)
    if aws_meta is None:
        raise FetchError(
            f"{pmcid} has no PMC AWS metadata object (metadata/{pmcid}.1.json not found) — "
            f"not available via the PMC Article Datasets on AWS. Replace this manifest entry."
        )
    if not aws_meta.get("is_pmc_openaccess"):
        raise FetchError(
            f"{pmcid} is not marked is_pmc_openaccess in its PMC AWS metadata — not cleared "
            f"for automated bulk retrieval. Replace this manifest entry rather than scraping "
            f"the HTML article page as a workaround."
        )
    text_url = aws_meta.get("text_url")
    if not text_url:
        raise FetchError(f"{pmcid}'s PMC AWS metadata has no text_url.")
    resp = _get(pmc_aws.s3_to_https(text_url))
    text = resp.text
    if len(text.strip()) < 500:
        raise FetchError("Extracted PMC AWS text is suspiciously short (<500 chars) — "
                          "check the PMCID is correct and actually in the PMC OA subset.")
    return text


# Hosts that only list or redirect to the publisher's page: never a copy of the text.
_NOT_A_COPY = ("doaj.org", "doi.org", "dx.doi.org")


def _openalex_work(doi: str) -> "dict | None":
    """One work's OpenAlex record (single-work lookups are not metered, list queries are)."""
    import urllib.parse
    params = {"select": "doi,ids,locations,open_access", "mailto": "contact@learningdesignalliance.org"}
    try:
        resp = _get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}?"
                    + urllib.parse.urlencode(params))
        return resp.json()
    except (FetchError, requests.RequestException, compliance.ComplianceError, ValueError):
        return None


def _open_copy_urls(work: dict) -> list:
    """Candidate URLs for an open copy, best first: repositories (arXiv, OSF, institutional),
    then any other location's open PDF. An OSF page renders by JavaScript, so its plain
    /download link is used instead."""
    from urllib.parse import urlparse
    repo, other = [], []
    for loc in work.get("locations") or []:
        if not loc.get("is_oa"):
            continue
        url = loc.get("pdf_url") or loc.get("landing_page_url")
        if not url or urlparse(url).netloc.lower() in _NOT_A_COPY:
            continue
        host = urlparse(url).netloc.lower()
        if host.endswith("osf.io"):
            url = url.rstrip("/").split("?")[0]
            url = url if url.endswith("/download") else url + "/download"
        elif host.endswith("arxiv.org") and "/abs/" in url:
            url = url.replace("/abs/", "/pdf/")
        is_repo = (loc.get("source") or {}).get("type") == "repository"
        (repo if is_repo else other if loc.get("pdf_url") else []).append(url)
    seen, out = set(), []
    for u in repo + other:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def _fetch_copy(url: str) -> str:
    """One open-copy URL. PMC's own PDF links answer automated clients with a challenge page,
    so a PMC URL goes through the PMC open-access dataset instead; a figshare page is
    rendered by JavaScript, so its file comes from figshare's public API."""
    import re as _re
    m = _re.search(r"pmc\.ncbi\.nlm\.nih\.gov/(?:articles/)?(?:PMC)?(\d+)", url) or \
        _re.search(r"ncbi\.nlm\.nih\.gov/pmc/articles/(?:PMC)?(\d+)", url)
    if m:   # PMC links are written with and without the "PMC" prefix
        pmcid = "PMC" + m.group(1)
        return _fetch_pmc_via_aws({"id": pmcid, "pmcid": pmcid})
    m = _re.search(r"figshare\.com/articles/(?:[^/]+/)*?(\d{6,})(?:/|$)", url)
    if m:
        files = _get(f"https://api.figshare.com/v2/articles/{m.group(1)}").json().get("files") or []
        for f in files:
            if f.get("name", "").lower().endswith(".pdf") and f.get("download_url"):
                r = _get(f["download_url"])
                return _extract_pdf_text(r.content)
        raise FetchError(f"figshare item {m.group(1)} has no PDF file")
    return _fetch_web(url)


def fetch_open_copy(doi: str) -> str:
    """The text of an open copy of a DOI's work, found through OpenAlex: PMC's open-access
    subset first, then a repository or other open PDF. Used when the publisher's own page
    cannot be read (a JavaScript page, a 403, or robots.txt). Every request still goes through
    compliance.guard, so a host whose robots.txt disallows us is skipped, not worked around."""
    work = _openalex_work(doi)
    if not work:
        raise FetchError(f"no OpenAlex record for {doi}")
    errors = []
    pmcid = (work.get("ids") or {}).get("pmcid")
    if pmcid:
        try:
            return _fetch_pmc_via_aws({"id": pmcid.rstrip("/").split("/")[-1], "pmcid": pmcid.rstrip("/").split("/")[-1]})
        except Exception as e:  # noqa: BLE001
            errors.append(f"PMC: {e}"[:80])
    for url in _open_copy_urls(work):
        try:
            return _fetch_copy(url)
        except Exception as e:  # noqa: BLE001 - a broken PDF or a refusal on one copy: try the next
            errors.append(f"{url}: {e}"[:120])
    raise FetchError(f"no readable open copy of {doi}" + (f" ({'; '.join(errors[:3])})" if errors else ""))


def fetch_article_text(entry: dict, refresh: bool = False) -> str:
    """Fetch (or load from cache) the full text for one manifest entry."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"{entry['id']}.txt"

    if cache_path.exists() and not refresh:
        return cache_path.read_text(encoding="utf-8")

    source = entry["source"]
    fetch_url = entry["fetch_url"]

    try:
        # "oa": an open-access PDF found through OpenAlex's best_oa_location for a
        # named synthesis (the targeted pass, 2026-09-30); fetched like arXiv/ERIC.
        if source in ("arxiv", "eric", "oa"):
            resp = _get(fetch_url)
            text = _extract_pdf_text(resp.content)
        elif source == "web":
            try:
                text = _fetch_web(fetch_url)
            except (FetchError, requests.RequestException, compliance.ComplianceError) as e:
                # A DOI whose publisher page cannot be read may have an open copy elsewhere.
                if not entry.get("doi"):
                    raise
                try:
                    text = fetch_open_copy(entry["doi"])
                except FetchError as e2:
                    raise FetchError(f"{e}; {e2}") from e
        elif source == "pubmed":
            text = _fetch_pmc_via_aws(entry)
        else:
            raise FetchError(f"Unknown source type: {source}")
    except compliance.ComplianceError:
        raise
    except requests.HTTPError as e:
        raise FetchError(f"HTTP error fetching {fetch_url}: {e}") from e
    except ValueError as e:
        raise FetchError(f"Unparseable response from {fetch_url}: {e}") from e
    except requests.RequestException as e:
        raise FetchError(f"Network error fetching {fetch_url}: {e}") from e

    cache_path.write_text(text, encoding="utf-8")
    return text


def main() -> None:
    """Prefetch/verify the whole manifest without calling any model — run this
    first to confirm every URL in the manifest still resolves before spending
    money on generation calls. Pass --manifest <path> to check a different
    manifest file (e.g. discover_articles.py's output) instead of the default
    10-article benchmark corpus."""
    import json
    manifest_path = EVAL_ROOT / "corpus" / "manifest.json"
    if "--manifest" in sys.argv:
        manifest_path = Path(sys.argv[sys.argv.index("--manifest") + 1])
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    refresh = "--refresh-cache" in sys.argv

    ok, failed = 0, []
    for entry in manifest["articles"]:
        try:
            text = fetch_article_text(entry, refresh=refresh)
            print(f"[OK]   {entry['id']:20s} {len(text):>8,} chars — {entry['title'][:60]}")
            ok += 1
        except FetchError as e:
            print(f"[FAIL] {entry['id']:20s} {e}")
            failed.append(entry["id"])
        except compliance.ComplianceError as e:
            print(f"[BLOCKED] {entry['id']:20s} {e}")
            failed.append(entry["id"])

    print(f"\n{ok}/{len(manifest['articles'])} fetched successfully.")
    if failed:
        print(f"Failed: {', '.join(failed)}")
        print("Fix or replace these manifest entries before running the harness.")
        sys.exit(1)


if __name__ == "__main__":
    main()
