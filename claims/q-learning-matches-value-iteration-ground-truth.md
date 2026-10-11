---
type: claim
title: "The tool's Q-learning matches a value-iteration ground truth in 98.5% of non-terminal states on average"
description: "The tool's Q-learning matches a value-iteration ground truth in 98.5% of non-terminal states on average"
id: q-learning-matches-value-iteration-ground-truth
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jueng-2026
    resource: "https://arxiv.org/abs/2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802"
    author: Jueng, Ekkachai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The tool's Q-learning matches a value-iteration ground truth in 98.5% of non-terminal states on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 10 seeds, the greedy policy learned by the tool's Q-learning rule lies in the optimal action set for 98.5% of non-terminal states on average, with maximum absolute value error averaging 0.34. [→ Jueng 2026](#jueng-2026)

## Evidence

### Jueng 2026

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802

`q2 · i?` · `design · r2`

Numerical validation on a Python reference implementation mirroring the JavaScript environment constant-for-constant: tabular Q-learning run for 50,000 episodes with a Robbins–Monro learning-rate schedule against value iteration converged to tolerance 10−12, scoring agreement by Eq. 2. The greedy policy matches an optimal action 'in98.5%of non-terminal states on average'.

> "Across 10 seeds, the greedy policy matches an optimal action (Eq. 2) in98.5%of non-terminal states on average (minimum95%, i.e. at most one state per run)"

## Discussion


## Related Claims
- [Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges](hyperparameter-sweeps-reproduce-lesson-claims.md) — related
