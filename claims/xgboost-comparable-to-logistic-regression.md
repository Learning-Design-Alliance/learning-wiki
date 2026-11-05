---
type: claim
title: XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set
description: XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set
id: xgboost-comparable-to-logistic-regression
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: lai-wenyi-2026
    resource: "https://doi.org/10.1186/s12909-026-08741-7"
    title: "Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7"
    author: Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Compared with logistic regression, XGBoost showed comparable overall performance; the article reports XGBoost AUC 0.617 versus logistic regression AUC 0.659. [→ Lai Wenyi 2026](#lai-wenyi-2026)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

Results-section comparison in the same train-test study: the article states XGBoost "demonstrated comparable overall performance" to logistic regression, and adopted XGBoost as the primary model for its capacity to capture nonlinear relationships and SHAP compatibility.

> "Compared with the baseline logistic regression model, XGBoost demonstrated comparable overall performance."

## Discussion


## Related Claims
- [A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set](lr-baseline-gpa-classification.md) — a narrower finding that bears on this claim
- [An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set](xgboost-gpa-classification.md) — a narrower finding that bears on this claim
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
