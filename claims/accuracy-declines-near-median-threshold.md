---
type: claim
title: Classification accuracy declines near the median score threshold due to overlap between low‐ and high‐skill feature distributions
description: Classification accuracy declines near the median score threshold due to overlap between low‐ and high‐skill feature distributions
id: accuracy-declines-near-median-threshold
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

# Classification accuracy declines near the median score threshold due to overlap between low‐ and high‐skill feature distributions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Performance degrades for scores near the median threshold, likely due to substantial overlap between low‐ and high‐skill feature distributions in this region. [→ Loukas 2026](#loukas-2026)

## Evidence

### Loukas 2026

Loukas, C., Prevezanou, K., Seimenis, I., Kykalos, S., & Schizas, D. (2026). Cross‐Stream and Cross‐Channel Attention Networks for Surgical Skill Classification in Open Surgery From Hand Kinematics. The International Journal of Medical Robotics + Computer Assisted Surgery. https://doi.org/10.1002/rcs.70215

`q2 · i?` · `design · r2`

Analysis of correct classification percentages across equal‐width skill score bins (Figure 6) shows low‐skill regions span more bins with greater variability, while high‐skill samples concentrate closer to the median with reduced separability, increasing misclassifications around the decision boundary.

> "Overall, both the proposed model xAtt‐Trans (inter‐hand) and ES2 achieve near‐perfect classification accuracy for low‐skill trainees. In contrast, performance degrades for scores near the median threshold, likely due to substantial overlap between low‐ and high‐skill feature distributions in this region."

## Discussion


## Related Claims
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Percent meeting standards is an imprecise metric whose cut-score concentration produced the Era 2 misconception that Chicago taught basic skills better than high-level skills](percent-meeting-standards-imprecise-metric.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
- [The inter‐hand xAtt‐Trans model achieves the best binary skill classification accuracy across all three open surgery tasks](inter-hand-xatt-trans-best-skill-classification.md) — related
- [The inter‐hand xAtt‐Trans model outperforms the human reviewer (ES2) in most classification metrics](model-outperforms-human-reviewer-skill-classification.md) — related
- [Threshold-based prediction models can classify countries as likely high performers, with proposed cutoff scores of 3.219 for reading, 2.396 for mathematics and 2.732 for science](pisa-early-warning-prediction-models.md) — related
