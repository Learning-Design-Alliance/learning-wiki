#!/usr/bin/env python3
"""
check_source_validity.py — can the sources themselves be believed?

Every other check in this repo asks whether a page says what its source says. This
one asks whether the source deserves to be said at all. Added 2026-10-25 after an
audit of AI-in-education meta-analyses (O'Neill, preprint, 2026) named a primary
study that six of them pooled and this wiki had made ten claims from: its ANOVA
table reports a partial eta squared of 1.374, its mean squares are not its sums of
squares over their degrees of freedom, and it cites five "ChatGPT-supported" studies
dated 2017-2020 (Alneyadi & Wardat 2024; its 2023 companion has the same defects).

Three checks, all mechanical, none of which edits a page:

  --stats         the cached text of every ingested source (eval/corpus/cache/<id>.txt)
                  read by stat_checks.py: impossible values, broken ANOVA rows,
                  p values their own statistics contradict, references dated before
                  the tool they name.
  --refs          the DOIs in a source's reference list, resolved against Crossref
                  (DataCite after a Crossref 404): a DOI that resolves nowhere, or to
                  a work whose title the reference does not carry, may be a reference
                  that cannot be what it says. Run on AI-era sources by default, where
                  invented references are a known failure; --all-sources for the rest.
                  Review-level only: extracted text breaks DOIs across lines and puts
                  another reference's title beside a DOI, so most findings are layout.
  --retractions   every DOI a content page cites, looked up on Crossref for a
                  retraction, withdrawal or expression of concern (Crossref carries
                  Retraction Watch's data since 2023). Retracted DOIs are recorded in
                  eval/source-validity/retracted.ndjson (committed), which lint reads.

Findings go to eval/runs/source-validity/ (not committed: the cached texts they are
read from are not either). What a person or agent decided about each finding goes
to eval/source-validity/reviewed.ndjson (committed, append-only), keyed on source id
and the finding's text, so a decided finding is not raised again and a new one is.

    python3 scripts/check_source_validity.py --stats [--new | --ids a,b]
    python3 scripts/check_source_validity.py --refs [--new | --ids a,b] [--all-sources]
    python3 scripts/check_source_validity.py --retractions [--new]
    python3 scripts/check_source_validity.py --report          # open findings, for a person
    python3 scripts/check_source_validity.py --review <source-id> --decision confirmed|false-alarm \
        --by claude/unspecified --note "..."                   # record a decision

`--report` exits 1 while a high-severity finding or a retraction is undecided, which
is what stops a batch (run_scrape_batch.py). A confirmed finding is acted on by
removing the source's claims (scripts/remove_pages.py) or, for a single slip that
does not touch what the wiki took from the source, by saying so on the claim.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402
import stat_checks  # noqa: E402

CACHE = WIKI_ROOT / "eval" / "corpus" / "cache"
MANIFEST = WIKI_ROOT / "sources" / "manifest.ndjson"
RUNS = WIKI_ROOT / "eval" / "runs" / "source-validity"
FINDINGS = RUNS / "findings.ndjson"
LOOKUPS = RUNS / "crossref-lookups.ndjson"
RECORD = WIKI_ROOT / "eval" / "source-validity"
REVIEWED = RECORD / "reviewed.ndjson"
COVERAGE = RECORD / "coverage.json"     # committed: what the last full run of each check covered
RETRACTED = RECORD / "retracted.ndjson"
MAILTO = "contact@learningdesignalliance.org"
UA = f"learning-wiki (mailto:{MAILTO})"
AI_TERMS = re.compile(r"chat\s*-?gpt|generative ai|gen-?ai\b|large language model|\bLLMs?\b|chatbot|"
                      r"artificial intelligence|\bGPT-?\d", re.I)
NOTICE_TYPES = {"retraction", "withdrawal", "removal", "expression_of_concern", "expression-of-concern"}


# ------------------------------------------------------------------ sources

def manifest_sources() -> list:
    out = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if r.get("status") == "ingested" and r.get("pages"):
            out.append(r)
    latest = {}
    for r in out:
        latest[r["id"]] = r            # a re-review supersedes
    return list(latest.values())


def new_source_ids() -> set:
    """Sources this working tree added to the manifest (a batch's own)."""
    r = subprocess.run(["git", "diff", "-U0", "--", str(MANIFEST.relative_to(WIKI_ROOT))],
                       cwd=WIKI_ROOT, capture_output=True, text=True)
    ids = set()
    for line in r.stdout.splitlines():
        if line.startswith("+{"):
            try:
                ids.add(json.loads(line[1:])["id"])
            except (ValueError, KeyError):
                pass
    return ids


def cached_text(sid: str):
    p = CACHE / f"{sid}.txt"
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else None


def fkey(sid: str, f: dict) -> str:
    return hashlib.sha1(f"{sid}|{f['check']}|{f['text'][:200]}".encode()).hexdigest()[:16]


def load_ndjson(path: Path) -> list:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def write_coverage(kind: str, **counts) -> None:
    """Record what a full (wiki-wide) run covered, for checks.md. Not written by a
    --new or --ids run, which covers a batch, not the wiki."""
    RECORD.mkdir(parents=True, exist_ok=True)
    cov = json.loads(COVERAGE.read_text(encoding="utf-8")) if COVERAGE.exists() else {}
    cov[kind] = {**counts, "at": datetime.date.today().isoformat()}
    COVERAGE.write_text(json.dumps(cov, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def write_findings(kind: str, rows: list, ids: "set | None") -> None:
    """Replace this check's findings for the sources just checked, keep the rest."""
    RUNS.mkdir(parents=True, exist_ok=True)
    keep = [r for r in load_ndjson(FINDINGS)
            if not (r["kind"] == kind and (ids is None or r["source"] in ids))]
    with FINDINGS.open("w", encoding="utf-8") as fh:
        for r in keep + rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


# ------------------------------------------------------------------ crossref

_lock = threading.Lock()


def _lookups() -> dict:
    return {r["doi"]: r for r in load_ndjson(LOOKUPS)}


def lookup(doi: str, cache: dict, force: bool = False) -> dict:
    """Crossref record summary for a DOI, DataCite after a Crossref 404. A network
    failure returns status 'error' and is not cached: it says nothing about the DOI."""
    doi = doi.lower()
    if doi in cache and not force:
        return cache[doi]
    rec = {"doi": doi, "at": datetime.date.today().isoformat()}
    for attempt in range(3):
        try:
            r = requests.get(f"https://api.crossref.org/works/{doi}", params={"mailto": MAILTO},
                             headers={"User-Agent": UA}, timeout=30)
        except requests.RequestException:
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 200:
            m = r.json()["message"]
            rec.update(status="crossref", title=" ".join((m.get("title") or [""])[0].split()),
                       year=((m.get("issued") or {}).get("date-parts") or [[None]])[0][0],
                       notices=[{"type": u.get("type"), "doi": u.get("DOI"), "source": u.get("source"),
                                 "date": ((u.get("updated") or {}).get("date-time") or "")[:10]}
                                for u in (m.get("updated-by") or [])
                                if (u.get("type") or "").lower() in NOTICE_TYPES])
            break
        if r.status_code == 404:
            try:
                d = requests.get(f"https://api.datacite.org/dois/{doi}", headers={"User-Agent": UA}, timeout=30)
            except requests.RequestException:
                return {"doi": doi, "status": "error"}
            if d.status_code == 200:
                a = d.json()["data"]["attributes"]
                rec.update(status="datacite", title=" ".join(((a.get("titles") or [{}])[0].get("title") or "").split()),
                           year=a.get("publicationYear"), notices=[])
            elif d.status_code == 404:
                rec.update(status="not-found")
            else:
                return {"doi": doi, "status": "error"}
            break
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(2 ** attempt * 2)
            continue
        return {"doi": doi, "status": "error"}
    else:
        return {"doi": doi, "status": "error"}
    with _lock:
        cache[doi] = rec
        RUNS.mkdir(parents=True, exist_ok=True)
        with LOOKUPS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


# ------------------------------------------------------------------ checks

def run_stats(sources: list) -> list:
    rows = []
    for s in sources:
        text = cached_text(s["id"])
        if not text:
            continue
        found = stat_checks.check_text(text)
        sev = stat_checks.severity(found)
        for f in found:
            rows.append({"kind": "stats", "source": s["id"], "title": s.get("title"), "pages": s["pages"],
                         "severity": sev, **f, "key": fkey(s["id"], f)})
    return rows


_WORD = re.compile(r"[a-z0-9]{4,}")
LIGATURES = str.maketrans({"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "‐": "-", "–": "-",
                           "\u200b": None, "\u00ad": None})
_DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.I)


def reference_dois(refs: str) -> list:
    """(doi, the reference text before it) for each DOI printed in a reference list.
    Only DOIs printed whole on one line: extraction breaks long ones across lines,
    and a broken DOI would read as one that does not exist."""
    out, seen = [], set()
    refs = refs.translate(LIGATURES)
    for line_m in re.finditer(r"[^\n]+", refs):
        line = line_m.group(0)
        for m in _DOI.finditer(line):
            doi = re.sub(r"(?:eprint|arxiv|url|http).*$", "", m.group(1), flags=re.I).rstrip(".,;:)]").lower()
            prefix, _, suffix = doi.partition("/")
            # a suffix this short is a DOI cut by a line or column break, not a whole one
            if doi in seen or len(suffix) < 8 or doi.endswith(("/", "-", ".")) or not suffix[-1].isalnum():
                continue
            if m.end() >= len(line.rstrip()) - 1 and re.search(r"[-./]$", line.rstrip()):
                continue
            seen.add(doi)
            start = line_m.start() + m.start()
            out.append((doi, " ".join(refs[max(0, start - 500):start + 300].split())))
    return out


def ref_matches(context: str, title: str) -> bool:
    """The resolved title's words are mostly in the text before the DOI (the reference
    the DOI was printed with)."""
    words = [w for w in _WORD.findall(title.lower()) if w not in {"with", "from", "that", "this", "their"}][:10]
    if len(words) < 2:
        return True
    have = set(_WORD.findall(context.lower().replace("-", " ")))
    words = [w.replace("-", "") for w in words]
    return sum(w in have for w in words) / len(words) >= 0.5


def is_ai_era(text: str) -> bool:
    return bool(AI_TERMS.search(text[:4000]))


def run_refs(sources: list, all_sources: bool, per_source: int, workers: int) -> list:
    cache = _lookups()
    jobs = []
    for s in sources:
        text = cached_text(s["id"])
        if not text or not (all_sources or is_ai_era(text)):
            continue
        _, refs = stat_checks.body_and_refs(text)
        for doi, ctx in reference_dois(refs)[:per_source]:
            jobs.append((s, doi, ctx))
    print(f"--refs: {len(jobs)} reference DOIs from {len({j[0]['id'] for j in jobs})} sources "
          f"({sum(j[1] in cache for j in jobs)} already looked up)", file=sys.stderr)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(lookup, doi, cache): doi for _, doi, _ in jobs if doi not in cache}
        for i, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            results[futs[fut]] = fut.result()
            if i % 500 == 0:
                print(f"  {i}/{len(futs)}", file=sys.stderr)
    run_refs.sources, run_refs.dois = len({j[0]["id"] for j in jobs}), len(jobs)
    rows, per = [], {}
    for s, doi, ctx in jobs:
        rec = cache.get(doi) or results.get(doi) or {}
        st = rec.get("status")
        per.setdefault(s["id"], [0, 0])
        if st in ("crossref", "datacite"):
            per[s["id"]][0] += 1
            if rec.get("title") and not ref_matches(ctx, rec["title"]):
                f = {"check": "reference-doi", "what": f"{doi} is \"{rec['title'][:90]}\"", "text": ctx[-250:]}
            else:
                continue
        elif st == "not-found":
            per[s["id"]][0] += 1
            f = {"check": "reference-doi", "what": f"{doi} is registered at neither Crossref nor DataCite",
                 "text": ctx[-250:]}
        else:
            continue
        per[s["id"]][1] += 1
        rows.append({"kind": "refs", "source": s["id"], "title": s.get("title"), "pages": s["pages"], **f,
                     "key": fkey(s["id"], f)})
    # Review only, never high: measured 2026-10-25 on 610 AI-era sources, most findings were
    # DOIs cut by a line or column break, or a two-column layout putting another reference's
    # title beside the DOI. Extracted text cannot tell a truncated DOI from an invented one,
    # so this lists for a person and stops nothing. The anachronism check is the one precise
    # enough to act on.
    for r in rows:
        checked, bad = per[r["source"]]
        r["severity"] = "review"
        r["rate"] = f"{bad} of {checked}"
    return rows


# Balanced brackets are part of a DOI (10.1016/s0959-4752(01)00002-x), and so are the
# angle brackets of an old SICI DOI (...(199601)33:1<101::aid-tea6>3.0.co;2-z); an
# unbalanced closing one is the markdown link around it (check_load_bearing.DOI_RE).
CITED_DOI = re.compile(r"doi\.org/(10\.\d{4,9}/(?:\([^\s()]*\)|\[[^\s\[\]]*\]|<[^\s<>]*>|[^\s()\[\]<>\"])+)", re.I)


def cited_dois(only_pages: "set | None" = None) -> dict:
    """doi -> pages citing it, across every content folder."""
    out = {}
    for folder in okf_lib.CONTENT_FOLDERS:
        for p in (WIKI_ROOT / folder).glob("*.md"):
            rel = f"{folder}/{p.name}"
            if only_pages is not None and rel not in only_pages:
                continue
            for m in CITED_DOI.finditer(p.read_text(encoding="utf-8", errors="replace")):
                out.setdefault(m.group(1).rstrip(".,;").lower(), set()).add(rel)
    return out


def run_retractions(only_pages: "set | None", workers: int, max_age: int = 90) -> list:
    cache = _lookups()
    dois = cited_dois(only_pages)
    # A paper can be retracted after it was first looked up: a lookup older than
    # --max-age days is made again.
    cutoff = (datetime.date.today() - datetime.timedelta(days=max_age)).isoformat()
    todo = [d for d in dois if d not in cache or "notices" not in cache[d] or cache[d].get("at", "") < cutoff]
    print(f"--retractions: {len(dois)} cited DOIs, {len(todo)} to look up", file=sys.stderr)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for i, _ in enumerate(ex.map(lambda d: lookup(d, cache, force=True), todo), 1):
            if i % 500 == 0:
                print(f"  {i}/{len(todo)}", file=sys.stderr)
    rows, recorded = [], {r["doi"] for r in load_ndjson(RETRACTED)}
    for d, pages in sorted(dois.items()):
        rec = cache.get(d) or {}
        if rec.get("status") == "not-found":
            # A DOI on a page that no registry knows reads as verified and leads nowhere:
            # find the real one (title, first author and year must agree) or take it off.
            f = {"check": "dead-doi", "what": f"{d} is registered at neither Crossref nor DataCite", "text": d}
            rows.append({"kind": "retractions", "source": f"doi:{d}", "title": "", "pages": sorted(pages),
                         "severity": "high", **f, "key": fkey(f"doi:{d}", f)})
        for n in rec.get("notices") or []:
            f = {"check": "retraction", "what": f"{d} has a {n['type']} notice ({n.get('doi')}, {n.get('date')})",
                 "text": rec.get("title", "")}
            rows.append({"kind": "retractions", "source": f"doi:{d}", "title": rec.get("title"),
                         "pages": sorted(pages), "severity": "high", **f, "key": fkey(f"doi:{d}", f)})
            if d not in recorded and n["type"].lower() in ("retraction", "withdrawal", "removal"):
                RECORD.mkdir(parents=True, exist_ok=True)
                with RETRACTED.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"doi": d, "notice": n.get("doi"), "type": n["type"],
                                         "date": n.get("date"), "title": rec.get("title"),
                                         "recorded": datetime.date.today().isoformat()}, ensure_ascii=False) + "\n")
                recorded.add(d)
    return rows


# ------------------------------------------------------------------ report / review

def reviewed() -> dict:
    out = {}
    for r in load_ndjson(REVIEWED):
        for k in r.get("keys") or []:
            out[k] = r
    return out


def report(show_review: bool) -> int:
    done = reviewed()
    rows = [r for r in load_ndjson(FINDINGS) if r["key"] not in done]
    by_src = {}
    for r in rows:
        by_src.setdefault(r["source"], []).append(r)
    open_high = {s: rs for s, rs in by_src.items() if any(x["severity"] == "high" for x in rs)}
    print(f"# Source validity: {len(by_src)} source(s) with undecided findings, "
          f"{len(open_high)} high severity\n")
    for s, rs in sorted(by_src.items(), key=lambda kv: (kv[0] not in open_high, kv[0])):
        if s not in open_high and not show_review:
            continue
        sev = "HIGH" if s in open_high else "review"
        print(f"## {s} [{sev}] {rs[0].get('title') or ''}")
        print(f"   pages: {', '.join(rs[0]['pages'][:6])}{' ...' if len(rs[0]['pages']) > 6 else ''}")
        for r in rs[:8]:
            print(f"   - {r['check']}: {r['what']}" + (f" ({r['rate']})" if r.get("rate") else ""))
            print(f"       {r['text'][:220]}")
        if len(rs) > 8:
            print(f"   ... {len(rs) - 8} more")
        print()
    if not show_review:
        n = len(by_src) - len(open_high)
        if n:
            print(f"({n} source(s) with review-level findings only: --all to list)")
    return 1 if open_high else 0


def record_review(sid: str, decision: str, by: str, note: str) -> None:
    keys = [r["key"] for r in load_ndjson(FINDINGS) if r["source"] == sid]
    if not keys:
        raise SystemExit(f"no findings recorded for {sid}")
    if decision == "confirmed" and not note:
        raise SystemExit("--note is required: say what was confirmed and what was done about it")
    RECORD.mkdir(parents=True, exist_ok=True)
    with REVIEWED.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"source": sid, "decision": decision, "by": by, "at": datetime.date.today().isoformat(),
                             "note": note, "keys": keys}, ensure_ascii=False) + "\n")
    print(f"recorded {decision} for {sid} ({len(keys)} finding(s))")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--refs", action="store_true")
    ap.add_argument("--retractions", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--all", action="store_true", help="--report: list review-level findings too")
    ap.add_argument("--new", action="store_true", help="only sources this working tree added")
    ap.add_argument("--ids", help="comma-separated source ids")
    ap.add_argument("--all-sources", action="store_true", help="--refs: not only AI-era sources")
    ap.add_argument("--per-source", type=int, default=15)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--max-age", type=int, default=90, help="--retractions: re-look-up DOIs checked longer ago (days)")
    ap.add_argument("--review")
    ap.add_argument("--decision", choices=["confirmed", "false-alarm"])
    ap.add_argument("--by", default="claude/unspecified")
    ap.add_argument("--note", default="")
    a = ap.parse_args()

    if a.review:
        if not a.decision:
            raise SystemExit("--review needs --decision")
        record_review(a.review, a.decision, a.by, a.note)
        return
    sources = manifest_sources()
    ids = None
    if a.new:
        ids = new_source_ids()
    elif a.ids:
        ids = set(a.ids.split(","))
    if ids is not None:
        sources = [s for s in sources if s["id"] in ids]
    if a.stats:
        rows = run_stats(sources)
        write_findings("stats", rows, None if ids is None else {s["id"] for s in sources})
        scanned = sum(1 for s in sources if (CACHE / f"{s['id']}.txt").exists())
        print(f"--stats: {len({r['source'] for r in rows})} of {scanned} sources with text have findings")
        if ids is None:
            write_coverage("stats", sources_ingested=len(sources), sources_with_text=scanned,
                           with_findings=len({r["source"] for r in rows}),
                           high=len({r["source"] for r in rows if r["severity"] == "high"}))
    if a.refs:
        rows = run_refs(sources, a.all_sources, a.per_source, a.workers)
        write_findings("refs", rows, None if ids is None else {s["id"] for s in sources})
        print(f"--refs: {len({r['source'] for r in rows})} sources with unresolvable or mismatched reference DOIs")
        if ids is None:
            write_coverage("refs", scope="all sources" if a.all_sources else "AI-era sources",
                           sources_checked=getattr(run_refs, "sources", 0), dois_checked=getattr(run_refs, "dois", 0),
                           with_findings=len({r["source"] for r in rows}),
                           high=len({r["source"] for r in rows if r["severity"] == "high"}))
    if a.retractions:
        pages = None
        if ids is not None:
            pages = {p for s in sources for p in s["pages"]}
        rows = run_retractions(pages, a.workers, a.max_age)
        write_findings("retractions", rows, None)
        print(f"--retractions: {sum(r['check'] == 'retraction' for r in rows)} notice(s) on cited DOIs, "
              f"{sum(r['check'] == 'dead-doi' for r in rows)} cited DOIs registered nowhere")
        if ids is None:
            cache = _lookups()
            dois = cited_dois()
            write_coverage("retractions", dois_cited=len(dois),
                           dois_looked_up=sum(1 for d in dois if (cache.get(d) or {}).get("status") in ("crossref", "datacite", "not-found")),
                           notices=sum(r["check"] == "retraction" for r in rows),
                           dead=sum(r["check"] == "dead-doi" for r in rows))
    if a.report:
        sys.exit(report(a.all))


if __name__ == "__main__":
    main()
