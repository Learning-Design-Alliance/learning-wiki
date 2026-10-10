---
type: claim
title: "Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900"
description: "Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900"
id: rejection-04-accuracy-gain-hybrid-confidence
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

# Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` At a rejection rate of 0.4, accuracy of retained responses rises to approximately 0.900 versus 0.704 with no confidence-based selection. [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200

`q2 · i?` · `design · r2`

ARC analysis reported in the Results section (Fig. 1) for the hybrid model with aleatoric uncertainty on the SciEntsBank Test_UD split. The printed values are descriptive accuracies at the 0.4 rejection rate; no test statistic or effect size is reported for this contrast.

> "at a rejection rate of 0.4, corresponding to filtering out 40% of low-confidence predictions, the accuracy of the remaining responses increases to approximately 0.900, compared to 0.704 when no confidence-based selection is applied"

## Discussion


## Related Claims
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](hybrid-confidence-highest-auroc-selective-asag.md) — a broader claim this one bears on
