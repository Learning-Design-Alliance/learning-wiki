---
type: claim
title: SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods
description: SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods
id: spdl-significantly-increases-asymptotic-reward-point-mass
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In Point Mass experiments with PPO and SAC over 2D and 3D context spaces, SPDL significantly increases asymptotic reward on the target task compared to all other methods (ALP-GMM, GoalGAN, Random, Default). [→ Pascal Klink 2020](#pascal-klink-2020)

## Evidence

### Pascal Klink 2020

Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)

`q2 · i?` · `causal · r2`

Simulation experiments in the Point Mass environment with 2D and 3D context spaces using PPO and SAC, 20 algorithm runs per method (e.g. SPDL 9.35 ± 0.1 vs ALP-GMM 2.34 ± 0.2 for PPO P3D; significance by t-test with p < 1% per Table 1). The article reports that "SPDL signiﬁcantly increases the asymptotic reward on the target task compared to all other methods."

> "As Figure 2 and Table 1 indicate, SPDL signiﬁcantly increases the asymptotic reward on the target task compared to all other methods."

## Discussion


## Related Claims
- [In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance](all-curricula-enable-learning-ball-catching.md) — related
- [SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward](spdl-escapes-local-optimum-ant.md) — related
- [SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments](sebn-curricula-outperform-baselines-continuous-robotics.md) — related
