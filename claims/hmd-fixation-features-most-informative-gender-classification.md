---
type: claim
title: HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.
description: HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.
id: hmd-fixation-features-most-informative-gender-classification
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

# HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SHAP analysis identified hmdMoveRate, meanTeacherFixationDuration, and maxScreenFixationDuration as the top three features, with HMD and fixation features contributing more than saccade and pupil features. [→ Gao 2023](#gao-2023)

## Evidence

### Gao 2023

Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z

`q2 · i?` · `associational · r2`

SHAP global feature importance and local explanation summary plots were computed for the best LightGBM model. "features hmdMoveRate, meanTeacherFixationDuration, and maxScreenFixationDuration followed by fixedPeerNumber and dwellOnPeer provide the maximum information".

> "features hmdMoveRate, meanTeacherFixationDuration, and maxScreenFixationDuration followed by fixedPeerNumber and dwellOnPeer provide the maximum information for the LightGBM(best) model in gender classification"

## Discussion


## Related Claims
- [Head movement frequency was the single most informative feature, with more head movements associated with classification as male.](head-movement-rate-most-informative-gender-feature.md) — possibly the same claim (merge candidate)
- [SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features.](shap-feature-selection-improves-gender-classification.md) — related
- [Girls directed more visual attention to instructional content (virtual teacher and screen) while boys distributed attention more broadly including to virtual peer learners.](gender-differences-visual-attention-vr-classroom.md) — related
