#!/usr/bin/env python3
"""
sort_claims.py — sort claims by how a design decision could depend on them.

The test is the maintainer's (2026-10-13): a claim belongs in the wiki when a design decision could
change because of it. A first sort asked "is this about learners learning?" and filed knowledge-
tracing accuracy as not-design, though a course built on knowledge tracing is designed differently if
KT is inaccurate. That sort drove a removal that was reverted the same day. So the categories are:

  design-choice      evidence about an instructional or design choice, or about how a learner
                     characteristic relates to learning outcomes
  component          the accuracy, reliability, validity or failure modes of a tool, model, instrument
                     or technology a design could rely on (knowledge tracing, automated scoring, AI
                     feedback or tutoring, AI-text detection, early-warning prediction, placement tests)
  context-general    a need, a learner population or a baseline that informs a design beyond the one
                     setting it was measured in (attainment gaps, typical growth, the size of a need)
  context-local      a fact about one district, institution, programme or year that a designer
                     elsewhere could not use
  research-practice  about how research is done (coder agreement, model fit of a questionnaire,
                     bibliometric counts) with no bearing on a design

Two models from different families read each claim; a category is settled only where they agree.
Everything is kept; only settled research-practice and context-local claims are candidates for the
maintainer to remove.

    python3 scripts/sort_claims.py --uncited            # claims no concept page cites
    python3 scripts/sort_claims.py --summary
"""
import argparse
import collections
import concurrent.futures
import json
import os
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402

OUT = WIKI_ROOT / "eval" / "claim-sort" / "sort.ndjson"
MODELS = ("z-ai/glm-5.3-flash", "openai/gpt-5.6-luna")
CATEGORIES = ("design-choice", "component", "context-general", "context-local", "research-practice")
PROMPT = """A learning-design wiki keeps an empirical claim when a design decision could change because of it.
Sort this claim into exactly one category.

Claim: {title}
{description}

- design-choice: evidence about an instructional or design choice (a strategy, activity, feedback,
  technology use, programme, curriculum, tutoring, assessment practice), or about how a learner
  characteristic relates to learning outcomes.
- component: the accuracy, reliability, validity or failure modes of a tool, model, instrument or
  technology a course could rely on (knowledge tracing, automated scoring, AI feedback or tutoring,
  AI-text detection, early-warning prediction, a placement test). A designer building on it would
  design differently if it does not work as expected.
- context-general: a need, a learner population or a baseline that informs designs beyond the one
  setting it was measured in (an attainment gap, typical growth, how widespread a problem is).
- context-local: a fact about one district, institution, programme or year that a designer elsewhere
  could not use.
- research-practice: about how research is done (coder agreement, a questionnaire's factor structure,
  bibliometric counts, study quality) with no bearing on any design.
For component, name the component in two to four words.
Reply with JSON only: {{"category": "<one of the five>", "component": "<name or null>"}}"""


def uncited_claims() -> list:
    rev = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))["edges"].get("claims", {})
    return sorted(p.stem for p in (WIKI_ROOT / "claims").glob("*.md")
                  if p.stem != "index" and not any(k != "claims" and v for k, v in (rev.get(p.stem) or {}).items()))


def ask(model: str, slug: str, key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    fm_lines, _ = okf_lib.split_frontmatter((WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8"))
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)
    gen = oc.generate(model, "Reply with one JSON object.",
                      PROMPT.format(title=fm.get("title") or slug, description=fm.get("description") or ""),
                      key, max_tokens=1500)
    d = extract_json(gen.raw_text) or {}
    cat = str(d.get("category") or "").strip().lower()
    return {"category": cat if cat in CATEGORIES else None, "component": d.get("component"),
            "cost_usd": gen.cost_usd or 0}


def run(slugs: list, workers: int) -> None:
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    done = {json.loads(l)["claim"] for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()} \
        if OUT.exists() else set()
    todo = [s for s in slugs if s not in done]
    print(f"{len(slugs)} claim(s), {len(todo)} to sort", flush=True)

    def one(slug):
        votes = {}
        for m in MODELS:
            try:
                votes[m] = ask(m, slug, key)
            except Exception as e:  # noqa: BLE001 - a failed call is a missing vote, never a category
                votes[m] = {"category": None, "error": f"{type(e).__name__}: {e}"[:200], "cost_usd": 0}
        cats = {v["category"] for v in votes.values()}
        settled = cats.pop() if len(cats) == 1 and None not in cats else None
        return {"claim": slug, "category": settled, "votes": votes}

    with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        for i, rec in enumerate(ex.map(one, todo)):
            fh.write(json.dumps(rec) + "\n")
            fh.flush()
            if i % 500 == 0:
                print(i, flush=True)
    summary()


def summary() -> None:
    recs = [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines() if l.strip()]
    live = [r for r in recs if (WIKI_ROOT / "claims" / f"{r['claim']}.md").exists()]
    print(f"{len(live)} sorted claim(s) on disk")
    for cat, n in collections.Counter(r["category"] or "disputed" for r in live).most_common():
        print(f"  {cat:18} {n}")
    print(f"cost ${sum(v.get('cost_usd') or 0 for r in recs for v in r['votes'].values()):.2f}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--uncited", action="store_true", help="claims no page outside claims/ cites")
    g.add_argument("--summary", action="store_true")
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()
    if args.summary:
        summary()
    else:
        run(uncited_claims(), args.workers)


if __name__ == "__main__":
    main()
