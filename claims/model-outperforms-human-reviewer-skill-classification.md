---
type: claim
title: The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics
description: The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics
id: model-outperforms-human-reviewer-skill-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: loukas-2026
    resource: "https://doi.org/10.1002/rcs.70215"
    title: "Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215"
    author: "Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Compared to the human annotator (ES2), the xAtt‐Trans inter‐hand model is superior in most cases, particularly in Recall and F1 score, though ES2 maintains higher Precision in task CS. [→ Loukas 2026](#loukas-2026)

## Evidence

### Loukas 2026

Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215

`q2 · i?` · `design · r2`

Direct comparison between the best model and the second reviewer's labels on the same 201 trials. The model exceeded ES2 in Recall, F1, and Accuracy on tasks KT and IS, and in task CS achieved slightly higher Accuracy (0.84 vs. 0.83) and substantially higher AUC (0.94 vs. 0.81), while ES2 maintained higher Precision (0.93 vs. 0.86).

> "Compared to the human annotator (ES2), the xAtt‐Trans inter‐hand model is superior in most cases, for example in tasks KT and IS across nearly all metrics, particularly in Recall (task KT: 0.97 vs. 0.69 and task IS: 0.69 vs. 0.32), F1 score (task IS: 0.78 vs. 0.49) and Accuracy (task IS: 0.81 vs. 0.68)."

## Discussion


## Related Claims
- [Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance](cross-attention-improves-transformer-not-bilstm.md) — related
- [The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration](inter-hand-outperforms-intra-hand-attention.md) — a broader claim this one bears on
- [The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks](inter-hand-xatt-trans-best-skill-classification.md) — related
- [Transformer‐based models consistently outperform BiLSTM‐based models for surgical skill classification from hand kinematics](transformer-outperforms-bilstm-skill-classification.md) — a broader claim this one bears on
- [Classification accuracy declines near the median score threshold due to overlap between low‐ and high‐skill feature distributions](accuracy-declines-near-median-threshold.md) — related
