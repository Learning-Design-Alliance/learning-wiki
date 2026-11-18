---
type: claim
title: Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model
description: Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model
id: demographic-variables-low-importance-dfw-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: jie-yang-2020
    resource: "https://doi.org/10.1103/physrevphyseducres.16.020130"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: jie-yang-2020-2
    resource: "https://doi.org/10.1103/physrevphyseducres.16.020130"
    title: "Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)"
    author: Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Model performance for minority demographic subgroups was approximately that of overall model performance, suggesting low demographic-variable importance was not an artifact of sample imbalance. [→ Jie Yang 2020](#jie-yang-2020)
`q2 i?` Variable importance plots show demographic variables were not important for predicting the DFW outcome, likely because their effect is already carried by variables such as CGPA. [→ Jie Yang 2020 (2)](#jie-yang-2020-2)

## Evidence

### Jie Yang 2020

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Sample 3 (N = 926, Hispanic-serving institution with a more diverse population) classification of demographic subgroups in the test dataset. The article reports subgroup model performance was "consistent with those obtained from Sample 1", indicating subgroup differences were not caused by low group representation.

> "Model performance metrics were consistent with those obtained from Sample 1, suggesting the low variable importance was not the result of the restricted number of underrepresented students in the sample."

### Jie Yang 2020 (2)

Jie Yang, Seth DeVore, Dona Hewagallage, Paul Miller, Qing X. Ryan, and John Stewart. (2020). Using Machine Learning to Identify the Most At-Risk Students in Physics Classes. [doi:10.1103/physrevphyseducres.16.020130](https://doi.org/10.1103/physrevphyseducres.16.020130)

`q2 · i?` · `associational · r2`

Variable importance analysis (mean decrease in DFW accuracy, precision, and overall accuracy when each variable is removed) for the Sample 2 week-2 model, shown in Fig. 1. "homework average followed by CGPA were the most important variables"; demographic variables were of low importance.

> "The variable importance plots shown in Fig. 1 show that homework average followed by CGPA were the most important variables in accurately identifying DFW students."

## Discussion


## Related Claims
- [Classification accuracy of the optimized physics-grade model varies across demographic subgroups](subgroup-variation-physics-grade-classification.md) — reports the opposite
- [Low importance of demographic variables in physics grade prediction was not caused by sample imbalance](demographic-variable-importance-not-sample-imbalance.md) — possibly the same claim (merge candidate)
- [Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women](gender-sensitivity-gap-cdf-prediction.md) — reports the opposite
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [A random forest restricted to the variable set available for Sample 3 performed more weakly, with DFW accuracy reduced by 7%, indicating richer institutional data improves classification](restricted-variable-set-reduces-dfw-accuracy-7-percent.md) — related
- [An optimized random forest classifier for physics grades used a 50% test-train split, no downsampling, and tuned decision thresholds](optimized-rf-classifier-physics-grades.md) — related
- [Downsampling improved minority-outcome sensitivity but was not adopted by the optimized classifier, and upsampling was ineffective](resampling-effects-physics-grade-classifier.md) — related
