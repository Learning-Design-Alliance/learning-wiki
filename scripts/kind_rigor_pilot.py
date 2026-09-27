#!/usr/bin/env python3
"""
kind_rigor_pilot.py — code a sample of evidence entries with an evidence KIND and a
rigour tier judged within that kind (eval/kind-rigor/RUBRIC.md), beside their
current `q`, to see whether the split is worth making wiki-wide. Writes nothing to
any page.

    python3 scripts/kind_rigor_pilot.py --sample 40            # two runs, GPT, ~$0.10
    python3 scripts/kind_rigor_pilot.py --report                # summarise the last run

The sample is stratified by current q (1-4) and deliberately includes entries whose
text names a qualitative method, because the question is how those fare. Each entry
is judged against its study's own text (cached article, else the OpenAlex abstract),
the same sources check_load_bearing.py uses, and coded twice independently so the
agreement between runs can be read.
"""
import argparse
import collections
import concurrent.futures
import hashlib
import json
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import check_load_bearing as clb  # noqa: E402

OUT = WIKI_ROOT / "eval" / "runs" / "kind-rigor" / "pilot.ndjson"
RUBRIC = (WIKI_ROOT / "eval" / "kind-rigor" / "RUBRIC.md").read_text(encoding="utf-8")
KINDS = ["causal", "quant-synthesis", "review", "associational", "qualitative", "design", "theoretical"]
QUAL = re.compile(r"qualitativ|interview|focus group|ethnograph|thematic|case study|phenomenolog|grounded theory", re.I)
SYSTEM = "You appraise research evidence for a learning-design wiki. Reply with JSON only."


def sample(n: int) -> list:
    pages = clb.claim_pages()
    rows = clb.ranking(pages)
    jobs, _ = clb.entry_jobs(rows, pages, offline=True)
    by_q, qual = collections.defaultdict(list), []
    for j in jobs:
        codes = re.search(r"^`q[^\n]*`\s*$", j[3], re.M)
        m = re.search(r"\bq([1-4])\b", codes.group(0)) if codes else None
        if not m:
            continue
        item = (int(m.group(1)), j)
        (qual if QUAL.search(j[3]) else by_q[item[0]]).append(item)
    key = lambda it: hashlib.sha1(f"{it[1][0]['claim']}#{it[1][1]}".encode()).hexdigest()
    picked = sorted(qual, key=key)[: n // 4]
    per = (n - len(picked)) // 4
    for q in (1, 2, 3, 4):
        picked += sorted(by_q[q], key=key)[:per]
    return picked


def code(q: int, job: tuple, run: int, key: str, model: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    r, anchor, title, block, subs, source, basis, text = job[:8]
    text = text if len(text) <= 30000 else text[:30000] + "\n[TRUNCATED]"
    prompt = (f"{RUBRIC}\n\n## The study ({basis}: {source})\n{text}\n\n## The wiki's evidence entry\n{block}\n\n"
              'Code this study. Reply: {"kind": one of ' + json.dumps(KINDS) + ', "rigour": 1-3, '
              '"why": "one sentence naming the criteria met or missed", '
              '"q_fits_question": "does the current q code (' + f"q{q}" + ') misrepresent this study\'s value '
              'for the question it answers? yes/no and one clause"}')
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=1500)
    d = extract_json(gen.raw_text)
    return {"claim": r["claim"], "entry": anchor, "q": q, "run": run, "basis": basis,
            "qual_text": bool(QUAL.search(block)), "kind": d.get("kind"), "rigour": d.get("rigour"),
            "why": d.get("why"), "q_fits_question": d.get("q_fits_question"), "cost_usd": gen.cost_usd}


def report(rows: list) -> None:
    by = collections.defaultdict(dict)
    for x in rows:
        by[(x["claim"], x["entry"])][x["run"]] = x
    pairs = [v for v in by.values() if 1 in v and 2 in v]
    agree_kind = sum(v[1]["kind"] == v[2]["kind"] for v in pairs)
    agree_rig = sum(v[1]["rigour"] == v[2]["rigour"] for v in pairs)
    print(f"{len(by)} entries, {len(pairs)} coded twice: kind agrees {agree_kind}/{len(pairs)}, "
          f"rigour agrees {agree_rig}/{len(pairs)}; cost ${sum(x.get('cost_usd') or 0 for x in rows):.3f}")
    first = [v[1] for v in by.values() if 1 in v]
    table = collections.Counter((x["q"], x["kind"], x["rigour"]) for x in first)
    print("\ncurrent q -> kind, rigour (run 1):")
    for (q, k, g), n in sorted(table.items(), key=lambda t: (t[0][0], str(t[0][1]), t[0][2] or 0)):
        print(f"  q{q}  {k:16} r{g}  x{n}")
    mis = [x for x in first if str(x.get("q_fits_question", "")).lower().startswith("yes")]
    print(f"\nq misrepresents the study's value (run 1): {len(mis)} of {len(first)}")
    for x in mis:
        print(f"  q{x['q']} {x['kind']} r{x['rigour']}  claims/{x['claim']}.md#{x['entry']}\n      {x['why']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sample", type=int, default=40)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    args = ap.parse_args()
    if args.report:
        report([json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()])
        return
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    picked = sample(args.sample)
    print(f"{len(picked)} entries sampled ({sum(1 for q, j in picked if QUAL.search(j[3]))} with qualitative text)")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    with OUT.open("w", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(8) as ex:
        futs = [ex.submit(code, q, j, run, key, args.model) for q, j in picked for run in (1, 2)]
        for f in concurrent.futures.as_completed(futs):
            try:
                x = f.result()
            except Exception as e:
                print("  error:", str(e)[:120])
                continue
            rows.append(x)
            fh.write(json.dumps(x) + "\n")
    report(rows)


if __name__ == "__main__":
    main()
