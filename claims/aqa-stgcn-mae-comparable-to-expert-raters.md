---
type: claim
title: A multiview pose-estimation deep learning model assesses overall CPR performance quality with mean absolute error comparable to expert human raters, with margins typically below 1 point on a 4-point item scale.
description: A multiview pose-estimation deep learning model assesses overall CPR performance quality with mean absolute error comparable to expert human raters, with margins typically below 1 point on a 4-point item scale.
id: aqa-stgcn-mae-comparable-to-expert-raters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
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

# A multiview pose-estimation deep learning model assesses overall CPR performance quality with mean absolute error comparable to expert human raters, with margins typically below 1 point on a 4-point item scale.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In fivefold cross-validation on 53 CPR recordings, the automatic AQA framework's overall MAE against expert-consensus scores (2.98) fell between the two individual expert raters' MAEs (3.96 and 2.69), and most item error margins were below 1. [→ Constable 2025](#constable-2025)

## Evidence

### Constable 2025

Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5

`q2 · i?` · `design · r2`

Evaluation of the automatic AQA framework on the authors' CPR dataset (53 recordings) using Mean Absolute Error with fivefold cross-validation (80% train, 20% test per fold), compared against expert-agreed ground-truth ratings. The article reports that "the error margin of our framework remains below 1" in most cases; Table 2 shows total MAE 2.98 for AQA versus 3.96 (Evaluator 1) and 2.69 (Evaluator 2), full item score = 4.

> "In most cases, the error margin of our framework remains below 1, underscoring our automated methods' potential accuracy and applicability."

## Discussion


## Related Claims
- [Aqa Pose Items Outperform Depth Rate Items](aqa-pose-items-outperform-depth-rate-items.md)
- [Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture.](multiview-fusion-robust-pose-ratings.md) — a narrower finding that bears on this claim
- [Two expert raters rating CPR cycles alone reached moderate agreement for Cycles 2-4 but poor agreement for Cycle 1, which the authors attribute to inconsistencies in an initial 'practice' cycle.](expert-rater-agreement-cpr-performance-cycles.md) — related
