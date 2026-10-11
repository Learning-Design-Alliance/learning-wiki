---
type: claim
title: "Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation"
description: "Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation"
id: ensemble-majority-vote-modest-gains-no-degradation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: schroeder-2026
    resource: "https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark"
    title: "Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C. (2026). A Benchmark for LLM's Understanding of Middle School and High School Science. https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark"
    author: "Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Ensemble majority-vote scoring across three runs increased benchmark accuracy by 1% to 5% and caused no score degradation for any model. [→ Schroeder 2026](#schroeder-2026)

## Evidence

### Schroeder 2026

Schroeder, N. L., Ambarwati, Y. E., Zhang, Y., & Zhai, C. (2026). A Benchmark for LLM's Understanding of Middle School and High School Science. https://github.com/InviteInstitute/MS-NGSS-Aligned-Benchmark

`q2 · i?` · `design · r2`

Benchmarking results (Part II, RQ1) comparing single-shot versus ensemble accuracy for all nine models on both benchmarks. The article reports gains "from 1% to 5%" and no degradation; ensemble scores served as a measure of model self-consistency.

> "Using majority-vote ensemble methods did not cause drastic improvements in scores on either benchmark, with increases from 1% to 5% being observed. We did not observe any model score degradation from using ensemble methods."

## Discussion


## Related Claims
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — reports the opposite
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — a broader claim this one bears on
- [Model self-confidence, weighted probabilistic scoring, and ensemble modeling each significantly improve LLM-based divergent thinking scoring, raising correlation with human judges from r = 0.781 to r = 0.823](llm-scoring-three-techniques-raise-human-judge-correlation.md) — a broader claim this one bears on
- [Among remnant data types, the combined ensemble model reduced sampling variance most, the action-level model least, and the assignment-level model performed nearly as well as the combined model](remnant-data-type-contribution-variance.md) — related
- [Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects](rater-ensembles-outperform-llms-feedback.md) — related
