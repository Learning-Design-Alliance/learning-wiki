#!/usr/bin/env python3
"""
chase_citations.py — find the next studies to ingest by following the reference lists of the
strongest studies the wiki already holds.

Strong studies mostly cite strong studies (maintainer, 2026-10-15: "quality articles are more
likely to point to other quality articles"). Topic search on ERIC and arXiv returned mostly weak
work; this reads backwards from the evidence that has already proved itself.

1. **Seeds** are the wiki's studies with a DOI that are a quantitative synthesis, or coded `q4`,
   or coded `q3` with a printed effect size (`evidence_rollup.Studies`).
2. Each seed's reference list comes from Crossref (`message.reference`; many publishers deposit
   it, some do not, and a seed without one adds nothing). Only references that carry a DOI count.
3. A referenced work is a **candidate** when two or more seeds cite it (`--min-seeds`). Co-citation
   by independent strong studies is the signal; one citation is not.
4. Each candidate's Crossref record is read. Works already in the wiki (a DOI on a claim page or in
   `sources/manifest.ndjson`) and anything that is not a journal article, a report or a proceedings
   paper are dropped. The rest are ranked: syntheses and trials first (by their registered title),
   then by how many seeds cite them.

Decisions go to `eval/citation-chase/candidates.ndjson` (committed: what was found and why), and the
top `--take` go to a batch queue in the `eval/runs/queues/` format for
`run_scrape_batch.py --queue`. Nothing touches a wiki page.

    python3 scripts/chase_citations.py --take 400
    python3 scripts/chase_citations.py --min-seeds 3 --take 200 --queue eval/runs/queues/citation-chase.ndjson
"""
import argparse
import concurrent.futures
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import evidence_rollup as er  # noqa: E402
from find_page_syntheses import known_dois  # noqa: E402

OUT = WIKI_ROOT / "eval" / "citation-chase" / "candidates.ndjson"
MAILTO = "contact@learningdesignalliance.org"
DOI = re.compile(r"10\.\d{4,9}/[^\s)\]>\"]+")
KEEP_TYPES = {"journal-article", "report", "proceedings-article"}
SYNTHESIS = re.compile(r"meta-?analy|systematic review|synthesis|research review|review of", re.I)
TRIAL = re.compile(r"randomi[sz]ed|controlled trial|field experiment|experiment", re.I)
# Every synthesis cites the meta-analysis methods literature (Egger's test, I-squared, metafor), so it
# tops a co-citation count without being learning research. Its venues and titles are dropped.
METHODS_VENUES = {"psychological methods", "bmj", "statistics in medicine", "journal of statistical software",
                  "research synthesis methods", "biometrics", "multivariate behavioral research",
                  "behavior research methods", "organizational research methods", "journal of clinical epidemiology",
                  "annals of internal medicine", "plos medicine", "journal of educational and behavioral statistics",
                  "educational and psychological measurement", "psychometrika", "the lancet"}
METHODS_TITLE = re.compile(r"publication bias|heterogeneity|inconsistency in meta|bias in meta|effect sizes? "
                           r"(estimate|calculation|for)|conducting meta|meta-analytic (review|methods)|writing meta|"
                           r"random[- ]effects|fixed[- ]effects?|trim and fill|statistical power|prisma|reporting items|"
                           r"matched groups or repeated|combining effect|meta-analysis in r|practical meta-analysis|"
                           r"robust variance|dependent effect sizes|small-study|meta-analytic models|tutorial|primary, secondary, and meta|"
                           r"quantitative synthesis of single|meta-analysis: (a|an) (guide|introduction)|how to (do|conduct)|fail-safe|file-drawer|methodolog|statistical methods|"
                           r"quantitative methods|complex research designs|confounded moderators|dichotomization|"
                           r"response ratios|in clinical trials", re.I)


def crossref(doi: str):
    for attempt in range(3):
        try:
            r = requests.get(f"https://api.crossref.org/works/{doi}", params={"mailto": MAILTO}, timeout=30)
            if r.status_code == 200:
                return r.json()["message"]
            if r.status_code in (429, 503):
                time.sleep(5 * (attempt + 1))
                continue
            return None
        except requests.RequestException:
            time.sleep(3)
    return None


def seeds() -> dict:
    """{seed doi: study key} for the strong studies with a DOI."""
    claims = er.load_claims()
    st = er.Studies(claims, list(claims))
    out = {}
    for key, entries in st.entries.items():
        strong = (st.kind(key) == "quant-synthesis" or st.q(key) == 4
                  or (st.q(key) == 3 and st.reports_effect(key)))
        if not strong:
            continue
        for e in entries:
            m = DOI.search(f"{e.get('resource', '')} {e.get('title', '')}")
            if m:
                out[m.group(0).rstrip(".,;").lower()] = key
                break
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--min-seeds", type=int, default=2)
    ap.add_argument("--take", type=int, default=400)
    ap.add_argument("--queue", default=str(WIKI_ROOT / "eval" / "runs" / "queues" / "citation-chase.ndjson"))
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    seed = seeds()
    print(f"{len(seed)} seed studies with a DOI", flush=True)
    cited_by = defaultdict(set)
    with_refs = 0
    with concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for doi, msg in zip(seed, ex.map(crossref, seed)):
            refs = (msg or {}).get("reference") or []
            if refs:
                with_refs += 1
            for r in refs:
                if r.get("DOI"):
                    cited_by[r["DOI"].lower()].add(doi)
    known = known_dois()
    pool = [d for d, s in cited_by.items() if len(s) >= args.min_seeds and d not in known and d not in seed]
    print(f"{with_refs} seeds have a deposited reference list; {len(cited_by)} cited DOIs; "
          f"{len(pool)} cited by {args.min_seeds}+ seeds and not in the wiki", flush=True)

    rows = []
    with concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for doi, msg in zip(pool, ex.map(crossref, pool)):
            if not msg:
                rows.append({"doi": doi, "kept": False, "why": "no Crossref record"})
                continue
            title = re.sub(r"<[^>]+>", "", (msg.get("title") or [""])[0])
            title = re.sub(r"\s+", " ", title).strip()
            kind = msg.get("type")
            year = ((msg.get("issued") or {}).get("date-parts") or [[None]])[0][0]
            authors = [f"{a.get('family', '')}" for a in (msg.get("author") or [])][:3]
            row = {"doi": doi, "title": title, "type": kind, "year": year, "authors": authors,
                   "venue": (msg.get("container-title") or [""])[0], "seeds": len(cited_by[doi]),
                   "synthesis": bool(SYNTHESIS.search(title)), "trial": bool(TRIAL.search(title))}
            methods = (row["venue"].replace("&amp;", "&").lower() in METHODS_VENUES
                       or bool(METHODS_TITLE.search(title)))
            row["kept"] = kind in KEEP_TYPES and bool(title) and not methods
            row["why"] = ("kept" if row["kept"] else "research-methods literature" if methods else f"type {kind}")
            rows.append(row)
    kept = sorted((r for r in rows if r["kept"]),
                  key=lambda r: (-(2 * r["synthesis"] + r["trial"]), -r["seeds"], -(r["year"] or 0)))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for r in sorted(rows, key=lambda r: r["doi"]):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    q = Path(args.queue)
    q.parent.mkdir(parents=True, exist_ok=True)
    with q.open("w", encoding="utf-8") as fh:
        for r in kept[:args.take]:
            slug = re.sub(r"[^a-z0-9]+", "-", f"{(r['authors'] or ['anon'])[0]}-{r['year']}-{r['title']}".lower())[:70].strip("-")
            fh.write(json.dumps({"id": f"cc-{slug}", "source": "web", "title": r["title"],
                                 "authors": ", ".join(r["authors"]), "year": r["year"],
                                 "url": f"https://doi.org/{r['doi']}", "fetch_url": f"https://doi.org/{r['doi']}",
                                 "doi": r["doi"], "topic_hint": f"citation chase: cited by {r['seeds']} strong studies",
                                 "list_key": f"cc-{slug}"}, ensure_ascii=False) + "\n")
    c = Counter((r["synthesis"], r["trial"]) for r in kept)
    print(f"{len(kept)} candidates kept ({c[(True, False)] + c[(True, True)]} syntheses, "
          f"{c[(False, True)]} trials or experiments); queued {min(len(kept), args.take)} -> {q}")


if __name__ == "__main__":
    main()
