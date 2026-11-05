---
type: claim
title: "Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision"
description: "Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision"
id: recall-precision-tradeoff-early-warning-models
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

# Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Logistic Regression achieved the highest recall (0.94) but generated more false positives, whereas XGBoost combined high recall with stronger precision. [→ Al Hashmi Reem A. M. 2025](#al-hashmi-reem-a-m-2025)

## Evidence

### Al Hashmi Reem A. M. 2025

Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M. (2025). Early detection of at-risk health sciences students: a machine learning-based predictive study using midterm grades. BMC Medical Education. https://doi.org/10.1186/s12909-025-08192-6

`q2 · i?` · `associational · r2`

Comparative evaluation of the five trained classifiers on the hold-out test set, with confusion matrices showing e.g. Logistic Regression missed only 2 at-risk cases but produced 11 false positives, while XGBoost identified 31/36 with 7 false positives.

> "Logistic Regression also demonstrated the highest recall (0.94), meaning it captured the largest proportion of at-risk students but generated more false positives. By contrast, XGBoost combined high recall with stronger precision, providing a more balanced model for institutional use."

## Discussion


## Related Claims
- [XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91](xgboost-logreg-highest-f1-midterm-risk-prediction.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [A 10-point decrease in Biology midterm score raises predicted at-risk probability by about 31 percentage points, with smaller effects for Introduction to Health Sciences (~25) and English (~18)](ten-point-biology-decline-raises-risk-31-points.md) — related
