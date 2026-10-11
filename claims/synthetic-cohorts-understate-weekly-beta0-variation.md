---
type: claim
title: Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point
description: Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point
id: synthetic-cohorts-understate-weekly-beta0-variation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: inoue-2026
    resource: "https://arxiv.org/abs/2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: inoue-2026-2
    resource: "https://arxiv.org/abs/2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In every cohort the real weekly β0 curve moves between 2.6 and 4.9 times as much across the term as the synthetic curve, with no overlap in coefficient-of-variation ranges. [→ Inoue 2026](#inoue-2026)
`q2 i?` The separation holds at a pre-specified data-independent threshold grid: across sixteen synthetic and sixteen real values no synthetic value reaches any real value. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265

`q2 · i?` · `design · r2`

Analysis of four annual cohorts (2022–2025, 117–120 learners each) of lower-secondary study-habit logs from ReLEAF, comparing coefficient of variation of the weekly β0 curve at a common working point ε = 0.68 (Table 2). The article reports "The two ranges do not overlap."

> "The two ranges do not overlap. In every cohort the real curve moves between 2.6 and 4.9 times as much across the term as the synthetic curve."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265

`q2 · i?` · `design · r2`

Robustness check at the pre-specified reference grid of 0.40, 0.60, 0.80 and 1.00: synthetic coefficients fall between 0.05 and 0.17 and real ones between 0.34 and 0.54, so "no synthetic value reaches any real value."

> "Across the four cohorts and the four thresholds we have sixteen synthetic values against sixteen real values, and no synthetic value reaches any real value."

## Discussion


## Related Claims
- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) — related
- [Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not](synthetic-cohorts-misplace-examination-week-structure.md) — related
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) — related
- [In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity](structural-check-calibrated-passable-separability-not-fidelity.md) — related
- [The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together](disclosed-statistics-do-not-constrain-band-week-co-occurrence.md) — related
- [The routine rule for selecting the graph threshold makes naive comparisons of β0 between two datasets invalid](rule-selected-thresholds-make-cross-dataset-beta0-comparison-invalid.md) — related
