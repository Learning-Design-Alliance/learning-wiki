---
type: research-method
id: r2de-regressor-for-difficulty-and-discrimination-estimation
title: R2DE (Regressor for Difficulty and Discrimination Estimation)
description: R2DE (Regressor for Difficulty and Discrimination Estimation) is a model that estimates the two-parameter IRT latent traits of multiple-choice questions from text, addressing the cold-start problem for newly generated items.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# R2DE (Regressor for Difficulty and Discrimination Estimation)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size

## Description
R2DE (Regressor for Difficulty and Discrimination Estimation) is a model that estimates the two-parameter IRT latent traits of multiple-choice questions from text, addressing the cold-start problem for newly generated items. It builds an input text per question under three encodings (question_only, question_correct, question_full), applies NLP preprocessing and TF-IDF, keeps the NW most frequent keywords, and "contains two regressors that work in parallel to estimate i) the difficulty and ii) the discrimination of multi-choice questions".

## Accounts
<!-- How each source describes or uses the method -->
- **R2DE: a regressor estimating IRT difficulty and discrimination of multiple-choice questions from text**: R2DE (Regressor for Difficulty and Discrimination Estimation) is a model that estimates the two-parameter IRT latent traits of multiple-choice questions from text, addressing the cold-start problem for newly generated items. It builds an input text per question under three encodings (question_only, question_correct, question_full), applies NLP preprocessing and TF-IDF, keeps the NW most frequent keywords, and "contains two regressors that work in parallel to estimate i) the difficulty and ii) the discrimination of multi-choice questions". (R2DE: a NLP approach to estimating IRT parameters of newly generated questions)

### Claims
- [R2DE estimates the IRT difficulty and discrimination of unseen multiple-choice questions from text with a relative MAE of 6.39% and 9.4% respectively](../claims/r2de-latent-trait-estimation-accuracy.md) [+M]
- [Latent traits estimated by R2DE from question text yield performance prediction close to IRT-estimated traits and generally outperform majority prediction](../claims/r2de-performance-prediction-accuracy.md) [+M]

## Related Research Methods
-

## Key Sources
- Luca Benedetto, Andrea Cappelli, Roberto Turrin, and Paolo Cremonesi. 2020. R2DE: a NLP approach to estimating IRT parameters of newly generated questions. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (LAK '20). https://doi.org/10.1145/3375462.3375517
