---
type: claim
title: "LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it"
description: "LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it"
id: llm-upward-cognitive-shift-asymmetry
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

# LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Under both general difficulty prompts and targeted Bloom's levels, the evaluated models more easily add cognitively demanding operations than remove or replace them with lower-level operations. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Behavioral evaluation of 2,520 programming tasks from three benchmarks, judged with an LLM-as-a-judge framework. Under the "Easier" prompt both models still produced positive OCS scores (0.715 and 0.194), and the general model achieved only a marginal negative shift of -0.134 under targeted "Lower" Bloom prompts.

> "OCS scores reveal that the models more easily add cognitively demanding operations than remove or replace them with lower-level operations, under both general difficulty prompts and targeted Bloom's levels."

## Discussion


## Related Claims
- [Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles](downward-shift-benchmark-dependence.md) — a narrower finding that bears on this claim
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — a narrower finding that bears on this claim
