---
type: claim
title: "Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges"
description: "Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges"
id: hyperparameter-sweeps-reproduce-lesson-claims
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jueng-2026
    resource: "https://doi.org/10.48550/arxiv.2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802 [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)"
    author: Jueng, Ekkachai
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jueng-2026-2
    resource: "https://arxiv.org/abs/2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802"
    author: Jueng, Ekkachai
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` In the exploration and learning-rate sweeps, all tested ε values including ε = 1 eventually reach the optimal return, and all tested α values converge on this small problem. [→ Jueng 2026](#jueng-2026)
`q2 i?` In the discount sweep, γ ∈ {0.5, 0.95} reach the optimum while γ = 0 never solves the task, with a final return of −6.1. [→ Jueng 2026 (2)](#jueng-2026-2)

## Evidence

### Jueng 2026

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802 [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)

`q2 · i?` · `causal · r2`

Multi-seed numerical sweep experiment: for each setting the reference implementation trains for 600 episodes and evaluates the greedy policy every 20 episodes by undiscounted return from the start state, aggregating 10 random seeds. All tested ε values 'eventually reach the optimal return—includingε= 1'.

> "Allε∈{0.05,0.3,1.0}eventually reach the optimal return—includingε= 1, a nice classroom demonstration that Q-learning is off-policy and learns the greedy policy even from purely random behavior, though with slower, noisier progress."

### Jueng 2026 (2)

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802

`q2 · i?` · `causal · r2`

Same 600-episode, 10-seed sweep experiment, discount factor arm. The article reports that 'γ= 0never solves the task (final return−6.1)' while γ ∈ {0.5, 0.95} reach the optimum of 9.3.

> "The discount sweep is the starkest:γ∈{0.5,0.95}reach the optimum, whileγ= 0never solves the task (final return−6.1)—the myopic agent cannot propagate the goal reward backwards, exactly the “short-sighted agent” the lesson describes."

## Discussion


## Related Claims
- OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT — related
- [The tool's Q-learning matches a value-iteration ground truth in 98.5% of non-terminal states on average](q-learning-matches-value-iteration-ground-truth.md) — related
