---
type: claim
title: A Random Forest regressor with question_only text encoding performed best for estimating both IRT latent traits in cross-validated model choice
description: A Random Forest regressor with question_only text encoding performed best for estimating both IRT latent traits in cross-validated model choice
id: r2de-random-forest-question-only-best
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
sources:
  - id: luca-benedetto-2020
    title: Luca Benedetto 2020
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A Random Forest regressor with question_only text encoding performed best for estimating both IRT latent traits in cross-validated model choice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the preliminary model-choice experiment, the Random Forest regressor with the question_only encoding achieved the lowest error for both difficulty and discrimination estimation. [→ Luca Benedetto 2020](#luca-benedetto-2020)

## Evidence

### Luca Benedetto 2020

Luca Benedetto, Andrea Cappelli, Roberto Turrin, and Paolo Cremonesi. 2020. R2DE: a NLP approach to estimating IRT parameters of newly generated questions. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK '20). https://doi.org/10.1145/3375462.3375517

`q2 · i?` · `design · r2`

Preliminary model-choice experiment using five-fold cross validation on DSTRain over Random Forest, Decision Tree, Linear Regression and Support Vector Regression, each tested with three text encodings. The article reports that "the best performing model was the Random Forest (RF) regressor, with the input text encoded using the question_only encoding".

> "For both latent traits the best performing model was the Random Forest (RF) regressor, with the input text encoded using the question_only encoding."

## Discussion


## Related Claims
- [R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively](r2de-latent-trait-estimation-accuracy.md) — related
- [Latent traits estimated by R2DE from question text yield performance prediction close to IRT-estimated traits and generally outperform majority prediction](r2de-performance-prediction-accuracy.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
