"""
ground_truth.py — Live verification for citations the model claims exist,
instead of only trusting a plausible-looking DOI/year pattern.

validator.py's `_looks_like_real_citation()` is a pure shape check: does the
text contain something that looks like a year and something that looks like
a doi.org/http link. A model can satisfy that with a completely fabricated
DOI, and per this project's own failure data, "fabrication" and "inaccuracy"
are the #1 or #2 judge complaint category for every model tested so far —
the one thing schema/prompt rules can never fix on their own, since they can
only forbid a known-bad shape, not confirm a specific claimed fact is real.

Opt-in (--ground-truth on `run`/`optimize`/`auto-optimize`/`spotcheck`), not
the default: this adds real network calls (Crossref's public API — free, no
key, but still a live external dependency) to every validation pass, which
changes cost/latency characteristics the benchmark shouldn't silently take
on for everyone. `spotcheck --ground-truth` is the cheapest way to try this
against already-generated results, since it doesn't re-pay for generation.
"""

import re
import time

import requests

from . import compliance

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>,)]+", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
CROSSREF_TIMEOUT = 8.0

# Crossref's public API has no hard rate limit for the "polite pool" (a
# mailto identifying the caller, same courtesy convention as compliance.py's
# USER_AGENT), but there's no reason to hammer it either — the same DOI
# often repeats across models/rounds testing the same corpus, so an
# in-process cache means most of a batch's citations cost zero extra calls.
_MIN_CROSSREF_DELAY = 0.15
_last_crossref_call = [0.0]
_doi_cache: dict = {}


def extract_doi(citation_text) -> "str | None":
    if not isinstance(citation_text, str):
        return None
    m = DOI_RE.search(citation_text)
    if not m:
        return None
    return m.group(0).rstrip(".,;)")


def verify_doi(doi: str) -> dict:
    """{"exists": bool | None, "year": int | None, "error": str | None}
    exists=None (neither True nor False) means Crossref couldn't be reached
    at all — treat that as "unverifiable", never as evidence of fabrication;
    only a confirmed 404 (exists=False) is a real, ground-truthed finding."""
    if doi in _doi_cache:
        return _doi_cache[doi]

    elapsed = time.monotonic() - _last_crossref_call[0]
    if elapsed < _MIN_CROSSREF_DELAY:
        time.sleep(_MIN_CROSSREF_DELAY - elapsed)
    _last_crossref_call[0] = time.monotonic()

    params = {"mailto": compliance.CONTACT_EMAIL} if compliance.CONTACT_EMAIL else {}
    result = {"exists": None, "year": None, "error": None}
    try:
        resp = requests.get(
            f"https://api.crossref.org/works/{doi}",
            params=params, headers={"User-Agent": compliance.USER_AGENT}, timeout=CROSSREF_TIMEOUT,
        )
        if resp.status_code == 404:
            result["exists"] = False
        elif resp.status_code == 200:
            result["exists"] = True
            message = resp.json().get("message", {})
            for date_field in ("published-print", "published-online", "issued"):
                parts = (message.get(date_field) or {}).get("date-parts")
                if parts and parts[0] and parts[0][0]:
                    result["year"] = int(parts[0][0])
                    break
        else:
            result["error"] = f"Crossref returned HTTP {resp.status_code}"
    except requests.RequestException as e:
        result["error"] = f"Crossref request failed: {type(e).__name__}: {e}"
    except (ValueError, KeyError, TypeError) as e:
        # A malformed/unexpected JSON body shouldn't be treated as proof the
        # DOI doesn't exist — it exists (status 200), we just couldn't parse
        # its date; still "unverifiable" for the year-match check only.
        result["exists"] = True
        result["error"] = f"Could not parse Crossref response: {type(e).__name__}: {e}"

    _doi_cache[doi] = result
    return result


def verify_citation(citation_text: str) -> "dict | None":
    """Ground-truths one citation string end to end. Returns None if it has
    no extractable DOI (nothing to verify against Crossref — the existing
    shape check in validator.py already flags a missing DOI on its own).
    Otherwise returns {"doi", "exists", "year_match", "error"}; year_match
    is None when there's no claimed year in the text or the DOI itself
    didn't resolve, so there's nothing to compare."""
    doi = extract_doi(citation_text)
    if not doi:
        return None

    doi_result = verify_doi(doi)
    year_match = None
    if doi_result["year"] is not None:
        m = YEAR_RE.search(citation_text)
        if m:
            year_match = int(m.group(0)) == doi_result["year"]

    return {
        "doi": doi,
        "exists": doi_result["exists"],
        "year_match": year_match,
        "error": doi_result["error"],
    }
