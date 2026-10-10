---
type: claim
title: "A DQN-trained battery storage policy reduced complete cost by 5.9% relative to no storage on a synthetic 24-h training-day rollout"
description: "A DQN-trained battery storage policy reduced complete cost by 5.9% relative to no storage on a synthetic 24-h training-day rollout"
id: dqn-bess-training-day-cost-reduction
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: junjie-yin-2026
    resource: "https://arxiv.org/abs/2608.02599"
    title: "Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599"
    author: Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A DQN-trained battery storage policy reduced complete cost by 5.9% relative to no storage on a synthetic 24-h training-day rollout

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The DQN greedy training-day rollout had a complete cost of $180.19 versus $191.58 without storage and $216.34 for a straightforward cycle rule, a 5.9% reduction. [→ Junjie Yin 2026](#junjie-yin-2026)

## Evidence

### Junjie Yin 2026

Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599

`q1 · i?` · `design · r2`

Simulation example: a deep Q-network trained for 300 episodes on one synthetic 24-h load and time-of-use price profile. The greedy rollout cut complete cost to $180.19, a "5.9% reduction relative to the no-storage case," returning the battery to its initial empty state.

> "Fig. 9(b) shows that its greedy training-day rollout has a complete cost of $180.19, compared with $191.58 without storage and $216.34 for the straightforward cycle rule. The 5.9% reduction relative to the no-storage case is obtained while returning the 60-kWh battery to its initial empty state."

## Discussion


## Related Claims
-
