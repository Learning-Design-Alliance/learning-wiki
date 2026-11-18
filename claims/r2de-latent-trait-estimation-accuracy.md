---
type: claim
title: "R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively"
description: "R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively"
id: r2de-latent-trait-estimation-accuracy
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
  - id: luca-benedetto-2020-2
    title: Luca Benedetto 2020 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On the held-out test questions, R2DE estimated difficulty with a MAE of 0.639, i.e. 6.39% of the difficulty range. [→ Luca Benedetto 2020](#luca-benedetto-2020)
`q2 i?` On the same test questions, R2DE estimated discrimination with a MAE of 0.329, i.e. 9.4% of the discrimination range. [→ Luca Benedetto 2020 (2)](#luca-benedetto-2020-2)

## Evidence

### Luca Benedetto 2020

Luca Benedetto, Andrea Cappelli, Roberto Turrin, and Paolo Cremonesi. 2020. R2DE: a NLP approach to estimating IRT parameters of newly generated questions. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK '20). https://doi.org/10.1145/3375462.3375517

`q2 · i?` · `design · r2`

Test of R2DE's difficulty estimation on the held-out question set (DSTEST), comparing R2DE estimates with the IRT-estimated values treated as ground truth. The article reports "a MAE of 0.639 for difficulty estimation (6.39% of the whole difficulty range)".

> "Specifically, it reached a MAE of 0.639 for difficulty estimation (6.39% of the whole difficulty range) and a MAE of 0.329 for discrimination estimation (9.4% of the overall discrimination range)."

### Luca Benedetto 2020 (2)

Luca Benedetto, Andrea Cappelli, Roberto Turrin, and Paolo Cremonesi. 2020. R2DE: a NLP approach to estimating IRT parameters of newly generated questions. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK '20). https://doi.org/10.1145/3375462.3375517

`q2 · i?` · `design · r2`

Test of R2DE's discrimination estimation on the same held-out question set, compared with IRT-estimated values. The table reports RMSE, relative RMSE, MAE and relative MAE of "0.447 12.8% 0.329 9.4%".

> "Table 8: Test of discrimination estimation. RMSE Relative RMSE MAE Relative MAE 0.447 12.8% 0.329 9.4%"

## Discussion


## Related Claims
- [R2DE's relative difficulty-estimation error (8.23%) is smaller than that of recent NLP difficulty-prediction works, though this does not assure better performance across datasets](r2de-difficulty-error-smaller-than-prior-work.md) — related
- [A Random Forest regressor with question_only text encoding performed best for estimating both IRT latent traits in cross-validated model choice](r2de-random-forest-question-only-best.md) — related
- [Latent traits estimated by R2DE from question text yield performance prediction close to IRT-estimated traits and generally outperform majority prediction](r2de-performance-prediction-accuracy.md) — related
