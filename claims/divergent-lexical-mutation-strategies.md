---
type: claim
title: The general and coder models deploy distinct lexical strategies when raising cognitive demand, and neither deploys simplification vocabulary downward
description: The general and coder models deploy distinct lexical strategies when raising cognitive demand, and neither deploys simplification vocabulary downward
id: divergent-lexical-mutation-strategies
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

# The general and coder models deploy distinct lexical strategies when raising cognitive demand, and neither deploys simplification vocabulary downward

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Under the Harder setting the general model forms nine distinct clusters using varied structural terms, while the coder model concentrates mutations into three tight clusters focused on input rules and error handling. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)
`q2 i?` When attempting to lower cognitive load, neither model consistently deploys vocabulary indicative of Bloom-level simplification, instead falling back on structural or descriptive boilerplate. [→ Yi Zhang & Julia Rayz 2026 (2)](#yi-zhang-julia-rayz-2026-2)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Semantic-delta clustering (SBERT embeddings, UMAP, HDBSCAN) of mutations across the 2,520 tasks, with Weighted Log Odds Ratio keyword extraction per cluster. The analysis is described by the authors as exploratory.

> "The general model forms nine distinct clusters in the "Harder" setting, employing varied terms such asoptional,bool, andnestedto increase structural complexity in multiple ways. Conversely, the coder model concentrates its "Harder" mutations into just three tight clusters"

### Yi Zhang & Julia Rayz 2026 (2)

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009

`q2 · i?` · `causal · r2`

Keyword analysis of downward mutations suggests the models may satisfy surface-form instructions by making tasks more explicit or more formatted while leaving the core reasoning operation intact.

> "When at-tempting to lower cognitive load, they often fall back on structural or descriptive boilerplate, using words such asfunction,takes,write, andlistfor "Easier", andgiven,following, anddoes for "Lower"."

## Discussion


## Related Claims
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — related
- [Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles](downward-shift-benchmark-dependence.md) — related
