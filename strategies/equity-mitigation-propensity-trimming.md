---
type: strategy
id: equity-mitigation-propensity-trimming
title: Mitigate equity risk from propensity-based trimming by reporting subgroup trimming rates, varying cutoffs, and excluding protected variables from the treatment model
description: "The article warns that statistical cutoff constraints can encode inequity: if students from historically underserved groups rarely take Calculus, a propensity model \"assigns low probability and therefore marks Calculu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: chenguang-pan-2026
    resource: "https://arxiv.org/abs/2610.10843"
    title: "Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. https://arxiv.org/abs/2610.10843"
    author: Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk
---

# Mitigate equity risk from propensity-based trimming by reporting subgroup trimming rates, varying cutoffs, and excluding protected variables from the treatment model

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article warns that statistical cutoff constraints can encode inequity: if students from historically underserved groups rarely take Calculus, a propensity model "assigns low probability and therefore marks Calculus infeasible for them, so that the regime never recommends it". It proposes several mitigation strategies: report who gets trimmed based on sensitive variables like race/ethnicity, socioeconomic quartile, or school locale; vary the cutoff and report changes across these groups; and exclude protected variables from the treatment model while retaining them in the outcome model if fairness is a serious concern.

## Design Implications

### Context
#### Requirements
- Reporting of trimming rates by sensitive subgroups such as race/ethnicity, socioeconomic quartile, or school locale
#### Constraints
- Excluding protected variables from the treatment model may reintroduce confounding bias since the fitted propensity model no longer conditions on all variables

### Target Learners
- high school students
- students from historically underserved groups

### Target Learning Goals
- equitable course placement recommendations

## Claims

- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](../claims/ews-and-algorithm-less-accurate-black-students.md) [+W]

## Related Strategies

- [Match statistical control methods to variable structure and measurement quality, preferring stratification, covariate adjustment, matching, or regression discontinuity accordingly](statistical-control-method-selection-strategy.md)
- [Use post hoc interpretation tools (ALE and fANOVA, or SHAP) across three layers to explain ML-based regime recommendations to families and administrators](interpretability-layers-ale-fanova.md)

## Examples
-

## Key Sources
- Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. https://arxiv.org/abs/2610.10843
