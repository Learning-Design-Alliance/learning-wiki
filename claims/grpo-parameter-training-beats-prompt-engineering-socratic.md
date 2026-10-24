---
type: claim
title: Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone
description: Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone
id: grpo-parameter-training-beats-prompt-engineering-socratic
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: xiaokun-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` PT-GRPO w/o Rdir outperforms the PE-GRPO prompt-engineering reference in SE (0.633 vs 0.400) and J (0.567 vs 0.367). [→ Xiaokun Wang 2026](#xiaokun-wang-2026)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)

`q2 · i?` · `causal · r1`

Comparison of the parameter-training track against the prompt-engineering reference track on the 30-question test set. The article reports "PT-GRPO w/oRdir outperforms PE-GRPO inSE(0 .633vs.0 .400) andJ (0.567vs.0 .367)".

> "PT-GRPO w/oRdir outperforms PE-GRPO inSE(0 .633vs.0 .400) andJ (0.567vs.0 .367), while using a 7B backbone rather than an API model."

## Discussion


## Related Claims
- [Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it](directness-penalty-harmful-as-grpo-reward.md) — related
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
- [The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression](grpo-without-directness-highest-conversation-depth.md) — related
- [Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage](scale-alone-does-not-induce-socratic-behavior.md) — related
