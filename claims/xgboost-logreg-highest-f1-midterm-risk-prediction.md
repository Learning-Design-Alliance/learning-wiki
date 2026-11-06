---
type: claim
title: XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91
description: XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91
id: xgboost-logreg-highest-f1-midterm-risk-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: al-hashmi-reem-a-m-2025
    resource: "https://doi.org/10.1186/s12909-025-08192-6"
    title: "Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M. (2025). Early detection of at-risk health sciences students: a machine learning-based predictive study using midterm grades. BMC Medical Education. https://doi.org/10.1186/s12909-025-08192-6"
    author: Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` XGBoost and Logistic Regression recorded the top F1-Scores (0.84) and AUC values above 0.91 in predicting at-risk status from midterm grades and demographics. [→ Al Hashmi Reem A. M. 2025](#al-hashmi-reem-a-m-2025)

## Evidence

### Al Hashmi Reem A. M. 2025

Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M. (2025). Early detection of at-risk health sciences students: a machine learning-based predictive study using midterm grades. BMC Medical Education. https://doi.org/10.1186/s12909-025-08192-6

`q2 · i?` · `associational · r2`

Predictive modeling study of 346 first-year UAE health sciences students, five supervised classifiers trained on ROSE-balanced data with 5-fold cross-validation and a 30% hold-out test set. XGBoost and Logistic Regression both reached F1 = 0.84; Random Forest had the highest AUC (0.933).

> "While Random Forest achieved the highest AUC (0.933), both XGBoost and Logistic Regression recorded the top F1-Scores (0.84), indicating a stronger balance between false positives and false negatives, critical for early risk identification."

## Discussion


## Related Claims
- [Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision](recall-precision-tradeoff-early-warning-models.md) — related
- [A 10-point decrease in Biology midterm score raises predicted at-risk probability by about 31 percentage points, with smaller effects for Introduction to Health Sciences (~25) and English (~18)](ten-point-biology-decline-raises-risk-31-points.md) — related
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — reports the opposite
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — reports the opposite
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
