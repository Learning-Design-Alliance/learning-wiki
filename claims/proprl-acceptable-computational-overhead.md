---
type: claim
title: ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference
description: ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference
id: proprl-acceptable-computational-overhead
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: xinghe-cheng-2026
    resource: "https://arxiv.org/abs/2608.03006"
    title: "Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006"
    author: Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Compared with DGCPL, ProPRL has a larger model (2.68M vs 1.89M parameters) and more training time, but is faster at inference on MOOC and UCD and slower on LectureBank. [→ Xinghe Cheng 2026](#xinghe-cheng-2026)

## Evidence

### Xinghe Cheng 2026

Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006

`q2 · i?` · `design · r2`

Efficiency comparison (Table 3) of ProPRL and DGCPL on the original data splits. ProPRL is "fasterthanDGCPLonMOOCandUCD,althoughitrequires more inference time on LectureBank"; the authors conclude the overhead is acceptable.

> "Nevertheless, ProPRL remains lightweight, using less than 40 MB of GPU memory on all datasets and requir-inglessthan0.18secondsfortest-timeinference."

## Discussion


## Related Claims
- [GNN training homogenizes concept representations, with 62.7% of prerequisite pairs becoming increasingly similar during DGCPL training](gnn-training-homogenizes-concept-representations.md) — related
- [ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit](proprl-hyperparameter-sensitivity.md) — related
- [ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline](proprl-state-of-the-art-prerequisite-relation-learning.md) — related
- [The linearity bias heuristic enables robust alignment with low-dimensional embeddings on standard CPUs, lowering computational prerequisites](linearity-bias-lowers-computational-prerequisites.md) — related
