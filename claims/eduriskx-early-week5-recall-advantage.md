---
type: claim
title: EduRiskX achieves substantially higher early-week recall than PatchTST and iTransformer on OULAD, with Week 5 recall of 0.681 versus 0.355 and 0.390
description: EduRiskX achieves substantially higher early-week recall than PatchTST and iTransformer on OULAD, with Week 5 recall of 0.681 versus 0.355 and 0.390
id: eduriskx-early-week5-recall-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yu-fu-2026
    resource: "https://doi.org/10.21203/rs.3.rs-8877832/v1"
    title: "Yu Fu, Yongqi Kang, Yong Zhao, and Rongfang Bie. (2026). EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction. arXiv. [doi:10.21203/rs.3.rs-8877832/v1](https://doi.org/10.21203/rs.3.rs-8877832/v1)"
    author: Yu Fu, Yongqi Kang, Yong Zhao, and Rongfang Bie
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EduRiskX achieves substantially higher early-week recall than PatchTST and iTransformer on OULAD, with Week 5 recall of 0.681 versus 0.355 and 0.390

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At Week 5, EduRiskX's recall (0.681) is 91.9% higher than PatchTST (0.355) and 74.6% higher than iTransformer (0.390) on OULAD. [→ Yu Fu 2026](#yu-fu-2026)

## Evidence

### Yu Fu 2026

Yu Fu, Yongqi Kang, Yong Zhao, and Rongfang Bie. (2026). EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction. arXiv. [doi:10.21203/rs.3.rs-8877832/v1](https://doi.org/10.21203/rs.3.rs-8877832/v1)

`q2 · i?` · `design · r2`

Evaluation on OULAD with an 80/10/10 student-level split comparing EduRiskX against SOTA time-series baselines at Week 5. The article reports "EduRiskX’s recall (0.681) is 91.9% higher than PatchTST (0.355)"; no standardized effect size is printed.

> "At Week 5, EduRiskX’s recall (0.681) is 91.9% higher than PatchTST (0.355) and 74.6% higher than iTransformer (0.390). This early recall advantage enables earlier and more reliable intervention."

## Discussion


## Related Claims
- [EduRiskX detects at-risk students earliest among compared models, with an average detection week of 9.32, lead time of 28.68 weeks, and detection rate of 94.30%](eduriskx-early-detection-metrics.md) — related
- [EduRiskX leads in F1-score at every time point on OULAD, reaching 0.894 F1 and 0.864 recall at Week 38](eduriskx-f1-leadership-all-weeks.md) — related
- [Omitting the class-weighted loss causes the most pronounced recall degradation among ablation variants, and removing temporal attention also substantially lowers early recall](class-weighted-loss-temporal-attention-ablations.md) — related
