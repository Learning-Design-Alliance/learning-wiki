"""
executive_summary.py — Synthesizes the per-model rows + failure_analysis
output into a plain-English recommendation: which model to use, what's
actually wrong, and what to fix in the extraction prompt or the validator
before the next batch. Rule-based (no extra LLM call) — every number in the
summary traces back to something already computed by eval_harness.py, so
adding this cost nothing and stays deterministic.
"""

# (keyword bucket, minimum mentions to surface, message template)
PROCESS_RECOMMENDATIONS = [
    ("fabrication", 1,
     "Fabrication was flagged by judges — models are inventing DOIs/identifiers for sources that don't have "
     "one (e.g. conference papers). Tighten the prompt: 'many sources have no DOI — leave doi_or_url blank "
     "rather than inventing one' with a concrete example."),
    ("duplication", 1,
     "Judges flagged near-duplicate contributions — a single finding is being multiplied into matching "
     "principle/element/pattern/strategy entries that just restate it. Tighten the 'be conservative' rule: "
     "one finding usually warrants one claim, not a bundle of contribution types."),
    ("omission", 2,
     "Omission was a recurring judge complaint — extractions are dropping the concrete numbers (means, %, n, "
     "specific design dimensions) that make a finding usable. Add: 'always include the actual reported "
     "statistics in the evidence description, not a paraphrase without numbers.'"),
    ("inaccuracy", 2,
     "Judges flagged inaccuracies beyond simple omission — findings are being restated in ways that change "
     "their meaning (e.g. conflating a theoretical explanation with something the study actually measured)."),
]

VALIDATOR_ID_FIELD_HINT = "id"


def _model_quality(row: dict) -> float:
    scores = [row.get("judge_opus_avg_score"), row.get("judge_gpt_avg_score"), row.get("judge_gemini_avg_score")]
    scores = [s for s in scores if s is not None]
    return sum(scores) / len(scores) if scores else None


def _model_cost_per_article(row: dict) -> float:
    n = row.get("n_articles") or 0
    return (row.get("total_generation_cost_usd") or 0) / n if n else None


def summarize(rows: list, failure_summary: dict) -> dict:
    max_n = max((r.get("n_articles", 0) for r in rows), default=0)
    total_cost = sum(r.get("total_generation_cost_usd", 0) for r in rows)
    total_articles = sum(r.get("n_articles", 0) for r in rows)

    scored_models = []
    for r in rows:
        quality = _model_quality(r)
        cost = _model_cost_per_article(r)
        if quality is None:
            continue
        scored_models.append({
            "model": r["model"], "quality": quality, "cost_per_article": cost,
            "n_articles": r.get("n_articles", 0),
            "validator_pass_rate": r.get("validator_pass_rate"),
            "partial_sample": r.get("n_articles", 0) < max_n,
        })
    scored_models.sort(key=lambda m: m["quality"], reverse=True)

    recommendation = None
    caveats = []
    if scored_models:
        best = scored_models[0]
        # Prefer a cheaper close second if it's within 0.3 judge points —
        # not worth paying more for a difference this small.
        for candidate in scored_models[1:]:
            if best["quality"] - candidate["quality"] <= 0.3 and candidate["cost_per_article"] < best["cost_per_article"]:
                best = candidate
        recommendation = best
        if any(m["partial_sample"] for m in scored_models):
            caveats.append("Not every model has finished the same number of articles yet — treat this "
                            "recommendation as preliminary until all models complete the same set.")
        if all((m["validator_pass_rate"] or 0) == 0 for m in scored_models):
            caveats.append("Every model shows a 0% validator pass rate so far — check the 'Failure patterns' "
                            "tab before reading that as 'nothing works': it's often one fixable formatting rule "
                            "(e.g. a claim id format) dominating the count, not a wholesale failure.")
        if recommendation["quality"] < 3.5:
            caveats.append(f"Even the best model so far averages {recommendation['quality']:.2f}/5 from the "
                            "judges — that's a real quality ceiling at this model tier, not just a formatting "
                            "issue. Consider testing a stronger model before committing to a bulk run.")

    process_fixes = []
    all_keywords = {}
    all_validator_issues = {}
    for data in failure_summary.values():
        for bucket, count in data.get("judge_keyword_tally", {}).items():
            all_keywords[bucket] = all_keywords.get(bucket, 0) + count
        for issue in data.get("validator_top_issues", []):
            key = (issue["field"], issue["message"])
            all_validator_issues[key] = all_validator_issues.get(key, 0) + issue["count"]

    for bucket, min_count, message in PROCESS_RECOMMENDATIONS:
        if all_keywords.get(bucket, 0) >= min_count:
            process_fixes.append({"issue": bucket, "count": all_keywords[bucket], "recommendation": message})

    id_format_issues = sum(n for (field, msg), n in all_validator_issues.items() if field == VALIDATOR_ID_FIELD_HINT)
    if id_format_issues:
        process_fixes.append({
            "issue": "id format", "count": id_format_issues,
            "recommendation": f"The 'CL-<shortcode>' id format was missed {id_format_issues}x — this is "
                               "cosmetic (doesn't affect content quality) but is likely inflating the "
                               "validator's pass/fail count. Either restate the format more forcefully in the "
                               "prompt with a right/wrong example, or downgrade this specific check from error "
                               "to warning so 'passed' better reflects substantive quality.",
        })

    return {
        "total_cost_usd": round(total_cost, 4),
        "total_articles": total_articles,
        "n_models": len(rows),
        "recommendation": recommendation,
        "ranked_models": scored_models,
        "caveats": caveats,
        "process_fixes": process_fixes,
    }


def render_markdown(summary: dict) -> str:
    lines = ["## Executive summary", ""]
    lines.append(f"{summary['n_models']} model(s), {summary['total_articles']} article results, "
                 f"${summary['total_cost_usd']} spent on generation so far.")
    lines.append("")

    rec = summary["recommendation"]
    if rec:
        lines.append(f"**Recommended model so far: `{rec['model']}`** — "
                     f"{rec['quality']:.2f}/5 avg judge score"
                     + (f", ${rec['cost_per_article']:.4f}/article" if rec["cost_per_article"] else "") + ".")
    else:
        lines.append("No model has a judge score yet — recommendation pending.")
    lines.append("")

    if summary["caveats"]:
        lines.append("**Caveats:**")
        for c in summary["caveats"]:
            lines.append(f"- {c}")
        lines.append("")

    if summary["process_fixes"]:
        lines.append("**Recommended fixes to the extraction prompt / validator:**")
        for f in summary["process_fixes"]:
            lines.append(f"- {f['recommendation']}")
        lines.append("")

    return "\n".join(lines)
