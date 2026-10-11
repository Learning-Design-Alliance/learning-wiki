---
type: claim
title: Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact
description: Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact
id: proprl-ablation-components-contribute
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
    kind: causal
    rigour: 1
---

# Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Ablating multi-hop propagation, the pair-conditioned gate, or the irreversibility constraint each consistently lowers F1; removing multi-hop propagation drops UCD F1 from 0.8788 to 0.7831. [→ Xinghe Cheng 2026](#xinghe-cheng-2026)

## Evidence

### Xinghe Cheng 2026

Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006

`q2 · i?` · `causal · r1`

Ablation study (Table 2, F1-score) on UCD, LectureBank, and MOOC. Multi-hop propagation removal causes "the most pronounced degradation on UCD, decreasing the F1-score from 0.8788 to 0.7831"; gate removal hurts MOOC most, anti-symmetry removal hurts LectureBank most.

> "Removing any component consistently reduces the F1-score across all three datasets, confirming that each component contributes positivelytothecompletemodel."

## Discussion


## Related Claims
- [ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit](proprl-hyperparameter-sensitivity.md) — related
- [ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline](proprl-state-of-the-art-prerequisite-relation-learning.md) — related
- [Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging](rec-cbm-ablation-components-complementary.md) — related
