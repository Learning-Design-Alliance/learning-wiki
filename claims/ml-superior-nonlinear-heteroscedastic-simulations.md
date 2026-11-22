---
type: claim
title: Machine learning outperformed regression for simulated nonlinear and heteroscedastic relationships, with regression using splines performing almost as well for nonlinear data
description: Machine learning outperformed regression for simulated nonlinear and heteroscedastic relationships, with regression using splines performing almost as well for nonlinear data
id: ml-superior-nonlinear-heteroscedastic-simulations
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

# Machine learning outperformed regression for simulated nonlinear and heteroscedastic relationships, with regression using splines performing almost as well for nonlinear data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In simulated data, machine learning techniques beat regression for nonlinear and heteroscedastic relationships; splines nearly matched machine learning for nonlinear data. [→ Froud R 2021](#froud-r-2021)

## Evidence

### Froud R 2021

Froud R, Hansen SH, Ruud HK, Foss J, Ferguson L, Fredriksen PM. (2021). Relative Performance of Machine Learning and Linear Regression in Predicting Quality of Life and Academic Performance of School Children in Norway: Data Analysis of a Quasi-Experimental Study. Journal of Medical Internet Research. https://doi.org/10.2196/22021

`q2 · i?` · `associational · r2`

Simulation study augmenting real HOPP academic performance data with a nonlinear simulated variable (no missing data). For the nonlinear simulation, "Regression with splines explained 83% of the variance in the training set and 85% of the variance in the validation set", with machine learning models at 81% to 86% in validation.

> "Regression with splines explained 83% of the variance in the training set and 85% of the variance in the validation set. Corresponding machine learning models explained 81% to 94% of variance in the training set and 81% to 86% of the variance in the validation set, with neural network performing best."

## Discussion


## Related Claims
- [Single-mean imputation improved machine learning performance for academic performance prediction but not enough to outperform regression](imputation-improves-ml-not-enough.md) — related
- [ChatGPT's simulated lab data is heteroscedastic and unrealistic because noise scales with the magnitude of the measured value](chatgpt-simulated-data-heteroscedastic-unrealistic.md) — related
