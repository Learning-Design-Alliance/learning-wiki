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
split. arXiv defaults to 0: export.arxiv.org (the host behind search_arxiv's
API calls) serves a real, deliberate `User-agent: * / Disallow: /` for its
entire domain (verified live — see eval/SOURCES.md), so there is no
compliant way to query it via this script at all, not just a volume concern.
Pass --arxiv > 0 with no --arxiv-snapshot to try the live API anyway
(compliance.py will correctly block it; this isn't a bug to route around).
Real arXiv coverage instead uses the officially sanctioned Kaggle bulk
metadata snapshot (https://www.kaggle.com/datasets/Cornell-University/arxiv,
updated weekly) — download it yourself (needs a Kaggle account API token)
and pass --arxiv-snapshot <path to arxiv-metadata-oai-snapshot.json>; see
build_arxiv_manifest_from_snapshot() below and eval/SOURCES.md. PMC
(1 req/s) and ERIC (2s/req) scale to hundreds/thousands of individual
fetches fine, so this weights entirely toward those two. This is a
DISCOVERY step only — it
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
DEFAULT_TARGETS = {"pmc": 700, "eric": 260, "arxiv": 0}

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
    """Returns manifest-shaped entries, restricted client-side to ED-prefixed
    ERIC ids. ERIC uses two id prefixes: EJ ("ERIC Journal" — bibliographic
    metadata only; the actual text stays with the original journal
    publisher, ERIC has no redistribution rights) and ED ("ERIC Document" —
    reports, conference papers, theses, and other grey literature ERIC does
    have the rights to host full-text on files.eric.ed.gov). There is no
    documented API field or query filter for this distinction (checked the
    raw response schema directly — no such field is present); this was
    confirmed empirically instead: every EJ-prefixed hit in an early test
    batch 404'd against fulltext/<id>.pdf, while ED-prefixed ids match what
    fetch_article.py can actually fetch. The filter is client-side, so this
    over-fetches (asks the API for more than `rows`) to still hit the target
    after EJ hits are discarded."""
    params = {
        "search": query,
        "format": "json",
        "rows": str(min(rows * 4, 200)),
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
        if not eric_id.upper().startswith("ED"):
            continue
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
        if len(entries) >= rows:
            break
    return entries


SEARCH_FNS = {"pmc": search_pmc, "arxiv": search_arxiv, "eric": search_eric}

# Per-topic search results, keyed by "source::topic::count" — re-running this
# script from scratch (e.g. after a downstream bug forced a fix + re-run)
# was re-hitting PMC/ERIC's live APIs for the same 137 topics every time:
# wasteful for them and slow for us. A cache hit skips the live call
# entirely; --refresh-cache (or use_cache=False) bypasses it.
DISCOVERY_CACHE_PATH = EVAL_ROOT / "corpus" / ".discovery_cache.json"


def _load_discovery_cache() -> dict:
    if DISCOVERY_CACHE_PATH.exists():
        try:
            return json.loads(DISCOVERY_CACHE_PATH.read_text(encoding="utf-8"))
        except ValueError:
            return {}
    return {}


def _save_discovery_cache(cache: dict) -> None:
    DISCOVERY_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    DISCOVERY_CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def build_manifest(targets: dict, topics: list, existing_ids: set, verbose: bool = True,
                    use_cache: bool = True) -> list:
    """Round-robins every topic across each source until that source's
    target count is met or topics run out, deduplicating against
    existing_ids (already in the benchmark manifest) and against itself.
    Dedup happens fresh on every run even for a cached topic result, so a
    changed existing_ids/seen_ids set is still respected correctly.

    A single topic's search call failing (compliance block, transient network
    error, malformed response) is logged and skipped rather than aborting the
    whole run — losing every already-collected result to one bad topic burned
    a real run of this script (PMC's 20/20 was discarded twice by a later
    ERIC/arXiv failure before this got fixed)."""
    manifest = []
    seen_ids = set(existing_ids)
    cache = _load_discovery_cache() if use_cache else {}

    for source, target in targets.items():
        fn = SEARCH_FNS[source]
        per_topic_counts = _round_robin_counts(topics, target)
        collected = 0
        for topic, count in zip(topics, per_topic_counts):
            if collected >= target:
                break
            cache_key = f"{source}::{topic}::{count}"
            if use_cache and cache_key in cache:
                if verbose:
                    print(f"[{source}] {topic!r} (cached, have {collected}/{target})...")
                results = cache[cache_key]
            else:
                if verbose:
                    print(f"[{source}] searching {topic!r} (have {collected}/{target})...")
                try:
                    results = fn(topic, count)
                except Exception as e:  # noqa: BLE001 - one bad topic must not lose everything else
                    print(f"  [WARN] {source} search failed for {topic!r}: {e}", file=sys.stderr)
                    continue
                if use_cache:
                    cache[cache_key] = results
                    _save_discovery_cache(cache)  # written per-topic, not just at the end, so a
                                                   # crash partway through doesn't lose progress
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


# ---------------------------------------------------------------------------
# arXiv via the Kaggle bulk metadata snapshot (offline — see module
# docstring for why the live API is unusable and eval/SOURCES.md for the
# verified robots.txt finding).
# ---------------------------------------------------------------------------

def build_arxiv_manifest_from_snapshot(snapshot_path: Path, topics: list, target: int,
                                        existing_ids: set, verbose: bool = True) -> list:
    """Single streaming pass over a downloaded Kaggle arXiv metadata snapshot
    (https://www.kaggle.com/datasets/Cornell-University/arxiv — JSON Lines,
    one paper object per line with id/title/abstract/authors/versions/...;
    the maintainer updates it weekly, so it lags live arXiv by at most a few
    days). This replaces search_arxiv()'s live API call, which
    export.arxiv.org's robots.txt genuinely disallows in full. Only the
    metadata comes from this offline file — the actual PDF fetch later, in
    fetch_article.py, still hits the network, against arxiv.org's /pdf/<id>
    path (a different, permitted host from export.arxiv.org), gated by
    compliance.py's existing 15s-per-request floor for it.

    One pass over the whole file, not one pass per topic — with millions of
    lines, re-scanning per topic would be far too slow. Topic targets are
    round-robined and a paper counts toward the first topic (in wiki order)
    whose target isn't yet met and whose phrase appears, case-insensitively,
    in that paper's title or abstract. This is a coarse substring match, not
    a real search index — good enough for "gather plausible candidates," not
    a precision claim; the prefetch-verify and downstream judging steps are
    what actually validate each article, same as every other source here.
    """
    if not snapshot_path.exists():
        raise DiscoveryError(
            f"arXiv snapshot not found at {snapshot_path}. Download it first (needs a "
            f"Kaggle account API token at ~/.kaggle/kaggle.json): "
            f"kaggle datasets download -d Cornell-University/arxiv -p <dir> --unzip"
        )

    remaining = dict(zip(topics, _round_robin_counts(topics, target)))
    seen_ids = set(existing_ids)
    manifest = []
    scanned = 0

    with snapshot_path.open("r", encoding="utf-8") as f:
        for line in f:
            if len(manifest) >= target or not any(v > 0 for v in remaining.values()):
                break
            scanned += 1
            if verbose and scanned % 200_000 == 0:
                print(f"[arxiv-snapshot] scanned {scanned:,} lines, {len(manifest)}/{target} found...")
            try:
                paper = json.loads(line)
            except ValueError:
                continue

            arxiv_id = (paper.get("id") or "").strip()
            entry_id = f"arxiv-{arxiv_id}"
            if not arxiv_id or entry_id in seen_ids:
                continue
            title = " ".join((paper.get("title") or "").split())
            abstract = " ".join((paper.get("abstract") or "").split())
            if not title:
                continue
            haystack = f"{title} {abstract}".lower()

            for topic, need in remaining.items():
                if need <= 0 or topic.lower() not in haystack:
                    continue
                year = None
                versions = paper.get("versions") or []
                date_str = versions[0].get("created") if versions else paper.get("update_date")
                if date_str:
                    m = re.search(r"\b(19|20)\d{2}\b", str(date_str))
                    if m:
                        year = int(m.group(0))
                manifest.append({
                    "id": entry_id,
                    "source": "arxiv",
                    "title": title,
                    "authors": paper.get("authors") or "et al.",
                    "year": year,
                    "url": f"https://arxiv.org/abs/{arxiv_id}",
                    "fetch_url": f"https://arxiv.org/pdf/{arxiv_id}",
                    "topic_hint": topic,
                })
                seen_ids.add(entry_id)
                remaining[topic] -= 1
                break  # one paper counts toward one topic only

    if verbose:
        print(f"[arxiv-snapshot] done: {len(manifest)}/{target} candidates found "
              f"(scanned {scanned:,} lines)\n")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pmc", type=int, default=DEFAULT_TARGETS["pmc"], help="Target PMC candidate count")
    parser.add_argument("--eric", type=int, default=DEFAULT_TARGETS["eric"], help="Target ERIC candidate count")
    parser.add_argument("--arxiv", type=int, default=DEFAULT_TARGETS["arxiv"],
                         help="Target arXiv candidate count (default 0 — export.arxiv.org's "
                              "robots.txt disallows all automated access; pass --arxiv-snapshot "
                              "to source candidates from the offline Kaggle metadata dump instead)")
    parser.add_argument("--arxiv-snapshot", default=None,
                         help="Path to a downloaded Kaggle arXiv metadata snapshot "
                              "(arxiv-metadata-oai-snapshot.json from "
                              "https://www.kaggle.com/datasets/Cornell-University/arxiv). If given "
                              "and --arxiv > 0, arXiv candidates come from this file instead of the "
                              "(blocked) live API.")
    parser.add_argument("--out", default=str(EVAL_ROOT / "corpus" / "manifest_bulk.json"),
                         help="Output manifest path (default: eval/corpus/manifest_bulk.json — "
                              "deliberately NOT manifest.json, so the original 10-article benchmark stays intact)")
    parser.add_argument("--refresh-cache", action="store_true",
                         help="Ignore cached per-topic PMC/ERIC search results and re-query live "
                              "(cache lives at eval/corpus/.discovery_cache.json)")
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

    targets = {"pmc": args.pmc, "eric": args.eric}
    if args.arxiv > 0 and not args.arxiv_snapshot:
        # No snapshot given — attempt the live API anyway via the normal
        # per-source loop, which now degrades gracefully (warns and moves on)
        # instead of aborting the whole run when compliance.py blocks it.
        targets["arxiv"] = args.arxiv
    manifest = build_manifest(targets, topics, existing_ids, use_cache=not args.refresh_cache)

    if args.arxiv > 0 and args.arxiv_snapshot:
        arxiv_entries = build_arxiv_manifest_from_snapshot(
            Path(args.arxiv_snapshot), topics, args.arxiv,
            existing_ids | {e["id"] for e in manifest},
        )
        manifest.extend(arxiv_entries)

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
