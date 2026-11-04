---
type: claim
title: The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks
description: The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks
id: inter-hand-xatt-trans-best-skill-classification
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

# The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The xAtt‐Trans inter‐hand model shows the highest Accuracy/AUC/F1 across all tasks: 0.88/0.92/0.87 (KT), 0.84/0.94/0.82 (CS), and 0.81/0.87/0.78 (IS). [→ Loukas 2026](#loukas-2026)

## Evidence

### Loukas 2026

Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215

`q2 · i?` · `design · r2`

Evaluation of six DL models on 201 trials from 20 trainees across three tasks (KT, CS, IS), with 10‐fold cross‐validation. The inter‐hand cross‐attention Transformer model achieved the highest accuracy, AUC, and F1 on every task, e.g., "0.88/0.92/0.87 (KT)".

> "The xAtt‐Trans inter‐hand model shows the highest Accuracy/AUC/F1 across all tasks: 0.88/0.92/0.87 (KT), 0.84/0.94/0.82 (CS), and 0.81/0.87/0.78 (IS)."

## Discussion


## Related Claims
- [Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance](cross-attention-improves-transformer-not-bilstm.md) — related
- [The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration](inter-hand-outperforms-intra-hand-attention.md) — a broader claim this one bears on
- [The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics](model-outperforms-human-reviewer-skill-classification.md) — related
- [Transformer‐based models consistently outperform BiLSTM‐based models for surgical skill classification from hand kinematics](transformer-outperforms-bilstm-skill-classification.md) — related
- [Classification accuracy declines near the median score threshold due to overlap between low‐ and high‐skill feature distributions](accuracy-declines-near-median-threshold.md) — related
