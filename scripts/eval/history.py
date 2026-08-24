"""
history.py — Cross-run trend view. A single run's report answers "how did
these models do this time"; this answers "are we actually improving as we
iterate on the prompt" — the thing you need to see progress across many
test batches rather than comparing two at a time by hand.
"""

import json
from pathlib import Path


def collect(runs_dir: Path) -> list:
    """One row per (run, model): earliest article timestamp (for chronological
    ordering), prompt version, judge scores, validator pass rate, cost."""
    rows = []
    for run_dir in sorted(runs_dir.iterdir()):
        if not run_dir.is_dir():
            continue
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
                "cost_per_article_usd": round(sum(g["cost_usd"] or 0 for g in gens) / len(gens), 5) if gens else None,
                "avg_latency_s": round(sum(g["latency_s"] for g in gens) / len(gens), 1) if gens else None,
            })

    rows.sort(key=lambda r: (r["earliest_timestamp"], r["run_id"], r["model"]))
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
    lines.append("Sorted chronologically by each run's earliest completed article. "
                  "A model with no judge score/pass rate either hasn't completed an article in "
                  "that run yet or errored on every attempt (check that run's report for gen errors).")
    return "\n".join(lines)
