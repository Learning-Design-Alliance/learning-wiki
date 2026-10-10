---
type: claim
title: Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration
description: Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration
id: latent-confidence-weakest-asag
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

# Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Latent confidence yields the lowest AUROC (0.699) and the highest Brier score (0.218) and ECE (0.096) among the compared methods. [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200

`q2 · i?` · `design · r2`

ROC analysis in the Results section (Fig. 1) plus Table 1 calibration metrics. Latent-based confidence scored AUROC 0.699 / AUARC 0.794, Brier 0.218, ECE 0.096; the article reports it "leads to only marginal accuracy improvements and degrades sharply at higher rejection rates".

> "latent confidence yields the lowest AUROC, indicating that raw token-level probability alone is insufficient to reliably distinguish correct from incorrect responses"

## Discussion


## Related Claims
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](hybrid-confidence-highest-auroc-selective-asag.md) — related
- [Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions](verbalizing-overconfidence-consistency-local-failures.md) — related
