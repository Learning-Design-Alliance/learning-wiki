---
type: claim
title: Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward
description: Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward
id: tza-higher-versus-lower-bloom-targets
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yi-zhang-julia-rayz-2026
    resource: "https://arxiv.org/abs/2607.08009"
    title: "Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009"
    author: "Yi Zhang & Julia Rayz"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Targeting Higher Bloom levels succeeds 79.2% for the general model versus 63.4% for the coder model, while Lower-target accuracy drops below 30% for both models. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Target Zone Accuracy results over 2,520 tasks (Table 2) measuring adherence to targeted Bloom zones (Remember/Understand for Lower, Evaluate/Create for Higher). Both architectures perform well upward but fail downward.

> "The general model succeeds 79.2% of the time, outperforming the coder model's 63.4% success rate. By contrast, targeting "Lower" levels exposes a clear weakness, with overall accuracy dropping below 30% for both models."

## Discussion


## Related Claims
- [The general and coder models deploy distinct lexical strategies when raising cognitive demand, and neither deploys simplification vocabulary downward](divergent-lexical-mutation-strategies.md) — related
- [Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles](downward-shift-benchmark-dependence.md) — related
- [Layer-wise probing shows clearer middle-layer separability in the general model and a weaker, deeper separability profile in the coder model](fdr-layerwise-separability-profiles.md) — related
- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — a broader claim this one bears on
