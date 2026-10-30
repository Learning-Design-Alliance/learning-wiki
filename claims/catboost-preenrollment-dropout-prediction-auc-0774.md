---
type: claim
title: A CatBoost classifier using only pre-enrollment achievement measures predicts dropout with an AUC of 0.774 and average precision of 0.847 on a held-out 2017 cohort.
description: A CatBoost classifier using only pre-enrollment achievement measures predicts dropout with an AUC of 0.774 and average precision of 0.847 on a held-out 2017 cohort.
id: catboost-preenrollment-dropout-prediction-auc-0774
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: nagy-2024
    resource: "https://doi.org/10.1007/s40593-023-00331-8"
    title: "Nagy, M., & Molontay, R. (2024). Interpretable Dropout Prediction: Towards XAI-Based Personalized Intervention. International Journal of Artificial Intelligence in Education, 34, 274–300. https://doi.org/10.1007/s40593-023-00331-8"
    author: "Nagy, M., & Molontay, R."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A CatBoost classifier using only pre-enrollment achievement measures predicts dropout with an AUC of 0.774 and average precision of 0.847 on a held-out 2017 cohort.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A CatBoost classifier trained on pre-enrollment achievement measures achieves an AUC of 0.774 and an average precision of 0.847 on a held-out 2017 cohort. [→ Nagy 2024](#nagy-2024)

## Evidence

### Nagy 2024

Nagy, M., & Molontay, R. (2024). Interpretable Dropout Prediction: Towards XAI-Based Personalized Intervention. International Journal of Artificial Intelligence in Education, 34, 274–300. https://doi.org/10.1007/s40593-023-00331-8

`q2 · i?` · `associational · r2`

Cohort-based train-test split (trained on 2013–2016, tested on 2017) at BME. The CatBoost model "achieved an average precision of 0.847 and AUC of 0.774" on the held-out cohort.

> "On the test data set, the CatBoost, optimized with Optuna (Akiba et al., 2019), achieved an average precision of 0.847 and AUC of 0.774."

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy](cross-semester-at-risk-prediction-high-accuracy.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
