---
type: claim
title: "GNN training homogenizes concept representations, with 62.7% of prerequisite pairs becoming increasingly similar during DGCPL training"
description: "GNN training homogenizes concept representations, with 62.7% of prerequisite pairs becoming increasingly similar during DGCPL training"
id: gnn-training-homogenizes-concept-representations
status: review
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

# GNN training homogenizes concept representations, with 62.7% of prerequisite pairs becoming increasingly similar during DGCPL training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Prerequisite pairs, labeled negative pairs, and random non-edges exhibit similarly high initial semantic similarities, and GNN training increases the similarity of many concept pairs, progressively homogenizing their representations. [→ Xinghe Cheng 2026](#xinghe-cheng-2026)

## Evidence

### Xinghe Cheng 2026

Xinghe Cheng, Jiapu Wang, Chaobo He, Ruihai Dong, Quanlong Guan. (2026). ProPRL: Property-Aware Prerequisite Relation Learning in Educational Knowledge Graphs. arXiv preprint. https://arxiv.org/abs/2608.03006 [doi:10.48550/arxiv.2608.03006](https://doi.org/10.48550/arxiv.2608.03006)

`q2 · i?` · `design · r2`

Motivating observational analysis (Figure 1) of representation similarity in pretrained semantic space and during DGCPL training; the figure caption reports that "62.7% of prerequisite pairs become increasingly similar". This motivates explicit modeling of directional asymmetry, multi-hop evidence, and pair-specific relevance.

> "Figure1(b) further shows that GNN training significantly increasesthesimilarityofmanyconceptpairs,progressively homogenizingtheirrepresentations."

## Discussion


## Related Claims
- [ProPRL incurs moderate overhead over DGCPL but remains lightweight, using under 40 MB GPU memory and under 0.18 seconds test-time inference](proprl-acceptable-computational-overhead.md) — related
- [The greedy cycle-break algorithm functions as a safety mechanism: none of the five evaluation topics required prerequisite-edge removal](cycle-break-safety-mechanism-concept-graphs.md) — related
