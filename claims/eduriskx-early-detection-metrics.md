---
type: claim
title: "EduRiskX detects at-risk students earliest among compared models, with an average detection week of 9.32, lead time of 28.68 weeks, and detection rate of 94.30%"
description: "EduRiskX detects at-risk students earliest among compared models, with an average detection week of 9.32, lead time of 28.68 weeks, and detection rate of 94.30%"
id: eduriskx-early-detection-metrics
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

# EduRiskX detects at-risk students earliest among compared models, with an average detection week of 9.32, lead time of 28.68 weeks, and detection rate of 94.30%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EduRiskX achieves the best performance in all early detection metrics: average detection week 9.32, lead time 28.68 weeks, and detection rate 94.30%, identifying risk 4.38 weeks earlier than PatchTST on average. [→ Yu Fu 2026](#yu-fu-2026)

## Evidence

### Yu Fu 2026

Yu Fu, Yongqi Kang, Yong Zhao, and Rongfang Bie. (2026). EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction. arXiv. [doi:10.21203/rs.3.rs-8877832/v1](https://doi.org/10.21203/rs.3.rs-8877832/v1)

`q2 · i?` · `design · r2`

Early detection comparison on OULAD across six models (Table 5). The article reports the framework "can identify at-risk students in the 9th week of the semester on average, providing nearly 29 weeks of intervention time"; no standardized effect size is printed.

> "EduRiskX (Complete) achieves the best performance in all early detection metrics: the average detection week is only 9.32, the lead time is 28.68 weeks, and the detection rate is 94.30%."

## Discussion


## Related Claims
- [Removing the F-Logic reasoning module delays average risk detection by approximately 1.5 weeks (8.78 to 10.29 weeks) in the ablation study](flogic-ablation-detection-delay.md) — related
- [EduRiskX leads in F1-score at every time point on OULAD, reaching 0.894 F1 and 0.864 recall at Week 38](eduriskx-f1-leadership-all-weeks.md) — related
- [EduRiskX achieves substantially higher early-week recall than PatchTST and iTransformer on OULAD, with Week 5 recall of 0.681 versus 0.355 and 0.390](eduriskx-early-week5-recall-advantage.md) — related
- [Omitting the class-weighted loss causes the most pronounced recall degradation among ablation variants, and removing temporal attention also substantially lowers early recall](class-weighted-loss-temporal-attention-ablations.md) — related
