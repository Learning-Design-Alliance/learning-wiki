---
type: claim
title: "Out-of-sample residual patterns differ across model types: OLS under-predicts low scores, and the mixed-effects model does not produce normally distributed residuals"
description: "Out-of-sample residual patterns differ across model types: OLS under-predicts low scores, and the mixed-effects model does not produce normally distributed residuals"
id: lasso-residual-patterns-model-type
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: john-m-aiken-2021
    resource: "https://doi.org/10.1103/physrevphyseducres.17.020104"
    title: "John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)"
    author: John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Out-of-sample residual patterns differ across model types: OLS under-predicts low scores, and the mixed-effects model does not produce normally distributed residuals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The ordinary least squares model under predicts low scores by a wide margin in comparison to the mixed effects model and the gradient boosted model, and the mixed effects model does not produce normally distributed residuals. [→ John M. Aiken 2021](#john-m-aiken-2021)

## Evidence

### John M. Aiken 2021

John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)

`q2 · i?` · `theoretical · r3`

Examination of out-of-sample residual plots (Fig. 4) for the three LASSO models. The Fig. 4 caption states the OLS and xgboost residuals are normally distributed with the majority within ±10 points of the true value, while "The mixed eﬀects model does not produce normally distributed residuals."

> "The ordinary least squares model under predicts low scores by a wide margin in comparison to the mixed eﬀects model and the gradient boosted model. The ordinary least squares model and the gradient boosted have larger numbers of very small residuals in the range of the most likely scores (20% to 60%)."

## Discussion


## Related Claims
- [Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores](gradient-boosted-lower-error-lasso-posttest.md) — related
- [OLS and hierarchical linear models over-predict post-test scores in the 30-60% range and under-predict higher scores on LASSO data](linear-models-mispredict-posttest-distribution.md) — related
