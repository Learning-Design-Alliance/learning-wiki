---
type: claim
title: SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments
description: SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments
id: sebn-curricula-outperform-baselines-continuous-robotics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
sources:
  - id: vincent-hsiao-2025
    resource: "https://doi.org/10.65109/ltnu1598"
    title: Vincent Hsiao 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In BipedalWalker and robosuite experiments, policies trained with the SEBN-guided curriculum reach positive reward and transfer better than uniform, anti-curriculum, and no-curriculum controls. [→ Vincent Hsiao 2025](#vincent-hsiao-2025)

## Evidence

### Vincent Hsiao 2025

Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau. 2025. Automating Curriculum Learning for Reinforcement Learning using a Skill-Based Bayesian Network. Proc. of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025). [doi:10.65109/ltnu1598](https://doi.org/10.65109/ltnu1598)

`q2 · i?` · `causal · r2`

Simulation evaluation across three environments (gridworld, continuous control, simulated robotics) comparing SEBN curricula against uniform (domain randomization) and anti-curriculum controls; the abstract-level summary states curricula "frequently outperform other baselines."

> "The results show that curricula constructed using SEBN frequently outperform other baselines."

## Discussion


## Related Claims
- [In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum](sebn-robosuite-heavy-door-transfer.md) — a narrower finding that bears on this claim
- In DoorKey, SEBN-guided curriculum policies generalize better to an unseen 32x32 grid (93 percent success versus 82 percent without a curriculum) — a narrower finding that bears on this claim
- [SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search](sebn-curriculum-higher-variance.md) — related
- [In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance](all-curricula-enable-learning-ball-catching.md) — related
- [SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods](spdl-significantly-increases-asymptotic-reward-point-mass.md) — related
