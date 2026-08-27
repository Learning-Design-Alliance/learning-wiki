"""
ground_truth.py — Live/local verification for facts a model claims, instead
of only trusting a plausible-looking pattern.

Two independent techniques live here:

1. Citation ground-truthing (verify_citation): validator.py's
   `_looks_like_real_citation()` is a pure shape check — does the text
   contain something that looks like a year and something that looks like a
   doi.org/http link. A model can satisfy that with a completely fabricated
   DOI. verify_citation() resolves the citation's DOI against Crossref, or
   its arXiv id against arXiv's API when there's no DOI (common for
   preprints — a real gap the DOI-only check left completely uncovered,
   since most preprints never get one).
2. Quote grounding (quote_is_grounded): a citation resolving to a REAL paper
   doesn't prove the specific CLAIM attributed to it is real — the model
   could cite a genuine DOI in support of something that paper never said.
   quote_is_grounded() checks a required verbatim source_quote field against
   the actual article text this model was given, which is the only local,
   deterministic way to catch that: no network call, no LLM judge, just a
   text match — but it does require the extraction schema to actually
   include a source_quote field (see validator.py's require_source_quotes
   flag and optimizer.py's rule 7 for how the schema gets there).

Per this project's own failure data, "fabrication" and "inaccuracy" are the
#1 or #2 judge complaint category for every model tested so far — the one
thing schema/prompt rules can never fix on their own, since a rule can only
forbid a known-bad shape, not confirm a specific claimed fact is real.

Citation ground-truthing is opt-in (--ground-truth on
run/optimize/auto-optimize/spotcheck), not the default: it adds real network
calls (Crossref/arXiv — free, no key, but still a live external dependency)
to every validation pass, changing cost/latency characteristics the
benchmark shouldn't silently take on for everyone. Quote grounding is a
separate opt-in (--require-source-quotes) since it's a genuine SCHEMA
change (a new required field no existing prompt version has yet) — turning
it on before any prompt version knows about the field will legitimately
crash validator_pass_rate to near zero, which is the intended signal for
the next auto-optimize round to react to, not a bug. `spotcheck
--ground-truth` is the cheapest way to try citation ground-truthing against
already-generated results, since it doesn't re-pay for generation.
"""

import re
import time
import xml.etree.ElementTree as ET

import requests

from . import compliance

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>,)]+", re.IGNORECASE)
ARXIV_ID_RE = re.compile(r"arxiv(?:\.org)?[\s:/]*(?:abs/|pdf/)?(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
CROSSREF_TIMEOUT = 8.0
ARXIV_TIMEOUT = 10.0
ARXIV_ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "opensearch": "http://a9.com/-/spec/opensearch/1.1/"}

# Crossref's public API has no hard rate limit for the "polite pool" (a
# mailto identifying the caller, same courtesy convention as compliance.py's
# USER_AGENT), but there's no reason to hammer it either — the same DOI
# often repeats across models/rounds testing the same corpus, so an
# in-process cache means most of a batch's citations cost zero extra calls.
_MIN_CROSSREF_DELAY = 0.15
_last_crossref_call = [0.0]
_doi_cache: dict = {}

# arXiv's API terms of use ask for no more than one request per 3 seconds —
# much stricter than Crossref — so a batch with several DISTINCT uncached
# arXiv citations can visibly add wall-clock time to validation. Cached per
# id for the same reason as DOIs: the same preprint often repeats across
# models/rounds testing the same corpus.
_MIN_ARXIV_DELAY = 3.0
_last_arxiv_call = [0.0]
_arxiv_cache: dict = {}


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


def extract_arxiv_id(citation_text) -> "str | None":
    if not isinstance(citation_text, str):
        return None
    m = ARXIV_ID_RE.search(citation_text)
    return m.group(1) if m else None


def verify_arxiv(arxiv_id: str) -> dict:
    """{"exists": bool | None, "year": int | None, "error": str | None} —
    same contract as verify_doi. A DOI only exists for a preprint once (and
    if) it's later published in a journal, so a DOI-only check left every
    citation to an unpublished/still-preprint arXiv paper completely
    unverifiable; this covers that gap via arXiv's own public API instead."""
    if arxiv_id in _arxiv_cache:
        return _arxiv_cache[arxiv_id]

    elapsed = time.monotonic() - _last_arxiv_call[0]
    if elapsed < _MIN_ARXIV_DELAY:
        time.sleep(_MIN_ARXIV_DELAY - elapsed)
    _last_arxiv_call[0] = time.monotonic()

    result = {"exists": None, "year": None, "error": None}
    try:
        resp = requests.get(
            "http://export.arxiv.org/api/query",
            params={"id_list": arxiv_id}, headers={"User-Agent": compliance.USER_AGENT},
            timeout=ARXIV_TIMEOUT,
        )
        if resp.status_code != 200:
            result["error"] = f"arXiv API returned HTTP {resp.status_code}"
        else:
            root = ET.fromstring(resp.text)
            total_el = root.find("opensearch:totalResults", ARXIV_ATOM_NS)
            total = int(total_el.text) if total_el is not None and total_el.text else 0
            result["exists"] = total > 0
            if result["exists"]:
                entry = root.find("atom:entry", ARXIV_ATOM_NS)
                published = entry.find("atom:published", ARXIV_ATOM_NS) if entry is not None else None
                if published is not None and published.text:
                    result["year"] = int(published.text[:4])
    except requests.RequestException as e:
        result["error"] = f"arXiv API request failed: {type(e).__name__}: {e}"
    except ET.ParseError as e:
        result["error"] = f"Could not parse arXiv API response: {e}"

    _arxiv_cache[arxiv_id] = result
    return result


def verify_citation(citation_text: str) -> "dict | None":
    """Ground-truths one citation string end to end: DOI first (Crossref),
    then an arXiv id if no DOI was found (arXiv's own API) — covering both
    published work and preprints, which a DOI-only check left completely
    unverifiable. Returns None if neither identifier is extractable (nothing
    to verify against — the existing shape check in validator.py already
    flags a missing DOI/URL on its own). Otherwise returns {"kind" ("DOI" or
    "arXiv id"), "id", "exists", "year_match", "error"}; year_match is None
    when there's no claimed year in the citation text or the identifier
    itself didn't resolve, so there's nothing to compare."""
    doi = extract_doi(citation_text)
    if doi:
        kind, ident, result = "DOI", doi, verify_doi(doi)
    else:
        arxiv_id = extract_arxiv_id(citation_text)
        if not arxiv_id:
            return None
        kind, ident, result = "arXiv id", arxiv_id, verify_arxiv(arxiv_id)

    year_match = None
    if result["year"] is not None:
        m = YEAR_RE.search(citation_text)
        if m:
            year_match = int(m.group(0)) == result["year"]

    return {
        "kind": kind,
        "id": ident,
        "exists": result["exists"],
        "year_match": year_match,
        "error": result["error"],
    }


_WORD_RE = re.compile(r"\w+")


def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def quote_is_grounded(quote, article_text: str, min_words: int = 4, shingle_size: int = 5,
                       shingle_threshold: float = 0.7) -> bool:
    """True if `quote` genuinely appears to come from `article_text` —
    checked two ways, cheapest first: (1) exact substring match after
    whitespace-only normalization (the common case — the model copied it
    correctly, possibly with reflowed line breaks), then (2) a
    punctuation-insensitive word-shingle overlap check, tolerating light
    reformatting (curly quotes, an ellipsis marking a truncated mid-sentence
    quote) without accepting a quote that bears no real resemblance to the
    source. Deterministic and free — no API call, no LLM judge, just a text
    match against the exact article this model was given — the cheapest and
    fastest fabrication signal available, and the only one that catches a
    citation to a REAL paper attributed to a claim that paper never made."""
    if not isinstance(quote, str) or not isinstance(article_text, str):
        return False
    words = _WORD_RE.findall(quote.lower())
    if len(words) < min_words:
        return False

    if _normalize_ws(quote) in _normalize_ws(article_text):
        return True

    article_words_only = " ".join(_WORD_RE.findall(article_text.lower()))
    size = min(shingle_size, len(words))
    shingles = [" ".join(words[i:i + size]) for i in range(len(words) - size + 1)]
    if not shingles:
        return False
    matched = sum(1 for s in shingles if s in article_words_only)
    return (matched / len(shingles)) >= shingle_threshold
