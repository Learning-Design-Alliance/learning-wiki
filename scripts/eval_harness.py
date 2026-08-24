#!/usr/bin/env python3
"""
eval_harness.py — Repeatable cost/speed/quality test harness for open-weight
OpenRouter models on the article-ingestion task, before committing to a full
scrape-and-ingest run.

For each (model x article) pair it: fetches the article, calls the model with
the ingest JSON contract (scripts/eval/prompts.py), runs a deterministic
structural validator (scripts/eval/validator.py), and scores the extraction
against the source with one or two LLM judges (scripts/eval/judge.py, Claude
Opus 5 and/or an OpenAI model). Every result is cached to disk per
(run, model, article) so a run is resumable and re-scoring doesn't require
paying for generation again.

Workflow:
    # 0. Confirm every manifest URL still resolves before spending money
    python3 -m scripts.eval.fetch_article

    # 1. Run a smoke test: a couple of cheap models across all 10 articles
    python3 scripts/eval_harness.py run \\
        --models qwen/qwen3-30b-a3b google/gemma-3-27b-it \\
        --judges opus gpt

    # 2. Look at the aggregate numbers
    python3 scripts/eval_harness.py report --run-id <run-id printed by `run`>

    # 3. Re-score an existing run (e.g. after tweaking the judge rubric) —
    #    free of OpenRouter generation cost, only re-pays judge cost
    python3 scripts/eval_harness.py spotcheck --run-id <run-id> --judges opus

Options (run):
    --models        space-separated OpenRouter model slugs (required)
    --articles      space-separated article ids to restrict to (default: whole manifest)
    --limit         cap number of articles per model (default: all)
    --judges        space-separated judge names: opus, gpt (default: both)
    --gpt-judge-model  override the OpenAI judge model id (default: gpt-5.6)
    --run-id        reuse an existing run directory instead of starting a new one
    --overwrite     re-generate even if a cached result already exists
    --refresh-cache force re-fetch of article text (bypasses the article text cache)
    --max-tokens    generation max_tokens (default: 8000)
"""

import argparse
import csv
import json
import os
import sys
import time
from dataclasses import asdict
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.eval import fetch_article, openrouter_client, validator, judge
from scripts.eval.jsonutil import extract_json, JSONExtractionError

WIKI_ROOT = Path(__file__).parent.parent
EVAL_ROOT = WIKI_ROOT / "eval"
MANIFEST_PATH = EVAL_ROOT / "corpus" / "manifest.json"
RUNS_DIR = EVAL_ROOT / "runs"
CONTENT_FOLDERS = ["principles", "elements", "patterns", "strategies", "theories", "claims"]


def get_existing_slugs() -> dict:
    result = {}
    for folder in CONTENT_FOLDERS:
        d = WIKI_ROOT / folder
        if d.exists():
            result[folder] = sorted(p.stem for p in d.glob("*.md") if p.stem != "index")
    return result


def load_manifest(article_ids=None) -> list:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    articles = manifest["articles"]
    if article_ids:
        wanted = set(article_ids)
        articles = [a for a in articles if a["id"] in wanted]
    return articles


def safe_model_dirname(model: str) -> str:
    return model.replace("/", "__").replace(":", "_")


def result_path(run_dir: Path, model: str, article_id: str) -> Path:
    return run_dir / safe_model_dirname(model) / f"{article_id}.json"


def run_one(model: str, entry: dict, existing_slugs: dict, api_key: str,
            judges: list, gpt_judge_model: str, max_tokens: int, refresh_cache: bool = False) -> dict:
    from scripts.eval.prompts import SYSTEM_PROMPT, build_user_prompt

    article_text = fetch_article.fetch_article_text(entry, refresh=refresh_cache)
    user_prompt = build_user_prompt(article_text, existing_slugs)

    record = {
        "article_id": entry["id"],
        "article_title": entry["title"],
        "model": model,
        "generated_at": None,
        "generation": None,
        "raw_text": None,
        "parsed": None,
        "parse_error": None,
        "validation": None,
        "judges": {},
    }

    try:
        gen = openrouter_client.generate(model, SYSTEM_PROMPT, user_prompt, api_key, max_tokens=max_tokens)
    except openrouter_client.GenerationError as e:
        record["generation"] = {"error": str(e)}
        return record

    record["generated_at"] = datetime.now(timezone.utc).isoformat()
    record["generation"] = {
        "prompt_tokens": gen.prompt_tokens,
        "completion_tokens": gen.completion_tokens,
        "latency_s": round(gen.latency_s, 2),
        "cost_usd": gen.cost_usd,
        "cost_source": gen.cost_source,
        "generation_id": gen.generation_id,
    }
    record["raw_text"] = gen.raw_text

    parsed = None
    try:
        parsed = extract_json(gen.raw_text)
        record["parsed"] = parsed
    except JSONExtractionError as e:
        record["parse_error"] = str(e)

    report = validator.validate_output(parsed or {}, existing_slugs)
    if parsed is None:
        report.parse_error = record["parse_error"]
    record["validation"] = {
        "passed": report.passed,
        "n_contributions": report.n_contributions,
        "completeness_score": report.completeness_score,
        "error_count": report.error_count,
        "warning_count": report.warning_count,
        "parse_error": report.parse_error,
        "issues": [asdict(i) for i in report.issues],
    }

    if parsed:
        record["judges"] = run_judges(article_text, parsed, judges, gpt_judge_model)

    return record


def run_judges(article_text: str, parsed: dict, judges: list, gpt_judge_model: str) -> dict:
    extraction_text = json.dumps(parsed, indent=2)
    out = {}
    for name in judges:
        try:
            if name == "opus":
                result = judge.judge_with_claude(article_text, extraction_text)
            elif name == "gpt":
                result = judge.judge_with_openai(article_text, extraction_text, model=gpt_judge_model)
            else:
                continue
            out[name] = {
                "scores": result.scores,
                "average_score": result.average_score,
                "verdict": result.verdict,
                "issues": result.issues,
                "latency_s": round(result.latency_s, 2),
                "cost_usd": round(result.cost_usd, 5),
                "parse_error": result.parse_error,
            }
        except Exception as e:  # judge availability varies by installed SDK/credentials
            out[name] = {"error": str(e)}
    return out


def cmd_run(args: argparse.Namespace) -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("[ERROR] OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Run ID: {run_id}  (results under {run_dir.relative_to(WIKI_ROOT)})")

    articles = load_manifest(args.articles)
    if args.limit:
        articles = articles[:args.limit]
    existing_slugs = get_existing_slugs()

    total = len(articles) * len(args.models)
    done = 0
    for model in args.models:
        for entry in articles:
            done += 1
            out_path = result_path(run_dir, model, entry["id"])
            if out_path.exists() and not args.overwrite:
                print(f"[{done}/{total}] SKIP (cached) {model} / {entry['id']}")
                continue

            print(f"[{done}/{total}] {model} / {entry['id']} — {entry['title'][:60]}")
            try:
                record = run_one(model, entry, existing_slugs, api_key, args.judges,
                                  args.gpt_judge_model, args.max_tokens, refresh_cache=args.refresh_cache)
            except fetch_article.FetchError as e:
                print(f"  [FETCH ERROR] {e}")
                continue

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps(record, indent=2), encoding="utf-8")

            gen = record.get("generation") or {}
            if "error" in gen:
                print(f"  [GEN ERROR] {gen['error']}")
            else:
                val = record["validation"]
                print(f"  latency={gen.get('latency_s')}s cost=${gen.get('cost_usd')} "
                      f"contributions={val['n_contributions']} completeness={val['completeness_score']} "
                      f"passed={val['passed']}")
            time.sleep(0.5)

    print(f"\nDone. Run report with: python3 scripts/eval_harness.py report --run-id {run_id}")


def cmd_spotcheck(args: argparse.Namespace) -> None:
    """Re-run validator + judges on cached generation output, without re-generating."""
    run_dir = RUNS_DIR / args.run_id
    if not run_dir.exists():
        print(f"[ERROR] No run directory: {run_dir}")
        sys.exit(1)

    existing_slugs = get_existing_slugs()
    result_files = sorted(run_dir.glob("*/*.json"))
    if args.models:
        wanted = {safe_model_dirname(m) for m in args.models}
        result_files = [p for p in result_files if p.parent.name in wanted]
    if args.n:
        result_files = result_files[:args.n]

    for i, path in enumerate(result_files, 1):
        record = json.loads(path.read_text(encoding="utf-8"))
        parsed = record.get("parsed")
        print(f"[{i}/{len(result_files)}] {record['model']} / {record['article_id']}")

        report = validator.validate_output(parsed or {}, existing_slugs)
        record["validation"] = {
            "passed": report.passed,
            "n_contributions": report.n_contributions,
            "completeness_score": report.completeness_score,
            "error_count": report.error_count,
            "warning_count": report.warning_count,
            "parse_error": report.parse_error,
            "issues": [asdict(i) for i in report.issues],
        }

        if parsed and args.judges:
            article_text = fetch_article.fetch_article_text(
                next(a for a in load_manifest() if a["id"] == record["article_id"])
            )
            record["judges"] = run_judges(article_text, parsed, args.judges, args.gpt_judge_model)

        path.write_text(json.dumps(record, indent=2), encoding="utf-8")

    print(f"\nRe-scored {len(result_files)} cached results in {run_dir.relative_to(WIKI_ROOT)}")


def cmd_report(args: argparse.Namespace) -> None:
    run_dir = RUNS_DIR / args.run_id
    if not run_dir.exists():
        print(f"[ERROR] No run directory: {run_dir}")
        sys.exit(1)

    by_model = {}
    for path in sorted(run_dir.glob("*/*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        by_model.setdefault(record["model"], []).append(record)

    rows = []
    for model, records in by_model.items():
        n = len(records)
        gens = [r["generation"] for r in records if r.get("generation") and "error" not in r["generation"]]
        vals = [r["validation"] for r in records if r.get("validation")]
        n_gen_errors = n - len(gens)

        total_cost = sum(g["cost_usd"] or 0 for g in gens)
        avg_latency = sum(g["latency_s"] for g in gens) / len(gens) if gens else 0
        pass_rate = sum(1 for v in vals if v["passed"]) / len(vals) if vals else 0
        avg_completeness = sum(v["completeness_score"] for v in vals) / len(vals) if vals else 0

        judge_summaries = {}
        for jname in ("opus", "gpt"):
            scores = [r["judges"][jname]["average_score"] for r in records
                      if r.get("judges", {}).get(jname, {}).get("average_score") is not None]
            costs = [r["judges"][jname].get("cost_usd", 0) for r in records if jname in r.get("judges", {})]
            fails = [r for r in records if r.get("judges", {}).get(jname, {}).get("verdict") == "fail"]
            if scores:
                judge_summaries[jname] = {
                    "avg_score": round(sum(scores) / len(scores), 2),
                    "fail_count": len(fails),
                    "total_judge_cost_usd": round(sum(costs), 4),
                }

        rows.append({
            "model": model,
            "n_articles": n,
            "n_generation_errors": n_gen_errors,
            "total_generation_cost_usd": round(total_cost, 4),
            "avg_latency_s": round(avg_latency, 2),
            "validator_pass_rate": round(pass_rate, 3),
            "avg_completeness_score": round(avg_completeness, 3),
            "cost_per_passed_article_usd": round(total_cost / max(1, sum(1 for v in vals if v["passed"])), 4),
            **{f"judge_{k}_avg_score": v["avg_score"] for k, v in judge_summaries.items()},
            **{f"judge_{k}_fail_count": v["fail_count"] for k, v in judge_summaries.items()},
        })

    csv_path = run_dir / "summary.csv"
    if rows:
        fieldnames = sorted({k for r in rows for k in r.keys()}, key=lambda k: (k != "model", k))
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    md_lines = [f"# Eval run: {args.run_id}", "", f"Generated: {date.today().isoformat()}", ""]
    md_lines.append("| Model | Articles | Gen errors | Total cost ($) | Avg latency (s) | "
                     "Validator pass rate | Avg completeness | Cost / passed article ($) | "
                     "Opus judge avg | GPT judge avg |")
    md_lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        md_lines.append(
            f"| {r['model']} | {r['n_articles']} | {r['n_generation_errors']} | "
            f"{r['total_generation_cost_usd']} | {r['avg_latency_s']} | "
            f"{r['validator_pass_rate']} | {r['avg_completeness_score']} | "
            f"{r['cost_per_passed_article_usd']} | {r.get('judge_opus_avg_score', '-')} | "
            f"{r.get('judge_gpt_avg_score', '-')} |"
        )
    md_lines.append("")
    md_lines.append("Raw per-article results: `*/<article-id>.json` in this directory. "
                     "Machine-readable summary: `summary.csv`.")

    report_path = run_dir / "report.md"
    report_path.write_text("\n".join(md_lines), encoding="utf-8")

    print("\n".join(md_lines))
    print(f"\nWrote {report_path.relative_to(WIKI_ROOT)} and {csv_path.relative_to(WIKI_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_run = subparsers.add_parser("run", help="Generate + validate + judge a batch of (model, article) pairs")
    p_run.add_argument("--models", nargs="+", required=True)
    p_run.add_argument("--articles", nargs="+", default=None, help="Article ids to restrict to (default: all)")
    p_run.add_argument("--limit", type=int, default=None)
    p_run.add_argument("--judges", nargs="+", default=["opus", "gpt"], choices=["opus", "gpt"])
    p_run.add_argument("--gpt-judge-model", default="gpt-5.6")
    p_run.add_argument("--run-id", default=None)
    p_run.add_argument("--overwrite", action="store_true")
    p_run.add_argument("--refresh-cache", action="store_true", help="Force re-fetch of article text")
    p_run.add_argument("--max-tokens", type=int, default=8000)

    p_spot = subparsers.add_parser("spotcheck", help="Re-validate/re-judge cached results without re-generating")
    p_spot.add_argument("--run-id", required=True)
    p_spot.add_argument("--models", nargs="+", default=None)
    p_spot.add_argument("--n", type=int, default=None, help="Limit to first N cached results")
    p_spot.add_argument("--judges", nargs="+", default=[], choices=["opus", "gpt"],
                         help="Judges to (re-)run; omit to only re-run the structural validator")
    p_spot.add_argument("--gpt-judge-model", default="gpt-5.6")

    p_report = subparsers.add_parser("report", help="Aggregate a run's cached results into report.md + summary.csv")
    p_report.add_argument("--run-id", required=True)

    args = parser.parse_args()
    dispatch = {"run": cmd_run, "spotcheck": cmd_spotcheck, "report": cmd_report}
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
