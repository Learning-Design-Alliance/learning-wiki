---
type: claim
title: The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression
description: The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression
id: grpo-without-directness-highest-conversation-depth
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# The best GRPO variant also achieves the highest Conversation Depth (0.722), suggesting stronger scaffolding accompanies deeper semantic progression

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` PT-GRPO w/o Rdir achieves the highest CD (0.722) among PT-track systems on the 30-question test set. [→ Xiaokun Wang 2026](#xiaokun-wang-2026)

## Evidence

### Xiaokun Wang 2026

Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996 [doi:10.48550/arxiv.2607.22996](https://doi.org/10.48550/arxiv.2607.22996)

`q2 · i?` · `causal · r1`

Main-results evaluation (Table 3) measuring Conversation Depth as the fraction of consecutive turn pairs with SBERT cosine similarity below 0.70. The article reports "PT-GRPO w/oRdir also achieves the highestCD(0.722)".

> "PT-GRPO w/oRdir also achieves the highestCD(0.722), suggesting that stronger scaffolding is accompanied by deeper semantic progression rather than simple paraphrase."

## Discussion


## Related Claims
- [Using the directness penalty Rdir as a GRPO reward is counterproductive: it lowers SE by 0.200 and raises leakage by 10 percentage points relative to omitting it](directness-penalty-harmful-as-grpo-reward.md) — related
- [Gradient-based GRPO alignment of a 7B model outperforms prompt engineering on scaffolding effectiveness (0.633 vs 0.400) despite the smaller backbone](grpo-parameter-training-beats-prompt-engineering-socratic.md) — related
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
