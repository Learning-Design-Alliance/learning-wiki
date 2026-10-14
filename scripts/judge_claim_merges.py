#!/usr/bin/env python3
"""
judge_claim_merges.py — decide which proposed "same claim" pairs are one finding, and merge those.

Extraction writes claims one article at a time, so the same finding from three studies is three
claim pages of one study each: on 2026-10-13, 17,559 of 17,943 claims rested on a single study.
link_claims.py proposes pairs it thinks state the same proposition and labels them on both pages
("possibly the same claim (merge candidate)"); 1,139 such pairs were open. One model's "same" is
not enough to fold a page, so this shows two models from different families both claims (title,
description and the opening of each evidence entry) and folds a pair only when both say it is the
same proposition: the same intervention or variable, the same outcome, the same direction, and
comparable learners. A broader and a narrower claim are not the same; neither are two outcomes
or two populations.

The claim more pages link to is kept; on a tie, the one with more studies. merge_claims.py does
the fold: the other claim's studies join the kept page, its slug becomes an alias, and a
differing write-up of a shared study is kept in a <!-- merged --> comment. Chains (a=b, b=c) fold
into whatever survived.

    python3 scripts/judge_claim_merges.py --judge            # decisions to eval/claim-merges/decisions.ndjson
    python3 scripts/judge_claim_merges.py --apply            # merge the pairs both models agreed on
"""
import argparse
import collections
import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402

OUT = WIKI_ROOT / "eval" / "claim-merges" / "decisions.ndjson"
FIRST = "openai/gpt-5.6-luna"
SECOND = "deepseek/deepseek-v4-pro"
LABEL_RE = re.compile(r"\]\(([^)#\s]+)\.md\)\s*—\s*possibly the same claim")
SYSTEM = "You maintain a learning-design wiki of empirical claims. Reply with one JSON object and nothing else."
PROMPT = """Two claim pages may state the same finding.

A: {a_title}
{a_text}

B: {b_title}
{b_text}

Are A and B the SAME proposition, so that one page with both studies' evidence would lose nothing?
They are the same only if they share the intervention or variable, the outcome, the direction of the
effect, and comparable learners. A broader claim and a narrower one are NOT the same. Two different
outcomes (retention vs transfer), two populations (children vs adults), two settings that change the
claim, or opposite directions are NOT the same.
Reply: {{"same": true|false, "why": "<one sentence>"}}"""


def pairs() -> list:
    out = set()
    for p in (WIKI_ROOT / "claims").glob("*.md"):
        for m in LABEL_RE.finditer(p.read_text(encoding="utf-8")):
            b = m.group(1).split("/")[-1]
            if b != p.stem:
                out.add(tuple(sorted((p.stem, b))))
    return sorted(out)


def text_of(slug: str) -> tuple:
    raw = (WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8")
    fm_lines, body = okf_lib.split_frontmatter(raw)
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    ev = body.split("## Evidence", 1)[1] if "## Evidence" in body else body
    ev = re.sub(r"^> .*$", "", ev.split("## Discussion", 1)[0], flags=re.M)
    return str(fm.get("title") or slug), (str(fm.get("description") or "") + "\n" + " ".join(ev.split())[:1500])


def studies(slug: str) -> int:
    raw = (WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8")
    return len(re.findall(r"^### ", raw.split("## Evidence", 1)[-1].split("## Discussion", 1)[0], re.M))


def ask(model: str, prompt: str, key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=3000)
    d = extract_json(gen.raw_text) or {}
    return {"same": d.get("same") is True, "why": d.get("why"), "cost_usd": gen.cost_usd or 0}


def judge(workers: int) -> None:
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    rev = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))["edges"].get("claims", {})
    inbound = {s: sum(len(v) for v in by.values()) for s, by in rev.items()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    done = {tuple(sorted((d["keep"], d["fold"]))) for d in decisions()}
    todo = [p for p in pairs() if p not in done and all((WIKI_ROOT / "claims" / f"{s}.md").exists() for s in p)]
    print(f"{len(todo)} pair(s) to judge", flush=True)

    def one(pair):
        a, b = pair
        at, ax = text_of(a)
        bt, bx = text_of(b)
        prompt = PROMPT.format(a_title=at, a_text=ax, b_title=bt, b_text=bx)
        try:
            first = ask(FIRST, prompt, key)
            second = ask(SECOND, prompt, key) if first["same"] else {"same": False, "why": None, "cost_usd": 0}
        except Exception as e:  # noqa: BLE001 - a failed call merges nothing
            return {"keep": a, "fold": b, "same": False, "error": f"{type(e).__name__}: {e}"[:200]}
        ka = (inbound.get(a, 0), studies(a))
        kb = (inbound.get(b, 0), studies(b))
        keep, fold = (a, b) if ka >= kb else (b, a)
        return {"keep": keep, "fold": fold, "same": first["same"] and second["same"],
                "first": first, "second": second, "cost_usd": first["cost_usd"] + second["cost_usd"]}

    with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        futs = [ex.submit(one, p) for p in todo]
        for n, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            fh.write(json.dumps(fut.result()) + "\n")
            fh.flush()
            if n % 200 == 0:
                print(n, flush=True)
    summary()


def decisions() -> list:
    return [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()] if OUT.exists() else []


def summary() -> None:
    ds = decisions()
    print(f"{len(ds)} judged: {sum(d['same'] for d in ds)} the same finding (both models), "
          f"{sum(1 for d in ds if d.get('first', {}).get('same') and not d['same'])} where the second model "
          f"disagreed, {sum(1 for d in ds if 'error' in d)} errors; cost ${sum(d.get('cost_usd') or 0 for d in ds):.2f}")


def apply() -> None:
    gone, to = set(), {}
    pairs_out = []
    for d in decisions():
        if not d["same"]:
            continue
        keep, fold = d["keep"], d["fold"]
        while keep in gone:
            keep = to[keep]
        while fold in gone:
            fold = to[fold]
        if keep == fold or not (WIKI_ROOT / "claims" / f"{fold}.md").exists():
            continue
        pairs_out.append((keep, fold))
        gone.add(fold)
        to[fold] = keep
    tsv = OUT.with_name("pairs.tsv")
    tsv.write_text("".join(f"{k}\t{f}\n" for k, f in pairs_out), encoding="utf-8")
    print(f"merging {len(pairs_out)} pair(s) -> {tsv}", flush=True)
    subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "merge_claims.py"), "--apply", "--pairs", str(tsv)],
                   cwd=WIKI_ROOT, check=True)
    # A page that cited both claims now lists the kept one twice in a section.
    subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "dedupe_claim_bullets.py"), "--apply"],
                   cwd=WIKI_ROOT, check=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--judge", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    if args.judge:
        judge(args.workers)
    if args.summary:
        summary()
    if args.apply:
        apply()


if __name__ == "__main__":
    main()
