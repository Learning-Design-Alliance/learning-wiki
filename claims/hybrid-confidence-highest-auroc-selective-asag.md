---
type: claim
title: A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers
description: A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers
id: hybrid-confidence-highest-auroc-selective-asag
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: longwei-cong-2026
    resource: "https://arxiv.org/abs/2605.00200"
    title: "Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200"
    author: Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The hybrid model incorporating aleatoric uncertainty achieves the highest AUROC (0.885) and AUARC (0.876) among all evaluated confidence estimation methods on the SciEntsBank Test_UD split. [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200

`q2 · i?` · `design · r2`

Numerical evaluation shown in Fig. 1 (ROC and ARC analyses) on the SciEntsBank Test_UD split using gpt-oss-20b grading decisions. The hybrid confidence with aleatoric features reached AUROC 0.885 and AUARC 0.876, versus 0.823/0.851 for the hybrid without aleatoric features, "the highest AUROC" among compared methods.

> "the hybrid model incorporating aleatoric uncertainty achieves the highest AUROC and yields the strongest accuracy gains as low-confidence responses are progressively rejected"

## Discussion


## Related Claims
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900](rejection-04-accuracy-gain-hybrid-confidence.md) — a narrower finding that bears on this claim
- [Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration](latent-confidence-weakest-asag.md) — related
