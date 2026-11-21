---
type: claim
title: Model prediction accuracy does not meaningfully vary across scientific disciplines, and shows no significant overfitting due to repeated instructors or institutions
description: Model prediction accuracy does not meaningfully vary across scientific disciplines, and shows no significant overfitting due to repeated instructors or institutions
id: prediction-accuracy-robust-discipline-instructor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: olive-ross-2026
    resource: "https://doi.org/10.21203/rs.3.rs-9955835/v1"
    title: "Olive Ross, Meagan Sundstrom and N.G. Holmes. (2026). Predictive Modeling for High Impact Active Learning Classrooms. arXiv. [doi:10.21203/rs.3.rs-9955835/v1](https://doi.org/10.21203/rs.3.rs-9955835/v1)"
    author: Olive Ross, Meagan Sundstrom and N.G. Holmes
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: olive-ross-2026-2
    resource: "https://doi.org/10.21203/rs.3.rs-9955835/v1"
    title: "Olive Ross, Meagan Sundstrom and N.G. Holmes. (2026). Predictive Modeling for High Impact Active Learning Classrooms. arXiv. [doi:10.21203/rs.3.rs-9955835/v1](https://doi.org/10.21203/rs.3.rs-9955835/v1)"
    author: Olive Ross, Meagan Sundstrom and N.G. Holmes
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Model prediction accuracy does not meaningfully vary across scientific disciplines, and shows no significant overfitting due to repeated instructors or institutions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean absolute errors on reliable predictions are 0.24, 0.29, and 0.26 for physics, biology, and astronomy respectively, indicating prediction accuracy is not meaningfully impacted by discipline. [→ Olive Ross 2026](#olive-ross-2026)
`q2 i?` LOO tests on classes with unique instructors and institutions yield MAE of 0.30, comparable to the full dataset, indicating no significant overfitting due to repeated instructors or institutions. [→ Olive Ross 2026 (2)](#olive-ross-2026-2)

## Evidence

### Olive Ross 2026

Olive Ross, Meagan Sundstrom and N.G. Holmes. (2026). Predictive Modeling for High Impact Active Learning Classrooms. arXiv. [doi:10.21203/rs.3.rs-9955835/v1](https://doi.org/10.21203/rs.3.rs-9955835/v1)

`q2 · i?` · `associational · r2`

Leave-one-out tests distinguishing fields (Fig. 7), with unreliable predictions removed. The article also reports higher error for classes under 50 students (0.33), attributed to higher variance in small classes.

> "the mean absolute errors on predictions are 0.24, 0.29, and 0.26 for physics, biology, and astronomy respectively, indicating that prediction accuracy is not meaningfully impacted by discipline"

### Olive Ross 2026 (2)

Olive Ross, Meagan Sundstrom and N.G. Holmes. (2026). Predictive Modeling for High Impact Active Learning Classrooms. arXiv. [doi:10.21203/rs.3.rs-9955835/v1](https://doi.org/10.21203/rs.3.rs-9955835/v1)

`q2 · i?` · `associational · r2`

LOO tests restricted to classes whose institutions and instructors are not repeated in the dataset (Fig. 8), checking for overfitting from repeated underlying variables.

> "The LOO MAE on reliable predictions for this set is 0.30, which is comparable to the analogous value in the full dataset. This indicates that there is no significant overfitting occurring due to repeated instructors or institutions."

## Discussion


## Related Claims
- [Gradient boosted models achieve lower out-of-sample mean absolute and mean squared error than OLS and mixed-effects models when predicting LASSO concept-inventory post-test scores](gradient-boosted-lower-error-lasso-posttest.md) — related
- [On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits](real-data-prediction-baseline-captures-most-gain.md) — related
