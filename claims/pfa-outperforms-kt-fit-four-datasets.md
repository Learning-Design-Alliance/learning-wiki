---
type: claim
title: "Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large"
description: "Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large"
id: pfa-outperforms-kt-fit-four-datasets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2009
recheck_by: 2012
sources:
  - id: pavlik-jr-2009
    resource: "https://doi.org/10.3233/978-1-60750-028-5-531"
    title: "Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531"
    author: Pavlik Jr., P.I., Cen, H., Koedinger, K.R.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` PFA shows better LL, BIC, r and A' than KT 1 and KT 2 across the Physics, Geometry, Algebra and Fractions datasets. [→ Pavlik Jr. 2009](#pavlik-jr-2009)

## Evidence

### Pavlik Jr. 2009

Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531

`q2 · i?` · `associational · r2`

Model-fitting comparison of PFA against KT 1 and KT 2 on four datasets from Carnegie Learning tutors and the Andes system, with a prediction floor of 0.01 and ceiling of 0.99 applied to KT. The paper reports "the PFA model has better LL, BIC, r and A’" though differences are not large.

> "Table 3 shows the results of the comparison for several fit statistics. While the differences are not large, the PFA model has better LL, BIC, r and A’."

## Discussion


## Related Claims
- [KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA](kt-overestimates-failure-impact.md) — related
- [Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset](pfa-approaches-lfa-accuracy.md) — related
- [Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well](pfa-crossvalidation-generalizes.md) — related
- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — a broader claim this one bears on
