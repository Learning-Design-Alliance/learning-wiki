---
type: claim
title: SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search
description: SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search
id: sebn-curriculum-higher-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
sources:
  - id: vincent-hsiao-2025
    resource: "https://doi.org/10.65109/ltnu1598"
    title: Vincent Hsiao 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The SEBN-guided curriculum's learning curve has much higher variance than other methods because sample-search may introduce sub-optimal environments. [→ Vincent Hsiao 2025](#vincent-hsiao-2025)

## Evidence

### Vincent Hsiao 2025

Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau. 2025. Automating Curriculum Learning for Reinforcement Learning using a Skill-Based Bayesian Network. Proc. of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025). [doi:10.65109/ltnu1598](https://doi.org/10.65109/ltnu1598)

`q2 · i?` · `causal · r2`

Authors' observation in the BipedalWalker results section: because approximate sample-search is used to select candidate environments, "sub-optimal environments can be introduced into the curriculum," adding variance beyond standard reinforcement learning noise.

> "It is interesting to observe that the learning curve for the SEBN-guided curriculum has much higher variance than the learning curves for other methods."

## Discussion


## Related Claims
- [SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments](sebn-curricula-outperform-baselines-continuous-robotics.md) — related
- [In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum](sebn-robosuite-heavy-door-transfer.md) — related
- In DoorKey, SEBN-guided curriculum policies generalize better to an unseen 32x32 grid (93 percent success versus 82 percent without a curriculum) — related
