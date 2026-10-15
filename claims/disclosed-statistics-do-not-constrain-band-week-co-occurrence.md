---
type: claim
title: "The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together"
description: "The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together"
id: disclosed-statistics-do-not-constrain-band-week-co-occurrence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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
---

# The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The differentially private summary for the study-habit records contains no statistic constraining joint band-by-week zeros, and the entropy over weeks is invariant to permuting them. [→ Inoue 2026](#inoue-2026)
`q2 i?` The excess of all-six-band zeros over what independent bands would give exceeds one in every real cohort (1.40 to 2.57) while synthetic values fall below one in two cohorts of four. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Analysis of the platform's disclosure: the private summary comprises the proportion of zeros across the 108 band-by-week combinations and two entropies, one marginalising over weeks and one over bands, so week identity and band-week co-occurrence are unconstrained.

> "No released statistic constrains which band and which week are zero together."

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Comparison of the all-six-band zero co-occurrence ratio: the marginal zero rate is reproduced to within 3% to 13%, but the co-occurrence excess, which no released statistic constrains, differs between real and synthetic cohorts.

> "The excess of all-six-band zeros over what independent bands would give is not: it exceeds one in every real cohort, from 1.40 to 2.57, while the synthetic values run from 0.41 to 2.15 and fall below one in two cohorts of four."

## Discussion


## Related Claims
- [In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity](structural-check-calibrated-passable-separability-not-fidelity.md) — related
- [Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not](synthetic-cohorts-misplace-examination-week-structure.md) — related
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) — related
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
