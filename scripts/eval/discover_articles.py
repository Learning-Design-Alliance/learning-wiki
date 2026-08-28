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
split, and ERIC is the majority share — it's the purpose-built education
research database, so even a loose keyword match against it stays on-topic.
PMC is general biomedical/life-sciences literature: live testing showed most
of its actually-fetchable hits were NOT learning science at all ("Canonical
Ru(ii) tris-polypyridyl complexes," "Fine-Tuned Regulation of mRNA
Translation") — the same keyword-collision problem arXiv had, just less
severe, and with no equivalent category filter available the way arXiv had
physics.ed-ph (PMC/PubMed has no reliably-scoped "education" subject filter
this project has verified). PMC stays in as a smaller supplementary source,
not the primary one.

arXiv defaults to 0: export.arxiv.org (the host behind search_arxiv's API
calls) serves a real, deliberate `User-agent: * / Disallow: /` for its
entire domain (verified live — see eval/SOURCES.md), so there is no
compliant way to query it via this script at all, not just a volume concern.
Real arXiv coverage instead uses the officially sanctioned Kaggle bulk
metadata snapshot (https://www.kaggle.com/datasets/Cornell-University/arxiv,
updated weekly). Any --arxiv > 0 is automatically resolved to a local copy
of that snapshot via resolve_arxiv_snapshot() — kagglehub downloads and
caches it on first use (auth from KAGGLE_USERNAME/KAGGLE_KEY, see
deploy/eval-harness.env.example), or pass --arxiv-snapshot <path> yourself
to use an already-downloaded file instead; see
build_arxiv_manifest_from_snapshot() below and eval/SOURCES.md — it's
restricted to the physics.ed-ph category, so its real yield is small by
design. This is a DISCOVERY step only — it
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
from datetime import date
from pathlib import Path

import requests

from . import compliance, pmc_aws

WIKI_ROOT = Path(__file__).parent.parent.parent
EVAL_ROOT = WIKI_ROOT / "eval"
TIMEOUT = 30

# Committed to git (small, text, a valuable historical record) — every
# article id that has ever reached generation (eval_harness.py run),
# so a later discovery batch doesn't re-spend the real cost (paid model
# calls) re-generating something already processed. Re-discovering and
# re-fetching a previously-failed-to-fetch article is cheap and sometimes
# even useful (a PMC article "not yet in the OA corpus" may become
# available later) — this registry is deliberately about the expensive
# step, not every step. Written by ingest_extractions.py after each run;
# read by load_excluded_ids() below, alongside the original benchmark
# manifest.json.
#
# "regardless of outcome" used to mean literally that — a single
# validation_failed touch excluded an id forever, identical to a genuinely
# successful ingest. That's wrong: a validator failure can be a transient
# bad roll, a prompt version that later improved, or a model that just had
# an off attempt — none of which mean the article can never become a good
# wiki page. "ingested" and "no_new_pages" ARE genuinely done (re-running
# either would produce a duplicate or the same no-contribution result) and
# stay excluded unconditionally; "validation_failed" instead gets a bounded
# number of separate batch exposures (MAX_VALIDATION_RETRY_ATTEMPTS) before
# giving up on it for good — see load_excluded_ids() and
# record_processed_articles().
PROCESSED_REGISTRY_PATH = EVAL_ROOT / "corpus" / "processed_articles.json"

# How many separate batch exposures (not correction-loop attempts within
# one run — eval_harness.py's max_correction_attempts already covers that)
# a validation_failed article gets before it's excluded for good. 3 batches
# x up to 3 correction attempts each (this project's current default) is
# still cheap in absolute terms (a few cents) for something that might
# otherwise be permanently unwritable wiki content.
MAX_VALIDATION_RETRY_ATTEMPTS = 3


def load_processed_registry() -> dict:
    if not PROCESSED_REGISTRY_PATH.exists():
        return {}
    try:
        return json.loads(PROCESSED_REGISTRY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def record_processed_articles(entries: dict) -> None:
    """Merge `entries` ({article_id: {outcome, run_id, model, pages}}) into
    the persistent registry, stamping today's date, and write it back.
    Tracks `attempts` — incremented each time an id is recorded — so
    load_excluded_ids() can tell "failed once, still worth trying again"
    apart from "failed repeatedly, genuinely not going to work." Never
    removes an existing entry; a later run touching the same id (expected
    now for a validation_failed id under the retry cap, not just a
    theoretical edge case) overwrites that id's outcome/run_id/model/pages
    while carrying its attempt count forward."""
    registry = load_processed_registry()
    today = date.today().isoformat()
    for article_id, info in entries.items():
        attempts = registry.get(article_id, {}).get("attempts", 0) + 1
        registry[article_id] = {**info, "date": today, "attempts": attempts}
    PROCESSED_REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_REGISTRY_PATH.write_text(
        json.dumps(registry, indent=2, sort_keys=True), encoding="utf-8"
    )


def load_excluded_ids() -> set:
    """Article ids a fresh discovery pass should never re-surface: the
    original 10-article benchmark corpus (manifest.json) plus the
    processed-articles registry — except a validation_failed id that
    hasn't yet used up its MAX_VALIDATION_RETRY_ATTEMPTS separate batch
    exposures stays OUT of this set, i.e. still eligible to be found again
    by the normal search machinery next time a matching batch runs (no
    special resurfacing logic needed — the same query just hits it again).
    The single source of truth for this union — both discover_articles.py's
    own main() and run_scrape_batch.py's run() call this instead of each
    keeping their own copy of the manifest.json-loading logic (they used
    to; that duplication is exactly how this kind of check silently drifts
    out of sync)."""
    ids = set()
    for article_id, info in load_processed_registry().items():
        if info.get("outcome") == "validation_failed" and info.get("attempts", 1) < MAX_VALIDATION_RETRY_ATTEMPTS:
            continue
        ids.add(article_id)
    manifest_path = EVAL_ROOT / "corpus" / "manifest.json"
    if manifest_path.exists():
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = {}
        existing_entries = existing if isinstance(existing, list) else existing.get("articles", [])
        ids |= {e["id"] for e in existing_entries}
    return ids

# See the module docstring — ERIC is the majority share (purpose-built
# education database, stays on-topic), PMC is a smaller supplementary source
# (general biomedical literature, real risk of off-topic keyword-collision
# hits), arXiv defaults to 0 (needs --arxiv-snapshot; see docstring).
DEFAULT_TARGETS = {"pmc": 200, "eric": 700, "arxiv": 0}

ARXIV_ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "opensearch": "http://a9.com/-/spec/opensearch/1.1/"}


class DiscoveryError(RuntimeError):
    pass


MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 5  # seconds; doubled each attempt if the server gives no Retry-After


def _get(url: str, params: dict = None) -> requests.Response:
    """Bounded, Retry-After-respecting retry on 429/503 — see fetch_article.py's
    _get() for why this is empirically justified (a live 429 from
    www.ncbi.nlm.nih.gov while well under NCBI's documented rate ceiling),
    not speculative hardening. compliance.guard() re-runs on every attempt,
    so a retry still respects our own rate floor on top of any backoff."""
    full_url = url if not params else f"{url}?{requests.compat.urlencode(params)}"
    for attempt in range(MAX_RETRIES + 1):
        compliance.guard(full_url)
        resp = requests.get(url, params=params, headers={"User-Agent": compliance.USER_AGENT}, timeout=TIMEOUT)
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
    subset via the "open access[filter]" ESearch tag, then cross-checked
    per-candidate against the PMC Article Datasets on AWS (pmc_aws.py) — the
    ESearch flag alone is best-effort, not a guarantee (a very recently
    published PMCID can be flagged OA before it's actually processed into
    that dataset); `is_pmc_openaccess` in the AWS metadata is ground truth.
    A candidate this check can't verify (network hiccup) is kept rather than
    dropped — this is a safety net on top of the ESearch flag, not a hard
    dependency — but one confirmed NOT in the OA subset is dropped here,
    before it costs an ESummary call or a manifest slot."""
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

    confirmed_ids = []
    dropped = 0
    for uid in ids:
        pmcid = f"PMC{uid}"
        try:
            aws_meta = pmc_aws.fetch_metadata(pmcid)
        except (requests.RequestException, ValueError) as e:
            print(f"  [WARN] Could not check {pmcid} against the PMC AWS dataset ({e}) — "
                  f"keeping it on the ESearch flag alone.", file=sys.stderr)
            confirmed_ids.append(uid)
            continue
        if aws_meta is not None and aws_meta.get("is_pmc_openaccess"):
            confirmed_ids.append(uid)
        else:
            dropped += 1
    if dropped:
        print(f"  [pmc-oa] {query!r}: dropped {dropped}/{len(ids)} hit(s) not confirmed in the "
              f"PMC Open Access subset.")
    ids = confirmed_ids
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
            "fetch_url": pmc_aws.metadata_url(pmcid),
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

ARXIV_KAGGLE_HANDLE = "Cornell-University/arxiv"
ARXIV_SNAPSHOT_FILENAME = "arxiv-metadata-oai-snapshot.json"


def resolve_arxiv_snapshot(explicit_path: str = None) -> Path:
    """Returns a local path to the Kaggle arXiv metadata snapshot file (see
    build_arxiv_manifest_from_snapshot()'s docstring for its format).

    If explicit_path is given and actually exists, it's used as-is — this
    lets an already-downloaded file, or a non-default location, override
    the default. Otherwise the dataset is fetched via kagglehub, which
    authenticates from KAGGLE_USERNAME/KAGGLE_KEY (see
    deploy/eval-harness.env.example — already loaded into this process's
    environment the same way OPENROUTER_API_KEY etc. are) and maintains its
    own on-disk cache (~/.cache/kagglehub by default), so only the very
    first call ever actually downloads anything; every call after that,
    including every later scrape batch, resolves instantly from cache.
    """
    if explicit_path:
        p = Path(explicit_path)
        if p.is_file():
            return p

    try:
        import kagglehub
    except ImportError as e:
        raise DiscoveryError(
            f"No local --arxiv-snapshot file given/found, and kagglehub isn't installed "
            f"(`pip install kagglehub` — already in requirements-eval.txt) to auto-download "
            f"{ARXIV_KAGGLE_HANDLE!r}. See eval/SOURCES.md."
        ) from e

    try:
        dataset_dir = Path(kagglehub.dataset_download(ARXIV_KAGGLE_HANDLE))
    except Exception as e:
        raise DiscoveryError(
            f"kagglehub could not download {ARXIV_KAGGLE_HANDLE!r}: {e}. Check KAGGLE_USERNAME/"
            f"KAGGLE_KEY in /etc/eval-harness.env (see deploy/eval-harness.env.example)."
        ) from e

    snapshot_path = dataset_dir / ARXIV_SNAPSHOT_FILENAME
    if not snapshot_path.is_file():
        candidates = list(dataset_dir.glob("*.json"))
        if len(candidates) == 1:
            snapshot_path = candidates[0]
        else:
            raise DiscoveryError(
                f"kagglehub downloaded {dataset_dir} but couldn't find {ARXIV_SNAPSHOT_FILENAME} "
                f"in it (found: {sorted(p.name for p in dataset_dir.iterdir())})."
            )
    return snapshot_path


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
    lines, re-scanning per topic would be far too slow. Restricted first to
    the physics.ed-ph category (Physics Education Research) — arXiv doesn't
    have a general education-research corpus the way PMC/ERIC do, and a bare
    keyword match against ALL of arXiv produces real false positives: an
    early test hit "activation" (one of our wiki topics) matching "Resonant
    activation in bistable semiconductor lasers," a paper with nothing to do
    with learning science. physics.ed-ph is arXiv's one category that's
    actually about pedagogy, so within it a keyword match is far more likely
    to be genuinely relevant. This makes arXiv's real yield here small and
    that's expected, not a bug — see the module docstring on why arXiv is
    weighted small overall.

    Within that category, topic targets are round-robined and a paper counts
    toward the first topic (in wiki order) whose target isn't yet met and
    whose phrase appears, case-insensitively, in that paper's title or
    abstract — a coarse substring match, not a real search index, but the
    category restriction above is what actually keeps results on-topic; the
    prefetch-verify and downstream judging steps are what validate each
    article beyond that, same as every other source here.
    """
    RELEVANT_CATEGORIES = {"physics.ed-ph"}
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
            paper_categories = set((paper.get("categories") or "").split())
            if not (paper_categories & RELEVANT_CATEGORIES):
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
                              "robots.txt disallows all automated access; any value > 0 is sourced "
                              "from the offline Kaggle metadata snapshot, auto-downloaded via "
                              "kagglehub if --arxiv-snapshot isn't given — see resolve_arxiv_snapshot())")
    parser.add_argument("--arxiv-snapshot", default=None,
                         help="Path to an already-downloaded Kaggle arXiv metadata snapshot "
                              "(arxiv-metadata-oai-snapshot.json from "
                              "https://www.kaggle.com/datasets/Cornell-University/arxiv). Omit to "
                              "have it auto-downloaded via kagglehub instead (needs KAGGLE_USERNAME/"
                              "KAGGLE_KEY — see deploy/eval-harness.env.example).")
    parser.add_argument("--out", default=str(EVAL_ROOT / "corpus" / "manifest_bulk.json"),
                         help="Output manifest path (default: eval/corpus/manifest_bulk.json — "
                              "deliberately NOT manifest.json, so the original 10-article benchmark stays intact)")
    parser.add_argument("--refresh-cache", action="store_true",
                         help="Ignore cached per-topic PMC/ERIC search results and re-query live "
                              "(cache lives at eval/corpus/.discovery_cache.json)")
    args = parser.parse_args()

    existing_ids = load_excluded_ids()
    print(f"Excluding {len(existing_ids)} already-known article id(s) "
          f"(benchmark manifest + processed-articles registry).")

    topics = topics_from_wiki()
    if not topics:
        print("[ERROR] No topics found in theories/ or principles/ — is this running from the wiki root?")
        sys.exit(1)
    print(f"Seeded {len(topics)} search topics from theories/ + principles/.\n")

    targets = {"pmc": args.pmc, "eric": args.eric}
    manifest = build_manifest(targets, topics, existing_ids, use_cache=not args.refresh_cache)

    if args.arxiv > 0:
        # Always resolved to a local snapshot file — either the explicit
        # --arxiv-snapshot path, or an on-demand kagglehub download/cache
        # hit — never the live API, which export.arxiv.org's robots.txt
        # disallows outright. See resolve_arxiv_snapshot()'s docstring.
        snapshot_path = resolve_arxiv_snapshot(args.arxiv_snapshot)
        arxiv_entries = build_arxiv_manifest_from_snapshot(
            snapshot_path, topics, args.arxiv,
            existing_ids | {e["id"] for e in manifest},
        )
        manifest.extend(arxiv_entries)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # {"articles": [...]} — matches manifest.json's own shape exactly (see
    # fetch_article.py's main(), which reads manifest["articles"]) so this
    # drops straight into the existing prefetch-verify step with no
    # translation step in between.
    try:
        out_path.write_text(json.dumps({"articles": manifest}, indent=2), encoding="utf-8")
    except PermissionError as e:
        # A bare traceback here is actively misleading: this run's freshly
        # discovered manifest silently never reaches disk, so a downstream
        # fetch_article.py call reads the OLD stale file instead and looks
        # like nothing changed — burned a full debugging round here already,
        # tracing back to an earlier run (as a different user, e.g. root vs
        # evalrunner) having created out_path with different ownership.
        raise DiscoveryError(
            f"Permission denied writing {out_path} ({e}). This means the file already "
            f"exists, owned by a different user than the one running this now (e.g. an "
            f"earlier run as root, now being overwritten by evalrunner). Fix: "
            f"sudo rm -f {out_path} (safe — it's a regenerable output, not source of "
            f"truth) and re-run. Do NOT re-run fetch_article.py against the old file; "
            f"its results would silently be stale."
        ) from e

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
