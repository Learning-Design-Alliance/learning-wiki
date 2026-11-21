---
type: claim
title: The compact One Encoder gives a more balanced, stable and less overfitted predictor than the Raw Encoder, with higher average test ROCAUC (0.882 vs 0.860)
description: The compact One Encoder gives a more balanced, stable and less overfitted predictor than the Raw Encoder, with higher average test ROCAUC (0.882 vs 0.860)
id: one-encoder-outperforms-raw-encoder-balance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: xinzhe-zheng-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00863"
    title: "Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)"
    author: Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The compact One Encoder gives a more balanced, stable and less overfitted predictor than the Raw Encoder, with higher average test ROCAUC (0.882 vs 0.860)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` One Encoder achieves a higher average test ROCAUC than Raw Encoder (0.882 vs 0.860) with a smaller range across talent types. [→ Xinzhe Zheng 2025](#xinzhe-zheng-2025)

## Evidence

### Xinzhe Zheng 2025

Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. [doi:10.48550/arXiv.2509.00863](https://doi.org/10.48550/arXiv.2509.00863)

`q2 · i?` · `design · r2`

Comparison of the two encoder variants in the Results section (Table II and learning curves in Fig. 4). The article reports "the average test ROCAUC of One Encoder and Raw Encoder are 0.882 and 0.860 respectively" and states One Encoder is more stable and less overfitted.

> "the average test ROCAUC of One Encoder and Raw Encoder are 0.882 and 0.860 respectively, indicating a very good classifier. However, One Encoder gives a more balanced prediction"

## Discussion


## Related Claims
- [TalentPredictor predicts seven talent types in secondary school students with a best test micro ROCAUC of 0.908 on a real-world dataset of 1,041 students](talentpredictor-0908-micro-rocauc-seven-talent-types.md) — related
- [SHAP analysis on a logistic regression surrogate over One Encoder's size-1 embeddings makes the deep model interpretable at the feature level with similar predictive performance (0.880 accuracy, 0.878 ROCAUC)](shap-logistic-surrogate-feature-interpretation.md) — related
