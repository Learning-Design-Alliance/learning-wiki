---
type: claim
title: Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance
description: Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance
id: cross-attention-improves-transformer-not-bilstm
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

# Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For BiLSTM‐based models, xAtt does not yield improvements and often degrades performance, while Transformer models benefit substantially in all surgical tasks. [→ Loukas 2026](#loukas-2026)

## Evidence

### Loukas 2026

Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215

`q2 · i?` · `design · r2`

In the 10‐fold evaluation across three tasks, adding cross‐attention to BiLSTM models reduced accuracy (e.g., allCh‐BiLSTM 0.80 vs. xAtt‐BiLSTM intra‐hand 0.72 on KT), whereas Transformer models with xAtt improved, e.g., allCh‐Trans 0.81 vs. xAtt‐Trans inter‐hand 0.88 on KT.

> "Specifically, for BiLSTM‐based models, xAtt does not yield improvements and often degrades performance. The Transformer models, however, benefit substantially in all surgical tasks, demonstrating the ability to model interactions between input streams that are informative of the trainee's skill level."

## Discussion


## Related Claims
- [Transformer‐based models consistently outperform BiLSTM‐based models for surgical skill classification from hand kinematics](transformer-outperforms-bilstm-skill-classification.md) — related
- [The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks](inter-hand-xatt-trans-best-skill-classification.md) — related
- [The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration](inter-hand-outperforms-intra-hand-attention.md) — related
- [The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics](model-outperforms-human-reviewer-skill-classification.md) — related
