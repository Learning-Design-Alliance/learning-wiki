"""
agent_arm.py — the in-session arm of the pre-extractor test.

The other arms of eval/pre-extractor-test/ are ordinary `eval_harness.py run`
batches: one OpenRouter call per article, no tools. This arm is a Claude Code
subagent that gets the SAME system prompt and the same article text, plus what
a container session has and the droplet does not: the whole article (no 60k
truncation), the whole slug list, Crossref, and the wiki itself to grep.

It exists so the two can be scored by the same code. `prepare` writes one task
folder per article; the agent writes `output.json` there; `record` validates
and judges that output exactly as `eval_harness.run_one` does and writes a
harness-shaped record under eval/runs/<run-id>/, so `eval_harness.py report`,
`compare` and pre_extractor_test.py read it like any other model.

What differs, and is recorded rather than hidden:
  * generation.cost_usd is an ESTIMATE from the agent's reported total tokens
    (cost_source says so). A subagent's token count mixes cached reads, fresh
    input and output, and the Agent tool reports only the total, so the
    estimate is a bracket, not a bill. See pre_extractor_test.py.
  * generation.latency_s is the agent's wall-clock, tool calls included.
  * The agent may reject a source (INCLUSION.md E1-E4) with a top-level
    `inclusion` block. The headless contract has no way to say that, which is
    itself one of the things the reject-probe articles measure.

    python3 -m scripts.eval.agent_arm prepare --run-id pxt-agent-opus55
    python3 -m scripts.eval.agent_arm record  --run-id pxt-agent-opus55 \
        --article eric-ed409895 --wall-s 312 --total-tokens 184000 --tool-uses 22
"""

import argparse
import json
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from scripts import eval_harness
from scripts.eval import fetch_article, prompts, validator
from scripts.eval.jsonutil import extract_json, JSONExtractionError

WIKI_ROOT = Path(__file__).resolve().parents[2]

AGENT_MODEL = "claude-code-agent/opus-5.5"
# List price per token on OpenRouter as of 2026-09-24: (input, cache read, output).
# Used only for the cost bracket (see cost_bracket).
AGENT_PRICES = {
    "claude-code-agent/opus-5.5": (4.0e-6, 0.4e-6, 20.0e-6),
    "claude-code-agent/sonnet-5": (2.0e-6, 0.2e-6, 10.0e-6),
}
DEFAULT_MANIFEST = WIKI_ROOT / "eval" / "pre-extractor-test" / "manifest.json"


TASK_TEMPLATE = """# Extraction task: {article_id}

You are the in-session arm of a head-to-head extraction test. Another arm is a
headless model given exactly `system_prompt.txt` + `user_prompt.txt` and no
tools. You get the same instructions and the same article, and you may use
tools. Your output is scored by the same validator and the same judges.

## Inputs (all in this folder)
- `system_prompt.txt` — the extraction instructions (prompt {prompt_version}). Follow its
  output contract exactly. Its private passes (coverage plan, quote ledger)
  are yours to do in your own working; they never go in the output.
- `article.txt` — the article's full text, untruncated.
- `slugs.json` — every real wiki slug, by folder. Cross-link ONLY to these or
  to a sibling contribution in your own output. Grep the wiki
  (/home/user/learning-wiki/<folder>/<slug>.md) if you need to know what a
  page says before linking it.
- `/home/user/learning-wiki/INCLUSION.md` — the inclusion criteria.

## What you may do that the headless arm cannot
- Read the whole article, in as many passes as you need.
- Check that every `source_quote` really is a verbatim substring of article.txt
  (e.g. with python) before you finish. A quote that is not is a fabrication.
- Resolve DOIs against Crossref (`https://api.crossref.org/works/<doi>`, via
  python requests; the proxy is preconfigured). Put a DOI in a citation ONLY
  if it is printed in the article OR Crossref confirms it resolves to this
  exact title. Never write a DOI from memory. Omitting one is always safe.
- Decide the source should not be ingested. If INCLUSION.md excludes it (E1
  opinion-piece, E2 out-of-scope — not about learning at all, E3
  no-ingestable-content, E4 already-covered), output
  `{{"article": {{...}}, "inclusion": {{"verdict": "reject", "reason_code":
  "out-of-scope", "reason": "one sentence"}}, "contributions": []}}`.
  Otherwise add `"inclusion": {{"verdict": "include"}}` and extract normally.
  Remember the default is to include: domain or setting is never a reason
  to exclude, and a theoretical or qualitative source is eligible.

{benchmark_note}## Rules
- Do NOT write, edit or create any file outside this folder. Do not touch the
  wiki's content folders, git, or any other task folder.
- Keep any helper scripts in this folder too, never in a shared scratchpad: parallel agents
  run at the same time and overwrite each other's files.
- Write exactly one file of output: `output.json` in this folder, a single JSON object
  matching the output contract. Validate it with
  `python3 -c "import json; json.load(open('output.json'))"` before finishing.
- Then run the structural validator and fix every ERROR it reports:
  `cd /home/user/learning-wiki && python3 -m scripts.eval.agent_arm check --run-id {run_id} --article {article_id}`
- Finish with a two-line reply: the number of contributions, and anything you
  could not establish. Nothing else.
"""


# For re-running an article the wiki already holds, e.g. to compare a second
# model on the same corpus. Without it an agent correctly rejects the source as
# E4 already-covered, and the run measures nothing.
BENCHMARK_NOTE = """## This is a benchmark run
This article may already be in the wiki: another extractor's output from it
may have been ingested earlier. Do NOT reject it as E4 already-covered, and do
not read or copy the existing pages it produced. Extract it as though the wiki
had never seen it. Every other inclusion rule still applies.

"""


def _task_dir(run_id: str, article_id: str) -> Path:
    return eval_harness.RUNS_DIR / run_id / "_tasks" / article_id


def _load_articles(manifest: Path, ids=None) -> list:
    arts = json.loads(manifest.read_text(encoding="utf-8"))["articles"]
    return [a for a in arts if not ids or a["id"] in ids]


def cmd_prepare(args) -> None:
    slugs = eval_harness.get_existing_slugs()
    system_prompt = prompts.load_prompt(args.prompt_version)
    for entry in _load_articles(Path(args.manifest), args.articles):
        d = _task_dir(args.run_id, entry["id"])
        d.mkdir(parents=True, exist_ok=True)
        text = fetch_article.fetch_article_text(entry)
        (d / "article.txt").write_text(text, encoding="utf-8")
        (d / "system_prompt.txt").write_text(system_prompt, encoding="utf-8")
        (d / "user_prompt.txt").write_text(
            prompts.build_user_prompt(text, slugs, max_chars=10**9), encoding="utf-8")
        (d / "slugs.json").write_text(json.dumps(slugs), encoding="utf-8")
        (d / "entry.json").write_text(json.dumps(entry, indent=2), encoding="utf-8")
        (d / "TASK.md").write_text(TASK_TEMPLATE.format(
            article_id=entry["id"], prompt_version=args.prompt_version, run_id=args.run_id,
            benchmark_note=BENCHMARK_NOTE if args.benchmark else ""), encoding="utf-8")
        print(f"[prepared] {d.relative_to(WIKI_ROOT)}  ({len(text):,} chars)")


def _validate(d: Path, parsed, slugs):
    text = (d / "article.txt").read_text(encoding="utf-8")
    return text, validator.validate_output(parsed or {}, slugs, article_text=text)


def cmd_check(args) -> None:
    d = _task_dir(args.run_id, args.article)
    raw = (d / "output.json").read_text(encoding="utf-8")
    try:
        parsed = extract_json(raw)
    except JSONExtractionError as e:
        print(f"PARSE ERROR: {e}")
        sys.exit(1)
    if (parsed.get("inclusion") or {}).get("verdict") == "reject":
        print("Rejected source: validator not applicable (no contributions expected).")
        return
    _, report = _validate(d, parsed, eval_harness.get_existing_slugs())
    for i in report.issues:
        print(f"[{i.severity}] {i.field}: {i.message}")
    print(f"passed={report.passed} completeness={report.completeness_score} "
          f"errors={report.error_count} warnings={report.warning_count}")


def cost_bracket(total_tokens: int, output_tokens_guess: int = 20_000,
                 model: str = AGENT_MODEL) -> dict:
    """Low: everything but the output is a cache read. High: everything but
    the output is fresh input. The truth sits between, nearer the low end
    for a long agent loop, which rereads its context on every turn."""
    fresh, cache_read, output = AGENT_PRICES[model]
    out = min(output_tokens_guess, total_tokens)
    rest = max(0, total_tokens - out)
    return {
        "low_usd": round(rest * cache_read + out * output, 4),
        "high_usd": round(rest * fresh + out * output, 4),
    }


def cmd_record(args) -> None:
    d = _task_dir(args.run_id, args.article)
    entry = json.loads((d / "entry.json").read_text(encoding="utf-8"))
    slugs = eval_harness.get_existing_slugs()
    raw = (d / "output.json").read_text(encoding="utf-8") if (d / "output.json").exists() else ""
    bracket = cost_bracket(args.total_tokens, model=args.agent_model)
    record = {
        "article_id": entry["id"],
        "article_title": entry["title"],
        "model": args.agent_model,
        "prompt_version": args.prompt_version,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generation": {
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": args.total_tokens,
            "tool_uses": args.tool_uses,
            "latency_s": args.wall_s,
            # Midpoint of the bracket, so harness tables have one number;
            # pre_extractor_test.py reports the bracket itself.
            "cost_usd": round((bracket["low_usd"] + bracket["high_usd"]) / 2, 4),
            "cost_bracket_usd": bracket,
            "cost_source": "estimate:agent-total-tokens",
        },
        "raw_text": raw,
        "parsed": None,
        "parse_error": None,
        "validation": None,
        "judges": {},
        "correction_attempts": 0,
        "initial_passed": None,
    }
    parsed = None
    try:
        parsed = extract_json(raw)
        record["parsed"] = parsed
    except JSONExtractionError as e:
        record["parse_error"] = str(e)

    text, report = _validate(d, parsed, slugs)
    record["validation"] = {
        "passed": report.passed, "n_contributions": report.n_contributions,
        "completeness_score": report.completeness_score, "error_count": report.error_count,
        "warning_count": report.warning_count, "parse_error": report.parse_error or record["parse_error"],
        "issues": [asdict(i) for i in report.issues],
    }
    # The agent validated its own output before finishing, so its first
    # attempt is not comparable to a headless first attempt. Recorded as
    # such rather than as a pass it never had to earn.
    record["initial_passed"] = None
    rejected = (parsed or {}).get("inclusion", {}).get("verdict") == "reject"
    if parsed and not rejected and args.judges:
        record["judges"] = eval_harness.run_judges(
            text, parsed, args.judges, "gpt-5.6-luna",
            api_key=__import__("os").environ.get("OPENROUTER_API_KEY"))
    out = eval_harness.result_path(eval_harness.RUNS_DIR / args.run_id, args.agent_model, entry["id"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2), encoding="utf-8")
    j = {k: v.get("average_score") for k, v in record["judges"].items() if isinstance(v, dict)}
    print(f"[recorded] {entry['id']} passed={report.passed} n={report.n_contributions} "
          f"rejected={rejected} judges={j}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    pp = sub.add_parser("prepare")
    pp.add_argument("--run-id", required=True)
    pp.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    pp.add_argument("--articles", nargs="+", default=None)
    pp.add_argument("--prompt-version", default="v130")
    pp.add_argument("--benchmark", action="store_true",
                    help="tell agents the article may already be ingested and E4 does not apply")
    pc = sub.add_parser("check")
    pc.add_argument("--run-id", required=True)
    pc.add_argument("--article", required=True)
    pr = sub.add_parser("record")
    pr.add_argument("--run-id", required=True)
    pr.add_argument("--article", required=True)
    pr.add_argument("--wall-s", type=float, required=True)
    pr.add_argument("--total-tokens", type=int, required=True)
    pr.add_argument("--tool-uses", type=int, default=None)
    pr.add_argument("--prompt-version", default="v130")
    pr.add_argument("--judges", nargs="*", default=["gpt", "gemini"])
    pr.add_argument("--agent-model", default=AGENT_MODEL, choices=sorted(AGENT_PRICES),
                    help="which subagent model produced this output (sets the record's model and price)")
    args = p.parse_args()
    {"prepare": cmd_prepare, "check": cmd_check, "record": cmd_record}[args.cmd](args)


if __name__ == "__main__":
    main()
