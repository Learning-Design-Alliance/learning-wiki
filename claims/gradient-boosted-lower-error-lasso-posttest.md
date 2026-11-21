---
type: claim
title: Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores
description: Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores
id: gradient-boosted-lower-error-lasso-posttest
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

# Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the LASSO data set, the gradient boosted model has a lower mean absolute error and lower mean squared error than the ordinary least squares and mixed effects models. [→ John M. Aiken 2021](#john-m-aiken-2021)

## Evidence

### John M. Aiken 2021

John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)

`q2 · i?` · `theoretical · r3`

Out-of-sample evaluation of three models (OLS, mixed effects, xgboost gradient boosted) trained on the 2016-2018 LASSO data set of 6688 students across 20 institutions and 90 courses, predicting FCI/FMCE post-test scores. Table III reports mean absolute error of 0.0804 for the boosted model versus 0.0975 (OLS) and 0.111 (mixed effects), and mean squared error of 0.0152 versus 0.0200 and 0.0217.

> "Overall, the gradient boosted model has a lower mean absolute error and lower mean squared error than the linear models (Tab. III). The mixed eﬀects model has slightly better ﬁt statistics in comparison to the ordinary least squares model."

## Discussion


## Related Claims
- [OLS and hierarchical linear models over-predict post-test scores in the 30-60% range and under-predict higher scores on LASSO data](linear-models-mispredict-posttest-distribution.md) — related
- [Out-of-sample residual patterns differ across model types: OLS under-predicts low scores, and the mixed-effects model does not produce normally distributed residuals](lasso-residual-patterns-model-type.md) — related
- [A predictive model using four classroom variables accounts for 49% of the variance in concept-inventory effect sizes across 69 undergraduate science courses](copus-predictive-model-49-percent-variance.md) — related
- [Model prediction accuracy does not meaningfully vary across scientific disciplines, and shows no significant overfitting due to repeated instructors or institutions](prediction-accuracy-robust-discipline-instructor.md) — related
