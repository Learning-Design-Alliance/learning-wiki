---
type: claim
title: "In the four-cluster k-means partition, cluster Cl1 is the densest and best represented by its centroid, while Cl4 is the most spread out and Cl3's centroid represents it least"
description: "In the four-cluster k-means partition, cluster Cl1 is the densest and best represented by its centroid, while Cl4 is the most spread out and Cl3's centroid represents it least"
id: cluster-density-centroid-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2014
sources:
  - id: battaglia-2014
    resource: "https://doi.org/10.48550/arXiv.1512.08998"
    title: "Battaglia, Di Paola & Fazio. (2014). Cluster Analysis of Educational Data: an Example of Quantitative Study on the answers to an Open-Ended Questionnaire. Università di Palermo. [doi:10.48550/arXiv.1512.08998](https://doi.org/10.48550/arXiv.1512.08998)"
    author: "Battaglia, Di Paola & Fazio"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In the four-cluster k-means partition, cluster Cl1 is the densest and best represented by its centroid, while Cl4 is the most spread out and Cl3's centroid represents it least

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Cluster Cl1 has the highest average silhouette (0.750) and normalized centroid reliability (1.40), while Cl4 is the most spread out and C3 is the least representative centroid (r_norm = -0.92). [→ Battaglia 2014](#battaglia-2014)

## Evidence

### Battaglia 2014

Battaglia, Di Paola & Fazio. (2014). Cluster Analysis of Educational Data: an Example of Quantitative Study on the answers to an Open-Ended Questionnaire. Università di Palermo. [doi:10.48550/arXiv.1512.08998](https://doi.org/10.48550/arXiv.1512.08998)

`q2 · i?` · `associational · r2`

K-means partition of the N = 124 sample into four clusters (sizes 18, 19, 63, 24; Table II), with per-cluster silhouette values and the authors' normalized centroid-reliability index. The quote supports "cluster Cl1 is denser than the others"; Table II prints mean S from 0.750 (Cl1) down to 0.56 (Cl4) and r_norm from 1.40 (C1) to -0.92 (C3).

> "The (4)kS〈〉  value indicates that cluster Cl1 is denser than the others, and Cl4 is the most spread out."

## Discussion


## Related Claims
- [The k-means and hierarchical partitions of the same student sample are consistent, with the best agreement (VI = 0.28) between the four-cluster k-means solution and the six-cluster hierarchical solution](variation-of-information-method-agreement.md) — related
- [Under the reported settings, K-Means++ achieved the best internal clustering indices, though the K-Means baseline used a single initialization](kmeans-plus-best-benchmark.md) — related
