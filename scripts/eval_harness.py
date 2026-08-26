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

    # While a batch is running: how many (model, article) pairs are done vs.
    # still queued (defaults come from deploy/run-config.env on a droplet)
    python3 scripts/eval_harness.py status --run-id <run-id> --models <...>

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
import concurrent.futures
import csv
import json
import os
import re
import sys
import threading
import time
from dataclasses import asdict
from datetime import date, datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
EVAL_ROOT = WIKI_ROOT / "eval"
MANIFEST_PATH = EVAL_ROOT / "corpus" / "manifest.json"
RUNS_DIR = EVAL_ROOT / "runs"
CONTENT_FOLDERS = ["principles", "elements", "patterns", "strategies", "theories", "claims"]
SECRETS_ENV_FILE = Path("/etc/eval-harness.env")


def _load_secrets_env(path: Path = SECRETS_ENV_FILE) -> None:
    """Load API keys from /etc/eval-harness.env when running this script
    directly (bypassing systemd, which normally supplies them via
    EnvironmentFile=) — e.g. `venv/bin/python scripts/eval_harness.py report
    ...` run by hand on the droplet. A no-op wherever the file doesn't exist
    (a local dev machine). Never overrides a variable already set in the
    environment, so an explicit `export` still wins."""
    if not path.exists():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except PermissionError:
        print(f"[WARN] {path} exists but isn't readable by this user — secrets in it won't be "
              f"auto-loaded (systemd's EnvironmentFile= reads it as root before dropping "
              f"privileges, which is why the service itself still works). To fix ad-hoc runs: "
              f"chown root:evalrunner {path} && chmod 640 {path}", file=sys.stderr)
        return
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


# Must run BEFORE any scripts.eval submodule is imported below, not just at
# the top of main() — scripts/eval/compliance.py reads EVAL_HARNESS_CONTACT_EMAIL
# into a module-level constant at import time, and Python executes every
# top-level `import` in this file before main() ever runs. Calling this only
# inside main() (its original location) meant compliance.py always saw the
# bare, secrets-file-free environment regardless of invocation path — this
# is what kept printing "EVAL_HARNESS_CONTACT_EMAIL is not set" even for a
# plain, direct CLI invocation with the file correctly filled in. main()
# still calls this too (harmless — the "don't override an already-set var"
# guard makes a second call a no-op), so an explicit `export` still wins.
_load_secrets_env()

sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.eval import (fetch_article, openrouter_client, validator, judge, failure_analysis, html_report,
                          executive_summary, cost_projection, history, prompts, optimizer, model_catalog,
                          auto_optimize_report, index_report, consistency)
from scripts.eval.jsonutil import extract_json, JSONExtractionError

RUN_CONFIG_PATH = WIKI_ROOT / "deploy" / "run-config.env"


def _parse_run_args() -> list:
    """Split deploy/run-config.env's RUN_ARGS into argv tokens, the same way
    run.sh's bash `source` + word-splitting does. [] if the file or the
    RUN_ARGS assignment isn't present (e.g. running from a local checkout
    that hasn't set one up)."""
    if not RUN_CONFIG_PATH.exists():
        return []
    match = re.search(r'^RUN_ARGS="(.*)"\s*$', RUN_CONFIG_PATH.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).split() if match else []


def _run_config_models() -> list:
    """The --models list configured in deploy/run-config.env, so `status`
    doesn't require retyping the model roster already tracked there."""
    argv = _parse_run_args()
    if "--models" not in argv:
        return []
    models = []
    for tok in argv[argv.index("--models") + 1:]:
        if tok.startswith("--"):
            break
        models.append(tok)
    return models


def _run_config_run_id() -> str:
    argv = _parse_run_args()
    if "--run-id" in argv:
        idx = argv.index("--run-id")
        if idx + 1 < len(argv):
            return argv[idx + 1]
    return None


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
            judges: list, gpt_judge_model: str, max_tokens: int, refresh_cache: bool = False,
            prompt_version: str = None, max_correction_attempts: int = 0, ground_truth: bool = False,
            require_source_quotes: bool = False, consistency_samples: int = 1,
            subclaim_judging: bool = False) -> dict:
    """max_correction_attempts=0 (default) is exactly the original single-shot
    behavior — this matters for benchmark integrity: the whole point of
    `run`/`optimize`/`auto-optimize` is measuring how a model does on its
    FIRST attempt, so retrying silently until something passes would erase
    the very signal being measured. Set it > 0 to explicitly opt into a
    bounded "show the model its own validator issues and ask it to fix
    them" loop instead — the record keeps both `initial_passed` (the
    benchmark-pure first-attempt result) and `validation.passed` (the final,
    post-correction result actually used for validator_pass_rate downstream)
    so neither number is lost."""
    system_prompt = prompts.load_prompt(prompt_version)
    prompt_version = prompt_version or prompts.current_version()

    article_text = fetch_article.fetch_article_text(entry, refresh=refresh_cache)
    current_prompt = prompts.build_user_prompt(article_text, existing_slugs)
    original_user_prompt = current_prompt  # captured before the correction loop below can rewrite it

    record = {
        "article_id": entry["id"],
        "article_title": entry["title"],
        "model": model,
        "prompt_version": prompt_version,
        "generated_at": None,
        "generation": None,
        "raw_text": None,
        "parsed": None,
        "parse_error": None,
        "validation": None,
        "judges": {},
        "correction_attempts": 0,
        "initial_passed": None,
    }

    parsed = None
    total_cost = 0.0
    total_completion_tokens = 0

    for attempt in range(max_correction_attempts + 1):
        try:
            gen = openrouter_client.generate(model, system_prompt, current_prompt, api_key, max_tokens=max_tokens,
                                              disable_reasoning=model_catalog.needs_reasoning_disabled(model))
        except openrouter_client.GenerationError as e:
            record["generation"] = {"error": str(e)}
            return record

        total_cost += gen.cost_usd or 0
        total_completion_tokens += gen.completion_tokens
        record["generated_at"] = datetime.now(timezone.utc).isoformat()
        record["generation"] = {
            "prompt_tokens": gen.prompt_tokens,
            "completion_tokens": total_completion_tokens,
            "latency_s": round(gen.latency_s, 2),
            "cost_usd": round(total_cost, 6),
            "cost_source": gen.cost_source,
            "generation_id": gen.generation_id,
        }
        record["raw_text"] = gen.raw_text

        parsed = None
        try:
            parsed = extract_json(gen.raw_text)
            record["parsed"] = parsed
            record["parse_error"] = None
        except JSONExtractionError as e:
            record["parse_error"] = str(e)

        try:
            report = validator.validate_output(parsed or {}, existing_slugs, ground_truth_enabled=ground_truth,
                                                require_source_quotes=require_source_quotes,
                                                article_text=article_text)
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
        except Exception as e:
            # A validator bug must never crash the whole batch, or throw away
            # the generation we already paid for — record it and stop; a
            # crash isn't something a correction retry can fix, and a fixed
            # validator can re-score this later via `spotcheck` for free.
            record["validation"] = {
                "passed": False, "n_contributions": 0, "completeness_score": 0.0,
                "error_count": 1, "warning_count": 0,
                "parse_error": f"validator crashed: {type(e).__name__}: {e}",
                "issues": [],
            }
            break

        if attempt == 0:
            record["initial_passed"] = record["validation"]["passed"]
        record["correction_attempts"] = attempt

        if record["validation"]["passed"] or attempt == max_correction_attempts:
            break

        current_prompt = prompts.build_correction_prompt(gen.raw_text, record["validation"]["issues"])

    if parsed:
        try:
            record["judges"] = run_judges(article_text, parsed, judges, gpt_judge_model)
        except Exception as e:
            record["judges"] = {"error": f"judging crashed: {type(e).__name__}: {e}"}

    if parsed and subclaim_judging:
        try:
            record["subclaim_judgment"] = judge.judge_subclaims(article_text, parsed, judges, gpt_judge_model)
        except Exception as e:
            record["subclaim_judgment"] = {"error": f"subclaim judging crashed: {type(e).__name__}: {e}"}

    if parsed and consistency_samples > 1:
        # SelfCheckGPT-style: independently re-generate the SAME original
        # query (never the correction-loop's rewritten prompt) N-1 more
        # times and see which citations/quotes survive. Comparison-sample
        # cost is tracked separately from record["generation"]["cost_usd"]
        # so this opt-in extra signal never silently inflates the per-model
        # cost figure every other run/comparison/leaderboard is ranked on.
        comparison_sets = []
        comparison_cost = 0.0
        for _ in range(consistency_samples - 1):
            try:
                extra_gen = openrouter_client.generate(
                    model, system_prompt, original_user_prompt, api_key, max_tokens=max_tokens,
                    disable_reasoning=model_catalog.needs_reasoning_disabled(model))
            except openrouter_client.GenerationError:
                continue  # a failed comparison sample just shrinks the comparison pool, not a hard error
            comparison_cost += extra_gen.cost_usd or 0
            try:
                extra_parsed = extract_json(extra_gen.raw_text)
            except JSONExtractionError:
                continue
            comparison_sets.append(consistency.extraction_identifier_set(extra_parsed))

        record["consistency_samples_used"] = len(comparison_sets)
        record["consistency_check_cost_usd"] = round(comparison_cost, 6)
        if comparison_sets:
            report = validator.validate_output(parsed, existing_slugs, ground_truth_enabled=ground_truth,
                                                require_source_quotes=require_source_quotes,
                                                article_text=article_text, comparison_sets=comparison_sets)
            record["validation"] = {
                "passed": report.passed,
                "n_contributions": report.n_contributions,
                "completeness_score": report.completeness_score,
                "error_count": report.error_count,
                "warning_count": report.warning_count,
                "parse_error": report.parse_error,
                "issues": [asdict(i) for i in report.issues],
            }

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


def run_batch(models: list, articles: list, judges: list, run_id: str, api_key: str,
              gpt_judge_model: str = "gpt-5.6", max_tokens: int = 8000, overwrite: bool = False,
              refresh_cache: bool = False, prompt_version: str = None, concurrency: int = 1,
              max_correction_attempts: int = 0, retry_errors_only: bool = False,
              ground_truth: bool = False, require_source_quotes: bool = False,
              consistency_samples: int = 1, subclaim_judging: bool = False) -> Path:
    """The actual (model x article) loop, shared by `run`, `optimize`, and
    `auto-optimize` — the latter two call this directly (not through
    argparse) to run each candidate prompt against the same articles as the
    baseline.

    concurrency=1 (the default) preserves the original one-pair-at-a-time
    behavior exactly, including print ordering. concurrency>1 dispatches
    pairs to a thread pool — safe because each pair writes its own result
    file (out_path is unique per model/article) and openrouter_client/judge
    calls carry no shared mutable state; only the shared progress counter,
    console output, and generate_reports()'s file writes need a lock.

    retry_errors_only: like --overwrite, but only for pairs whose cached
    result has a generation error — a pair that already succeeded is left
    alone (no re-pay for a result that's already good). For a "Rerun" click
    after fixing something external (a billing cap, an expired key) rather
    than a fresh --overwrite of the whole run."""
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"Run ID: {run_id}  (results under {run_dir.relative_to(WIKI_ROOT)})")

    # Records the *intended* model list + article ids for this run (not
    # just a count) so the `status` command and dashboard's queue section
    # can show a model that hasn't produced any result files yet as
    # "queued" instead of it being invisible, AND so a "Rerun" click from
    # the dashboard can reconstruct this exact invocation later without
    # guessing — see dashboard_server.py's _handle_rerun. Model/article
    # lists are merged with whatever's already recorded (rather than
    # overwritten) so a targeted re-run of one model — e.g. `run --models
    # qwen/qwen3.8-27b --overwrite` against an existing run-id — doesn't
    # wipe the others out of the queue panel or the rerun metadata; the
    # rest of the metadata (prompt_version, judges, ...) just reflects
    # whatever this specific call used.
    queue_path = run_dir / "queue.json"
    existing_models, existing_article_ids = [], []
    if queue_path.exists():
        try:
            old_meta = json.loads(queue_path.read_text(encoding="utf-8"))
            existing_models = old_meta.get("models", [])
            existing_article_ids = old_meta.get("article_ids", [])
        except (json.JSONDecodeError, OSError):
            pass
    merged_models = existing_models + [m for m in models if m not in existing_models]
    new_article_ids = [a["id"] for a in articles]
    merged_article_ids = existing_article_ids + [a for a in new_article_ids if a not in existing_article_ids]
    queue_path.write_text(json.dumps({
        "models": merged_models,
        "total_articles": len(articles),
        "article_ids": merged_article_ids,
        "prompt_version": prompt_version or prompts.current_version(),
        "judges": judges,
        "max_tokens": max_tokens,
        "gpt_judge_model": gpt_judge_model,
        "concurrency": concurrency,
        "max_correction_attempts": max_correction_attempts,
        "ground_truth": ground_truth,
        "require_source_quotes": require_source_quotes,
        "consistency_samples": consistency_samples,
        "subclaim_judging": subclaim_judging,
    }, indent=2), encoding="utf-8")

    existing_slugs = get_existing_slugs()
    # Article-major, not model-major: interleaves every model's pair for
    # article 1, then article 2, etc., instead of listing all of model 1's
    # articles before model 2's. With concurrency < total pairs, the thread
    # pool below pulls submitted work roughly in order — model-major order
    # meant it would burn its worker slots finishing one model's whole
    # batch before touching the next model's first pair at all, which reads
    # as "waiting for Gemini to finish before testing Qwen" even though
    # concurrency>1 nominally means "in parallel." Interleaving means a
    # concurrency >= len(models) actually runs every model's current
    # article at roughly the same time, as intended.
    pairs = [(model, entry) for entry in articles for model in models]
    total = len(pairs)
    state = {"done": 0}
    print_lock = threading.Lock()
    report_lock = threading.Lock()

    def process_pair(model: str, entry: dict) -> None:
        out_path = result_path(run_dir, model, entry["id"])
        should_skip = out_path.exists() and not overwrite
        if should_skip and retry_errors_only:
            try:
                existing_record = json.loads(out_path.read_text(encoding="utf-8"))
                if (existing_record.get("generation") or {}).get("error"):
                    should_skip = False  # previously failed — retry it
            except (json.JSONDecodeError, OSError):
                should_skip = False  # unreadable — safest to redo it
        if should_skip:
            with print_lock:
                state["done"] += 1
                print(f"[{state['done']}/{total}] SKIP (cached) {model} / {entry['id']}")
            return

        with print_lock:
            print(f"[{model} / {entry['id']}] {entry['title'][:60]}")
        try:
            record = run_one(model, entry, existing_slugs, api_key, judges, gpt_judge_model,
                              max_tokens, refresh_cache=refresh_cache, prompt_version=prompt_version,
                              max_correction_attempts=max_correction_attempts, ground_truth=ground_truth,
                              require_source_quotes=require_source_quotes,
                              consistency_samples=consistency_samples, subclaim_judging=subclaim_judging)
        except fetch_article.FetchError as e:
            with print_lock:
                state["done"] += 1
                print(f"[{state['done']}/{total}] [FETCH ERROR] {model}/{entry['id']}: {e}")
            return
        except Exception as e:
            # Last-resort backstop: run_one() already handles the expected
            # failure points (generation, parsing, validation, judging)
            # without crashing, but this run can be one of several parallel
            # candidates in an unattended, hours-long auto-optimize search —
            # nothing here should ever be allowed to kill the whole batch.
            with print_lock:
                state["done"] += 1
                print(f"[{state['done']}/{total}] [INTERNAL ERROR] {model}/{entry['id']}: "
                      f"{type(e).__name__}: {e}")
            return

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(record, indent=2), encoding="utf-8")

        gen = record.get("generation") or {}
        with print_lock:
            state["done"] += 1
            if "error" in gen:
                print(f"[{state['done']}/{total}] [GEN ERROR] {model}/{entry['id']}: {gen['error']}")
            else:
                val = record["validation"]
                print(f"[{state['done']}/{total}] {model}/{entry['id']} latency={gen.get('latency_s')}s "
                      f"cost=${gen.get('cost_usd')} contributions={val['n_contributions']} "
                      f"completeness={val['completeness_score']} passed={val['passed']}")

        with report_lock:
            generate_reports(run_dir, run_id, verbose=False)

    if concurrency <= 1:
        for model, entry in pairs:
            process_pair(model, entry)
            time.sleep(0.5)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = [executor.submit(process_pair, model, entry) for model, entry in pairs]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # re-raise anything unexpected rather than swallow it silently

    return run_dir


def cmd_run(args: argparse.Namespace) -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("[ERROR] OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    articles = load_manifest(args.articles)
    if args.limit:
        articles = articles[:args.limit]

    run_batch(args.models, articles, args.judges, run_id, api_key,
              gpt_judge_model=args.gpt_judge_model, max_tokens=args.max_tokens,
              overwrite=args.overwrite, refresh_cache=args.refresh_cache,
              prompt_version=args.prompt_version, concurrency=args.concurrency,
              max_correction_attempts=args.max_correction_attempts,
              retry_errors_only=args.retry_errors_only, ground_truth=args.ground_truth,
              require_source_quotes=args.require_source_quotes,
              consistency_samples=args.consistency_samples, subclaim_judging=args.subclaim_judging)

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

    # Only resolved when actually needed (require_source_quotes) — a plain
    # spotcheck (or one only re-scoring judges) has no reason to touch the
    # article cache at all.
    articles_by_id = {a["id"]: a for a in load_manifest()} if args.require_source_quotes else {}

    for i, path in enumerate(result_files, 1):
        record = json.loads(path.read_text(encoding="utf-8"))
        parsed = record.get("parsed")
        print(f"[{i}/{len(result_files)}] {record['model']} / {record['article_id']}")

        article_text = None
        if args.require_source_quotes:
            entry = articles_by_id.get(record["article_id"])
            if entry:
                try:
                    article_text = fetch_article.fetch_article_text(entry)
                except fetch_article.FetchError as e:
                    print(f"  [WARN] Could not fetch article text for {record['article_id']} ({e}) — "
                          f"source_quote will only be checked for presence, not grounding.")

        report = validator.validate_output(parsed or {}, existing_slugs, ground_truth_enabled=args.ground_truth,
                                            require_source_quotes=args.require_source_quotes,
                                            article_text=article_text)
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

    generate_reports(run_dir, args.run_id, verbose=False)
    print(f"\nRe-scored {len(result_files)} cached results in {run_dir.relative_to(WIKI_ROOT)}")


def compute_rows(run_dir: Path) -> tuple:
    """Load every cached result under run_dir and compute the per-model summary
    rows both generate_reports() and `compare` build on. Returns (by_model, rows)."""
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

        # FActScore-style (--subclaim-judging): averaged separately from the
        # whole-extraction judge scores above — a fraction-supported metric,
        # not a 1-5 scale, and only present on records that opted in.
        subclaim_summaries = {}
        for jname in ("opus", "gpt"):
            factscores = [r["subclaim_judgment"][jname]["factscore"] for r in records
                          if r.get("subclaim_judgment", {}).get(jname, {}).get("factscore") is not None]
            sc_costs = [r["subclaim_judgment"][jname].get("cost_usd", 0) for r in records
                        if jname in r.get("subclaim_judgment", {})]
            if factscores:
                subclaim_summaries[jname] = {
                    "avg_factscore": round(sum(factscores) / len(factscores), 3),
                    "total_cost_usd": round(sum(sc_costs), 4),
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
            **{f"judge_{k}_total_cost_usd": v["total_judge_cost_usd"] for k, v in judge_summaries.items()},
            **{f"subclaim_factscore_{k}": v["avg_factscore"] for k, v in subclaim_summaries.items()},
            **{f"subclaim_judging_{k}_cost_usd": v["total_cost_usd"] for k, v in subclaim_summaries.items()},
        })

    return by_model, rows


def _collect_worked_examples(by_model: dict, articles: list, max_examples: int = 2,
                              min_avg_score: float = 4.5) -> list:
    """Pulls this run's own best (validator-clean, high-judge-score)
    extractions to show the prompt-engineer model as concrete demonstrations
    alongside the failure data — the same real (article, extraction) pairs
    already sitting in this run's cached result files, so no new generation
    calls are needed. optimizer.py's system prompt tells the model to prefer
    distilling a short in-prompt example from one of these over inventing an
    abstract rule, which a plain failure-pattern summary can't offer: it only
    shows what went wrong, never what a passing extraction actually looks
    like. Distinct articles only, so two near-duplicate wins on the same
    article don't crowd out variety; empty when nothing in the run clears
    the bar, which is fine — failure data alone is still useful."""
    articles_by_id = {a["id"]: a for a in articles}
    candidates = []
    for records in by_model.values():
        for rec in records:
            if not rec.get("parsed") or not (rec.get("validation") or {}).get("passed"):
                continue
            judges = rec.get("judges") or {}
            scores = [j["average_score"] for j in judges.values()
                      if isinstance(j, dict) and j.get("average_score") is not None]
            if not scores or any(j.get("verdict") == "fail" for j in judges.values() if isinstance(j, dict)):
                continue
            avg = sum(scores) / len(scores)
            if avg >= min_avg_score:
                candidates.append((avg, rec))

    candidates.sort(key=lambda pair: pair[0], reverse=True)
    examples = []
    seen_articles = set()
    for avg, rec in candidates:
        article_id = rec["article_id"]
        if article_id in seen_articles:
            continue
        entry = articles_by_id.get(article_id)
        if not entry:
            continue
        try:
            article_text = fetch_article.fetch_article_text(entry)
        except Exception:
            continue
        seen_articles.add(article_id)
        examples.append({
            "article_title": rec.get("article_title") or entry.get("title", article_id),
            "article_excerpt": article_text[:1500],
            "extraction_json": json.dumps(rec["parsed"], indent=2),
            "avg_judge_score": round(avg, 2),
        })
        if len(examples) >= max_examples:
            break
    return examples


def compute_queue_status(by_model: dict, models: list, total_articles: int, concurrency: int = 1) -> list:
    """Per-model done/error/pending counts against the *intended* model list
    and article count — the answer to "which models are tested, which are
    still in the queue" that by_model alone can't give (a model with zero
    result files so far is indistinguishable from one that doesn't exist).

    run_batch dispatches pairs article-major (every model gets a pair for
    article 1 before any model gets a pair for article 2), submitted all at
    once to a `concurrency`-worker thread pool — so with concurrency >=
    len(models), every incomplete model is genuinely being worked at once,
    not one after another. "queued" only applies to models beyond the first
    `concurrency` incomplete ones, approximating which models the pool
    hasn't gotten a worker to yet."""
    statuses = []
    running_slots = max(1, concurrency)
    running_count = 0
    for model in models:
        records = by_model.get(model, [])
        errors = sum(1 for r in records if (r.get("generation") or {}).get("error"))
        done = len(records) - errors
        pending = max(0, total_articles - done - errors)
        if pending == 0:
            phase = "done" if errors == 0 else "done-with-errors"
        elif running_count < running_slots:
            phase = "running"
            running_count += 1
        else:
            phase = "queued"
        statuses.append({"model": model, "total": total_articles, "done": done,
                          "errors": errors, "pending": pending, "phase": phase})
    return statuses


def generate_reports(run_dir: Path, run_id: str, verbose: bool = True) -> None:
    """Regenerate report.md/summary.csv/report.html from whatever result files
    currently exist under run_dir. Cheap enough (a few ms for a run this size)
    to call after every completed pair, not just on demand — that's what makes
    the HTML dashboard's auto-refresh (see html_report.py) actually live."""
    by_model, rows = compute_rows(run_dir)

    queue_status = []
    queue_path = run_dir / "queue.json"
    if queue_path.exists():
        try:
            queue_meta = json.loads(queue_path.read_text(encoding="utf-8"))
            queue_status = compute_queue_status(
                by_model, queue_meta.get("models", []), queue_meta.get("total_articles", 0),
                concurrency=queue_meta.get("concurrency", 1))
        except (json.JSONDecodeError, OSError):
            queue_status = []

    csv_path = run_dir / "summary.csv"
    if rows:
        fieldnames = sorted({k for r in rows for k in r.keys()}, key=lambda k: (k != "model", k))
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    md_lines = [f"# Eval run: {run_id}", "", f"Generated: {date.today().isoformat()}", ""]
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

    failure_summary = failure_analysis.analyze(by_model)
    exec_summary = executive_summary.summarize(rows, failure_summary)
    md_lines.append("")
    md_lines.append(executive_summary.render_markdown(exec_summary))
    md_lines.append(failure_analysis.render_markdown(failure_summary))

    report_path = run_dir / "report.md"
    report_path.write_text("\n".join(md_lines), encoding="utf-8")

    html_path = run_dir / "report.html"
    html_path.write_text(
        html_report.render_html(run_id, date.today().isoformat(), rows, by_model, failure_summary, exec_summary,
                                 queue_status),
        encoding="utf-8",
    )

    if verbose:
        print("\n".join(md_lines))
        print(f"\nWrote {report_path.relative_to(WIKI_ROOT)}, {csv_path.relative_to(WIKI_ROOT)}, "
              f"and {html_path.relative_to(WIKI_ROOT)} (open the .html one in a browser for a visual dashboard)")

    generate_index(verbose=False)


_VERSIONED_RUN_ID_RE = re.compile(r"^.+-v(\d+)$")


def _run_order_key(r: dict) -> tuple:
    """Natural/logical ordering for the landing page's "All runs" table —
    NOT recency-of-completion. auto-optimize/optimize runs finish in
    whatever order their API calls happen to return, so sorting by
    last-modified made an earlier test appear "current" while a later one
    was still in flight above/below it — confusing, since it looked like
    the search had gone backwards. The prompt version number embedded in
    the run id (e.g. auto-v16) reflects the actual sequence tests were
    generated in — a single monotonic lineage, one test per version, no
    round-grouping — regardless of which one happened to finish first;
    anything that doesn't match this naming scheme (manual/baseline runs)
    sorts before all versioned runs, oldest-created first."""
    m = _VERSIONED_RUN_ID_RE.match(r["run_id"])
    if m:
        return (1, int(m.group(1)))
    return (0, r["first_created"])


_INDEX_LOCK = threading.Lock()


def generate_index(verbose: bool = True) -> None:
    """Regenerates eval/runs/index.html — the landing page python's
    http.server shows at http://localhost:8080/ — from every run directory
    currently on disk. Called from generate_reports() (so it's live during
    any active run, same guarantee as an individual run's own dashboard) and
    available standalone via the `index` command for a one-off refresh.

    generate_reports()'s own report_lock is scoped to one run_batch() call,
    so it does nothing to protect this function — auto-optimize runs
    several candidates concurrently as threads *within one process*, each
    with its own run_batch() and its own report_lock, and every one of them
    calls this same function against the one shared index.html. Without a
    lock here, two candidates' scan-then-write cycles can interleave, and
    whichever finishes last "wins" even if its own scan was started first
    (a stale write clobbering a fresher one) — this lock serializes every
    call in this process so each write reflects its own full, current scan."""
    with _INDEX_LOCK:
        _generate_index_locked(verbose)


def _generate_index_locked(verbose: bool) -> None:
    run_summaries = []
    for run_dir in sorted(RUNS_DIR.iterdir()):
        if not run_dir.is_dir():
            continue
        result_files = list(run_dir.glob("*/*.json"))
        if not result_files:
            continue

        by_model, rows = compute_rows(run_dir)

        total_pairs = done_pairs = None
        queue_path = run_dir / "queue.json"
        if queue_path.exists():
            try:
                queue_meta = json.loads(queue_path.read_text(encoding="utf-8"))
                queue_status = compute_queue_status(
                    by_model, queue_meta.get("models", []), queue_meta.get("total_articles", 0),
                    concurrency=queue_meta.get("concurrency", 1))
                total_pairs = sum(s["total"] for s in queue_status)
                done_pairs = sum(s["done"] for s in queue_status)
            except (json.JSONDecodeError, OSError):
                pass

        # Max, not mean, across models: a run mixes several unrelated models,
        # and averaging their scores together answers "did the blended batch
        # move" rather than "did any specific model actually get better" —
        # the latter is what matters when optimizing one model's prompt.
        scores = [v for r in rows for v in (r.get("judge_opus_avg_score"), r.get("judge_gpt_avg_score")) if v is not None]
        total_cost = sum(r.get("total_generation_cost_usd") or 0 for r in rows)
        latencies = [r["avg_latency_s"] for r in rows if r.get("avg_latency_s")]
        versions = sorted({rec.get("prompt_version") for recs in by_model.values() for rec in recs
                            if rec.get("prompt_version")})

        run_summaries.append({
            "run_id": run_dir.name,
            "done": done_pairs, "total": total_pairs,
            "best_judge_score": round(max(scores), 2) if scores else None,
            "total_cost_usd": round(total_cost, 4),
            "avg_latency_s": round(sum(latencies) / len(latencies), 1) if latencies else None,
            "prompt_versions": ", ".join(versions) if versions else "unknown",
            "n_models": len(by_model),
            "last_modified": max((f.stat().st_mtime for f in result_files), default=0),
            "first_created": min((f.stat().st_mtime for f in result_files), default=0),
        })

    run_summaries.sort(key=_run_order_key, reverse=True)
    history_rows = history.collect(RUNS_DIR)

    auto_optimize_state = None
    state_path = RUNS_DIR / ".auto_optimize_state.json"
    if state_path.exists():
        try:
            auto_optimize_state = json.loads(state_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            auto_optimize_state = None

    if auto_optimize_state and auto_optimize_state.get("status") in ("starting", "running"):
        # A process that dies uncleanly (SSH disconnect, kill -9 — anything
        # that skips cmd_auto_optimize's `finally` block) never gets to write
        # a terminal status here, so without this check the landing page
        # would show "RUNNING" forever even though nothing is actually
        # running anymore — cross-check against the lock file's PID (see
        # _acquire_auto_optimize_lock) rather than trusting the last-written
        # status at face value.
        lock_pid = None
        if AUTO_OPTIMIZE_LOCK_PATH.exists():
            try:
                lock_pid = json.loads(AUTO_OPTIMIZE_LOCK_PATH.read_text(encoding="utf-8")).get("pid")
            except (json.JSONDecodeError, OSError):
                lock_pid = None
        if not (lock_pid and _pid_is_alive(lock_pid)):
            auto_optimize_state = {**auto_optimize_state, "status": "stopped_interrupted"}

    try:
        live_prompt_version = prompts.current_version()
    except FileNotFoundError:
        live_prompt_version = None

    index_path = RUNS_DIR / "index.html"
    index_path.write_text(
        index_report.render_html(run_summaries, history_rows, auto_optimize_state, live_prompt_version),
        encoding="utf-8")
    if verbose:
        print(f"Wrote {index_path.relative_to(WIKI_ROOT)} ({len(run_summaries)} run(s))")


def cmd_index(args: argparse.Namespace) -> None:
    generate_index(verbose=True)


def cmd_report(args: argparse.Namespace) -> None:
    run_dir = RUNS_DIR / args.run_id
    if not run_dir.exists():
        print(f"[ERROR] No run directory: {run_dir}")
        sys.exit(1)
    generate_reports(run_dir, args.run_id)


def _fmt_pair(before, after, decimals=2, pct=False) -> str:
    if before is None and after is None:
        return "–"
    b = "-" if before is None else f"{before * 100:.{decimals}f}%" if pct else f"{before:.{decimals}f}"
    a = "-" if after is None else f"{after * 100:.{decimals}f}%" if pct else f"{after:.{decimals}f}"
    if before is None or after is None:
        return f"{b} → {a}"
    delta = after - before
    arrow = "▲" if delta > 0 else ("▼" if delta < 0 else "▬")
    delta_str = f"{delta * 100:.{decimals}f}pp" if pct else f"{delta:.{decimals}f}"
    sign = "+" if delta > 0 else ""
    return f"{b} → {a} ({arrow} {sign}{delta_str})"


def _avg_judge_score(row: dict) -> float:
    scores = [row.get("judge_opus_avg_score"), row.get("judge_gpt_avg_score")]
    scores = [s for s in scores if s is not None]
    return sum(scores) / len(scores) if scores else None


def build_compare(baseline_id: str, candidate_id: str, models_filter: list = None) -> dict:
    """Shared by `compare` and `optimize` — the latter uses avg_score_delta to
    decide whether a candidate prompt actually improved on the baseline."""
    baseline_dir = RUNS_DIR / baseline_id
    candidate_dir = RUNS_DIR / candidate_id

    base_by_model, base_rows = compute_rows(baseline_dir)
    cand_by_model, cand_rows = compute_rows(candidate_dir)
    base_fail = failure_analysis.analyze(base_by_model)
    cand_fail = failure_analysis.analyze(cand_by_model)

    base_by_name = {r["model"]: r for r in base_rows}
    cand_by_name = {r["model"]: r for r in cand_rows}
    models = sorted(set(base_by_name) & set(cand_by_name))
    if models_filter:
        models = [m for m in models if m in models_filter]
    if not models:
        return {"error": f"No model is present in both {baseline_id} and {candidate_id} "
                          f"(or the model filter excluded everything)."}

    keywords = ("fabrication", "omission", "duplication", "inaccuracy")
    lines = [f"# Compare: {baseline_id} (baseline) vs {candidate_id} (candidate)", "",
             f"Generated: {date.today().isoformat()}", ""]
    lines.append("| Model | Opus judge | GPT judge | Validator pass rate | " +
                 " | ".join(k.capitalize() for k in keywords) + " |")
    lines.append("|---|---|---|---|" + "---|" * len(keywords))

    deltas = []
    for model in models:
        b, c = base_by_name[model], cand_by_name[model]
        b_kw = base_fail.get(model, {}).get("judge_keyword_tally", {})
        c_kw = cand_fail.get(model, {}).get("judge_keyword_tally", {})
        row = [
            model,
            _fmt_pair(b.get("judge_opus_avg_score"), c.get("judge_opus_avg_score")),
            _fmt_pair(b.get("judge_gpt_avg_score"), c.get("judge_gpt_avg_score")),
            _fmt_pair(b.get("validator_pass_rate"), c.get("validator_pass_rate"), decimals=0, pct=True),
        ]
        for k in keywords:
            row.append(_fmt_pair(b_kw.get(k, 0), c_kw.get(k, 0), decimals=0))
        lines.append("| " + " | ".join(row) + " |")

        b_score, c_score = _avg_judge_score(b), _avg_judge_score(c)
        if b_score is not None and c_score is not None:
            deltas.append(c_score - b_score)

    lines.append("")
    lines.append(f"Sample sizes: {baseline_id} = " +
                 ", ".join(f"{m}: {base_by_name[m]['n_articles']}" for m in models) +
                 f"; {candidate_id} = " +
                 ", ".join(f"{m}: {cand_by_name[m]['n_articles']}" for m in models))
    lines.append("Read deltas with that in mind — a fair comparison needs the same article count on both sides.")

    return {
        "markdown": "\n".join(lines),
        "models": models,
        "avg_score_delta": (sum(deltas) / len(deltas)) if deltas else None,
    }


def cmd_compare(args: argparse.Namespace) -> None:
    """Diff two runs model-by-model — e.g. the same models/articles run again
    after a prompt or validator change, to see if it actually moved the
    numbers instead of just feeling like it should have."""
    for run_id in (args.baseline, args.candidate):
        if not (RUNS_DIR / run_id).exists():
            print(f"[ERROR] No run directory: {RUNS_DIR / run_id}")
            sys.exit(1)

    result = build_compare(args.baseline, args.candidate, models_filter=args.models)
    if "error" in result:
        print(f"[ERROR] {result['error']}")
        sys.exit(1)

    out_path = RUNS_DIR / args.candidate / f"compare_vs_{args.baseline}.md"
    out_path.write_text(result["markdown"], encoding="utf-8")
    print(result["markdown"])
    print(f"\nWrote {out_path.relative_to(WIKI_ROOT)}")


def cmd_project_cost(args: argparse.Namespace) -> None:
    run_dir = RUNS_DIR / args.run_id
    if not run_dir.exists():
        print(f"[ERROR] No run directory: {run_dir}")
        sys.exit(1)
    _, rows = compute_rows(run_dir)
    if args.models:
        rows = [r for r in rows if r["model"] in args.models]
    projected = cost_projection.project(rows, sizes=args.sizes, qa_sample_rate=args.qa_sample_rate)
    if not projected:
        print("[ERROR] No model in this run has completed any articles yet.")
        sys.exit(1)
    md = cost_projection.render_markdown(projected, qa_sample_rate=args.qa_sample_rate)
    print(md)
    out_path = run_dir / "cost_projection.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"\nWrote {out_path.relative_to(WIKI_ROOT)}")


def cmd_history(args: argparse.Namespace) -> None:
    rows = history.collect(RUNS_DIR)
    if args.models:
        rows = [r for r in rows if r["model"] in args.models]
    if not rows:
        print("[ERROR] No runs found under eval/runs/.")
        sys.exit(1)
    md = history.render_markdown(rows)
    print(md)
    out_path = RUNS_DIR / "history.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"\nWrote {out_path.relative_to(WIKI_ROOT)}")


def cmd_status(args: argparse.Namespace) -> None:
    """Progress tracker for an in-flight or completed batch — answers "is the
    batch done yet" and "which models are tested vs. still queued" directly,
    instead of inferring it from partial `history` output or the order models
    happen to appear on disk (which just reflects run_batch processing them
    to completion one at a time, in list order)."""
    run_id = args.run_id or _run_config_run_id()
    if not run_id:
        print("[ERROR] No --run-id given, and none found in deploy/run-config.env's RUN_ARGS.")
        sys.exit(1)

    models = args.models or _run_config_models()
    if not models:
        print("[ERROR] No --models given, and none found in deploy/run-config.env's RUN_ARGS.")
        sys.exit(1)

    total = len(load_manifest(args.articles))
    run_dir = RUNS_DIR / run_id
    by_model, _ = compute_rows(run_dir) if run_dir.exists() else ({}, [])
    concurrency = 1
    queue_path = run_dir / "queue.json"
    if queue_path.exists():
        try:
            concurrency = json.loads(queue_path.read_text(encoding="utf-8")).get("concurrency", 1)
        except (json.JSONDecodeError, OSError):
            pass
    statuses = compute_queue_status(by_model, models, total, concurrency=concurrency)

    total_pairs = total * len(models)
    print(f"Run: {run_id}")
    print(f"{total} article(s) x {len(models)} model(s) = {total_pairs} pair(s)\n")

    phase_label = {"done": "done", "done-with-errors": "done (errors)", "running": "running", "queued": "queued"}
    bar_width = 24
    grand_done = grand_errors = grand_pending = 0
    for s in statuses:
        pct = (s["done"] / s["total"]) if s["total"] else 0
        filled = round(bar_width * pct)
        bar = "#" * filled + "-" * (bar_width - filled)
        desc = model_catalog.describe(s["model"])
        model_label = f"{s['model']} ({desc})" if desc else s["model"]
        print(f"  [{bar}] {s['done']:>2}/{s['total']} done  {s['errors']:>2} err  {s['pending']:>2} pending   "
              f"{model_label:<60} {phase_label[s['phase']]}")
        grand_done += s["done"]
        grand_errors += s["errors"]
        grand_pending += s["pending"]

    print(f"\nOverall: {grand_done}/{total_pairs} done, {grand_errors} generation error(s), {grand_pending} pending.")
    if grand_pending == 0:
        note = " (some pairs had generation errors — see the report for detail)" if grand_errors else ""
        print(f"Batch complete.{note}")
    else:
        n_queued = sum(1 for s in statuses if s["phase"] == "queued")
        if n_queued:
            print(f"{n_queued} model(s) still queued behind the one currently running.")
        else:
            print("The last model in the list is still running.")


def _append_prompt_changelog(new_version: str, based_on_version: str, based_on_run: str, changes_summary: str) -> None:
    changelog_path = prompts.PROMPT_VERSIONS_DIR / "CHANGELOG.md"
    entry = (f"\n## {new_version}\n\n"
             f"Proposed from `{based_on_run}` (based on {based_on_version}):\n"
             f"{changes_summary}\n")
    with open(changelog_path, "a", encoding="utf-8") as f:
        f.write(entry)


def cmd_optimize(args: argparse.Namespace) -> None:
    """Propose -> re-run -> compare -> keep-or-stop, for up to --iterations
    rounds. Never auto-adopts a regression: prompts.CURRENT only advances when
    a candidate's avg judge-score delta clears --min-improvement, per the
    ratchet documented in prompts.py."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("[ERROR] OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)
    if not (RUNS_DIR / args.baseline_run).exists():
        print(f"[ERROR] No run directory: {RUNS_DIR / args.baseline_run}")
        sys.exit(1)

    current_run_id = args.baseline_run

    for i in range(1, args.iterations + 1):
        print(f"\n=== optimize iteration {i}/{args.iterations} — baseline: {current_run_id} ===")
        current_dir = RUNS_DIR / current_run_id
        by_model, _ = compute_rows(current_dir)
        if not by_model:
            print(f"[ERROR] {current_run_id} has no completed results to learn from.")
            sys.exit(1)

        models = args.models or sorted(by_model.keys())
        article_ids = sorted({rec["article_id"] for records in by_model.values() for rec in records})
        articles = load_manifest(article_ids)
        if not articles:
            print("[ERROR] Could not resolve manifest articles from the baseline run's article ids.")
            sys.exit(1)

        sample_record = next(iter(by_model.values()))[0]
        current_prompt_version = sample_record.get("prompt_version") or prompts.current_version()
        current_prompt_text = prompts.load_prompt(current_prompt_version)

        failure_summary = failure_analysis.analyze(by_model)
        has_findings = any(d.get("validator_top_issues") or d.get("judge_keyword_tally")
                            for d in failure_summary.values())
        if not has_findings:
            print(f"No validator issues or judge complaints found in {current_run_id} — "
                  f"nothing to optimize against. Stopping.")
            break

        worked_examples = _collect_worked_examples(by_model, articles)
        print(f"Asking Claude Opus to propose a revision to {current_prompt_version} "
              f"from {current_run_id}'s failure data ({len(worked_examples)} worked example(s))...")
        try:
            proposal = optimizer.propose_revision(current_prompt_text, failure_summary,
                                                   worked_examples=worked_examples)
        except Exception as e:
            print(f"[ERROR] Prompt proposal failed: {e}")
            sys.exit(1)

        new_version = prompts.save_new_version(proposal["revised_prompt"])
        _append_prompt_changelog(new_version, current_prompt_version, current_run_id, proposal["changes_summary"])
        print(f"Saved candidate {new_version} (based on {current_prompt_version}): {proposal['changes_summary']}")

        new_run_id = f"{args.run_id_prefix}-{new_version}"
        print(f"Running {new_version} as '{new_run_id}' against the same {len(articles)} article(s) "
              f"and {len(models)} model(s) as {current_run_id}...")
        run_batch(models, articles, args.judges, new_run_id, api_key,
                  gpt_judge_model=args.gpt_judge_model, max_tokens=args.max_tokens, prompt_version=new_version,
                  max_correction_attempts=args.max_correction_attempts, ground_truth=args.ground_truth,
                  require_source_quotes=args.require_source_quotes,
                  consistency_samples=args.consistency_samples)

        result = build_compare(current_run_id, new_run_id, models_filter=models)
        if "error" in result:
            print(f"[ERROR] {result['error']}")
            sys.exit(1)
        print(result["markdown"])
        (RUNS_DIR / new_run_id / f"compare_vs_{current_run_id}.md").write_text(
            result["markdown"], encoding="utf-8")

        delta = result["avg_score_delta"]
        if delta is not None and delta >= args.min_improvement:
            prompts.set_current_version(new_version)
            print(f"IMPROVED: avg judge-score delta {delta:+.2f} >= threshold {args.min_improvement} — "
                  f"{new_version} is now the current default prompt.")
            current_run_id = new_run_id
        else:
            shown = f"{delta:+.2f}" if delta is not None else "unknown (no model scored in both runs)"
            print(f"NOT ADOPTED: avg judge-score delta {shown} did not clear threshold {args.min_improvement}. "
                  f"{new_version} stays saved for the record but the current default prompt is unchanged. Stopping.")
            break

    print(f"\nDone. Current prompt version: {prompts.current_version()}. "
          f"Run `python3 scripts/eval_harness.py history` to see the trend across every iteration.")


def _render_auto_optimize_summary(round_log: list, baseline_run: str, final_run_id: str) -> str:
    """One row per round — a single evolving lineage, not a per-round table
    of competing candidates (see cmd_auto_optimize's docstring): round N is
    always exactly one test, and it always becomes the new current prompt,
    whether or not it actually scored better than round N-1."""
    lines = [
        "# Auto-optimize summary", "",
        f"Started from: `{baseline_run}`", f"Final run: `{final_run_id}`",
        f"Current prompt version: `{prompts.current_version()}`", "",
    ]
    if not round_log:
        lines.append("No round completed — stopped before the first test finished (see console output for why).")
        return "\n".join(lines)

    lines.append("| Round | Version | Run | Gen errors | Pass rate | Completeness | Judge score | "
                  "Δ vs previous | Changes |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for r in round_log:
        pass_rate = f"{r['validator_pass_rate'] * 100:.0f}%" if r["validator_pass_rate"] is not None else "–"
        completeness = f"{r['avg_completeness_score'] * 100:.0f}%" if r["avg_completeness_score"] is not None else "–"
        score = f"{r['judge_score']:.2f}" if r["judge_score"] is not None else "–"
        delta = f"{r['delta_vs_previous']:+.2f}" if r["delta_vs_previous"] is not None else "–"
        changes = (r["changes_summary"][:120] + "…") if len(r["changes_summary"]) > 120 else r["changes_summary"]
        lines.append(f"| {r['round']} | `{r['version']}` | [{r['run_id']}](./{r['run_id']}/report.html) | "
                      f"{r['generation_error_count']} | {pass_rate} | {completeness} | {score} | {delta} | "
                      f"{changes} |")

    lines.append("")
    lines.append(f"**Recommendation:** run `python3 scripts/eval_harness.py history` for the full "
                  f"cross-run trend, and `python3 scripts/eval_harness.py report --run-id {final_run_id}` "
                  f"for the dashboard behind the final numbers above.")
    return "\n".join(lines)


def _generation_error_count(rows: list) -> int:
    """Total (model, article) pairs across a run's rows that failed at the
    generation-API step (bad slug, rate limit, expired key, model outage,
    ...) rather than producing content to validate/judge. A run with any
    of these "completed" in the sense that run_batch attempted every pair
    and moved on, but the results aren't real signal — treating them as
    such is exactly how a broken batch can get silently adopted as the
    next round's baseline (see cmd_auto_optimize's gates around this)."""
    return sum(r.get("n_generation_errors", 0) for r in rows)


AUTO_OPTIMIZE_LOCK_PATH = RUNS_DIR / ".auto_optimize.lock"


def _pid_is_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # process exists, just owned by someone else — treat as alive
    return True


def _acquire_auto_optimize_lock(baseline_run: str) -> None:
    """Cross-invocation mutex: refuses to start a second auto-optimize search
    while one is already running, however it was launched. Without this, two
    overlapping searches each treat their own baseline as "current" while
    racing to save prompt versions and advance CURRENT — exactly the
    confusion of a landing page showing v33 candidates in progress while the
    status banner still reads "baseline v13," and two searches burning API
    budget optimizing against two different baselines at once. The web
    dashboard's own pgrep-based check (deploy/dashboard_server.py) only
    guards its own subprocess.Popen launch and gives faster feedback in that
    path, but this is the real, always-enforced guard: it also covers a
    directly-invoked CLI run, which that check never sees."""
    if AUTO_OPTIMIZE_LOCK_PATH.exists():
        try:
            info = json.loads(AUTO_OPTIMIZE_LOCK_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            info = {}
        pid = info.get("pid")
        if pid and _pid_is_alive(pid):
            print(f"[ERROR] Another auto-optimize search is already running (pid {pid}, "
                  f"baseline {info.get('baseline_run', '?')}, started {info.get('started_at', '?')}). "
                  f"Wait for it to finish — check eval/runs/.auto_optimize_state.json or the landing "
                  f"page — before starting another one. If it's actually dead, remove "
                  f"{AUTO_OPTIMIZE_LOCK_PATH.relative_to(WIKI_ROOT)} by hand and retry.")
            sys.exit(1)
        print(f"[WARN] Found a stale auto-optimize lock (pid {pid} is no longer running) — "
              f"removing it and proceeding.")

    AUTO_OPTIMIZE_LOCK_PATH.write_text(json.dumps({
        "pid": os.getpid(),
        "baseline_run": baseline_run,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")


def _release_auto_optimize_lock() -> None:
    try:
        AUTO_OPTIMIZE_LOCK_PATH.unlink()
    except FileNotFoundError:
        pass


def _write_auto_optimize_state(baseline_run: str, current_run_id: str, round_num: int, rounds_total: int,
                                status: str, error_detail: str = None, run_id_prefix: str = None) -> None:
    """Round-level progress, separate from any one candidate's own
    (model, article) progress bar — answers "how many rounds are left in
    this whole search," not "how far along is this one candidate." Read by
    the landing page (index_report.py) and by the web launcher to resolve
    where a "launch more rounds" click should continue from.

    error_detail: the actual error text for a "stopped_error" status,
    shown directly in the landing page's status banner. A bare "stopped —
    error, check the log" forces whoever's watching to go SSH in and dig
    through journalctl for something that's already sitting in a Python
    exception message at the point of failure — just carry it along
    instead.

    Also regenerates index.html immediately (not just this state file) —
    otherwise the landing page wouldn't visibly change until the first
    candidate's own run_batch finished a full report cycle, which can be
    minutes away. Without this, clicking "Launch" looks like a no-op even
    when the search started successfully: the click, the "starting"
    status, and every round transition are all invisible until real
    (model, article) data starts landing."""
    (RUNS_DIR / ".auto_optimize_state.json").write_text(json.dumps({
        "baseline_run": baseline_run,
        "current_run_id": current_run_id,
        "prompt_version": prompts.current_version(),
        "round": round_num,
        "rounds_total": rounds_total,
        "status": status,
        "error_detail": error_detail,
        "run_id_prefix": run_id_prefix,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")
    generate_index(verbose=False)


def _write_auto_optimize_outputs(round_log: list, baseline_run: str, final_run_id: str) -> tuple:
    """Writes both the markdown summary and its HTML dashboard companion,
    called after every round (not just at the end) so a search left running
    unattended has a visual, up-to-date report to open at any point, not
    only once the whole thing finishes. Returns (markdown_text, md_path, html_path)."""
    summary_md = _render_auto_optimize_summary(round_log, baseline_run, final_run_id)
    summary_path = RUNS_DIR / f"auto-optimize-summary-{baseline_run}.md"
    summary_path.write_text(summary_md, encoding="utf-8")

    html_path = RUNS_DIR / f"auto-optimize-summary-{baseline_run}.html"
    html_path.write_text(
        auto_optimize_report.render_html(round_log, baseline_run, final_run_id, prompts.current_version()),
        encoding="utf-8",
    )
    return summary_md, summary_path, html_path


AUTO_OPTIMIZE_CONSOLE_LOG_PATH = RUNS_DIR / ".auto_optimize_console.log"


class _ConsoleTee:
    """Duplicates every write to the real stream AND a fixed log file, so
    the landing page can show live console output regardless of how
    auto-optimize was launched — the web button, systemd, and a bare CLI
    invocation each send this process's own stdout somewhere different (a
    per-launch log file, journald, a terminal), but this always
    additionally lands in one predictable place (AUTO_OPTIMIZE_CONSOLE_LOG_PATH)
    the dashboard knows to poll."""
    def __init__(self, stream, log_file):
        self._stream = stream
        self._log_file = log_file

    def write(self, s):
        self._stream.write(s)
        self._log_file.write(s)
        self._log_file.flush()

    def flush(self):
        self._stream.flush()
        self._log_file.flush()

    def isatty(self):
        return False


def cmd_auto_optimize(args: argparse.Namespace) -> None:
    """Self-driving optimization loop: one test per round, strictly serial.
    Each round:
      1. Takes the previous round's full results — validator issues, judge
         complaints, AND generation/API errors alike (a failed pair still
         counts as a completed one, just a failed one) — and asks Claude
         Opus for ONE revised prompt informed by all of it.
      2. Runs that single revision as this round's test, all configured
         models in parallel (bounded by --concurrency), against the same
         articles as the previous round.
      3. Unconditionally adopts it as the new current prompt — this is one
         evolving lineage, not a search across competing candidates kept
         only if they win, so a round that didn't improve still becomes
         next round's starting point (and its own shortfall becomes new
         failure data to react to).
    Round N+1 never starts until round N has fully completed. Stops on
    --rounds or --time-budget-minutes, whichever comes first, then writes
    a final recommendation summary (one row per round + the resulting
    current prompt version) so an unattended run started before walking
    away has something concrete to read on return, not just scrollback."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("[ERROR] OPENROUTER_API_KEY environment variable not set.")
        sys.exit(1)
    if not (RUNS_DIR / args.baseline_run).exists():
        print(f"[ERROR] No run directory: {RUNS_DIR / args.baseline_run}")
        sys.exit(1)

    _acquire_auto_optimize_lock(args.baseline_run)
    console_log_file = open(AUTO_OPTIMIZE_CONSOLE_LOG_PATH, "w", encoding="utf-8")
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    sys.stdout = _ConsoleTee(orig_stdout, console_log_file)
    sys.stderr = _ConsoleTee(orig_stderr, console_log_file)
    try:
        _run_auto_optimize_loop(args)
    finally:
        sys.stdout, sys.stderr = orig_stdout, orig_stderr
        console_log_file.close()
        _release_auto_optimize_lock()


def _run_auto_optimize_loop(args: argparse.Namespace) -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    deadline = time.monotonic() + args.time_budget_minutes * 60
    current_run_id = args.baseline_run
    round_log = []

    def _write_state(round_num: int, status: str, error_detail: str = None) -> None:
        _write_auto_optimize_state(args.baseline_run, current_run_id, round_num, args.rounds, status,
                                    error_detail=error_detail, run_id_prefix=args.run_id_prefix)

    _write_state(0, "starting")

    for round_num in range(1, args.rounds + 1):
        remaining_min = (deadline - time.monotonic()) / 60
        if remaining_min <= 0:
            print(f"\nTime budget ({args.time_budget_minutes} min) exhausted before round {round_num}. Stopping.")
            _write_state(round_num - 1, "stopped_time_budget")
            break
        print(f"\n=== auto-optimize round {round_num}/{args.rounds} — testing from: {current_run_id} "
              f"(~{remaining_min:.1f} min left in budget) ===")
        _write_state(round_num, "running")

        current_dir = RUNS_DIR / current_run_id
        by_model, base_rows = compute_rows(current_dir)
        if not by_model:
            error_detail = f"{current_run_id} has no completed results to learn from."
            print(f"[ERROR] {error_detail}")
            _write_state(round_num - 1, "stopped_error", error_detail=error_detail)
            sys.exit(1)

        models = args.models or sorted(by_model.keys())
        article_ids = sorted({rec["article_id"] for records in by_model.values() for rec in records})
        articles = load_manifest(article_ids)
        if not articles:
            error_detail = "Could not resolve manifest articles from the baseline run's article ids."
            print(f"[ERROR] {error_detail}")
            _write_state(round_num - 1, "stopped_error", error_detail=error_detail)
            sys.exit(1)

        sample_record = next(iter(by_model.values()))[0]
        current_prompt_version = sample_record.get("prompt_version") or prompts.current_version()
        current_prompt_text = prompts.load_prompt(current_prompt_version)

        failure_summary = failure_analysis.analyze(by_model)
        base_gen_errors = _generation_error_count(base_rows)
        # Generation/API errors count as findings too — a round that failed
        # outright still has something to react to (see optimizer.py's
        # system prompt, which is told these are infra failures, not
        # content problems, and to say so rather than inventing a fix).
        # Only a genuinely clean, issue-free round has nothing left to do.
        has_findings = base_gen_errors > 0 or any(
            d.get("validator_top_issues") or d.get("judge_keyword_tally") for d in failure_summary.values())
        if not has_findings:
            print(f"No validator issues, judge complaints, or generation errors found in {current_run_id} — "
                  f"nothing left to optimize against. Stopping.")
            _write_state(round_num - 1, "stopped_no_findings")
            break

        worked_examples = _collect_worked_examples(by_model, articles)
        print(f"Asking Claude Opus to propose a revision to {current_prompt_version} "
              f"from {current_run_id}'s results ({len(worked_examples)} worked example(s))...")
        try:
            proposal = optimizer.propose_revision(current_prompt_text, failure_summary,
                                                   worked_examples=worked_examples)
        except Exception as e:
            error_detail = f"Prompt proposal failed: {type(e).__name__}: {e}"
            print(f"[ERROR] {error_detail}")
            _write_state(round_num - 1, "stopped_error", error_detail=error_detail)
            break

        new_version = prompts.save_new_version(proposal["revised_prompt"])
        _append_prompt_changelog(new_version, current_prompt_version, current_run_id, proposal["changes_summary"])
        new_run_id = f"{args.run_id_prefix}-{new_version}"
        print(f"Saved {new_version} (based on {current_prompt_version}): {proposal['changes_summary'][:150]}")
        print(f"Running {new_version} as '{new_run_id}' against {len(models)} model(s) x "
              f"{len(articles)} article(s) (concurrency={args.concurrency})...")

        run_batch(models, articles, args.judges, new_run_id, api_key,
                  gpt_judge_model=args.gpt_judge_model, max_tokens=args.max_tokens,
                  prompt_version=new_version, concurrency=args.concurrency,
                  max_correction_attempts=args.max_correction_attempts, ground_truth=args.ground_truth,
                  require_source_quotes=args.require_source_quotes,
                  consistency_samples=args.consistency_samples)

        _, new_rows = compute_rows(RUNS_DIR / new_run_id)
        new_gen_errors = _generation_error_count(new_rows)
        compare = build_compare(current_run_id, new_run_id, models_filter=models)
        delta = None
        if "error" not in compare:
            (RUNS_DIR / new_run_id / f"compare_vs_{current_run_id}.md").write_text(
                compare["markdown"], encoding="utf-8")
            delta = compare["avg_score_delta"]
        shown = f"{delta:+.2f}" if delta is not None else "unknown"
        print(f"  {new_version}: {new_gen_errors} generation error(s), avg judge-score delta vs "
              f"{current_run_id}: {shown}")

        # No adopt/reject gate: every round's revision becomes the new
        # current prompt unconditionally — see cmd_auto_optimize's
        # docstring. A regression is not discarded; it becomes next
        # round's own baseline and its shortfall becomes new failure data.
        prompts.set_current_version(new_version)
        current_run_id = new_run_id

        new_scores = [v for r in new_rows for v in (r.get("judge_opus_avg_score"), r.get("judge_gpt_avg_score"))
                      if v is not None]
        pass_rates = [r["validator_pass_rate"] for r in new_rows]
        completeness = [r["avg_completeness_score"] for r in new_rows]

        round_log.append({
            "round": round_num,
            "run_id": new_run_id,
            "version": new_version,
            "based_on_run": current_dir.name,
            "changes_summary": proposal["changes_summary"],
            "generation_error_count": new_gen_errors,
            "validator_pass_rate": round(sum(pass_rates) / len(pass_rates), 3) if pass_rates else None,
            "avg_completeness_score": round(sum(completeness) / len(completeness), 3) if completeness else None,
            "judge_score": round(max(new_scores), 2) if new_scores else None,
            "delta_vs_previous": delta,
        })
        _write_auto_optimize_outputs(round_log, args.baseline_run, current_run_id)
    else:
        # The for loop ran to completion (no break) — every round up to
        # --rounds ran and advanced.
        _write_state(args.rounds, "completed")

    summary_md, summary_path, html_path = _write_auto_optimize_outputs(round_log, args.baseline_run, current_run_id)
    print(f"\n{summary_md}")
    print(f"\nDone. Wrote {summary_path.relative_to(WIKI_ROOT)} and {html_path.relative_to(WIKI_ROOT)}. "
          f"Current prompt version: {prompts.current_version()}.")


def main() -> None:
    _load_secrets_env()
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
    p_run.add_argument("--retry-errors-only", action="store_true",
                        help="Like --overwrite, but only for pairs whose cached result has a generation "
                             "error — a pair that already succeeded is left alone. For retrying after "
                             "fixing something external (a billing cap, an expired key) without re-paying "
                             "for results that are already good.")
    p_run.add_argument("--refresh-cache", action="store_true", help="Force re-fetch of article text")
    p_run.add_argument("--max-tokens", type=int, default=8000)
    p_run.add_argument("--concurrency", type=int, default=1,
                        help="Max concurrent (model, article) generation calls (default: 1, i.e. sequential)")
    p_run.add_argument("--prompt-version", default=None,
                        help="Extraction prompt version to use, e.g. v1, v2 (default: latest in scripts/eval/prompt_versions/)")
    p_run.add_argument("--max-correction-attempts", type=int, default=0,
                        help="After a validator failure, show the model its own issues and let it retry up "
                             "to N times (default: 0, i.e. the original single-shot benchmark behavior — "
                             "this measures FIRST-attempt quality, so opt in explicitly rather than "
                             "changing the default). Each record keeps both `initial_passed` (first "
                             "attempt) and the final post-correction `validation.passed`.")
    p_run.add_argument("--ground-truth", action="store_true",
                        help="Live-verify each citation's DOI (Crossref) or arXiv id (arXiv API) instead of "
                             "only checking it LOOKS like a real citation (see scripts/eval/ground_truth.py) "
                             "— catches a fabricated-but-plausible identifier a shape check can't. Off by "
                             "default: adds real network calls to every validation pass.")
    p_run.add_argument("--require-source-quotes", action="store_true",
                        help="Require (and verify against the actual article text) a verbatim source_quote "
                             "field on every claim's evidence entries — see scripts/eval/ground_truth.py's "
                             "quote_is_grounded(). Off by default: no existing prompt version's schema "
                             "includes this field yet, so turning it on before one does will legitimately "
                             "fail almost every extraction.")
    p_run.add_argument("--consistency-samples", type=int, default=1,
                        help="SelfCheckGPT-style: independently re-generate each (model, article) pair this "
                             "many times total (default: 1, i.e. off) and flag any citation/quote that isn't "
                             "reproduced across ALL samples as a possible confabulation — see "
                             "scripts/eval/consistency.py. N-1 extra generation calls per pair: real added "
                             "cost, roughly proportional to N. Can't be applied to spotcheck (needs fresh "
                             "generation, nothing to resample from a cached result).")
    p_run.add_argument("--subclaim-judging", action="store_true",
                        help="FActScore-style (Min et al., EMNLP 2023): judge each claim's subclaims "
                             "independently instead of one holistic score for the whole extraction — a "
                             "localized 'which exact sentence is wrong' signal instead of a blended average. "
                             "See scripts/eval/judge.py's judge_subclaims(). Real cost multiplier: roughly "
                             "one extra judge call per subclaim, not per article, using the same --judges "
                             "models as the normal whole-extraction judging.")

    p_spot = subparsers.add_parser("spotcheck", help="Re-validate/re-judge cached results without re-generating")
    p_spot.add_argument("--run-id", required=True)
    p_spot.add_argument("--models", nargs="+", default=None)
    p_spot.add_argument("--n", type=int, default=None, help="Limit to first N cached results")
    p_spot.add_argument("--judges", nargs="+", default=[], choices=["opus", "gpt"],
                         help="Judges to (re-)run; omit to only re-run the structural validator")
    p_spot.add_argument("--gpt-judge-model", default="gpt-5.6")
    p_spot.add_argument("--ground-truth", action="store_true",
                         help="Live-verify each cached extraction's citations against Crossref/arXiv — the "
                              "cheapest way to try this, since it re-uses already-generated output for free.")
    p_spot.add_argument("--require-source-quotes", action="store_true",
                         help="Also check each cached extraction's source_quote fields (see `run --help`) — "
                              "re-fetches article text from the cache (free) to check grounding.")

    p_report = subparsers.add_parser("report", help="Aggregate a run's cached results into report.md + summary.csv")
    p_report.add_argument("--run-id", required=True)

    p_compare = subparsers.add_parser("compare", help="Diff two runs model-by-model (e.g. before/after a prompt change)")
    p_compare.add_argument("--baseline", required=True, help="Run id to compare from (the 'before')")
    p_compare.add_argument("--candidate", required=True, help="Run id to compare to (the 'after')")
    p_compare.add_argument("--models", nargs="+", default=None, help="Restrict to these models (default: all common to both runs)")

    p_cost = subparsers.add_parser("project-cost", help="Extrapolate a run's measured $/article to hypothetical corpus sizes")
    p_cost.add_argument("--run-id", required=True)
    p_cost.add_argument("--models", nargs="+", default=None)
    p_cost.add_argument("--sizes", nargs="+", type=int, default=None,
                         help=f"Corpus sizes to project (default: {cost_projection.DEFAULT_SIZES})")
    p_cost.add_argument("--qa-sample-rate", type=float, default=cost_projection.DEFAULT_QA_SAMPLE_RATE,
                         help="Fraction of the projected corpus spot-checked with both judges (default: 0.05)")

    p_hist = subparsers.add_parser("history", help="Trend view across every run under eval/runs/")
    p_hist.add_argument("--models", nargs="+", default=None)

    subparsers.add_parser(
        "index", help="Regenerate eval/runs/index.html (the http://localhost:8080/ landing page) on demand")

    p_status = subparsers.add_parser(
        "status", help="Progress tracker: how many (model, article) pairs are done/errored/pending, per model and overall")
    p_status.add_argument("--run-id", default=None, help="Default: --run-id in deploy/run-config.env's RUN_ARGS")
    p_status.add_argument("--models", nargs="+", default=None, help="Default: --models in deploy/run-config.env's RUN_ARGS")
    p_status.add_argument("--articles", nargs="+", default=None, help="Article ids to restrict to (default: all)")

    p_opt = subparsers.add_parser(
        "optimize",
        help="Auto-iterate the extraction prompt: propose a revision from a run's failures, re-run, compare, keep only if improved")
    p_opt.add_argument("--baseline-run", required=True, help="Run id to start from")
    p_opt.add_argument("--models", nargs="+", default=None, help="Default: every model present in the baseline run")
    p_opt.add_argument("--judges", nargs="+", default=["opus", "gpt"], choices=["opus", "gpt"])
    p_opt.add_argument("--gpt-judge-model", default="gpt-5.6")
    p_opt.add_argument("--max-tokens", type=int, default=8000)
    p_opt.add_argument("--max-correction-attempts", type=int, default=0,
                        help="Let the model retry up to N times after a validator failure (default: 0). "
                             "See `run --help` for why this defaults off.")
    p_opt.add_argument("--ground-truth", action="store_true",
                        help="Live-verify citations against Crossref/arXiv during each candidate's validation "
                             "pass (see `run --help`). Also surfaces any fabricated-identifier findings to "
                             "the prompt-engineer as real failure data for the next revision.")
    p_opt.add_argument("--require-source-quotes", action="store_true",
                        help="Require a verbatim source_quote field on evidence entries (see `run --help`). "
                             "Surfaces missing/fabricated-quote findings to the prompt-engineer, which is "
                             "explicitly instructed to add the field to the schema in response.")
    p_opt.add_argument("--consistency-samples", type=int, default=1,
                        help="SelfCheckGPT-style consistency sampling per pair (see `run --help`). Real added "
                             "cost: N-1 extra generation calls per (model, article) pair.")
    p_opt.add_argument("--iterations", type=int, default=1, help="Max propose/re-run rounds (default: 1)")
    p_opt.add_argument("--min-improvement", type=float, default=0.0,
                        help="Minimum avg judge-score delta to adopt a candidate as the new current prompt (default: 0.0, i.e. any improvement)")
    p_opt.add_argument("--run-id-prefix", default="optimize", help="New runs are named <prefix>-<version>, e.g. optimize-v3")

    p_auto = subparsers.add_parser(
        "auto-optimize",
        help="Self-driving optimization: one test per round, strictly serial — propose a revision from the "
             "previous round's full results (failures included), run it, unconditionally adopt it, repeat "
             "until the time budget or round cap is hit or nothing is left to react to")
    p_auto.add_argument("--baseline-run", required=True, help="Run id to start from")
    p_auto.add_argument("--models", nargs="+", default=None, help="Default: every model present in the baseline run")
    p_auto.add_argument("--judges", nargs="+", default=["opus", "gpt"], choices=["opus", "gpt"])
    p_auto.add_argument("--gpt-judge-model", default="gpt-5.6")
    p_auto.add_argument("--max-tokens", type=int, default=8000)
    p_auto.add_argument("--max-correction-attempts", type=int, default=0,
                         help="Let each round's test retry up to N times after a validator failure (default: 0). "
                              "See `run --help` for why this defaults off.")
    p_auto.add_argument("--ground-truth", action="store_true",
                         help="Live-verify citations against Crossref/arXiv during each round's validation "
                              "pass (see `run --help`). Also surfaces any fabricated-identifier findings to "
                              "the prompt-engineer as real failure data for the next revision.")
    p_auto.add_argument("--require-source-quotes", action="store_true",
                         help="Require a verbatim source_quote field on evidence entries (see `run --help`). "
                              "Surfaces missing/fabricated-quote findings to the prompt-engineer, which is "
                              "explicitly instructed to add the field to the schema in response.")
    p_auto.add_argument("--consistency-samples", type=int, default=1,
                         help="SelfCheckGPT-style consistency sampling per pair (see `run --help`). Real added "
                              "cost: N-1 extra generation calls per (model, article) pair.")
    p_auto.add_argument("--rounds", type=int, default=3, help="Max rounds (default: 3)")
    p_auto.add_argument("--concurrency", type=int, default=6,
                         help="Max concurrent (model, article) generation calls within one round's test "
                              "(default: 6)")
    p_auto.add_argument("--time-budget-minutes", type=float, default=60,
                         help="Stop starting new rounds once this much wall-clock time has elapsed (default: 60)")
    p_auto.add_argument("--run-id-prefix", default="auto",
                         help="New runs are named <prefix>-<version>, e.g. auto-v16 — one run per round, "
                              "no round number in the name")

    args = parser.parse_args()
    dispatch = {"run": cmd_run, "spotcheck": cmd_spotcheck, "report": cmd_report, "compare": cmd_compare,
                "project-cost": cmd_project_cost, "history": cmd_history, "index": cmd_index, "optimize": cmd_optimize,
                "status": cmd_status, "auto-optimize": cmd_auto_optimize}
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
