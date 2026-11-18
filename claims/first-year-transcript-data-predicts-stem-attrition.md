---
type: claim
title: STEM attrition is predictable from first-year registrar transcript data, with four ML models reaching AUROCs between 0.87 and 0.89 and logistic regression performing slightly better
description: STEM attrition is predictable from first-year registrar transcript data, with four ML models reaching AUROCs between 0.87 and 0.89 and logistic regression performing slightly better
id: first-year-transcript-data-predicts-stem-attrition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
sources:
  - id: lovenoor-aulck-2017
    title: Lovenoor Aulck 2017
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: lovenoor-aulck-2017-2
    title: Lovenoor Aulck 2017 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# STEM attrition is predictable from first-year registrar transcript data, with four ML models reaching AUROCs between 0.87 and 0.89 and logistic regression performing slightly better

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Four supervised ML models predicted STEM graduation from first-year records with similar performance (AUROCs 0.87-0.89; F1 0.80-0.82), logistic regression slightly best. [→ Lovenoor Aulck 2017](#lovenoor-aulck-2017)
`q2 i?` The authors characterize the predictions as about a 30 percentage point accuracy increase over baseline proportions. [→ Lovenoor Aulck 2017 (2)](#lovenoor-aulck-2017-2)

## Evidence

### Lovenoor Aulck 2017

Lovenoor Aulck, Rohan Aras, Lysia Li, Coulter L'Heureux, Peter Lu, Jevin D. West. 2017. STEM-ming the Tide: Predicting STEM attrition using student transcript data. In Proceedings of Machine Learning for Education (ml4ed) Workshop at ACM Knowledge Discovery and Data Mining Conference, Halifax, Nova Scotia, Canada, August 2017 (KDD'17). https://doi.org/10.475/123_4

`q2 · i?` · `associational · r2`

Supervised ML experiments predicting STEM graduation from first-year registrar records of STEM-intending students compared four models; performance was similar, with "AUROCs between 0.87 and 0.89, F1 scores between 0.80 and 0.82", and logistic regression "performing slightly better than the other models".

> "In all, model performance was similar across all models (AUROCs between 0.87 and 0.89, F1 scores between 0.80 and 0.82), with logistic regression performing slightly better than the other models."

### Lovenoor Aulck 2017 (2)

Lovenoor Aulck, Rohan Aras, Lysia Li, Coulter L'Heureux, Peter Lu, Jevin D. West. 2017. STEM-ming the Tide: Predicting STEM attrition using student transcript data. In Proceedings of Machine Learning for Education (ml4ed) Workshop at ACM Knowledge Discovery and Data Mining Conference, Halifax, Nova Scotia, Canada, August 2017 (KDD'17). https://doi.org/10.475/123_4

`q2 · i?` · `associational · r2`

The conclusions section summarizes the supervised prediction results as "promising results with about a 30 percentage point increase in accuracy over the baseline proportions", using only data mined from university registrar databases.

> "The predictions yielded promising results with about a 30 percentage point increase in accuracy over the baseline proportions."

## Discussion


## Related Claims
- [XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91](xgboost-logreg-highest-f1-midterm-risk-prediction.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — reports the opposite
- [Performance in math courses supplies five of the ten best single predictors of STEM attrition, including the four most predictive](math-course-performance-top-single-predictor.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
