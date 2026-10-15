#!/usr/bin/env python3
"""
choose_fold_parent.py — for a thin principle or pattern page, the page it folds into.

A canonical principle or pattern still resting on two studies or fewer after its evidence search
(`upgrade_worklist.py`, `find_page_syntheses.py`) is folded into a parent (maintainer, 2026-10-14):
most were placeholders written from one source, and a recommendation with no research behind it is
better read as a qualification or example on the general page it narrows than as a page of its own.

Each page is shown its candidates: the canonical page triage named for it, and the most similar
principles and patterns that are not themselves thin (BM25 over title and description). Two models
of different families each pick the general page this one narrows, applies or restates, or "none".
A parent is chosen only when both name the same page; a disagreement or "none" leaves the page for a
reader, and it is not folded.

    python3 scripts/choose_fold_parent.py --pages principles/x patterns/y
    python3 scripts/choose_fold_parent.py --from-worklist search      # the thin pages
    python3 scripts/choose_fold_parent.py --adjudicate                # a third model settles disagreements
    python3 scripts/choose_fold_parent.py --pairs                     # agreed pairs, merge_pages.py form

`--adjudicate` shows a third model (another family) each page the two disagreed on, with both
answers and reasons. The page is settled when it sides with one of them: a parent, or "none".

Decisions go to eval/page-upgrade/fold-parents.ndjson.
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import search_index  # noqa: E402
import upgrade_worklist  # noqa: E402

OUT = WIKI_ROOT / "eval" / "page-upgrade" / "fold-parents.ndjson"
FIRST, SECOND = "openai/gpt-5.6-luna", "deepseek/deepseek-v4-pro"
THIRD = "moonshotai/kimi-k3"   # settles a disagreement, as in the 2026-10-02 page triage

PROMPT = """A learning-design wiki is folding thin principle and pattern pages into the general page they
narrow. A thin page rests on one source or none; its recommendation will survive on the parent as a
qualification, variant or example, with its claims and text kept.

THIN PAGE: {key}
{page}

CANDIDATE PARENTS (each a general page with more evidence; a theory, element or learner variable is a
parent when this page is one application or one source's version of it):
{cands}

Pick the candidate that this page most directly narrows, applies to one setting, or restates: the page
a designer reading this recommendation should have been reading. Pick "none" if no candidate is the
general version of this idea (a page that merely shares a topic or a word is not a parent).
Reply JSON: {{"parent": "<candidate key>" or "none", "why": "one clause"}}"""


def summary(key: str, n: int = 900) -> str:
    text = re.sub(r"<!--.*?-->", "", (WIKI_ROOT / f"{key}.md").read_text(encoding="utf-8"), flags=re.S)
    fm, _, body = text.partition("\n---\n")
    title = re.search(r"^title:\s*\"?(.*?)\"?\s*$", fm, re.M)
    desc = re.search(r"^description:\s*\"?(.*?)\"?\s*$", fm, re.M)
    body = re.sub(r"\s+", " ", re.sub(r"^>.*$", "", body, flags=re.M))
    return f"{title.group(1) if title else key}: {desc.group(1) if desc else ''}\n{body[:n]}"


WIDE = ("elements", "theories", "learner-variables")


def canonical_pages(folders) -> set:
    """Canonical pages of the wider kinds (every learner variable is one)."""
    out = set()
    for folder in folders:
        for p in (WIKI_ROOT / folder).glob("*.md"):
            if p.stem == "index":
                continue
            head = p.read_text(encoding="utf-8")[:3000].split("\n---", 1)[0]
            if folder == "learner-variables" or re.search(r"^canonical:\s*true\s*$", head, re.M):
                out.add(f"{folder}/{p.stem}")
    return out


def candidates(key: str, row: dict, eligible: set, db, folders=("principles", "patterns")) -> list:
    out = []
    if row.get("parent"):
        for folder in (key.split("/")[0], "principles", "patterns"):
            k = f"{folder}/{row['parent']}"
            if k in eligible and k not in out:
                out.append(k)
                break
    text = summary(key, 300)
    per = 10 // len(folders) + 2
    for folder in folders:
        n = 0
        for r in search_index.query(db, text, folder=folder, limit=30, mode="OR"):
            k = f"{r[1]}/{r[2]}"
            if k in eligible and k != key and k not in out:
                out.append(k)
                n += 1
            if n >= per:
                break
    return out[:12]


def ask(model: str, prompt: str, api_key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    try:
        res = oc.generate(model, "You judge the structure of a reference wiki. Reply with JSON only.", prompt,
                          api_key, max_tokens=2000, temperature=0.0)
        ans = extract_json(res.raw_text)
        return {"parent": ans.get("parent") or "none", "why": ans.get("why"), "cost_usd": res.cost_usd or 0}
    except Exception as e:
        return {"parent": None, "error": str(e)[:200], "cost_usd": 0}


def latest() -> dict:
    out = {}
    for line in OUT.read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        out[d["page"]] = d
    return out


def adjudicate(api_key: str, workers: int) -> None:
    todo = [d for d in latest().values() if not d.get("parent") and d.get("candidates")
            and (d.get("first") or {}).get("parent") and (d.get("second") or {}).get("parent")
            and d["first"]["parent"] != d["second"]["parent"]
            and (WIKI_ROOT / f"{d['page']}.md").exists()]

    def one(d):
        prompt = PROMPT.format(key=d["page"], page=summary(d["page"]),
                               cands="\n".join(f"- {c}: {summary(c, 250)}" for c in d["candidates"]))
        prompt += (f"\n\nTwo earlier readers disagreed. One chose {d['first']['parent']} ({d['first'].get('why')}); "
                   f"the other chose {d['second']['parent']} ({d['second'].get('why')}). Choose for yourself.")
        c = ask(THIRD, prompt, api_key)
        sides = c.get("parent") in (d["first"]["parent"], d["second"]["parent"])
        parent = c["parent"] if sides and c["parent"] in d["candidates"] else None
        return {**d, "third": c, "parent": parent, "settled": sides,
                "cost_usd": (d.get("cost_usd") or 0) + (c.get("cost_usd") or 0)}

    with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(one, todo))
        for r in res:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(res)} disagreement(s): parent {sum(1 for r in res if r['parent'])}, "
          f"none {sum(1 for r in res if r['settled'] and not r['parent'])}, "
          f"unsettled {sum(1 for r in res if not r['settled'])}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pages", nargs="+")
    g.add_argument("--from-worklist", metavar="STEP")
    g.add_argument("--pairs", action="store_true")
    g.add_argument("--adjudicate", action="store_true")
    ap.add_argument("--wide", action="store_true",
                    help="also offer canonical elements, theories and learner variables as parents, for pages "
                         "no principle or pattern is the general version of (merge_pages.py folds across kinds)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    if args.pairs:
        for d in latest().values():
            if d.get("parent"):
                print(f"{d['parent']}\t{d['page']}")
        return
    api_key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    if args.adjudicate:
        adjudicate(api_key, args.workers)
        return
    rows = {r["page"]: r for r in upgrade_worklist.rows()}
    eligible = {k for k, r in rows.items() if r["step"] in ("done", "reread", "convert")}
    folders = ("principles", "patterns")
    if args.wide:
        eligible |= canonical_pages(WIDE)
        folders = folders + WIDE
    keys = args.pages or [k for k, r in rows.items() if r["step"] == args.from_worklist]
    db = search_index.ensure()

    # The search index's connection belongs to this thread; gather candidates before the pool.
    cand_of = {key: candidates(key, rows.get(key, {}), eligible, db, folders) for key in keys}

    def one(key):
        cands = cand_of[key]
        if not cands:
            return {"page": key, "candidates": [], "parent": None, "why": "no candidate"}
        prompt = PROMPT.format(key=key, page=summary(key),
                               cands="\n".join(f"- {c}: {summary(c, 250)}" for c in cands))
        a, b = ask(FIRST, prompt, api_key), ask(SECOND, prompt, api_key)
        agreed = a.get("parent") == b.get("parent") and a.get("parent") in cands
        return {"page": key, "candidates": cands, "first": a, "second": b,
                "parent": a["parent"] if agreed else None,
                "cost_usd": (a.get("cost_usd") or 0) + (b.get("cost_usd") or 0)}

    OUT.parent.mkdir(parents=True, exist_ok=True)
    results = []
    with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
        for r in ex.map(one, keys):
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
            fh.flush()
            results.append(r)
    agreed = [r for r in results if r.get("parent")]
    none = [r for r in results if (r.get("first") or {}).get("parent") == "none" == (r.get("second") or {}).get("parent")]
    print(f"{len(results)} page(s): parent agreed for {len(agreed)}; both said none for {len(none)}; "
          f"{len(results) - len(agreed) - len(none)} disagree or failed; "
          f"cost ${sum(r.get('cost_usd') or 0 for r in results):.3f}")


if __name__ == "__main__":
    main()
