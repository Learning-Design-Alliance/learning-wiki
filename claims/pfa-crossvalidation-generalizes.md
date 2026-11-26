---
type: claim
title: "Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well"
description: "Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well"
id: pfa-crossvalidation-generalizes
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

# Despite BIC suggesting overfitting, PFA's 7-fold crossvalidated mean absolute deviation shows it generalizes well

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The 7-fold crossvalidation MAD indicates PFA generalizes well despite higher BIC values. [→ Pavlik Jr. 2009](#pavlik-jr-2009)

## Evidence

### Pavlik Jr. 2009

Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531

`q2 · i?` · `associational · r2`

Crossvalidation analysis in the LFA/PFA model comparison section: BIC suggested overfitting relative to the other models, but "the mean absolute deviation for a 7-fold crossvalidation (MAD CV) shows the model generalizes well."

> "Although the BIC values suggest overfitting relative to the other models, the mean absolute deviation for a 7-fold crossvalidation (MAD CV) shows the model generalizes well."

## Discussion


## Related Claims
- [Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset](pfa-approaches-lfa-accuracy.md) — related
- [PFA models overfit blocked-sequence learning-session accuracy and predict the posttest poorly, motivating AFM-based attentional modeling](pfa-overfits-learning-session-posttest-bias.md) — reports the opposite
- [The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.](overfitting-from-small-labeled-set-and-high-dimensionality.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large](pfa-outperforms-kt-fit-four-datasets.md) — related
