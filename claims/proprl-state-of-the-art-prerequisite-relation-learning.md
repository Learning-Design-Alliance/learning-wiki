---
type: claim
title: "ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline"
description: "ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline"
id: proprl-state-of-the-art-prerequisite-relation-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: xinghe-cheng-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03006"
    title: "Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006 [doi:10.48550/arxiv.2608.03006](https://doi.org/10.48550/arxiv.2608.03006)"
    author: Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` ProPRL outperforms the strongest baseline in every dataset–metric comparison on UCD, LectureBank, and MOOC in ACC, F1, and AUC. [→ Xinghe Cheng 2026](#xinghe-cheng-2026)

## Evidence

### Xinghe Cheng 2026

Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006 [doi:10.48550/arxiv.2608.03006](https://doi.org/10.48550/arxiv.2608.03006)

`q2 · i?` · `design · r2`

Benchmark comparison on three datasets (MOOC, LectureBank, UCD) against general-purpose and task-specific baselines; Table 1 reports ProPRL best on all nine combinations, with the largest relative AUC gain of 6.11% on UCD and improvements "from 1.96% to 6.11%".

> "ProPRL nev- ertheless outperforms the strongest baseline in every com- parison, demonstrating a consistent performance advantage across different evaluation settings."

## Discussion


## Related Claims
- [Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact](proprl-ablation-components-contribute.md) — related
- [ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference](proprl-acceptable-computational-overhead.md) — related
- [ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit](proprl-hyperparameter-sensitivity.md) — related
