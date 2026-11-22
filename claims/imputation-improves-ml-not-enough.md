---
type: claim
title: Single-mean imputation improved machine learning performance for academic performance prediction but not enough to outperform regression
description: Single-mean imputation improved machine learning performance for academic performance prediction but not enough to outperform regression
id: imputation-improves-ml-not-enough
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: froud-r-2021
    resource: "https://doi.org/10.2196/22021"
    title: "Froud R, Hansen SH, Ruud HK, Foss J, Ferguson L, Fredriksen PM. (2021). Relative Performance of Machine Learning and Linear Regression in Predicting Quality of Life and Academic Performance of School Children in Norway: Data Analysis of a Quasi-Experimental Study. Journal of Medical Internet Research. https://doi.org/10.2196/22021"
    author: Froud R, Hansen SH, Ruud HK, Foss J, Ferguson L, Fredriksen PM
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Single-mean imputation improved machine learning performance for academic performance prediction but not enough to outperform regression

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With imputation, machine learning validation R2 for academic performance rose to 9% to 14%, still below regression's 15% to 18%. [→ Froud R 2021](#froud-r-2021)

## Evidence

### Froud R 2021

Froud R, Hansen SH, Ruud HK, Foss J, Ferguson L, Fredriksen PM. (2021). Relative Performance of Machine Learning and Linear Regression in Predicting Quality of Life and Academic Performance of School Children in Norway: Data Analysis of a Quasi-Experimental Study. Journal of Medical Internet Research. https://doi.org/10.2196/22021

`q2 · i?` · `associational · r2`

Sensitivity analysis using single-mean imputation on the HOPP academic performance data (training n=962, validation n=406). The article reports that "machine learning performance improved after imputation; however, regression models outperformed machine learning" (Table 5 shows validation R2 of 0.09-0.14 for machine learning vs 0.15-0.18 for regression).

> "Table 5 shows machine learning performance improved after imputation; however, regression models outperformed machine learning."

## Discussion


## Related Claims
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — reports the opposite
- [Machine learning outperformed regression for simulated nonlinear and heteroscedastic relationships, with regression using splines performing almost as well for nonlinear data](ml-superior-nonlinear-heteroscedastic-simulations.md) — related
- [Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.](attributes-autoregression-improve-response-prediction.md) — related
