---
type: claim
title: Low importance of demographic variables in physics grade prediction was not caused by sample imbalance
description: Low importance of demographic variables in physics grade prediction was not caused by sample imbalance
id: demographic-variable-importance-not-sample-imbalance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: seth-devore-2020
    resource: "https://doi.org/10.48550/arXiv.2002.01964"
    title: "Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)"
    author: Seth DeVore, Jie Yang, and John Stewart
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Low importance of demographic variables in physics grade prediction was not caused by sample imbalance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Downsampling analyses showed that the low variable importance of gender, URM status, and first-generation status in Study 1 did not result from underrepresentation of these students. [→ Seth DeVore 2020](#seth-devore-2020)

## Evidence

### Seth DeVore 2020

Seth DeVore, Jie Yang, and John Stewart. (2020). Extending Machine Learning to Predict Unbalanced Physics Course Outcomes. [doi:10.48550/arXiv.2002.01964](https://doi.org/10.48550/arXiv.2002.01964)

`q2 · i?` · `associational · r2`

Bootstrap analysis varying downsampling levels for each dichotomous independent variable (Gender, URM, FirstGen, CalReady), with sensitivity plots for models including and excluding each variable. The authors found model performance was "fairly insensitive to the level of downsampling", ruling out underrepresentation as the cause of low demographic variable importance.

> "As such, the conclusions about the low importance of demographic variables in Study 1 (gender, underrepresented minority status, and ﬁrst generation status) in predicting physics grade were not the result of the imbalance of the sample."

## Discussion


## Related Claims
- [Students with minoritized identities earned lower overall lab grades regardless of group formation: women lower than men, URM students lower than non-URM, and first-generation students lower than continuing-generation](demographic-disparities-overall-lab-grades.md) — related
- [Undergraduate women earned slightly but significantly higher course grades than men in both life and physical science STEM courses](women-higher-course-grades-stem-courses.md) — related
- [Model sensitivity for predicting CDF physics outcomes is about 10% higher for men than for women](gender-sensitivity-gap-cdf-prediction.md) — related
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](demographic-variables-low-importance-dfw-models.md) — possibly the same claim (merge candidate)
