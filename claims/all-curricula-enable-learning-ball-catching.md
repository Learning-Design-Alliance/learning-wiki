---
type: claim
title: In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance
description: In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance
id: all-curricula-enable-learning-ball-catching
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
  - id: pascal-klink-2020-2
    resource: "https://doi.org/10.48550/arXiv.2004.11812"
    title: "Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)"
    author: "Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In ball-catching with sparse reward, all curriculum methods enable learning and achieve similar reward, whereas sampling directly from the target distribution fails regardless of policy initialization; context-distribution initialization does not significantly change performance. [→ Pascal Klink 2020](#pascal-klink-2020)
`q2 i?` SPDL shrinks the initially wide context distribution to recover the subspace where the initial policy performs well, then gradually matches the target distribution, at differing pace across runs. [→ Pascal Klink 2020 (2)](#pascal-klink-2020-2)

## Evidence

### Pascal Klink 2020

Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)

`q2 · i?` · `causal · r2`

Experiments with TRPO, PPO and SAC on the Barrett WAM ball-catching environment (20 seeds, Figure 3 and Table 1), with and without pre-trained policy and initialized context distribution. The article reports that "all curricula enable learning in this environment and achieve a similar reward."

> "We see that sampling tasks directly from the target distribution does not allow the agent to learn a meaningful policy, regardless of the initial one. Further, all curricula enable learning in this environment and achieve a similar reward. The results also highlight that initialization of the context distribution does not signiﬁcantly change the performance in this task."

### Pascal Klink 2020 (2)

Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)

`q2 · i?` · `causal · r2`

Qualitative visualization of sampled context distributions at iterations 0 through 200 (Figure 3 lower plots). The article states SPDL "shrinks the initially wide context distribution in early iterations to recover the subspace of ball target positions" before gradually matching the target distribution, with differing pace across runs.

> "The context distributions p(c) visualized in Figure 3 indicate that SPDL shrinks the initially wide context distribution in early iterations to recover the subspace of ball target positions, in which the initial policy performs well."

## Discussion


## Related Claims
- [SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward](spdl-escapes-local-optimum-ant.md) — related
- [SPDL significantly increases asymptotic reward on the target task in the Point Mass environment compared to all other curriculum methods](spdl-significantly-increases-asymptotic-reward-point-mass.md) — related
- [The exploration advantage in semantic search is interpreted as context-dependent, potentially beneficial in sparsely distributed target environments](exploration-bias-benefit-context-dependent.md) — related
- [Fitting the episodic SPRL policy is computationally costly and numerically unstable for high-dimensional policy parameterizations, which SPDL's step-based formulation avoids](sprl-episodic-policy-fitting-impractical-high-dimensions.md) — related
- [SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments](sebn-curricula-outperform-baselines-continuous-robotics.md) — related
- [Scaffold access improves sparse-reward learning across six navigation and manipulation settings, enabling success in three where unassisted target-start training fails within the budget](scaffold-access-improves-sparse-reward-learning.md) — related
