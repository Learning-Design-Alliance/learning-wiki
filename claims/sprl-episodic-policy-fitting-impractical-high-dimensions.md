---
type: claim
title: "Fitting the episodic SPRL policy is computationally costly and numerically unstable for high-dimensional policy parameterizations, which SPDL's step-based formulation avoids"
description: "Fitting the episodic SPRL policy is computationally costly and numerically unstable for high-dimensional policy parameterizations, which SPDL's step-based formulation avoids"
id: sprl-episodic-policy-fitting-impractical-high-dimensions
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
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Fitting the episodic SPRL policy is computationally costly and numerically unstable for high-dimensional policy parameterizations, which SPDL's step-based formulation avoids

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` In the Ant environment, SPRL's episodic policy would need to fit a 6464-dimensional Gaussian, taking up to 25 minutes per update and being prone to numerical instabilities, motivating SPDL's unification of curriculum generation for episodic and step-based RL. [→ Pascal Klink 2020](#pascal-klink-2020)

## Evidence

### Pascal Klink 2020

Pascal Klink, Carlo D'Eramo, Jan Peters, Joni Pajarinen. (2020). Self-Paced Deep Reinforcement Learning. 34th Conference on Neural Information Processing Systems (NeurIPS 2020). [doi:10.48550/arXiv.2004.11812](https://doi.org/10.48550/arXiv.2004.11812)

`q1 · i?` · `causal · r2`

Authors' observation in the Ant environment section about applying SPRL to a policy network with 6464 parameters. They report fitting "a 6464-dimensional Gaussian" takes "up to 25 minutes per update on our hardware" and is prone to numerical instabilities, stressing the benefit of SPDL's step-based curriculum generation.

> "ﬁtting the new episodic policy (i.e. a 6464-dimensional Gaussian) to the generated samples requires signiﬁcantly more computation time than an update of a step-based policy, taking up to 25 minutes per update on our hardware. Furthermore, this step is prone to numerical instabilities due to the large covariance matrix that needs to be estimated."

## Discussion


## Related Claims
- [SPDL lets the agent escape the local optimum in the Ant environment where ALP-GMM and random curricula do not improve reward](spdl-escapes-local-optimum-ant.md) — related
- [In the sparse-reward ball-catching environment all curricula enable learning with similar reward, and initializing the context distribution does not significantly change performance](all-curricula-enable-learning-ball-catching.md) — related
