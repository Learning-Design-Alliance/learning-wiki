"""
failure_analysis.py — Automatic "why did this fail" summary across a run,
so a recurring problem shows up as a pattern instead of requiring someone to
manually open failed records one at a time.

Two free (no extra API cost) passes:
  1. Validator issues are exact and structured — tally (field, message) pairs
     verbatim. If the same message fires on 8/10 articles for a model, that's
     very likely one systematic issue (a prompt gap, a model formatting habit),
     not ten unrelated ones.
  2. Judge issues are free-text — bucket them by keyword into rough categories
     (fabrication, omission, duplication, inaccuracy) so a shape emerges
     without paying for another LLM call to categorize them.
"""

import re
from collections import Counter

KEYWORD_BUCKETS = {
    "fabrication": ["fabricat", "hallucinat", "invented", "not identified as belonging",
                    "misattribut", "no doi", "made up"],
    "omission": ["omit", "drop", "miss", "incomplete", "leaves out"],
    "duplication": ["duplicate", "near-duplicate", "redundant", "restate", "repeats"],
    "inaccuracy": ["garbled", "inaccura", "incorrect", "unsupported", "not established",
                   "not reported", "not measured", "not discussed", "not tested",
                   "misrepresent", "overstate"],
}


def _bucket_issue(issue: str) -> list:
    lower = issue.lower()
    return [name for name, keywords in KEYWORD_BUCKETS.items()
            if any(kw in lower for kw in keywords)]


def analyze(by_model: dict, top_n: int = 5, sample_n: int = 5) -> dict:
    """Returns {model: {validator_top_issues, judge_keyword_tally,
    judge_sample_issues, worst_articles}}."""
    summary = {}

    for model, records in by_model.items():
        validator_counter = Counter()
        for rec in records:
            for issue in (rec.get("validation") or {}).get("issues", []):
                key = (issue["severity"], issue["field"], issue["message"])
                validator_counter[key] += 1
        validator_top = [
            {"severity": sev, "field": field, "message": msg, "count": n}
            for (sev, field, msg), n in validator_counter.most_common(top_n)
        ]

        keyword_tally = Counter()
        sample_issues = []
        for rec in records:
            for jname, jdata in (rec.get("judges") or {}).items():
                if jdata.get("verdict") != "fail":
                    continue
                for issue in jdata.get("issues", []):
                    for bucket in _bucket_issue(issue):
                        keyword_tally[bucket] += 1
                    if len(sample_issues) < sample_n:
                        sample_issues.append({
                            "article_id": rec["article_id"], "judge": jname, "issue": issue,
                        })

        scored = []
        for rec in records:
            judges = rec.get("judges") or {}
            scores = [j.get("average_score") for j in judges.values() if j.get("average_score") is not None]
            if scores:
                scored.append((rec["article_id"], sum(scores) / len(scores)))
        worst = sorted(scored, key=lambda x: x[1])[:3]

        gen_errors = [rec["generation"]["error"] for rec in records
                      if (rec.get("generation") or {}).get("error")]

        summary[model] = {
            "validator_top_issues": validator_top,
            "judge_keyword_tally": dict(keyword_tally.most_common()),
            "judge_sample_issues": sample_issues,
            "worst_articles": [{"article_id": a, "avg_judge_score": round(s, 2)} for a, s in worst],
            # Generation/API failures (bad slug, rate limit, expired key, an
            # exhausted account) are a different animal from a validator or
            # judge complaint — they say nothing about prompt quality, but a
            # round dominated by them still needs to be visible as "this
            # test didn't really produce content to learn from" rather than
            # silently looking like a clean, issue-free run.
            "generation_error_count": len(gen_errors),
            "generation_error_samples": gen_errors[:sample_n],
        }

    return summary


def render_markdown(summary: dict) -> str:
    lines = ["## Common failure patterns", ""]
    for model, data in summary.items():
        lines.append(f"### {model}")
        if data["validator_top_issues"]:
            lines.append("")
            lines.append("**Most common validator issues:**")
            for issue in data["validator_top_issues"]:
                lines.append(f"- `{issue['count']}x` [{issue['severity']}] {issue['field']}: {issue['message']}")
        if data["judge_keyword_tally"]:
            lines.append("")
            lines.append("**Judge complaint categories (failed verdicts only):**")
            for bucket, count in data["judge_keyword_tally"].items():
                lines.append(f"- {bucket}: {count} mentions")
        if data["worst_articles"]:
            lines.append("")
            lines.append("**Lowest-scoring articles:**")
            for w in data["worst_articles"]:
                lines.append(f"- {w['article_id']}: {w['avg_judge_score']}/5 avg judge score")
        lines.append("")
    return "\n".join(lines)
