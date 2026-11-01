---
type: claim
title: Head movement frequency was the single most informative feature, with more head movements associated with classification as male.
description: Head movement frequency was the single most informative feature, with more head movements associated with classification as male.
id: head-movement-rate-most-informative-gender-feature
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

# Head movement frequency was the single most informative feature, with more head movements associated with classification as male.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The frequency of participants' head movements (hmdMoveRate) had the greatest influence on classification into class-male, suggesting boys may show more head movement than girls during a VR lesson. [→ Gao 2023](#gao-2023)

## Evidence

### Gao 2023

Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z

`q2 · i?` · `associational · r2`

SHAP analysis of the best LightGBM model identified hmdMoveRate as the top-ranked feature. "the frequency of participants' head movements was found to be the most informative feature for predicting gender".

> "the frequency of participants' head movements was found to be the most informative feature for predicting gender. It was observed that head movement has the greatest influence on classification into class-male"

## Discussion


## Related Claims
- [Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level.](eye-movements-discriminative-gender-classification-vr-ct.md) — related
- [HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.](hmd-fixation-features-most-informative-gender-classification.md) — possibly the same claim (merge candidate)
- [Girls directed more visual attention to instructional content (virtual teacher and screen) while boys distributed attention more broadly including to virtual peer learners.](gender-differences-visual-attention-vr-classroom.md) — related
- [SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features.](shap-feature-selection-improves-gender-classification.md) — related
- [Textual analysis of student blogs showed girls wrote with higher relative frequency about mentors, while boys' use of \"team\" surpassed \"group\"](blog-textual-analysis-gender-differences.md) — related
