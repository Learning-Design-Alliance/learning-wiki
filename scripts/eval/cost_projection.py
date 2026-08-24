"""
cost_projection.py — Extrapolates a run's measured $/article rate to
hypothetical corpus sizes, so "should we run this at scale" has a real
number attached instead of a guess. Every rate here comes from actual
generation/judge costs already recorded for the run — this module only
multiplies, it never invents a price.

Corpus-size context (see eval/SOURCES.md for sourcing): the realistic
scope for "open-access education/learning-science articles across arXiv,
ERIC, and PMC" is very unlikely to be anywhere near arXiv/ERIC/PMC's full
multi-million-record totals — those cover every field, not just education —
research while building this suggested more like tens of thousands to a few
hundred thousand once narrowed to education-relevant + freely-fetchable
full text (ERIC alone publishes ~350K full-text items out of ~2M total
records; arXiv's education-adjacent categories run in the thousands to low
tens of thousands each). Treat DEFAULT_SIZES as bracketing the plausible
range, not a prediction — get an actual candidate count (e.g. from the ERIC
bulk API or an arXiv category export) before trusting one number over the
others.
"""

DEFAULT_SIZES = [10_000, 50_000, 100_000, 500_000, 1_000_000]
DEFAULT_QA_SAMPLE_RATE = 0.05  # spot-check this fraction with both judges in production, not every article


def project(rows: list, sizes: list = None, qa_sample_rate: float = DEFAULT_QA_SAMPLE_RATE) -> list:
    """One row per (model, corpus size): generation-only cost, and generation
    + a QA judge pass sampled at qa_sample_rate (double-judging every single
    production article forever is rarely the right call — that's an
    evaluation-time cost, not a recurring production one)."""
    sizes = sizes or DEFAULT_SIZES
    results = []
    for r in rows:
        n = r.get("n_articles") or 0
        if not n:
            continue
        gen_per_article = (r.get("total_generation_cost_usd") or 0) / n
        judge_cost_total = (r.get("judge_opus_total_cost_usd") or 0) + (r.get("judge_gpt_total_cost_usd") or 0)
        n_judged = sum(1 for k in ("judge_opus_avg_score", "judge_gpt_avg_score") if r.get(k) is not None)
        judge_per_article = (judge_cost_total / n) if n_judged else 0.0

        for size in sizes:
            gen_only = gen_per_article * size
            qa_cost = judge_per_article * size * qa_sample_rate
            results.append({
                "model": r["model"],
                "corpus_size": size,
                "gen_cost_per_article_usd": round(gen_per_article, 6),
                "generation_only_usd": round(gen_only, 2),
                "qa_sample_rate": qa_sample_rate,
                "with_qa_usd": round(gen_only + qa_cost, 2),
            })
    return results


def render_markdown(rows: list, qa_sample_rate: float = DEFAULT_QA_SAMPLE_RATE) -> str:
    lines = [
        "## Projected cost at scale",
        "",
        f"Extrapolated from this run's measured $/article; QA column assumes spot-checking "
        f"{qa_sample_rate * 100:.0f}% of production articles with both judges, not judging every one.",
        "",
        "| Model | Corpus size | $/article (generation) | Generation only | + spot-check QA |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['model']} | {row['corpus_size']:,} | ${row['gen_cost_per_article_usd']:.5f} | "
            f"${row['generation_only_usd']:,.2f} | ${row['with_qa_usd']:,.2f} |"
        )
    lines.append("")
    lines.append("Corpus-size columns are scenarios, not a prediction — see the module docstring in "
                 "scripts/eval/cost_projection.py for why. Get an actual candidate count before trusting one over the others.")
    return "\n".join(lines)
