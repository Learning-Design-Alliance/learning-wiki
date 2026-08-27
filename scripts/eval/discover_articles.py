"""
discover_articles.py — Finds candidate articles for a real-scale ingest
batch, via each source's own sanctioned SEARCH API (never scraping a search
results page) and compliance.py's rate limiting for every request, exactly
like fetch_article.py does for full-text fetches. Output is a manifest.json
file in the same shape as eval/corpus/manifest.json, so it drops straight
into fetch_article.py / eval_harness.py with no format translation.

Seeded from the wiki's OWN existing theories/ and principles/ page titles
(its established topic vocabulary) rather than an invented topic list, per
this project's "start from the classics" approach — see topics_from_wiki().

Allocation across sources is deliberately uneven, not an even three-way
split, per eval/SOURCES.md's own prior research: arXiv's 15s/request
crawl-delay makes more than a few dozen individual PDF fetches impractical
for a live batch ("explicitly discouraged for indiscriminate volume" per
arXiv's own robots.txt header) — real arXiv scale needs the S3/Kaggle bulk
channels, not this script. PMC (1 req/s) and ERIC (2s/req) scale to
hundreds/thousands of individual fetches fine, so this weights toward those
two and caps arXiv's share on purpose. This is a DISCOVERY step only — it
finds candidates and writes a manifest; it does not fetch full text (that's
still fetch_article.py, one call per article, same as always) and it does
not guarantee every candidate is actually fetchable (a PMC hit that isn't
really in the OA subset, an ERIC id with no PDF, a dead arXiv id) — that's
exactly what running this manifest through
`python3 -m scripts.eval.fetch_article --manifest <path>` (its main() is a
prefetch/verify pass — see its own docstring) is for, before spending any
generation money.
"""

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

from . import compliance

WIKI_ROOT = Path(__file__).parent.parent.parent
EVAL_ROOT = WIKI_ROOT / "eval"
TIMEOUT = 30

# See the module docstring — not an even split, PMC and ERIC scale to a live
# per-article batch far better than arXiv does at this project's documented
# rate-limit floors.
DEFAULT_TARGETS = {"pmc": 700, "eric": 220, "arxiv": 40}

ARXIV_ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "opensearch": "http://a9.com/-/spec/opensearch/1.1/"}


class DiscoveryError(RuntimeError):
    pass


def _get(url: str, params: dict = None) -> requests.Response:
    full_url = url if not params else f"{url}?{requests.compat.urlencode(params)}"
    compliance.guard(full_url)
    resp = requests.get(url, params=params, headers={"User-Agent": compliance.USER_AGENT}, timeout=TIMEOUT)
    resp.raise_for_status()
    return resp


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug


def topics_from_wiki() -> list:
    """Search query seeds from the wiki's own existing theories/ (full
    concept names — these map cleanly to well-established academic search
    terms) plus principles/ (more specific, converts the slug filename back
    to a phrase). Deliberately not elements/patterns/strategies/claims —
    those are typically too narrow or too compound to work well as a single
    search query on their own."""
    topics = []
    for folder in ("theories", "principles"):
        folder_path = WIKI_ROOT / folder
        if not folder_path.is_dir():
            continue
        for path in sorted(folder_path.glob("*.md")):
            if path.stem in ("index",):
                continue
            phrase = path.stem.replace("-", " ").replace("_", " ")
            if phrase and phrase not in topics:
                topics.append(phrase)
    return topics


def _round_robin_counts(topics: list, total: int) -> list:
    """Per-topic result counts summing to ~total, spread evenly across
    however many topics there are, so one broad topic doesn't crowd out a
    narrow one — each topic gets at least 1 if total >= len(topics)."""
    if not topics:
        return []
    base = max(1, total // len(topics))
    return [base] * len(topics)


# ---------------------------------------------------------------------------
# PMC (NCBI E-utilities: ESearch for ids, ESummary for title/author/year —
# see eval/SOURCES.md for why PMC is fetched via NCBI's own sanctioned API
# family rather than any scraped page).
# ---------------------------------------------------------------------------

PMC_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PMC_ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def search_pmc(query: str, retmax: int) -> list:
    """Returns manifest-shaped entries. Restricted to the PMC Open Access
    subset via the "open access[filter]" ESearch tag — narrows results to
    what's actually retrievable through the BioC API fetch_article.py uses,
    though this is a best-effort filter, not a guarantee (see the prefetch-
    verify step for the real check)."""
    search_params = {
        "db": "pmc",
        "term": f"({query}) AND open access[filter]",
        "retmax": str(retmax),
        "retmode": "json",
    }
    try:
        resp = _get(PMC_ESEARCH_URL, params=search_params)
        data = resp.json()
        ids = data.get("esearchresult", {}).get("idlist", [])
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"  [WARN] PMC search failed for {query!r}: {e}", file=sys.stderr)
        return []
    if not ids:
        return []

    try:
        summary_params = {"db": "pmc", "id": ",".join(ids), "retmode": "json"}
        resp = _get(PMC_ESUMMARY_URL, params=summary_params)
        summaries = resp.json().get("result", {})
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"  [WARN] PMC summary fetch failed for {query!r}: {e}", file=sys.stderr)
        return []

    entries = []
    for uid in ids:
        doc = summaries.get(uid)
        if not isinstance(doc, dict):
            continue
        pmcid = f"PMC{uid}"
        title = doc.get("title", "").strip()
        if not title:
            continue
        authors = ", ".join(a.get("name", "") for a in doc.get("authors", []) if a.get("name")) or "et al."
        year = None
        pubdate = doc.get("pubdate", "") or doc.get("epubdate", "")
        m = re.search(r"\b(19|20)\d{2}\b", pubdate)
        if m:
            year = int(m.group(0))
        entries.append({
            "id": f"pmc-{uid}",
            "source": "pubmed",
            "pmcid": pmcid,
            "title": title,
            "authors": authors,
            "year": year,
            "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}",
            "fetch_url": f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode",
            "topic_hint": query,
        })
    return entries


# ---------------------------------------------------------------------------
# arXiv (Atom search API — same endpoint family ground_truth.py's
# verify_arxiv() already uses for citation checks, reused here for search).
# ---------------------------------------------------------------------------

ARXIV_SEARCH_URL = "http://export.arxiv.org/api/query"


def search_arxiv(query: str, max_results: int) -> list:
    params = {
        "search_query": f"all:{query}",
        "start": "0",
        "max_results": str(max_results),
    }
    try:
        resp = _get(ARXIV_SEARCH_URL, params=params)
        root = ET.fromstring(resp.text)
    except (requests.RequestException, ET.ParseError) as e:
        print(f"  [WARN] arXiv search failed for {query!r}: {e}", file=sys.stderr)
        return []

    entries = []
    for entry in root.findall("atom:entry", ARXIV_ATOM_NS):
        id_el = entry.find("atom:id", ARXIV_ATOM_NS)
        title_el = entry.find("atom:title", ARXIV_ATOM_NS)
        published_el = entry.find("atom:published", ARXIV_ATOM_NS)
        if id_el is None or title_el is None or not id_el.text:
            continue
        # atom:id looks like http://arxiv.org/abs/2105.15106v2 — strip version suffix.
        m = re.search(r"abs/(\d{4}\.\d{4,5})", id_el.text)
        if not m:
            continue
        arxiv_id = m.group(1)
        title = " ".join(title_el.text.split())
        authors = ", ".join(
            (a.find("atom:name", ARXIV_ATOM_NS).text or "").strip()
            for a in entry.findall("atom:author", ARXIV_ATOM_NS)
            if a.find("atom:name", ARXIV_ATOM_NS) is not None
        ) or "et al."
        year = None
        if published_el is not None and published_el.text:
            m2 = re.match(r"(\d{4})", published_el.text)
            if m2:
                year = int(m2.group(1))
        entries.append({
            "id": f"arxiv-{arxiv_id}",
            "source": "arxiv",
            "title": title,
            "authors": authors,
            "year": year,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "fetch_url": f"https://arxiv.org/pdf/{arxiv_id}",
            "topic_hint": query,
        })
    return entries


# ---------------------------------------------------------------------------
# ERIC (ERIC's own public search API — JSON, no key required).
# ---------------------------------------------------------------------------

ERIC_SEARCH_URL = "https://api.ies.ed.gov/eric/"


def search_eric(query: str, rows: int) -> list:
    params = {
        "search": query,
        "format": "json",
        "rows": str(rows),
        # Only records ERIC itself marks as having a full-text PDF on
        # files.eric.ed.gov — matches what fetch_article.py can actually fetch.
        "fields": "id,title,author,publicationdateyear,peerreviewed",
    }
    try:
        resp = _get(ERIC_SEARCH_URL, params=params)
        docs = resp.json().get("response", {}).get("docs", [])
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"  [WARN] ERIC search failed for {query!r}: {e}", file=sys.stderr)
        return []

    entries = []
    for doc in docs:
        eric_id = doc.get("id", "").strip()
        title = doc.get("title", "").strip()
        if not eric_id or not title:
            continue
        authors = ", ".join(doc.get("author", [])) if isinstance(doc.get("author"), list) else (doc.get("author") or "et al.")
        year = doc.get("publicationdateyear")
        try:
            year = int(year) if year else None
        except (TypeError, ValueError):
            year = None
        entries.append({
            "id": f"eric-{eric_id.lower()}",
            "source": "eric",
            "title": title,
            "authors": authors or "et al.",
            "year": year,
            "url": f"https://eric.ed.gov/?id={eric_id}",
            "fetch_url": f"https://files.eric.ed.gov/fulltext/{eric_id}.pdf",
            "topic_hint": query,
        })
    return entries


SEARCH_FNS = {"pmc": search_pmc, "arxiv": search_arxiv, "eric": search_eric}


def build_manifest(targets: dict, topics: list, existing_ids: set, verbose: bool = True) -> list:
    """Round-robins every topic across each source until that source's
    target count is met or topics run out, deduplicating against
    existing_ids (already in the benchmark manifest) and against itself."""
    manifest = []
    seen_ids = set(existing_ids)

    for source, target in targets.items():
        fn = SEARCH_FNS[source]
        per_topic_counts = _round_robin_counts(topics, target)
        collected = 0
        for topic, count in zip(topics, per_topic_counts):
            if collected >= target:
                break
            if verbose:
                print(f"[{source}] searching {topic!r} (have {collected}/{target})...")
            results = fn(topic, count)
            for entry in results:
                if entry["id"] in seen_ids:
                    continue
                seen_ids.add(entry["id"])
                manifest.append(entry)
                collected += 1
                if collected >= target:
                    break
        if verbose:
            print(f"[{source}] done: {collected}/{target} candidates found\n")

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pmc", type=int, default=DEFAULT_TARGETS["pmc"], help="Target PMC candidate count")
    parser.add_argument("--eric", type=int, default=DEFAULT_TARGETS["eric"], help="Target ERIC candidate count")
    parser.add_argument("--arxiv", type=int, default=DEFAULT_TARGETS["arxiv"], help="Target arXiv candidate count")
    parser.add_argument("--out", default=str(EVAL_ROOT / "corpus" / "manifest_bulk.json"),
                         help="Output manifest path (default: eval/corpus/manifest_bulk.json — "
                              "deliberately NOT manifest.json, so the original 10-article benchmark stays intact)")
    args = parser.parse_args()

    existing_manifest_path = EVAL_ROOT / "corpus" / "manifest.json"
    existing_ids = set()
    if existing_manifest_path.exists():
        existing = json.loads(existing_manifest_path.read_text(encoding="utf-8"))
        existing_entries = existing if isinstance(existing, list) else existing.get("articles", [])
        existing_ids = {e["id"] for e in existing_entries}

    topics = topics_from_wiki()
    if not topics:
        print("[ERROR] No topics found in theories/ or principles/ — is this running from the wiki root?")
        sys.exit(1)
    print(f"Seeded {len(topics)} search topics from theories/ + principles/.\n")

    targets = {"pmc": args.pmc, "eric": args.eric, "arxiv": args.arxiv}
    manifest = build_manifest(targets, topics, existing_ids)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # {"articles": [...]} — matches manifest.json's own shape exactly (see
    # fetch_article.py's main(), which reads manifest["articles"]) so this
    # drops straight into the existing prefetch-verify step with no
    # translation step in between.
    out_path.write_text(json.dumps({"articles": manifest}, indent=2), encoding="utf-8")

    by_source = {}
    for e in manifest:
        by_source[e["source"]] = by_source.get(e["source"], 0) + 1
    print(f"Wrote {len(manifest)} candidate(s) to {out_path}:")
    for source, n in sorted(by_source.items()):
        print(f"  {source}: {n}")
    print(f"\nNext: verify these actually fetch before spending any generation money —")
    print(f"  python3 -m scripts.eval.fetch_article --manifest {out_path}")


if __name__ == "__main__":
    main()
