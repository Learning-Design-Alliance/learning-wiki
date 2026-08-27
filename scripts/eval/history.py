"""
history.py — Cross-run trend view. A single run's report answers "how did
these models do this time"; this answers "are we actually improving as we
iterate on the prompt" — the thing you need to see progress across many
test batches rather than comparing two at a time by hand.
"""

import json
import re
from pathlib import Path

# Mirrors eval_harness.py's _run_order_key (duplicated rather than shared —
# a small self-contained regex, and importing eval_harness from here would
# be circular since eval_harness imports this module). auto-optimize/
# optimize runs are named <prefix>-v<N>, one test per version, a single
# monotonic sequence — sorting by that number is the actual chronological
# order tests were generated in, regardless of which one happened to
# finish first. Plain alphabetical sort (the previous behavior) put v2
# after v19, which is why the trend charts' x-axis read as scrambled.
_VERSIONED_RUN_ID_RE = re.compile(r"^.+-v(\d+)$")


def _run_order_key(run_dir: Path) -> tuple:
    m = _VERSIONED_RUN_ID_RE.match(run_dir.name)
    if m:
        return (1, int(m.group(1)))
    try:
        first_created = min((f.stat().st_mtime for f in run_dir.glob("*/*.json")), default=0)
    except OSError:
        first_created = 0
    return (0, first_created)


def collect(runs_dir: Path) -> list:
    """One row per (run, model): earliest article timestamp (for chronological
    ordering), prompt version, judge scores, validator pass rate, cost."""
    rows = []
    run_dirs = sorted((d for d in runs_dir.iterdir() if d.is_dir()), key=_run_order_key)
    for run_dir in run_dirs:
        by_model = {}
        for path in sorted(run_dir.glob("*/*.json")):
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            by_model.setdefault(record["model"], []).append(record)

        for model, records in by_model.items():
            n = len(records)
            gens = [r["generation"] for r in records if r.get("generation") and "error" not in r["generation"]]
            vals = [r["validation"] for r in records if r.get("validation")]
            timestamps = [r["generated_at"] for r in records if r.get("generated_at")]
            versions = {r.get("prompt_version") for r in records if r.get("prompt_version")}

            opus_scores = [r["judges"]["opus"]["average_score"] for r in records
                           if r.get("judges", {}).get("opus", {}).get("average_score") is not None]
            gpt_scores = [r["judges"]["gpt"]["average_score"] for r in records
                          if r.get("judges", {}).get("gpt", {}).get("average_score") is not None]
            all_scores = opus_scores + gpt_scores

            rows.append({
                "run_id": run_dir.name,
                "prompt_version": ", ".join(sorted(versions)) if versions else "unknown",
                "model": model,
                "n_articles": n,
                "n_ok": len(gens),
                "earliest_timestamp": min(timestamps) if timestamps else "",
                "avg_judge_score": round(sum(all_scores) / len(all_scores), 2) if all_scores else None,
                "validator_pass_rate": round(sum(1 for v in vals if v["passed"]) / len(vals), 3) if vals else None,
                "avg_completeness_score": round(sum(v["completeness_score"] for v in vals) / len(vals), 3) if vals else None,
                "cost_per_article_usd": round(sum(g["cost_usd"] or 0 for g in gens) / len(gens), 5) if gens else None,
                "avg_latency_s": round(sum(g["latency_s"] for g in gens) / len(gens), 1) if gens else None,
            })

    # Deliberately NOT re-sorted by earliest_timestamp: rows are already in
    # run_dirs' order (built above), and wall-clock timestamps are exactly
    # what can't be trusted here — two auto-optimize searches running at
    # once (the actual root cause of a very real earlier incident) can
    # generate an earlier version's results LATER in wall-clock time than
    # a later version's, which silently scrambled this list before.
    return rows


def render_markdown(rows: list) -> str:
    lines = [
        "# History across runs", "",
        "| Run | Prompt | Model | Articles OK | Avg judge score | Validator pass rate | $/article |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        judge_str = r["avg_judge_score"] if r["avg_judge_score"] is not None else "-"
        pass_rate_str = f"{r['validator_pass_rate'] * 100:.0f}%" if r["validator_pass_rate"] is not None else "-"
        cost_str = f"${r['cost_per_article_usd']:.5f}" if r["cost_per_article_usd"] is not None else "-"
        lines.append(
            f"| {r['run_id']} | {r['prompt_version']} | {r['model']} | {r['n_ok']}/{r['n_articles']} | "
            f"{judge_str} | {pass_rate_str} | {cost_str} |"
        )
    lines.append("")
    lines.append("Sorted by run/version sequence (not wall-clock time, which can't be trusted if two "
                  "searches ever ran at once). A model with no judge score/pass rate either hasn't "
                  "completed an article in that run yet or errored on every attempt (check that run's "
                  "report for gen errors).")
    return "\n".join(lines)
