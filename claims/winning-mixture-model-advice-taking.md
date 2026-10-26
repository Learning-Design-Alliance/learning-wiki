---
type: claim
title: "A computational model combining informed and non-informed advice-taking with individual learning (Model 5) best predicts participants' choices"
description: "A computational model combining informed and non-informed advice-taking with individual learning (Model 5) best predicts participants' choices"
id: winning-mixture-model-advice-taking
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: maayan-pereg-2024
    resource: "https://doi.org/10.1038/s41539-024-00214-0"
    title: "Maayan Pereg, Uri Hertz, Ido Ben-Artzi and Nitzan Shahar. (2024). Disentangling the contribution of individual and social learning processes in human advice-taking behavior. npj Science of Learning 9:4. https://doi.org/10.1038/s41539-024-00214-0"
    author: Maayan Pereg, Uri Hertz, Ido Ben-Artzi and Nitzan Shahar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A computational model combining informed and non-informed advice-taking with individual learning (Model 5) best predicts participants' choices

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Model 5, including individual learning, informed advice-taking and non-informed advice-taking, outperformed all nested alternatives in leave-one-block-out comparison. [→ Maayan Pereg 2024](#maayan-pereg-2024)

## Evidence

### Maayan Pereg 2024

Maayan Pereg, Uri Hertz, Ido Ben-Artzi and Nitzan Shahar. (2024). Disentangling the contribution of individual and social learning processes in human advice-taking behavior. npj Science of Learning 9:4. https://doi.org/10.1038/s41539-024-00214-0

`q2 · i?` · `causal · r2`

Leave-one-block-out cross-validated model comparison (elpd via the loo package) of five prediction-error-based RL models on the empirical choice data; Table 1 shows the null model at −4147.2 (88.4) elpd difference versus Model 5, with Model 2 at −514.1 (33.4).

> "We found Model 5 to be the winning model"

## Discussion


## Related Claims
- [Simulated data show a double dissociation: early-trial reveal effects arise only from non-informed advice-taking, while outcome-dependent coherence repetition arises only from informed advice-taking](double-dissociation-advice-signatures.md) — related
- [Estimated parameters indicate simultaneous reliance on individual learning (ω ≈ 0.70) and a fixed non-informed bias to follow advice (φ ≈ 0.2)](parameters-individual-and-advice-bias.md) — related
- [Mentalizing-network regions (TPJ, STS, dmPFC, MTG) signal social prediction errors beyond ToM tasks](mentalizing-network-social-prediction-error.md) — related
