---
type: claim
title: Machine learning techniques showed high training-set variance explained but near-zero validation performance, indicating overfitting for continuous outcomes
description: Machine learning techniques showed high training-set variance explained but near-zero validation performance, indicating overfitting for continuous outcomes
id: ml-overfitting-continuous-health-outcomes
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

# Machine learning techniques showed high training-set variance explained but near-zero validation performance, indicating overfitting for continuous outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Machine learning models explained up to 63% of training variance but approximately 0% of validation variance for academic performance. [→ Froud R 2021](#froud-r-2021)

## Evidence

### Froud R 2021

Froud R, Hansen SH, Ruud HK, Foss J, Ferguson L, Fredriksen PM. (2021). Relative Performance of Machine Learning and Linear Regression in Predicting Quality of Life and Academic Performance of School Children in Norway: Data Analysis of a Quasi-Experimental Study. Journal of Medical Internet Research. https://doi.org/10.2196/22021

`q2 · i?` · `associational · r2`

Complete-case analysis of HOPP data (training n=962, validation n=406 per Table 3) comparing random forest, support vector machine, k-nearest neighbors, and neural network against regression. Models showed "between 13% and 63% of the variance in the training set and approximately 0% of the variance in validation".

> "Machine learning models explained between 13% and 63% of the variance in the training set and approximately 0% of the variance in validation (Table 3)."

## Discussion


## Related Claims
- [The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.](overfitting-from-small-labeled-set-and-high-dimensionality.md) — possibly the same claim (merge candidate)
