---
type: claim
title: Editing the pit reward produces two behaviorally identical but diagnostically opposite failure modes, separated by a threshold at 7.774
description: Editing the pit reward produces two behaviorally identical but diagnostically opposite failure modes, separated by a threshold at 7.774
id: reward-editing-two-failure-modes-q-learning
status: review
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
    kind: design
    rigour: 2
  - id: jueng-2026-2
    resource: "https://doi.org/10.48550/arxiv.2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802. [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)"
    author: Jueng, Ekkachai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Editing the pit reward produces two behaviorally identical but diagnostically opposite failure modes, separated by a threshold at 7.774

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` With pit reward +5, the agent ends in a pit in 10/10 seeds even though the optimal policy still reaches the goal — an exploration failure, not reward hacking, because pit-seeking is sub-optimal under the written reward. [→ Jueng 2026](#jueng-2026)
`q2 i?` With pit reward +20, above the 7.774 threshold, the optimal policy genuinely prefers the pit and Q-learning recovers that same pit-seeking policy in 10/10 seeds — genuine reward misspecification. [→ Jueng 2026 (2)](#jueng-2026-2)

## Evidence

### Jueng 2026

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802 [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)

`q2 · i?` · `design · r2`

Simulation study comparing the learned greedy policy against the value-iteration optimal policy on the same edited MDP. The agent ends in a pit in 10/10 seeds with 100% of training episodes terminating in a pit, yet 'pit-seeking issub-optimalunder the very reward that was written'.

> "Value iteration on this exact MDP givesV∗(s0) = 6.38with an optimal policy that still goes to thegoal(Figure 5, top-left): reaching a pit is worth only about4.0in return, so pit-seeking issub-optimalunder the very reward that was written."

### Jueng 2026 (2)

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802. [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)

`q2 · i?` · `design · r2`

Same edited-MDP simulation study, high-reward regime located by bisection. With the pit reward 'above the7.774threshold', value iteration yields V*(s0) = 16.86 with a pit-seeking optimal policy, which Q-learning recovers in 10/10 seeds.

> "Setting the pit reward to+20(above the7.774threshold) does this: value iteration now yieldsV ∗(s0) = 16.86with an optimal policy that deliberately terminates in the nearest pit(Figure5, bottom-left), andQ-learningrecoversthatsamepit-seekingpolicyin10/10seeds(bottom-right)."

## Discussion


## Related Claims
- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](rl-reward-misalignment-failure-modes.md) — a broader claim this one bears on
