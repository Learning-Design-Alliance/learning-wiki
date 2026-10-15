---
type: claim
title: Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels
description: Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels
id: clustering-recovers-expert-bundles
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: muntasir-hoq-2026
    resource: "https://doi.org/10.48550/arxiv.2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: muntasir-hoq-2026-2
    resource: "https://arxiv.org/abs/2607.05409"
    title: "Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409"
    author: Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Agglomerative clustering reached a best bundle-level ARI of 0.605 with V-measure 0.933, and 76.4% of nearest-neighbor matches were same-bundle. [→ Muntasir Hoq 2026](#muntasir-hoq-2026)
`q2 i?` Most nearest-neighbor matches fell in the same expert bundle, with mismatches often reflecting broadly used patterns spanning topic boundaries. [→ Muntasir Hoq 2026 (2)](#muntasir-hoq-2026-2)

## Evidence

### Muntasir Hoq 2026

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409 [doi:10.48550/arxiv.2607.05409](https://doi.org/10.48550/arxiv.2607.05409)

`q2 · i?` · `design · r2`

Agglomerative hierarchical clustering with cosine distance and complete linkage on the PCEX knowledge vectors; the dendrogram preserved pairwise geometry with cophenetic correlation r = 0.819. ARI and V-measure were computed post hoc across distance-cut thresholds.

> "At thebundlelevel, the best ARI was 0.605 at 0.6 threshold with63clusters, indicating substantial agreement beyond chance."

### Muntasir Hoq 2026 (2)

Muntasir Hoq, Griffin Pitts, Zhangqi Duan, Arun Balajiee Lekshmi Narayanan, Mohammad Hassany, Andrew Lan, Peter Brusilovsky and Bita Akram. (2026). Automated Recommendation of Programming Learning Content Using Pattern-based Knowledge Components. CSEDM'26: 10th Educational Data Mining in Computer Science Education Workshop. https://arxiv.org/abs/2607.05409

`q2 · i?` · `design · r2`

Local neighborhood analysis identifying, for every program, its single nearest neighbor excluding self-matches and categorizing the match type. The authors note mismatches often reflect common control-flow patterns in Loops, Nested Loops, and Strings that span topics.

> "The distribution of nearest-neighbor types was: 76.4% same bundle, 11.9% same topic/different bundle, and 11.7% different topic."

## Discussion


## Related Claims
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](six-behavioral-learner-profiles-kmeans-plus.md) — related
- [Cluster analysis of student-AI dialogue identifies three distinct collaboration profiles: Delegated Reasoning, Concerted Interpretation, and Delegated Elaboration](three-human-ai-cps-profiles-dr-ci-de.md) — related
- [Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions](pattern-kc-retrieval-outperforms-baselines.md) — related
- [Visualization analysis indicates the learned graph topology recovers interpretable relational structures such as modular node clusters and directed dependency hierarchies](adaptive-g-ukt-learned-topology-interpretable.md) — related
