#!/usr/bin/env python3
"""
source_lists.py — how much of a curated list the wiki has read, and a queue of the rest.

Two curated lists come before any ERIC, arXiv or PubMed topic search (maintainer,
2026-10-07): they are other people's selections of the research that matters, where a
topic sweep finds whatever full text happens to be open.

    hub    The Learning Agency's Renaissance AI and Education Resource Hub
           (github.com/jchoi92k/Learning-Engineering-Resource-Hub), read from its
           published data.json: ~3,900 entries from WWC, Evidence for ESSA, Mathematica,
           Campbell, Brookings, WestEd, RELs and others. **That repo has no licence,
           so nothing from it is committed here** (CLAUDE.md): the list is read at run
           time and the queue is written under eval/runs/, which is ignored.
    aied   The AI in Education Knowledge Base (github.com/edtechdev/aied), one page per
           paper under content/en/articles: ~1,650 papers, mostly arXiv and DOI-bearing
           journal articles. Its content is CC0.
    journal Every open-access article and review a journal has published, by ISSN, from
           OpenAlex (`--issn`, repeatable): the field's own journals, read whole rather
           than sampled by topic (maintainer, 2026-10-18: "every journal of the learning
           sciences open source article"). Only works OpenAlex marks open access are
           listed, each with its best open copy; editorials, errata and book reviews are
           left out by OpenAlex's type and by title.

For each entry it decides:

    covered    the manifest already records it (by catalogue id, DOI, or normalised
               title), ingested or rejected; or a wiki page already cites its URL or DOI
    skip       not a source the wiki ingests (a dataset, tool, platform or code entry), or
               one whose site's robots.txt refuses crawlers, which the pipeline respects
    queued     everything else, with a fetch route:
                 arxiv   the arXiv PDF (an arXiv id is known)
                 web     the publisher's page or its PDF (fetch_article's "web" source)
               An entry with only a DOI is queued as `web` on https://doi.org/<doi>, which
               lands on the publisher; a paywalled one fails at fetch and stays eligible.

The queue is ordered: the hub's research domain first (WWC, Evidence for ESSA, Campbell,
Mathematica, RELs and the two journals ahead of the rest), then learning-engineering
practice, then policy; then the AIED list. Each line is a manifest entry
`run_scrape_batch.py --queue` takes from, so a batch reads the next N entries nothing
has settled.

    python3 scripts/eval/source_lists.py --list hub  --report
    python3 scripts/eval/source_lists.py --list hub  --queue eval/runs/queues/hub.ndjson
    python3 scripts/eval/source_lists.py --list aied --source ~/aied --queue eval/runs/queues/aied.ndjson
    python3 scripts/eval/source_lists.py --list hub  --campbell eval/runs/queues/campbell.ndjson
    python3 scripts/eval/source_lists.py --list journal --issn 1050-8406 --queue eval/runs/queues/jls.ndjson
"""
import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
HUB_DATA = "https://jchoi92k.github.io/Learning-Engineering-Resource-Hub/data.json"
AIED_REPO = "https://github.com/edtechdev/aied.git"
SKIP_TYPES = {"dataset", "tool", "platform", "code", "project-website"}
HUB_DOMAIN_ORDER = {"research": 0, "le-practice": 1, "policy": 2, "datasets": 9}
HUB_SOURCE_ORDER = ["What Works Clearinghouse", "Evidence for ESSA", "Campbell Collaboration",
                    "Mathematica", "IES Regional Education Labs", "Journal of Educational Data Mining",
                    "Journal of Learning Analytics", "AIMS Collaboratory", "CREDO at Stanford",
                    "UChicago Consortium on School Research", "NWEA Research", "WestEd"]
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>)\]]+")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})|raw/papers/(\d{4}\.\d{4,5})")


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def clean_doi(d: str) -> str:
    return (d or "").strip().rstrip(".,;").lower()


# ---------------------------------------------------------------- loading the lists

def load_hub(source: str = None) -> list:
    import requests
    if source and Path(source).exists():
        data = json.loads(Path(source).read_text(encoding="utf-8"))
    else:
        data = requests.get(source or HUB_DATA, timeout=60).json()
    out = []
    for e in data["entries"]:
        url = e.get("document_url") or e.get("url")
        doi = clean_doi((DOI_RE.search(url or "") or [None])[0] if url else "")
        out.append({"list": "hub", "key": f"hub-{e['num']}", "title": e.get("title", ""),
                    "url": e.get("url"), "fetch_url": url, "doi": doi or None, "arxiv": None,
                    "type": e.get("type"), "group": e.get("source"), "domain": e.get("domain"),
                    "year": (e.get("published_date") or "")[:4] or None, "authors": e.get("authors")})
    return out


def load_aied(source: str = None) -> list:
    root = Path(source) if source else None
    if root is None or not root.exists():
        root = WIKI_ROOT / ".cache" / "aied"
        if not root.exists():
            subprocess.run(["git", "clone", "-q", "--depth", "1", AIED_REPO, str(root)], check=True)
    out = []
    for p in sorted((root / "content" / "en" / "articles").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        title = re.search(r'^title:\s*"?(.+?)"?\s*$', text, re.M)
        arx = ARXIV_RE.search(text)
        doi = DOI_RE.search(re.sub(r"\[\[[^\]]*\]\]", "", text))
        arxiv = (arx.group(1) or arx.group(2)) if arx else None
        doi = clean_doi(doi.group(0)) if doi else None
        if doi and doi.startswith("10.48550/arxiv."):          # arXiv's own DOI
            arxiv = arxiv or doi.split("arxiv.")[1]
            doi = None
        url = (f"https://arxiv.org/pdf/{arxiv}" if arxiv else f"https://doi.org/{doi}" if doi else None)
        out.append({"list": "aied", "key": f"aied-{p.stem}", "title": title.group(1) if title else p.stem,
                    "url": url, "fetch_url": url, "doi": doi, "arxiv": arxiv, "type": "paper",
                    "group": "AI in Education Knowledge Base", "domain": "research", "year": None,
                    "authors": None})
    return out


OPENALEX = "https://api.openalex.org/works"
NOT_RESEARCH_TITLE = re.compile(r"^(editorial|erratum|correction|corrigendum|book review|review of |"
                                r"introduction to the special issue|in memoriam|reviewers|call for|remembrance|a memorial|"
                                r"remembering|obituary)|tribute to", re.I)


# Publishers whose servers refuse the fetcher even for open-access articles (403 on every
# Taylor & Francis PDF in the first JLS batch, 2026-10-18): a repository copy is used instead.
BLOCKING_HOSTS = ("tandfonline.com",)


def open_copy(w: dict) -> "str | None":
    """The best open copy of a work the fetcher can read: OpenAlex's best location unless
    its host refuses fetchers, then any other open location, repository copies first."""
    locs = [w.get("best_oa_location") or {}] + sorted(
        (l for l in w.get("locations") or [] if l.get("is_oa")),
        key=lambda l: 0 if ((l.get("source") or {}).get("type") == "repository") else 1)
    for l in locs:
        url = l.get("pdf_url") or l.get("landing_page_url")
        if url and not re.search(r"ezproxy|/login", url) and not any(h in url for h in BLOCKING_HOSTS):
            return url
    return None


def load_journal(issns: list) -> list:
    """Open-access articles and reviews from journals given by ISSN, newest first. OpenAlex
    first; when its shared daily budget is spent (429 on every retry), Crossref and Unpaywall."""
    import requests
    out = []
    for issn in issns:
        try:
            out += _journal_openalex(issn)
        except requests.HTTPError as e:
            if e.response is None or e.response.status_code not in (401, 403, 429):
                raise
            print(f"OpenAlex budget spent; listing {issn} from Crossref and Unpaywall", file=sys.stderr)
            out += _journal_crossref(issn)
    return out


def _unpaywall_copy(doi: str) -> "str | None":
    """A readable open copy from Unpaywall, by the same rule as open_copy()."""
    import requests
    for attempt in range(3):
        try:
            r = requests.get(f"https://api.unpaywall.org/v2/{doi}", timeout=30,
                             params={"email": "contact@learningdesignalliance.org"})
        except requests.RequestException:
            time.sleep(3)
            continue
        if r.status_code in (429, 503):
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code != 200:
            return None
        d = r.json()
        locs = [d.get("best_oa_location") or {}] + sorted(
            d.get("oa_locations") or [], key=lambda l: 0 if l.get("host_type") == "repository" else 1)
        for l in locs:
            url = l.get("url_for_pdf") or l.get("url")
            if url and not re.search(r"ezproxy|/login", url) and not any(h in url for h in BLOCKING_HOSTS):
                return url
        return None
    return None


def _journal_crossref(issn: str) -> list:
    import requests
    from concurrent.futures import ThreadPoolExecutor
    works, cursor = [], "*"
    while cursor:
        r = requests.get(f"https://api.crossref.org/journals/{issn}/works", timeout=60, params={
            "filter": "type:journal-article", "rows": 1000, "cursor": cursor,
            "select": "DOI,title,author,issued", "mailto": "contact@learningdesignalliance.org"})
        r.raise_for_status()
        items = r.json()["message"]["items"]
        works += items
        cursor = r.json()["message"].get("next-cursor") if items else None
    src = issn
    works = [w for w in works if (w.get("title") or [""])[0] and not NOT_RESEARCH_TITLE.search(w["title"][0])]
    with ThreadPoolExecutor(8) as ex:
        urls = list(ex.map(lambda w: _unpaywall_copy(w["DOI"].lower()), works))
    out = []
    for w, url in zip(works, urls):
        if not url:
            continue
        doi = clean_doi(w["DOI"])
        names = [a.get("family", "") for a in (w.get("author") or [])[:3] if a.get("family")]
        year = str(((w.get("issued") or {}).get("date-parts") or [[None]])[0][0] or "")
        out.append({"list": "journal", "key": "jrnl-" + hashlib.sha1(doi.encode()).hexdigest()[:12],
                    "title": w["title"][0], "url": f"https://doi.org/{doi}", "fetch_url": url, "doi": doi,
                    "arxiv": None, "type": "article", "group": src, "domain": "research", "year": year,
                    "authors": ", ".join(names) or None})
    return out


def _journal_openalex(issn: str) -> list:
    import requests
    out = []
    cursor = "*"
    while cursor:
        for wait in (0, 5, 20):                         # OpenAlex answers bursts with 429
            time.sleep(wait)
            r = requests.get(OPENALEX, timeout=60, params={
                "filter": f"primary_location.source.issn:{issn},is_oa:true,type:article|review",
                "per-page": 200, "cursor": cursor, "mailto": "contact@learningdesignalliance.org",
                "select": "id,doi,title,publication_year,authorships,best_oa_location,locations,primary_location,type"})
            if r.status_code != 429:
                break
        r.raise_for_status()
        d = r.json()
        for w in d["results"]:
            title = w.get("title") or ""
            if not title or NOT_RESEARCH_TITLE.search(title):
                continue
            url = open_copy(w)
            doi = clean_doi((w.get("doi") or "").replace("https://doi.org/", ""))
            names = [a["author"]["display_name"].split()[-1] for a in w.get("authorships", [])[:3]
                     if a.get("author", {}).get("display_name")]
            src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or issn
            out.append({"list": "journal", "key": "jrnl-" + w["id"].rsplit("/", 1)[-1].lower(),
                        "title": title, "url": f"https://doi.org/{doi}" if doi else url,
                        "fetch_url": url,
                        "doi": doi or None, "arxiv": None, "type": w.get("type"), "group": src,
                        "domain": "research", "year": str(w.get("publication_year") or ""),
                        "authors": ", ".join(names) or None})
        cursor = d["meta"].get("next_cursor")
    return out


# ---------------------------------------------------------------- coverage

def wiki_citations() -> tuple:
    """Every DOI and URL a content page carries, read once."""
    dois, urls = set(), set()
    for folder in ("claims", "principles", "patterns", "elements", "strategies", "theories", "designs",
                   "processes", "methods", "learner-variables"):
        for p in (WIKI_ROOT / folder).glob("*.md"):
            t = p.read_text(encoding="utf-8")
            dois.update(clean_doi(d) for d in DOI_RE.findall(t))
            urls.update(u.rstrip("/").lower() for u in re.findall(r"https?://[^\s)<>\"\]]+", t))
    return dois, urls


def manifest_index() -> tuple:
    ids, dois, titles = {}, {}, {}
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        m = json.loads(line)
        ids[m["id"]] = m["status"]
        if m.get("doi"):
            dois[clean_doi(m["doi"])] = m["status"]
        if m.get("title"):
            titles[norm_title(m["title"])] = m["status"]
    return ids, dois, titles


def classify(entries: list) -> list:
    ids, mdois, mtitles = manifest_index()
    wdois, wurls = wiki_citations()
    for e in entries:
        mid = (f"arxiv-{e['arxiv']}" if e["arxiv"] else None)
        how = None
        if e["key"] in ids or (mid and mid in ids):
            how = "manifest id"
        elif e["doi"] and e["doi"] in mdois:
            how = "manifest doi"
        elif norm_title(e["title"]) in mtitles and len(norm_title(e["title"])) > 25:
            how = "manifest title"
        elif e["doi"] and e["doi"] in wdois:
            how = "cited doi"
        elif e["url"] and e["url"].rstrip("/").lower() in wurls:
            how = "cited url"
        if how:
            e["state"], e["why"] = "covered", how
        elif (e.get("type") or "") in SKIP_TYPES or e.get("domain") == "datasets":
            e["state"], e["why"] = "skip", f"type {e.get('type')}"
        elif not e["fetch_url"]:
            e["state"], e["why"] = "skip", ("no copy the fetcher can read" if e["list"] == "journal"
                                            else "no URL, DOI or arXiv id")
        elif not e["arxiv"] and not robots_allows(e["fetch_url"]):
            e["state"], e["why"] = "skip", "robots.txt disallows"
        else:
            e["state"], e["why"] = "queued", "arxiv" if e["arxiv"] else "web"
    return entries


def eric_twin(e: dict) -> "dict | None":
    """The same work in ERIC, with full text ERIC hosts, found by its title through
    ERIC's own API. Many WestEd, Learning Policy Institute and Education Trust reports
    are deposited there, and ERIC is the sanctioned route to them where the publisher's
    robots.txt refuses crawlers. Accepted only on an exact normalised-title match."""
    from eval import discover_articles as da
    title = e["title"]
    words = [w for w in re.findall(r"[A-Za-z]{4,}", title)][:12]
    if len(words) < 3:
        return None
    for hit in da.search_eric('title:(' + " ".join(words) + ')', 5):
        if norm_title(hit["title"]) == norm_title(title):
            return {**hit, "topic_hint": f"{e['list']}: {e['group']} (via ERIC)", "list_key": e["key"]}
    return None


CAMPBELL_ISSN = "1891-1803"  # Campbell Systematic Reviews


def campbell_pmc_twin(e: dict) -> "dict | None":
    """The PubMed Central copy of a Campbell Collaboration review.

    Campbell's review pages are rendered by JavaScript, so the `web` fetch reads an empty
    shell, and Wiley, which publishes *Campbell Systematic Reviews*, refuses automated PDF
    downloads (403). Reviews published since the journal moved to Wiley (2018) are
    deposited in PMC, which the pipeline fetches through the PMC Article Datasets on AWS.
    So: the review's DOI from Crossref, by title within the journal's ISSN, then its PMC
    record by DOI.

    A DOI is accepted only when the registry title is the hub's title, or the hub's title
    followed by a short subtitle ("...: A systematic review"); a protocol is never taken
    for its review, though the two share most of a title. Where several versions match
    (a review and its update), the latest is taken. Older reviews (10.4073/csr.*) have no
    PMC copy and return None."""
    from eval import discover_articles as da
    want = norm_title(e["title"])
    if len(want.split()) < 4:
        return None
    items = da._get("https://api.crossref.org/works", {
        "query.bibliographic": e["title"], "filter": f"issn:{CAMPBELL_ISSN}", "rows": 5,
    }).json()["message"]["items"]
    best = None
    for it in items:
        got = norm_title((it.get("title") or [""])[0])
        if got.startswith("protocol") or not got.startswith(want):
            continue
        if len(got.split()) - len(want.split()) > 6:
            continue
        issued = tuple((it.get("issued") or {}).get("date-parts", [[0]])[0])
        if best is None or issued > best[0]:
            best = (issued, it)
    if not best:
        return None
    doi = best[1]["DOI"].lower()
    ids = da._get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                  {"db": "pmc", "term": f"{doi}[doi]", "retmode": "json"}).json()["esearchresult"]["idlist"]
    if len(ids) != 1:
        return None
    uid = ids[0]
    pmcid = f"PMC{uid}"
    year = best[0][0] if best[0] and best[0][0] else None
    return {"id": f"pmc-{uid}", "source": "pubmed", "pmcid": pmcid,
            "title": (best[1].get("title") or [e["title"]])[0], "authors": e.get("authors") or "et al.",
            "year": year, "doi": doi, "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}",
            "fetch_url": da.pmc_aws.metadata_url(pmcid),
            "topic_hint": f"{e['list']}: {e['group']} (via PMC)", "list_key": e["key"]}


def robots_allows(url: str) -> bool:
    """The same robots.txt check every fetch makes (compliance.check_allowed), made
    up front so a batch does not spend its slots on a site that refuses crawlers:
    WestEd, the Learning Policy Institute and Education Trust did on 2026-10-07. A
    robots.txt that cannot be read is not a refusal, as in the fetch itself."""
    sys.path.insert(0, str(WIKI_ROOT / "scripts"))
    from eval import compliance
    try:
        compliance.check_allowed(url)
        return True
    except compliance.ComplianceError:
        return False


def priority(e: dict) -> tuple:
    grp = HUB_SOURCE_ORDER.index(e["group"]) if e["group"] in HUB_SOURCE_ORDER else len(HUB_SOURCE_ORDER)
    return (0 if e["list"] == "hub" else 1, HUB_DOMAIN_ORDER.get(e.get("domain"), 5), grp,
            0 if e.get("type") in ("paper", "review", "report", "article") else 1, e["key"])


def manifest_entry(e: dict) -> dict:
    """The shape discover_articles writes and fetch_article reads."""
    if e["arxiv"]:
        return {"id": f"arxiv-{e['arxiv']}", "source": "arxiv", "title": e["title"],
                "authors": e.get("authors") or "et al.", "year": e.get("year"),
                "url": f"https://arxiv.org/abs/{e['arxiv']}", "fetch_url": f"https://arxiv.org/pdf/{e['arxiv']}",
                "topic_hint": f"{e['list']}: {e['group']}", "list_key": e["key"]}
    # A stable id from the list key: the hub's `num` and AIED's slug are stable in their repos.
    sid = e["key"] if len(e["key"]) < 80 else e["list"] + "-" + hashlib.sha1(e["key"].encode()).hexdigest()[:12]
    return {"id": sid, "source": "web", "title": e["title"], "authors": e.get("authors") or "et al.",
            "year": int(e["year"]) if (e.get("year") or "").isdigit() else None,
            "url": e["url"], "fetch_url": e["fetch_url"], "doi": e["doi"],
            "topic_hint": f"{e['list']}: {e['group']}", "list_key": e["key"]}


def report(entries: list) -> None:
    by = collections.Counter(e["state"] for e in entries)
    print(f"{len(entries)} entries: {dict(by)}")
    print("covered by:", dict(collections.Counter(e["why"] for e in entries if e["state"] == "covered")))
    print("skipped:", dict(collections.Counter(e["why"] for e in entries if e["state"] == "skip")))
    print("queued by route:", dict(collections.Counter(e["why"] for e in entries if e["state"] == "queued")))
    rows = collections.defaultdict(collections.Counter)
    for e in entries:
        rows[(e.get("domain"), e["group"])][e["state"]] += 1
    print(f"\n{'domain':12} {'group':44} {'covered':>7} {'queued':>7} {'skip':>5}")
    for (dom, grp), c in sorted(rows.items(), key=lambda x: (HUB_DOMAIN_ORDER.get(x[0][0], 5), -sum(x[1].values()))):
        print(f"{(dom or '')[:12]:12} {(grp or '')[:44]:44} {c['covered']:7} {c['queued']:7} {c['skip']:5}")


def campbell_queue(entries: list, out: Path) -> None:
    """Campbell reviews not yet in the manifest, by their PMC copy, else their ERIC copy."""
    ids = manifest_index()[0]
    camp = [e for e in entries if "campbellcollaboration.org" in (e.get("url") or "") and e["state"] != "covered"]
    rows, seen, none = [], set(), 0
    for e in camp:
        twin = campbell_pmc_twin(e) or eric_twin(e)
        if not twin:
            none += 1
        elif twin["id"] not in ids and twin["id"] not in seen:
            seen.add(twin["id"])
            rows.append(twin)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"Campbell: {len(camp)} reviews not covered; {len(rows)} queued "
          f"({sum(r['source'] == 'pubmed' for r in rows)} PMC, {sum(r['source'] != 'pubmed' for r in rows)} ERIC); "
          f"{none} with no copy the pipeline can fetch -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", choices=["hub", "aied", "journal"], required=True)
    ap.add_argument("--issn", action="append", default=[], help="journal: an ISSN to list (repeatable)")
    ap.add_argument("--source", help="hub: a data.json path or URL; aied: a local clone")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--queue", type=Path, help="write the queued entries, in priority order, as NDJSON")
    ap.add_argument("--campbell", type=Path,
                    help="write a queue of the Campbell reviews the web fetch cannot read (their pages are "
                         "JavaScript-rendered): each review's PubMed Central copy, found by its DOI, else its "
                         "ERIC copy (hub only)")
    ap.add_argument("--eric-fallback", action="store_true",
                    help="look each robots-blocked entry up in ERIC by title, and queue the ERIC copy "
                         "(about 2 s an entry, ERIC's rate floor)")
    a = ap.parse_args()
    if a.list == "journal" and not a.issn:
        ap.error("--list journal needs at least one --issn")
    entries = classify(load_hub(a.source) if a.list == "hub" else load_journal(a.issn) if a.list == "journal"
                       else load_aied(a.source))
    if a.campbell:
        campbell_queue(entries, a.campbell)
        return
    if a.report or not a.queue:
        report(entries)
    if a.queue:
        q = sorted((e for e in entries if e["state"] == "queued"), key=priority)
        rows = [manifest_entry(e) for e in q]
        if a.eric_fallback:
            blocked = sorted((e for e in entries if e["why"] == "robots.txt disallows"), key=priority)
            found = 0
            for i, e in enumerate(blocked, 1):
                twin = eric_twin(e)
                if twin and twin["id"] not in manifest_index()[0]:
                    rows.append(twin)
                    found += 1
                if i % 100 == 0:
                    print(f"  ERIC fallback: {i}/{len(blocked)} looked up, {found} found", flush=True)
            print(f"ERIC fallback: {found} of {len(blocked)} robots-blocked entries found in ERIC with full text")
        a.queue.parent.mkdir(parents=True, exist_ok=True)
        a.queue.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
        print(f"\n{len(rows)} queued entries -> {a.queue}")


if __name__ == "__main__":
    main()
