---
type: claim
title: "R2DE's relative difficulty-estimation error (8.23%) is smaller than that of recent NLP difficulty-prediction works, though this does not assure better performance across datasets"
description: "R2DE's relative difficulty-estimation error (8.23%) is smaller than that of recent NLP difficulty-prediction works, though this does not assure better performance across datasets"
id: r2de-difficulty-error-smaller-than-prior-work
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: mixed
sources:
  - id: luca-benedetto-2020
    title: Luca Benedetto 2020
    q: 2
    i: "?"
---

# R2DE's relative difficulty-estimation error (8.23%) is smaller than that of recent NLP difficulty-prediction works, though this does not assure better performance across datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The relative RMSE for difficulty estimation reported for R2DE (8.23%) is smaller than the relative errors reported by Huang et al. (21%) and Yaneva et al. (22.4%), each on a different private dataset and difficulty range. [→ Luca Benedetto 2020](#luca-benedetto-2020)

## Evidence

### Luca Benedetto 2020

Luca Benedetto, Andrea Cappelli, Roberto Turrin, and Paolo Cremonesi. 2020. R2DE: a NLP approach to estimating IRT parameters of newly generated questions. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK '20). https://doi.org/10.1145/3375462.3375517

`q2 · i?`

Comparison of relative difficulty-estimation error against recent NLP difficulty-prediction works, each evaluated on its own private dataset and difficulty range. The table reports R2DE at "[-5; 5] 0.823 8.23%" versus "[0; 1] 0.21 21%" and "[0; 100] 22.45 22.4%".

> "Table 9: Comparison with state of the art. Paper Difficulty range RMSE Relative RMSE R2DE [-5; 5] 0.823 8.23% Huang et al. [11] [0; 1] 0.21 21% Yaneva et al. [29] [0; 100] 22.45 22.4%"

## Discussion


## Related Claims
- [R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively](r2de-latent-trait-estimation-accuracy.md) — related
- [In reviewed studies, word embeddings and linguistic features were the strongest difficulty predictors, with combined features giving the best results (RMSE 22.45 vs ZeroR 23.65)](embeddings-linguistic-features-strongest-predictors.md) — related
- [Latent traits estimated by R2DE from question text yield performance prediction close to IRT-estimated traits and generally outperform majority prediction](r2de-performance-prediction-accuracy.md) — related
