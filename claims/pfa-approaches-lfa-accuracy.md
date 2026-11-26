---
type: claim
title: Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset
description: Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset
id: pfa-approaches-lfa-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: mixed
newest_evidence: 2009
recheck_by: 2012
sources:
  - id: pavlik-jr-2009
    resource: "https://doi.org/10.3233/978-1-60750-028-5-531"
    title: "Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531"
    author: Pavlik Jr., P.I., Cen, H., Koedinger, K.R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LFA with a subject parameter is marginally superior in 3 of 4 datasets, while PFA ties (LL) or beats (BIC) LFA in the Fractions dataset. [→ Pavlik Jr. 2009](#pavlik-jr-2009)

## Evidence

### Pavlik Jr. 2009

Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531

`q2 · i?` · `design · r2`

Comparison of LFA ns, full LFA and PFA fit to four datasets maximizing loglikelihood. The paper reports LFA "is marginally superior in 3 of 4 datasets" while "the new PFA version ties (LL) or beats (BIC) LFA in the Fractions dataset."

> "According to Bayesian Information Criterion (BIC), and loglikelihood (LL), LFA is marginally superior in 3 of 4 datasets. While this is to be expected considering that LFA includes a subject parameter unlike the other 2 models, we can also see that the new PFA version ties (LL) or beats (BIC) LFA in the Fractions dataset."

## Discussion


## Related Claims
- [Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well](pfa-crossvalidation-generalizes.md) — related
- [Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large](pfa-outperforms-kt-fit-four-datasets.md) — related
- [KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA](kt-overestimates-failure-impact.md) — related
- [LFA finds alternative cognitive models with better statistical fit than the original Geometry Area Unit model](lfa-improves-cognitive-model-fit.md) — related
- [LFA discovered that backward application of the circle area formula is a distinct, harder skill with no transfer from forward application](lfa-circle-area-backward-separate-skill.md) — related
- [LFA-discovered cognitive models outperformed both original in-use and best hand-generated models in all eleven DataShop datasets](lfa-discovered-models-beat-hand-generated-eleven-datasets.md) — related
