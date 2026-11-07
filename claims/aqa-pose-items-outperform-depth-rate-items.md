---
type: claim
title: The automatic CPR assessment system shows lower error than human raters on hand, arm and shoulder position items but higher error on compression depth and rate, which depend on human-object interaction the model does not capture.
description: The automatic CPR assessment system shows lower error than human raters on hand, arm and shoulder position items but higher error on compression depth and rate, which depend on human-object interaction the model does...
id: aqa-pose-items-outperform-depth-rate-items
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: mixed
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
  - id: constable-2025-2
    resource: "https://doi.org/10.1007/s10459-024-10369-5"
    title: "Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5"
    author: "Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The automatic CPR assessment system shows lower error than human raters on hand, arm and shoulder position items but higher error on compression depth and rate, which depend on human-object interaction the model does not capture.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The automatic AQA consistently exhibited lower error than manual assessments for hand, arm, and shoulder positions. [→ Constable 2025](#constable-2025)
`q2 i?` The automatic AQA exhibited higher error rates than raters on compression depth and rate, attributed to unmodelled human-dummy interaction; Table 2 shows rate MAE 1.67 (AQA) versus 0.89 and 0.11 for the two raters. [→ Constable 2025 (2)](#constable-2025-2)

## Evidence

### Constable 2025

Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5

`q2 · i?` · `design · r2`

Cross-validated MAE comparison of the AQA framework against the two expert raters' scores in the article's Results and discussion of AQA section. The article attributes the lower posture-item error to "our framework's reliance on precise pose information, providing a more objective assessment of the participant's posture" (Table 2: hand 0.33 vs 1.62/1.08; arm 0.07 vs 0.70/0.15).

> "When comparing our method with manual assessments, we found that our automatic AQA consistently exhibits significantly lower error in evaluating hand, arm, and shoulder positions."

### Constable 2025 (2)

Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5

`q2 · i?` · `design · r2`

Same fivefold cross-validated MAE comparison, reported per item in the Results and discussion of AQA section. Table 2 prints depth MAE 0.69 (AQA) vs 0.49/0.30 and rate 1.67 vs 0.89/0.11; the authors note raters used a metronome for rate judgements, which may raise their accuracy in that dimension.

> "Our AQA exhibited higher error rates in the compression depth and compression rate items. This discrepancy could be because these two items require assessing interactions between the participant and the dummy (Kılıç et al., 2018), something our framework currently does not capture."

## Discussion


## Related Claims
- [Aqa Stgcn Mae Comparable To Expert Raters](aqa-stgcn-mae-comparable-to-expert-raters.md)
- [Real-time feedback systems generally improve CPR quality in simulation-based training, particularly compression rate and depth](real-time-feedback-improves-cpr-quality-simulation.md) — related
- [Feedback-equipped CPR training does not significantly change chest recoil or hand position, which were already near ceiling at baseline](feedback-cpr-no-change-recoil-hand-position.md) — related
- [Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture.](multiview-fusion-robust-pose-ratings.md) — related
