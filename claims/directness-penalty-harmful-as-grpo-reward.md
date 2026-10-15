---
type: claim
title: "Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it"
description: "Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it"
id: directness-penalty-harmful-as-grpo-reward
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: mixed
sources:
  - id: xiaokun-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: xiaokun-wang-2026-2
    resource: "https://arxiv.org/abs/2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1` · `q2`

## Subclaims
`q2 i?` Adding Rdir with γ=0.2 during GRPO reduces SE from 0.633 to 0.433 and raises leakage from 13.3% to 23.3% relative to γ=0. [→ Xiaokun Wang 2026](#xiaokun-wang-2026)
`q2 i?` Rdir helps as an inference-time constraint: the PE-GRPO reference achieves lower leakage (6.7%) via explicit term constraints. [→ Xiaokun Wang 2026 (2)](#xiaokun-wang-2026-2)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)

`q2 · i?` · `causal · r1`

Reward-component ablation on the PT track (n=30) comparing PT-GRPO Full against PT-GRPO w/o Rdir. The article reports "Adding Rdir with γ=0.2reducesSE by 0.200 and raises leakage by 10 percentage points relative toγ=0."

> "Adding Rdir with γ=0.2reducesSE by 0.200 and raises leakage by 10 percentage points relative toγ=0."

### Xiaokun Wang 2026 (2)

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996

`q2 · i?` · `causal · r1`

Comparison against the prompt-engineering reference track on the same 30-question test set. The article reports "PE- GRPO achieves lower leakage (6.7%) via explicit term constraints" while remaining below the PT model on SE.

> "PE- GRPO achieves lower leakage (6.7%) via explicit term constraints, but cannot close theSEgap without parameter updates."

## Discussion


## Related Claims
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
- [Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone](grpo-parameter-training-beats-prompt-engineering-socratic.md) — related
- [The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression](grpo-without-directness-highest-conversation-depth.md) — related
