#!/usr/bin/env python3
"""
eval_search.py — does search answer the questions a designer asks?

Scores the MCP server's `search` and `situations` tools against
eval/search/designer-queries.json: queries from learner analysis, context analysis and
choosing patterns and principles, each with the pages any of which is a good answer.
For search it reports hit@1, hit@5 and mean reciprocal rank (within the top 10) by
phase; for situations, whether each tag set returns enough pages and, where asked,
whether the first page speaks to every tag.

The scale test of 2026-10-09 judged search by reading results; this makes the same
judgement repeatable, so a ranking change is measured before it lands rather than
eyeballed after. It is a report, not a lint check: a miss is a finding about search or
about the wiki's pages, and either can be the one to change.

    python3 scripts/eval_search.py              # the report
    python3 scripts/eval_search.py --misses     # every query that missed, with what came back
    python3 scripts/eval_search.py --json       # machine-readable, for comparing two checkouts
    python3 scripts/eval_search.py --root DIR   # score another checkout (e.g. a worktree of main)
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUERIES = HERE.parent / "eval" / "search" / "designer-queries.json"


def run(root: Path, show_misses: bool) -> dict:
    sys.path.insert(0, str(root / "scripts"))
    import mcp_server as m

    wiki = m.Wiki(root)
    spec = json.loads(QUERIES.read_text(encoding="utf-8"))
    by_phase = defaultdict(lambda: {"n": 0, "hit1": 0, "hit5": 0, "rr": 0.0})
    misses = []
    for q in spec["search"]:
        got = [r["id"] for r in m.tool_search(wiki, q["query"], limit=10)["results"]]
        ranks = [i for i, pid in enumerate(got) if pid in q["expected"]]
        first = ranks[0] + 1 if ranks else None
        s = by_phase[q["phase"]]
        s["n"] += 1
        s["hit1"] += first == 1
        s["hit5"] += bool(first and first <= 5)
        s["rr"] += 1 / first if first else 0.0
        if not first or first > 5:
            misses.append({"query": q["query"], "rank": first, "expected": q["expected"], "got": got[:5]})

    situations = []
    if hasattr(m, "tool_situations") and (root / "situation-index.json").exists():
        for q in spec["situations"]:
            r = m.tool_situations(wiki, tags=q.get("tags"), text=q.get("text"), limit=50)
            pages = r["pages"]
            ok = len(pages) >= q.get("min_pages", 1)
            if q.get("top_covers_all"):
                ok = ok and bool(pages) and len(pages[0]["covers"]) == len(q["tags"])
            situations.append({"phase": q["phase"], "ask": q.get("tags") or q.get("text"),
                               "pages": r["pages_matched"], "top": pages[0]["id"] if pages else None,
                               "rows": sum(len(p["rows"]) for p in pages), "ok": ok})

    total = {"n": 0, "hit1": 0, "hit5": 0, "rr": 0.0}
    for s in by_phase.values():
        for k in total:
            total[k] += s[k]
    return {"search": dict(by_phase), "total": total, "misses": misses, "situations": situations}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(HERE.parent), help="the checkout to score")
    ap.add_argument("--misses", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    res = run(Path(args.root).resolve(), args.misses)
    if args.json:
        print(json.dumps(res, indent=1))
        return
    print(f"search ({QUERIES.relative_to(HERE.parent)})")
    print(f"  {'phase':9} {'queries':>7} {'hit@1':>6} {'hit@5':>6} {'MRR@10':>7}")
    for phase, s in list(res["search"].items()) + [("all", res["total"])]:
        n = s["n"] or 1
        print(f"  {phase:9} {s['n']:7} {s['hit1'] / n:6.0%} {s['hit5'] / n:6.0%} {s['rr'] / n:7.2f}")
    if res["situations"]:
        ok = sum(x["ok"] for x in res["situations"])
        print(f"\nsituations: {ok} of {len(res['situations'])} pass")
        for x in res["situations"]:
            print(f"  {'ok  ' if x['ok'] else 'FAIL'} {x['phase']:8} {str(x['ask']):48.48} "
                  f"{x['pages']:3} pages {x['rows']:4} rows  top {x['top']}")
    else:
        print("\nsituations: no situations tool in this checkout")
    if args.misses:
        print("\nmisses (not in the top 5):")
        for mi in res["misses"]:
            print(f"  {mi['query']!r}: rank {mi['rank']}; want {mi['expected']}")
            print(f"      got {mi['got']}")


if __name__ == "__main__":
    main()
