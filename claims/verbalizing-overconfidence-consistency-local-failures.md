---
type: claim
title: Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions
description: Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions
id: verbalizing-overconfidence-consistency-local-failures
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

# Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Verbalizing-based confidence exceeds empirical accuracy in the mid-confidence range (MCE 0.259); consistency-based confidence attains the lowest ECE (0.029) but a high MCE (0.279). [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200

`q2 · i?` · `design · r2`

Reliability analysis (Fig. 2, Table 1) on the SciEntsBank Test_UD split. Verbalizing-based confidence showed "clear deviations from the diagonal, particularly in the mid-confidence range" with MCE 0.259; consistency-based confidence had Brier 0.186, ECE 0.029, MCE 0.279.

> "Consistency-based confidence follows the diagonal more closely and attains the lowest ECE, suggesting good average calibration. However, its relatively high MCE indicates that substantial calibration errors still occur in certain confidence regions"

## Discussion


## Related Claims
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration](latent-confidence-weakest-asag.md) — related
- [Novice clinical learners show pervasive metacognitive calibration deficits, with overestimated performance and confidence exceeding accuracy](novice-metacognitive-calibration-deficits.md) — related
- [Prior Knowledge Needed For Accurate Self Assessment](prior-knowledge-needed-for-accurate-self-assessment.md) — related
