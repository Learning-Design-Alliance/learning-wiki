---
type: claim
title: In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity
description: In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity
id: structural-check-calibrated-passable-separability-not-fidelity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: inoue-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: inoue-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: inoue-2026-3
    resource: "https://doi.org/10.48550/arxiv.2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Over twenty-four replications the column-permuted synthetic version produced test statistics spread across the interval, consistent with uniformity, showing the check is calibrated. [→ Inoue 2026](#inoue-2026)
`q2 i?` A Gaussian copula version passes the check, with coefficient of variation within 3.5% of the real one in all four OULAD presentations. [→ Inoue 2026 (2)](#inoue-2026-2)
`q2 i?` A multivariate normal version separated from its own surrogates more sharply than the real data in every presentation while misstating β0 level and variation, showing separability is not fidelity. [→ Inoue 2026 (3)](#inoue-2026-3)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Control experiment on four OULAD presentations (376 to 2,049 learners over thirty-nine weeks): the column-permuted synthetic version, a draw from the null, yields uniformly distributed statistics, so "the check is calibrated rather than merely permissive."

> "Over twenty-four replications the column-permuted version produced test statistics spread across the interval, from 0.010 to 0.860 with a mean of 0.537, and a test of uniformity does not reject."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Of three synthetic versions built from OULAD (column-permuted, multivariate normal, Gaussian copula), only the copula, which preserves the rank correlation of the learner trajectory, recovers the weekly β0 variation: "its coefficient of variation lands within 3.5% of the real one."

> "Only the copula reproduces the weekly values themselves: its coefficient of variation lands within 3.5% of the real one in all four presentations, with mean β0 within 6%."

### Inoue 2026 (3)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

The multivariate normal synthetic version was highly distinguishable from its own marginals yet "a poor description of the cohort", misstating β0 level by 28% to 143% and variation by 14% to 38%, establishing that separability is not a measure of fidelity.

> "The multivariate normal version separated from its own surrogates more sharply than the real data did in every presentation, by as much as a factor of two, while misstating the level of β0 by between 28% and 143% and its variation by between 14% and 38%."

## Discussion


## Related Claims
- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) — related
- [The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together](disclosed-statistics-do-not-constrain-band-week-co-occurrence.md) — related
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
- [Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not](synthetic-cohorts-misplace-examination-week-structure.md) — related
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) — related
