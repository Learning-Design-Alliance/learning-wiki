---
type: claim
title: SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward
description: SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward
id: spdl-escapes-local-optimum-ant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2020
sources:
  - id: pascal-klink-2020
    resource: "https://doi.org/10.48550/arXiv.2004.11812"
    title: "Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)"
    author: "Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the Ant environment with PPO, SPDL allows the agent to escape the local optimum of not finding the gate, while ALP-GMM and a random curriculum do not improve reward over direct target-task learning. [→ Pascal Klink 2020](#pascal-klink-2020)

## Evidence

### Pascal Klink 2020

Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)

`q2 · i?` · `causal · r2`

PPO experiments in the torque-controlled quadruped Ant environment (20 seeds, Figure 3), using the Isaac Gym simulator. The article reports "SPDL allows the learning agent to escape the local optimum which results from the agent not ﬁnding the gate to pass through." Only PPO could be evaluated there because the Stable-Baselines TRPO and SAC implementations could not parallelize with Isaac Gym.

> "Looking at Figure 3, we see that SPDL allows the learning agent to escape the local optimum which results from the agent not ﬁnding the gate to pass through. ALP-GMM and a random curriculum do not improve the reward over directly learning on the target task."

## Discussion


## Related Claims
- [In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance](all-curricula-enable-learning-ball-catching.md) — related
- [Fitting the episodic SPRL policy is computationally costly and numerically unstable for high-dimensional policy parameterizations, which SPDL's step-based formulation avoids](sprl-episodic-policy-fitting-impractical-high-dimensions.md) — related
- [SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods](spdl-significantly-increases-asymptotic-reward-point-mass.md) — related
