#!/usr/bin/env python3
"""
find_page_syntheses.py — the evidence search a thin principle or pattern page gets before it is
converted or folded (`upgrade_worklist.py`, step "search").

For each page a model reads the page's title, description, opening text and the claims it cites,
and names the published research that tests the page's recommendation: systematic reviews and
meta-analyses first, then independent empirical studies. It also says whether the recommendation is
tested by research at all, or rests on practitioner opinion or one source's argument
(`research_status`). The maintainer expects most thin pages to be the second kind (2026-10-14).

A named work counts only when Crossref has it: the search takes the model's title and first author,
and a record is accepted on the same checks as `find_missing_dois.py` (the cited title, first
author, and year within one). A model's reference that Crossref does not confirm is dropped and
counted, never queued: a model asked for evidence will name plausible papers that do not exist.

A confirmed work is then looked up in the wiki: its DOI on a claim page or in
`sources/manifest.ndjson` means it is already in. The rest are written as a queue for
`run_scrape_batch.py --queue`, in the format of `eval/runs/queues/` (ignored).

    python3 scripts/find_page_syntheses.py --pages principles/x patterns/y
    python3 scripts/find_page_syntheses.py --from-worklist search
    python3 scripts/find_page_syntheses.py --from-worklist search --queue eval/runs/queues/page-syntheses.ndjson

Decisions go to eval/page-upgrade/syntheses.ndjson (committed: what was searched, what the model
named, what Crossref confirmed, and the model's read of whether the topic is researched).
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
from find_missing_dois import fold, record_of, same_title, MAILTO  # noqa: E402

OUT = WIKI_ROOT / "eval" / "page-upgrade" / "syntheses.ndjson"
MODEL = "openai/gpt-5.6-luna"

SYSTEM = """You know the education and learning-sciences research literature well. A learning-design wiki
has a page making a recommendation. Say what published research tests that recommendation.

Return JSON:
{"recommendation": "the page's recommendation in one sentence",
 "research_status": "tested" | "partly-tested" | "untested",
 "status_reason": "one sentence: what kind of support the recommendation has",
 "works": [{"first_author": "surname", "year": 2015, "title": "exact title", "kind": "meta-analysis" |
            "systematic-review" | "empirical-study" | "review", "bears_on": "one clause"}]}

- "tested": syntheses or several independent empirical studies test the recommendation itself.
- "partly-tested": research tests a nearby or more general claim the recommendation depends on.
- "untested": it rests on practitioner experience, one source's argument, or theory.
- Name at most 4 works, syntheses first. Name only works you are confident exist, with their exact
  title; an empty list is a correct answer. Never name the page's own source as its test."""


def page_text(key: str) -> str:
    text = (WIKI_ROOT / f"{key}.md").read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    fm, _, body = text.partition("\n---\n")
    title = re.search(r"^title:\s*\"?(.*?)\"?\s*$", fm, re.M)
    desc = re.search(r"^description:\s*\"?(.*?)\"?\s*$", fm, re.M)
    claims = re.findall(r"\[([^\]]+)\]\(\.\./claims/[^)]+\)", body)
    return (f"PAGE ({key.split('/')[0][:-1]}): {title.group(1) if title else key}\n"
            f"DESCRIPTION: {desc.group(1) if desc else ''}\n\n{body[:2500]}\n\n"
            f"CLAIMS IT CITES: {'; '.join(dict.fromkeys(claims)) or 'none'}")


def crossref(work: dict):
    q = urllib.parse.quote(f"{work.get('title', '')} {work.get('first_author', '')}"[:300])
    url = (f"https://api.crossref.org/works?query.bibliographic={q}&rows=5"
           f"&select=DOI,title,author,editor,issued,published-print,published-online,type,container-title"
           + (f"&mailto={MAILTO}" if MAILTO else ""))
    try:
        items = requests.get(url, timeout=30).json()["message"]["items"]
    except Exception as e:  # a failed lookup establishes nothing
        return {"error": str(e)[:120]}
    for item in items:
        rec = record_of(item)
        if not same_title(work.get("title", ""), rec["title"]):
            continue
        first = (rec["authors"] or rec["editors"] or [""])[0]
        if first and fold(work.get("first_author", "")) not in fold(first):
            continue
        years = {((item.get(k) or {}).get("date-parts") or [[None]])[0][0]
                 for k in ("published-print", "published-online", "issued")} - {None}
        if isinstance(work.get("year"), int) and not any(abs(y - work["year"]) <= 1 for y in years):
            continue
        return {"doi": item["DOI"].lower(), "title": rec["title"], "year": min(years) if years else None,
                "authors": rec["authors"][:3], "type": rec["type"]}
    return None


def known_dois() -> set:
    dois = set()
    for p in (WIKI_ROOT / "claims").glob("*.md"):
        dois.update(d.rstrip(".,;").lower() for d in re.findall(r"10\.\d{4,9}/[^\s)\]>\"]+", p.read_text(encoding="utf-8")))
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        try:
            d = json.loads(line).get("doi")
        except json.JSONDecodeError:
            continue
        if d:
            dois.add(d.lower())
    return dois


def search(key: str, api_key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    try:
        res = oc.generate(MODEL, SYSTEM, page_text(key), api_key, max_tokens=3000, temperature=0.1)
        ans = extract_json(res.raw_text)
        cost = res.cost_usd or 0
    except Exception as e:
        return {"page": key, "error": str(e)[:200]}
    works = []
    for w in (ans.get("works") or [])[:4]:
        hit = crossref(w)
        works.append({**w, "crossref": hit})
    return {"page": key, "model": MODEL, "recommendation": ans.get("recommendation"),
            "research_status": ans.get("research_status"), "status_reason": ans.get("status_reason"),
            "works": works, "cost_usd": cost}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pages", nargs="+")
    g.add_argument("--from-worklist", metavar="STEP")
    ap.add_argument("--queue", help="write unseen confirmed works here, as a batch queue")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    if args.pages:
        keys = args.pages
    else:
        import upgrade_worklist
        keys = [r["page"] for r in upgrade_worklist.rows() if r["step"] == args.from_worklist]
    print(f"searching {len(keys)} page(s) with {MODEL}", flush=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    results = []
    with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for r in ex.map(lambda k: search(k, api_key), keys):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            fh.flush()
            results.append(r)
    have = known_dois()
    named = [w for r in results for w in r.get("works") or []]
    confirmed = [w for w in named if w.get("crossref") and "doi" in w["crossref"]]
    unseen = {}
    for r in results:
        for w in r.get("works") or []:
            c = w.get("crossref") or {}
            if c.get("doi") and c["doi"] not in have:
                unseen.setdefault(c["doi"], (r["page"], c))
    status = {}
    for r in results:
        status[r.get("research_status") or "error"] = status.get(r.get("research_status") or "error", 0) + 1
    print(f"research status: {status}")
    print(f"works named {len(named)}; confirmed by Crossref {len(confirmed)}; not yet in the wiki {len(unseen)}; "
          f"cost ${sum(r.get('cost_usd') or 0 for r in results):.3f}")
    if args.queue:
        with open(args.queue, "w", encoding="utf-8") as fh:
            for doi, (page, c) in unseen.items():
                slug = re.sub(r"[^a-z0-9]+", "-", f"{(c['authors'] or ['anon'])[0]}-{c['year']}-{c['title']}".lower())[:60]
                fh.write(json.dumps({"id": f"pg-{slug}".strip("-"), "source": "web", "title": c["title"],
                                     "authors": ", ".join(c["authors"]), "year": c["year"],
                                     "url": f"https://doi.org/{doi}", "fetch_url": f"https://doi.org/{doi}",
                                     "doi": doi, "topic_hint": f"page evidence search: {page}",
                                     "list_key": f"pg-{slug}".strip("-")}, ensure_ascii=False) + "\n")
        print(f"queue -> {args.queue}")


if __name__ == "__main__":
    main()
