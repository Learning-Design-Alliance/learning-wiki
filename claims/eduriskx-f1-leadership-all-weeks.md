---
type: claim
title: EduRiskX leads in F1-score at every time point on OULAD, reaching 0.894 F1 and 0.864 recall at Week 38
description: EduRiskX leads in F1-score at every time point on OULAD, reaching 0.894 F1 and 0.864 recall at Week 38
id: eduriskx-f1-leadership-all-weeks
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

# EduRiskX leads in F1-score at every time point on OULAD, reaching 0.894 F1 and 0.864 recall at Week 38

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EduRiskX leads in F1-Score at every time point, with a Week 38 recall of 0.864 versus LSTM's 0.819 and F1 of 0.894 versus the ablation variant's 0.891. [→ Yu Fu 2026](#yu-fu-2026)

## Evidence

### Yu Fu 2026

Yu Fu, Yongqi Kang, Yong Zhao, and Rongfang Bie. (2026). EduRiskX: A Neuro-Symbolic Framework with F-Logic Reasoning for Early Academic Risk Prediction. arXiv. [doi:10.21203/rs.3.rs-8877832/v1](https://doi.org/10.21203/rs.3.rs-8877832/v1)

`q2 · i?` · `design · r2`

End-of-semester comparison on OULAD (Week 38) across six models. The article reports EduRiskX "maintains a 2.1% recall advantage over the nearest competitor" and a 1.5% F1 advantage; no standardized effect size is printed.

> "By Week 38, EduRiskX maintains a 2.1% recall advantage over the nearest competitor (0.864 vs. LSTM’s 0.819) and a 1.5% F1 advantage (0.894 vs. Ablation’s 0.891)."

## Discussion


## Related Claims
- [EduRiskX detects at-risk students earliest among compared models, with an average detection week of 9.32, lead time of 28.68 weeks, and detection rate of 94.30%](eduriskx-early-detection-metrics.md) — related
- [EduRiskX achieves substantially higher early-week recall than PatchTST and iTransformer on OULAD, with Week 5 recall of 0.681 versus 0.355 and 0.390](eduriskx-early-week5-recall-advantage.md) — related
- [Omitting the class-weighted loss causes the most pronounced recall degradation among ablation variants, and removing temporal attention also substantially lowers early recall](class-weighted-loss-temporal-attention-ablations.md) — related
- [Removing the F-Logic reasoning module delays average risk detection by approximately 1.5 weeks (8.78 to 10.29 weeks) in the ablation study](flogic-ablation-detection-delay.md) — related
