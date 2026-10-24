---
type: claim
title: Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration
description: Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration
id: latent-confidence-weakest-asag
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: longwei-cong-2026
    resource: "https://doi.org/10.48550/arxiv.2605.00200"
    title: "Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200 [doi:10.48550/arxiv.2605.00200](https://doi.org/10.48550/arxiv.2605.00200)"
    author: Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Latent confidence yields the lowest AUROC (0.699) and the highest Brier score (0.218) and ECE (0.096) among the compared methods. [→ Longwei Cong 2026](#longwei-cong-2026)

## Evidence

### Longwei Cong 2026

Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200 [doi:10.48550/arxiv.2605.00200](https://doi.org/10.48550/arxiv.2605.00200)

`q2 · i?` · `design · r2`

ROC analysis in the Results section (Fig. 1) plus Table 1 calibration metrics. Latent-based confidence scored AUROC 0.699 / AUARC 0.794, Brier 0.218, ECE 0.096; the article reports it "leads to only marginal accuracy improvements and degrades sharply at higher rejection rates".

> "latent confidence yields the lowest AUROC, indicating that raw token-level probability alone is insufficient to reliably distinguish correct from incorrect responses"

## Discussion


## Related Claims
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](hybrid-confidence-highest-auroc-selective-asag.md) — related
- [Verbalized self-reported confidence is overconfident in the mid-confidence range, while consistency-based confidence shows good average calibration but localized failure regions](verbalizing-overconfidence-consistency-local-failures.md) — related
- [Model self-confidence gauges LLM confidence in probability estimates and helps identify when machine-generated scoring outputs are trustworthy](llm-self-confidence-identifies-trustworthy-scoring-outputs.md) — a broader claim this one bears on
- [Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900](rejection-04-accuracy-gain-hybrid-confidence.md) — related
- [The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct](peer-grading-confidence-estimates-conservative.md) — related
- [NIG-head predictive uncertainty is dominated by epistemic uncertainty and shows negligible correlation with the absolute engagement score (Pearson r 0.016 aleatoric, 0.025 epistemic)](epistemic-dominant-uncertainty-uncorrelated-with-engagement.md) — related
