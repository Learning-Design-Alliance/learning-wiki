---
type: claim
title: The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration
description: The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration
id: inter-hand-outperforms-intra-hand-attention
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

# The inter‐hand cross‐attention configuration outperforms the intra‐hand configuration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The inter‐hand model outperformed the intra‐hand variant by about 2%–4%, likely because attention mechanisms are more effective when modelling relationships across heterogeneous inter‐hand channels. [→ Loukas 2026](#loukas-2026)

## Evidence

### Loukas 2026

Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215

`q2 · i?` · `design · r2`

Comparison of the two xAtt configurations within the Transformer family across all three tasks showed the inter‐hand variant (pairing left/right hands within same‐type channels) consistently achieved higher accuracy than the intra‐hand variant (pairing position/rotation within each hand).

> "In addition, the inter‐hand model outperformed the intra‐hand variant (where attention between position and rotation is evaluated separately within each hand) by about 2%–4%."

## Discussion


## Related Claims
- [Cross‐stream attention mechanisms improve Transformer model performance but not BiLSTM model performance](cross-attention-improves-transformer-not-bilstm.md) — related
- [The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics](model-outperforms-human-reviewer-skill-classification.md) — a narrower finding that bears on this claim
- [Transformer‐based models consistently outperform BiLSTM‐based models for surgical skill classification from hand kinematics](transformer-outperforms-bilstm-skill-classification.md) — related
- [The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks](inter-hand-xatt-trans-best-skill-classification.md) — a narrower finding that bears on this claim
