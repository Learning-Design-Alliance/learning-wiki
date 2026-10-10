---
type: claim
title: "Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles"
description: "Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles"
id: downward-shift-benchmark-dependence
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

# Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` SWE-Bench-Verified is the clearest case where simplification is comparatively easier, especially for the general model, while LiveCodeBench is the most resistant setting for downward shifts. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Benchmark-level TZA breakdown (Table 2): general model Lower-target accuracy reaches 0.786 on SWE-Bench-Verified but only 0.072 on LiveCodeBench; the coder model shows 0.630 versus 0.035 on the same contrast.

> "SWE-Bench-Verified stands out as the clearest case where simplification is comparatively easier, especially for the general model, while LiveCodeBench remains the most resistant setting for downward shifts."

## Discussion


## Related Claims
- [The general and coder models deploy distinct lexical strategies when raising cognitive demand, and neither deploys simplification vocabulary downward](divergent-lexical-mutation-strategies.md) — related
- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — a broader claim this one bears on
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — related
