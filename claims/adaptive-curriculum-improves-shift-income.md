---
type: claim
title: "An adaptive curriculum targeting the policy's measured weaknesses raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates"
description: "An adaptive curriculum targeting the policy's measured weaknesses raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates"
id: adaptive-curriculum-improves-shift-income
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: haoqiang-kang-2026
    resource: "https://doi.org/10.48550/arXiv.2609.19801"
    title: "Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. [doi:10.48550/arXiv.2609.19801](https://doi.org/10.48550/arXiv.2609.19801)"
    author: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: haoqiang-kang-2026-2
    resource: "https://doi.org/10.48550/arXiv.2609.19801"
    title: "Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. [doi:10.48550/arXiv.2609.19801](https://doi.org/10.48550/arXiv.2609.19801)"
    author: Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An adaptive curriculum targeting the policy's measured weaknesses raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The adaptive curriculum raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates. [→ Haoqiang Kang 2026](#haoqiang-kang-2026)
`q2 i?` Targeted practice yields gains of 16, 18, and 26 percentage points over uniform sampling on traffic compliance, obstacle recovery, and multi-order planning probes. [→ Haoqiang Kang 2026 (2)](#haoqiang-kang-2026-2)

## Evidence

### Haoqiang Kang 2026

Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. [doi:10.48550/arXiv.2609.19801](https://doi.org/10.48550/arXiv.2609.19801)

`q2 · i?` · `causal · r1`

Curriculum experiment (RQ3) comparing adaptive, uniform, static, and random-targeting sampling under the same safety reward and rollout budget. The adaptive condition "raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates".

> "Figure 5(A) shows that the adaptive curriculum raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates."

### Haoqiang Kang 2026 (2)

Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin. (2026). DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum. Preprint. [doi:10.48550/arXiv.2609.19801](https://doi.org/10.48550/arXiv.2609.19801)

`q2 · i?` · `design · r2`

Probe-assertion scores on fixed training probes: "gains of 16, 18, and 26 percentage points over uniform sampling" on traffic compliance, obstacle recovery, and multi-order planning probes, covering both rerouting and coordinating deliveries under shared constraints.

> "Figure 5(B) shows gains of 16, 18, and 26 percentage points over uniform sampling on traffic compliance, obstacle recovery, and multi-order planning probes at their measured phase endpoints."

## Discussion


## Related Claims
- [Training sequences sampled from an optimized time-varying word distribution yield significantly higher generalization accuracy than frequency-based and uniform baselines in a connectionist reading model](optimized-word-sequence-beats-frequency-baselines-reading-ann.md) — related
- [An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus](instance-level-curriculum-sample-efficiency.md) — related
- Scaling training environments improves shift income under a fixed interaction budget: a 47% gain from scaling the task pool within one city and a 61% gain from scaling from one to eight training maps — related
