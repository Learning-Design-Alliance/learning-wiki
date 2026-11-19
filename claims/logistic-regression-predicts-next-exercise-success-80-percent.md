---
type: claim
title: "A logistic regression model using topic success and topic skip features predicts next-exercise success with 80% accuracy"
description: "A logistic regression model using topic success and topic skip features predicts next-exercise success with 80% accuracy"
id: logistic-regression-predicts-next-exercise-success-80-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: elkins-2022
    resource: "https://doi.org/10.1007/978-3-031-11647-6_121"
    title: "Elkins, S., Belfer, R., Kochmar, E., Serban, I., and Cheung, J.C.K. (2022). Question Personalization in an Intelligent Tutoring System. [doi:10.1007/978-3-031-11647-6_121](https://doi.org/10.1007/978-3-031-11647-6_121)"
    author: Elkins, S., Belfer, R., Kochmar, E., Serban, I., and Cheung, J.C.K.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A logistic regression model using topic success and topic skip features predicts next-exercise success with 80% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly
> **Design limits** · Elkins 2022: no comparison group (read from the study by two models, 2026-11-19)

## Subclaims
`q2 i?` Using two features (topic success and topic skip rates per previously attempted exercises in a topic), a logistic regression model predicts whether a student will succeed on the next exercise with 80% accuracy. [→ Elkins 2022](#elkins-2022)

## Evidence

### Elkins 2022

Elkins, S., Belfer, R., Kochmar, E., Serban, I., and Cheung, J.C.K. (2022). Question Personalization in an Intelligent Tutoring System. [doi:10.1007/978-3-031-11647-6_121](https://doi.org/10.1007/978-3-031-11647-6_121)

`q2 · i?` · `causal · r1`

Model-building analysis of 2,137 students' interactions and 13,504 exercises on the Korbit platform. From an original 7-feature set, two features were selected based on preliminary experiments: topic success feature and topic skip feature, each in [0, 1]. Accuracy of 80% is printed; no other effect size is reported.

> "Using these features the model is able to predict next exercise success with an accuracy of80%."

## Discussion


## Related Claims
- [A logistic regression exercise affinity model predicted exercise outcomes with 66% cross-validated accuracy, above a 60% majority-class baseline, and was used to simulate unattempted exercises for bandit pre-training](exercise-affinity-model-66-percent-accuracy.md) — related
- [Expert-designed knowledge-component models add little to the accuracy of logistic-regression learner models on most tutoring datasets](expert-kc-models-add-little-to-performance-prediction.md) — related
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — related
- [Logistic regression on the first 60% of a student's design action sequence predicts zero-net-energy design success with greater than 60% accuracy](early-design-action-sequences-predict-cad-success.md) — related
- [Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses](multivariate-features-improve-accuracy-over-eda-only-benchmark.md) — related
