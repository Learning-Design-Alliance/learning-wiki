---
type: claim
title: "Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not"
description: "Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not"
id: synthetic-cohorts-misplace-examination-week-structure
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
---

# Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In every cohort the synthetic mean study time is higher in that year's own examination week and among the two highest of the eighteen, while in the real cohorts the mid-term week ranks ninth to fifteenth. [→ Inoue 2026](#inoue-2026)
`q2 i?` The Spearman rank correlation between real and synthetic weekly β0 curves runs from -0.22 to 0.57. [→ Inoue 2026 (2)](#inoue-2026-2)

## Evidence

### Inoue 2026

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265 [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Comparison of weekly mean study time placement across the four cohort pairs. The synthetic cohorts track a year-specific detail of the generator's documentation; "The real cohorts are not" so placed, and in two cohorts fall below the mean of the rest.

> "The mid-term examination falls in week 22 in 2022 and in week 23 in the other three years, and in every cohort the synthetic mean study time is higher in that year's own examination week, and among the two highest of the eighteen. The real cohorts are not: there the mid-term week ranks ninth to fifteenth"

### Inoue 2026 (2)

Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)

`q2 · i?` · `design · r2`

Rank correlation between real and synthetic weekly β0 curves across the four cohorts, ranging from -0.22 to 0.57, indicating the synthetic curves do not reproduce where in the term the real variation falls.

> "The synthetic cohorts therefore miss not only the size of the week-to-week movement but also its placement, and the Spearman rank correlation between the real and synthetic weekly β0 curves runs from -0.22 to 0.57."

## Discussion


## Related Claims
- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) — related
- [The variation gap traces to what the generator was disclosed: no released statistic constrains which band and which week are zero together](disclosed-statistics-do-not-constrain-band-week-co-occurrence.md) — related
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](synthetic-cohorts-understate-weekly-beta0-variation.md) — related
