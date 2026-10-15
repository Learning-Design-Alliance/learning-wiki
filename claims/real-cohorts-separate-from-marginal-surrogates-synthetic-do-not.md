---
type: claim
title: Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not
description: Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not
id: real-cohorts-separate-from-marginal-surrogates-synthetic-do-not
status: draft
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
    resource: "https://arxiv.org/abs/2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265"
    author: "Inoue, H., & Yasutake, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Every real cohort separates from 200 within-week column-permuted surrogates, with standardised positions of 3.77, 3.87, 6.36 and 7.81. [→ Inoue 2026](#inoue-2026)
`q2 i?` Three of the four synthetic cohorts do not separate from their own surrogates; only the 2025 synthetic cohort separates. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Permutation test on the four real study-habit cohorts: 200 surrogates constructed by permuting each feature column independently within each week, preserving weekly marginals exactly. "no surrogate lies further from the swarm than the observed curve" in all four years.

> "At the common working point every real cohort separates: no surrogate lies further from the swarm than the observed curve, in all four years, with standardised positions of 3.77, 3.87, 6.36 and 7.81."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265

`q2 · i?` · `design · r2`

Same permutation test applied to the synthetic versions under identical code: three return proportions of 0.800, 0.05 and 0.09, meaning the observed curve lies inside the surrogate swarm; only 2025 separates. This comparison "needs no real data."

> "Three of the four synthetic cohorts do not, returning 0.800, 0.05 and 0.09 at positions of -0.92, 1.78 and 1.47; the 2025 synthetic cohort separates at 3.70."

## Discussion


## Related Claims
- [In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity](structural-check-calibrated-passable-separability-not-fidelity.md) — related
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
- [Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not](synthetic-cohorts-misplace-examination-week-structure.md) — related
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) — related
