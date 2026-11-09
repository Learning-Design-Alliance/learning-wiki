---
type: claim
title: "A logistic regression model using SNA indicators classifies high versus low achievers with 93.3% accuracy (AUC 0.92) in the study dataset"
description: "A logistic regression model using SNA indicators classifies high versus low achievers with 93.3% accuracy (AUC 0.92) in the study dataset"
id: logistic-regression-classifies-achievement-93-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-09
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: saqr-m-2018
    resource: "https://doi.org/10.1371/journal.pone.0203590"
    title: "Saqr M, Fors U, Nouri J. (2018). Using social network analysis to understand online Problem-Based Learning and predict performance. PLoS ONE 13(9): e0203590. https://doi.org/10.1371/journal.pone.0203590"
    author: Saqr M, Fors U, Nouri J.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A logistic regression model using SNA indicators classifies high versus low achievers with 93.3% accuracy (AUC 0.92) in the study dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Stepwise backward logistic regression on SNA indicators classified 93.3% of cases correctly (88.24% of low achievers, 96.06% of high achievers; F-measure 90%, AUC 0.92). [→ Saqr M 2018](#saqr-m-2018)

## Evidence

### Saqr M 2018

Saqr M, Fors U, Nouri J. (2018). Using social network analysis to understand online Problem-Based Learning and predict performance. PLoS ONE 13(9): e0203590. https://doi.org/10.1371/journal.pone.0203590

`q2 · i?` · `associational · r2`

Predictive logistic regression (Rapidminer, Table 6) on 215 students, with bottom and top thirds labelled low and high achievers. Nagelkerke R Square was 0.84 and the Hosmer-Lemeshow test indicated no evidence of poor fit.

> "The model successfully classified 93.3% of cases, 88.24% of the low achievers, and 96.06% of the high achievers. The F-measure was 90%, and AUC was 0.92, full confusion matrix results are tabulated in Table 6."

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Random Forest is the best-performing classification model for predicting postgraduate public health students' CGPA category, with 71.43% accuracy and AUC 0.87](random-forest-best-classifier-ap.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
