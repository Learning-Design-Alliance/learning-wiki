---
type: claim
title: "Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture."
description: "Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture."
id: multiview-fusion-robust-pose-ratings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: constable-2025
    resource: "https://doi.org/10.1007/s10459-024-10369-5"
    title: "Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5"
    author: "Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The authors argue that single-camera judgements are limited by participants' angles toward the camera and varying initial postures, and that their multi-view fusion overcomes this limitation. [→ Constable 2025](#constable-2025)

## Evidence

### Constable 2025

Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5

`q2 · i?` · `design · r2`

Authors' interpretation (qualitative exemplar analysis in the Results and discussion of AQA section, Fig. 4 cases including a hand-position conflict where one rater scored 0 and the other 4 before agreeing on 4). The article reports that "summarising the motion information from multiple views makes our rating results more robust for pose-related scores".

> "Our method, which fuses information from multiple camera views, overcomes this limitation. Even though our pose estimation may occasionally show misdetections"

## Discussion


## Related Claims
- [A multiview pose-estimation deep learning model assesses overall CPR performance quality with mean absolute error comparable to expert human raters, with margins typically below 1 point on a 4-point item scale.](aqa-stgcn-mae-comparable-to-expert-raters.md) — a broader claim this one bears on
- [The automatic CPR assessment system shows lower error than human raters on hand, arm and shoulder position items but higher error on compression depth and rate, which depend on human-object interaction the model does not capture.](aqa-pose-items-outperform-depth-rate-items.md) — related
- [Head-pose-estimation-based proctoring systems report widely varying accuracies, from 75.6% for cheating detection to 100% for yaw-angle estimation](head-pose-proctoring-accuracy-range.md) — related
- [Limited camera views and poor sound quality are the two main weaknesses of live video observation](lvo-weaknesses-limited-view-poor-sound.md) — related
- [Recording angle alone does not affect self-reported cognitive load during video observation or task execution](recording-angle-no-cognitive-load-effect.md) — related
