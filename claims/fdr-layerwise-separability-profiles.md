---
type: claim
title: Layer-wise probing shows clearer middle-layer separability in the general model and a weaker, deeper separability profile in the coder model
description: Layer-wise probing shows clearer middle-layer separability in the general model and a weaker, deeper separability profile in the coder model
id: fdr-layerwise-separability-profiles
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: yi-zhang-julia-rayz-2026
    resource: "https://arxiv.org/abs/2607.08009"
    title: "Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009"
    author: "Yi Zhang & Julia Rayz"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: yi-zhang-julia-rayz-2026-2
    resource: "https://arxiv.org/abs/2607.08009"
    title: "Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009"
    author: "Yi Zhang & Julia Rayz"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Layer-wise probing shows clearer middle-layer separability in the general model and a weaker, deeper separability profile in the coder model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` The general model reaches peak linear separability at Layer 29 (FDR ≈ 0.0303) for difficulty and Layer 28 (FDR ≈ 0.0224) for Bloom targets, while the coder model's difficulty peak FDR remains low (≈ 0.0108 at Layer 28) and its Bloom peak shifts to Layer 36 of 48. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Layer-by-layer Fisher's Discriminant Ratio probing of residual-stream activations at the last instruction token across all 48 layers, with 95% confidence intervals from bootstrap resampling with 1000 samples (Figure 1).

> "Specifically, the model reaches peak linear separability at Layer 29 (FDR ≈ 0.0303) for difficulty and Layer 28 (FDR≈ 0.0224) for Bloom targets."

### Yi Zhang & Julia Rayz 2026 (2)

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Coder-model FDR trajectory contrasted with the general model's; projection distributions (Figures 2 and 3) show the coder model with more overlap and higher variance along the mean-difference direction.

> "For general difficulty instructions, its peak FDR remains low (≈ 0.0108 at Layer 28), indicating more overlapping activation distributions under this linear diagnostic. Furthermore, when processing targeted Bloom prompts, the layer of maximum separability shifts deeper into the network, peaking at Layer 36 of 48."

## Discussion


## Related Claims
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — related
