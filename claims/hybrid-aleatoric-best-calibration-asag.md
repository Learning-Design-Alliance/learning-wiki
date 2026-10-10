---
type: claim
title: The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods
description: The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods
id: hybrid-aleatoric-best-calibration-asag
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

# The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The hybrid model with aleatoric uncertainty closely tracks the reliability diagonal and achieves the best Brier score and lowest MCE, with improved calibration in the mid-confidence range. [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200

`q2 · i?` · `design · r2`

Reliability analysis (Fig. 2 and Table 1) on the SciEntsBank Test_UD split. Printed metrics for the hybrid with aleatoric uncertainty: Brier 0.138, ECE 0.044, MCE 0.100, versus Brier 0.172/0.194/0.186/0.218 for the other methods. No effect size is printed.

> "the hybrid model incorporating aleatoric uncertainty closely tracks the diagonal across confidence bins and achieves the best Brier score and lowest MCE, indicating both accurate probability estimates and reduced worst-case miscalibration"

## Discussion


## Related Claims
- [Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions](verbalizing-overconfidence-consistency-local-failures.md) — related
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](hybrid-confidence-highest-auroc-selective-asag.md) — related
- [Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration](latent-confidence-weakest-asag.md) — related
- [Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900](rejection-04-accuracy-gain-hybrid-confidence.md) — related
