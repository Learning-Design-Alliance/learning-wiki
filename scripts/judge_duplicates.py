#!/usr/bin/env python3
"""
judge_duplicates.py — decide which near-duplicate title pairs are one page written twice,
and fold those.

find_title_duplicates.py proposes pairs by title overlap alone, which is not enough to act
on: "Speech-to-Text Technology" and "Text-to-Speech Technology" overlap completely and are
different tools. This shows a model both pages (title, description and the opening of the
body) and asks whether they describe the same practice; a second model must agree before a
pair is folded. In search the unfolded pairs crowd the first results (four spacing
strategies above the spacing principle, 2026-10-12).

The page that stays is the one more pages link to; on a tie, the hyphenated slug, which is
the wiki's convention. merge_pages.py does the fold: the folded page's bullets the kept
page lacks are added, its body is kept in a <!-- merged --> comment, its slug becomes an
alias, and every inbound link is re-pointed.

    python3 scripts/judge_duplicates.py --type strategies              # ask; decisions to eval/duplicates/ (committed)
    python3 scripts/judge_duplicates.py --type strategies --apply      # ask, then fold the agreed pairs
    python3 scripts/judge_duplicates.py --from <decisions.ndjson> --apply
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

FIRST = "openai/gpt-5.6-luna"
SECOND = "deepseek/deepseek-v4-pro"
SYSTEM = "You maintain a learning-design wiki. Reply with one JSON object and nothing else."
PROMPT = """Two {kind} pages in the wiki may be one page written twice.

A: {a_title}
{a_text}

B: {b_title}
{b_text}

Are A and B the same {kind}: the same practice, for the same purpose, such that a reader
would want one page, not two? Pages that share words but differ in what is done (speech-to-text
against text-to-speech, monitoring progress against monitoring behaviour), in who does it, or
in what it is for are NOT the same; a broader page and a narrower one are not the same either.
Reply: {{"same": true|false, "why": "<one sentence>"}}"""


def pairs_from_report(kind: str) -> list:
    out = subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "find_title_duplicates.py"), "--type", kind,
                          "--out", "/dev/stdout"], cwd=WIKI_ROOT, capture_output=True, text=True).stdout
    return re.findall(r"^- `[\d.]+` (\S+)\.md ⇄ (\S+)\.md", out, re.M)


def text_of(kind: str, slug: str) -> tuple:
    path = WIKI_ROOT / kind / f"{slug}.md"
    fm_lines, body = okf_lib.split_frontmatter(path.read_text(encoding="utf-8"))
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"^> .*$", "", body, flags=re.M)
    return str(fm.get("title") or slug), (str(fm.get("description") or "") + "\n" + " ".join(body.split())[:900])


def ask(model: str, prompt: str, key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=3000)
    d = extract_json(gen.raw_text) or {}
    return {"same": bool(d.get("same")), "why": d.get("why"), "cost_usd": gen.cost_usd or 0}


def inbound(kind: str) -> dict:
    rev = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))
    return {slug: sum(len(v) for v in by.values()) for slug, by in rev["edges"].get(kind, {}).items()}


def judge(kind: str, pairs: list, out: Path, workers: int) -> list:
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    links = inbound(kind)

    def one(pair):
        a, b = pair
        if not ((WIKI_ROOT / kind / f"{a}.md").exists() and (WIKI_ROOT / kind / f"{b}.md").exists()):
            return None
        at, ax = text_of(kind, a)
        bt, bx = text_of(kind, b)
        prompt = PROMPT.format(kind=kind[:-1].replace("strategie", "strategy"), a_title=at, a_text=ax,
                               b_title=bt, b_text=bx)
        first = ask(FIRST, prompt, key)
        second = ask(SECOND, prompt, key) if first["same"] else {"same": False, "why": None, "cost_usd": 0}
        la, lb = links.get(a, 0), links.get(b, 0)
        keep, fold = (a, b) if (la, "_" not in a) >= (lb, "_" not in b) else (b, a)
        return {"kind": kind, "keep": keep, "fold": fold, "same": first["same"] and second["same"],
                "first": first, "second": second, "cost_usd": first["cost_usd"] + second["cost_usd"]}

    decisions = []
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        for d in ex.map(one, pairs):
            if d:
                fh.write(json.dumps(d) + "\n")
                decisions.append(d)
    print(f"judged {len(decisions)} pair(s): {sum(d['same'] for d in decisions)} the same page, "
          f"cost ${sum(d['cost_usd'] for d in decisions):.3f}; decisions -> {out}")
    return decisions


def apply(decisions: list) -> int:
    import merge_pages
    folded, gone = 0, set()
    for d in decisions:
        if not d["same"]:
            continue
        keep, fold = d["keep"], d["fold"]
        # A chain (a=b, b=c) folds into whatever survived the earlier fold.
        while keep in gone:
            keep = gone_to[keep]
        if fold in gone or keep == fold or not (WIKI_ROOT / d["kind"] / f"{fold}.md").exists():
            continue
        merge_pages.merge(d["kind"], keep, fold, True)
        gone.add(fold)
        gone_to[fold] = keep
        folded += 1
    return folded


gone_to = {}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--type", choices=list(okf_lib.CONTENT_FOLDERS))
    src.add_argument("--from", dest="from_file")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    if args.from_file:
        decisions = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        pairs = pairs_from_report(args.type)
        print(f"{len(pairs)} candidate pair(s) in {args.type}")
        out = WIKI_ROOT / "eval" / "duplicates" / f"{args.type}.ndjson"
        decisions = judge(args.type, pairs, out, args.workers)
    print(collections.Counter("same" if d["same"] else "different" for d in decisions))
    for d in [d for d in decisions if d["same"]][:15]:
        print(f"  fold {d['fold']} -> {d['keep']}: {(d['second'].get('why') or '')[:90]}")
    if args.apply:
        print(f"folded {apply(decisions)} page(s)")


if __name__ == "__main__":
    main()
