---
type: claim
title: "SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features."
description: "SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features."
id: shap-feature-selection-improves-gender-classification
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

# SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Feature selection using SHAP importance rankings improved all five models, with LightGBM showing the largest gain (over 5% accuracy improvement, from 65.5% to 70.8% with the top 24 features). [→ Gao 2023](#gao-2023)

## Evidence

### Gao 2023

Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z

`q2 · i?` · `associational · r2`

Sequential backward elimination of features based on SHAP importance was applied to all five models. "the improvement of the LightGBM model is the largest, over 5% improvement in accuracy from 65.5% ( SD = 1.8% ) to 70.8% ( SD = 1.7% ) trained with the top 24 features".

> "the improvement of the LightGBM model is the largest, over 5% improvement in accuracy from 65.5% ( SD = 1.8% ) to 70.8% ( SD = 1.7% ) trained with the top 24 features"

## Discussion


## Related Claims
- [Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level.](eye-movements-discriminative-gender-classification-vr-ct.md) — a broader claim this one bears on
- [Head movement frequency was the single most informative feature, with more head movements associated with classification as male.](head-movement-rate-most-informative-gender-feature.md) — related
- [HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.](hmd-fixation-features-most-informative-gender-classification.md) — related
- [Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis](feature-selection-effects-mixed-across-families.md) — related
