---
type: claim
title: Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts
description: Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts
id: synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association
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

# Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Two of four cohorts agree to within a few percent on every partition descriptor; 2023 and 2024 differ more, the synthetic version being the less fragmented by 55% and 24%. [→ Inoue 2026](#inoue-2026)
`q2 i?` The correlation between proportion of weeks in the majority component and total study time is negative in every cohort and version, from -0.97 to -0.81 synthetic and -0.90 to -0.63 real. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265

`q2 · i?` · `design · r2`

Table 1 reports mean weekly β0 relative to cohort size, isolated fraction, and component concentration at the common working point; on these quantities alone "a reader would have no reason to doubt the synthetic cohorts in at least half the years."

> "Two of the four cohorts agree to within a few percent on every column. The other two differ more: in 2023 the synthetic version is the less fragmented of the pair by 55%, and in 2024 by 24%."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265

`q2 · i?` · `design · r2`

Per-learner Spearman correlation using no outcome labels: negative in every cohort and version, with synthetic values the stronger of each pair in three of four cohorts, but sign and order of magnitude carry over.

> "Correlating, across learners, the proportion of weeks a learner spends in the majority component against that learner's total study time gives a negative coefficient in every cohort and every version, from -0.97 to -0.81 in the synthetic data and from -0.90 to -0.63 in the real data."

## Discussion


## Related Claims
- [Outcome turns on the structural location the synthetic position occupies, not the volume of use; population-level studies indexing use alone should record a washed-out average effect](structural-location-moderates-not-volume.md) — related
- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) — related
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
- [The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together](disclosed-statistics-do-not-constrain-band-week-co-occurrence.md) — related
