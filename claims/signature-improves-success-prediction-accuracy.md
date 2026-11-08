---
type: claim
title: "Adding signature classification as a feature improves success prediction accuracy from 36.8% to 44.2% on the test group"
description: "Adding signature classification as a feature improves success prediction accuracy from 36.8% to 44.2% on the test group"
id: signature-improves-success-prediction-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: baron-tal-2020
    resource: "https://doi.org/10.1371/journal.pone.0227108"
    title: "Baron Tal, Grossman Robert I., Abramson Steven B., Pusic Martin V., Rivera Rafael, Triola Marc M., Yanai Itai. (2020). Signatures of medical student applicants and academic success. PLoS ONE. https://doi.org/10.1371/journal.pone.0227108"
    author: Baron Tal, Grossman Robert I., Abramson Steven B., Pusic Martin V., Rivera Rafael, Triola Marc M., Yanai Itai
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Adding signature classification as a feature improves success prediction accuracy from 36.8% to 44.2% on the test group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A logistic regression model including the signature as a feature fits significantly better (likelihood-ratio test P < 0.001) and predicts the three-level success score more accurately on the held-out test group. [→ Baron Tal 2020](#baron-tal-2020)

## Evidence

### Baron Tal 2020

Baron Tal, Grossman Robert I., Abramson Steven B., Pusic Martin V., Rivera Rafael, Triola Marc M., Yanai Itai. (2020). Signatures of medical student applicants and academic success. PLoS ONE. https://doi.org/10.1371/journal.pone.0227108

`q2 · i?` · `associational · r2`

Test-group evaluation on 95 students: a base logistic regression on 40 binary features versus one adding signature assignment; model comparison by LR test on training data (P < 0.001). No effect size is printed.

> "the model that included the signature as a feature showed improved accuracy in predicting the three-level success score from 36.8% to 44.2% (Fig 4a)."

## Discussion


## Related Claims
- [Prediction accuracy improves in three of four signatures but not for the risers signature](prediction-improves-three-signatures-not-risers.md) — related
- [Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model](small-gain-from-question-level-features.md) — related
- [Each signature has a unique set of features correlating with success in medical school](signature-specific-success-predictors.md) — related
