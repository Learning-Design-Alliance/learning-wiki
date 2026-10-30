---
type: claim
title: "Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level."
description: "Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level."
id: eye-movements-discriminative-gender-classification-vr-ct
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: gao-2023
    resource: "https://doi.org/10.1007/s40593-022-00316-z"
    title: "Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z"
    author: "Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All five classification models (SVM, Logistic Regression, Random Forest, XGBoost, LightGBM) trained on 43 eye movement features performed above the 50% chance level across all tested time windows, with LightGBM achieving the highest accuracy of 65.5%. [→ Gao 2023](#gao-2023)

## Evidence

### Gao 2023

Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z

`q2 · i?` · `associational · r2`

Classification results from 280 participants (140 female, 140 male) using eye-tracking data collected during a VR CT lesson. Five ML models were trained with 43 features across ten time windows, with 60s optimal. "the performance of five models is higher than the chance level ( 50% ) in all time windows".

> "the performance of five models is higher than the chance level ( 50% ) in all time windows. Particularly, we found that a window size of 60s provides an optimal trade-off for gender classification compared to time windows of other lengths"

## Discussion


## Related Claims
- [SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features.](shap-feature-selection-improves-gender-classification.md) — a narrower finding that bears on this claim
- [Head movement frequency was the single most informative feature, with more head movements associated with classification as male.](head-movement-rate-most-informative-gender-feature.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
