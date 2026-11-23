---
type: claim
title: In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum
description: In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum
id: sebn-robosuite-heavy-door-transfer
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
    rigour: 1
---

# In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Policies learned with the SEBN curriculum transfer to an unseen heavy door environment with reward 240 compared to 150 without a curriculum. [→ Vincent Hsiao 2025](#vincent-hsiao-2025)

## Evidence

### Vincent Hsiao 2025

Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau. 2025. Automating Curriculum Learning for Reinforcement Learning using a Skill-Based Bayesian Network. Proc. of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025). [doi:10.65109/ltnu1598](https://doi.org/10.65109/ltnu1598)

`q2 · i?` · `causal · r1`

Generalization study in the robosuite Door simulation: PPO policies trained for 2 million timesteps with door mass up to 6 were tested on an unseen heavy door environment; the SEBN curriculum policy obtained "a reward of 240 on the heavy door env compared to 150 without a curriculum." No effect size is printed.

> "We observed that with the policy learned by the SEBN-guided curriculum is easily transferred to more heavy doors (obtaining a reward of 240 on the heavy door env compared to 150 without a curriculum), in contrast to the other methods."

## Discussion


## Related Claims
- [SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments](sebn-curricula-outperform-baselines-continuous-robotics.md) — a broader claim this one bears on
- [SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search](sebn-curriculum-higher-variance.md) — related
- In DoorKey, SEBN-guided curriculum policies generalize better to an unseen 32x32 grid (93 percent success versus 82 percent without a curriculum) — related
