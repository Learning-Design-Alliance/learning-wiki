---
type: claim
title: ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit
description: ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit
id: proprl-hyperparameter-sensitivity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Performance improves as propagation depth k increases from zero, with gains becoming limited once k reaches approximately 5; the learning rate has a substantially stronger effect, with best performance around 10^-4. [→ Xinghe Cheng 2026](#xinghe-cheng-2026)

## Evidence

### Xinghe Cheng 2026

Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006 [doi:10.48550/arxiv.2608.03006](https://doi.org/10.48550/arxiv.2608.03006)

`q2 · i?` · `design · r2`

Hyperparameter study (Figure 4) over propagation coefficient α, depth k, anti-symmetry weight λ, and learning rate. The effect of α is dataset-dependent (MOOC favors smaller α, UCD a moderate value); the article states ProPRL "requiresanappropriatelysmalllearning rate for reliable optimization".

> "The improvements become limited oncekreaches approximately 5, sug-gesting that a moderate propagation depth captures most of the useful multi-hop behavioral dependencies"

## Discussion


## Related Claims
- [Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact](proprl-ablation-components-contribute.md) — related
- [ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference](proprl-acceptable-computational-overhead.md) — related
- Task F1 saturates by K≈4 concepts and is insensitive to hidden dimension once d≥384, while learning rate forms a sharp inverted-U with collapse at LR≥10−3 — related
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related
- [ProPRL ranks first across all nine dataset–metric combinations on three prerequisite relation benchmarks, with relative improvements from 1.96% to 6.11% over the strongest baseline](proprl-state-of-the-art-prerequisite-relation-learning.md) — related
