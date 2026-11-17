---
type: claim
title: Hierarchical clustering with weighted average linkage yields a six-cluster partition of the sample under an Inconsistency Coefficient threshold of 1.25, and the Variation Ratio Criterion peaks at six clusters
description: Hierarchical clustering with weighted average linkage yields a six-cluster partition of the sample under an Inconsistency Coefficient threshold of 1.25, and the Variation Ratio Criterion peaks at six clusters
id: hierarchical-six-cluster-partition
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
    rigour: 1
  - id: battaglia-2014-2
    resource: "https://doi.org/10.48550/arXiv.1512.08998"
    title: "Battaglia, Di Paola & Fazio. (2014). Cluster Analysis of Educational Data: an Example of Quantitative Study on the answers to an Open-Ended Questionnaire. Università di Palermo. [doi:10.48550/arXiv.1512.08998](https://doi.org/10.48550/arXiv.1512.08998)"
    author: "Battaglia, Di Paola & Fazio"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Hierarchical clustering with weighted average linkage yields a six-cluster partition of the sample under an Inconsistency Coefficient threshold of 1.25, and the Variation Ratio Criterion peaks at six clusters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Applying a lower Inconsistency Coefficient threshold (Ik > 1.25) to the dendrogram produces six clusters. [→ Battaglia 2014](#battaglia-2014)
`q2 i?` The Variation Ratio Criterion attains its maximum for a six-cluster partition. [→ Battaglia 2014 (2)](#battaglia-2014-2)

## Evidence

### Battaglia 2014

Battaglia, Di Paola & Fazio. (2014). Cluster Analysis of Educational Data: an Example of Quantitative Study on the answers to an Open-Ended Questionnaire. Università di Palermo. [doi:10.48550/arXiv.1512.08998](https://doi.org/10.48550/arXiv.1512.08998)

`q2 · i?` · `associational · r1`

Agglomerative hierarchical clustering of the same N = 124 answer matrix using weighted average linkage (cophenetic coefficient 0.68). Reading the dendrogram with Inconsistency Coefficient threshold 1.25 produced "6 clusters" (α–ζ), which the authors call the more significant representation.

> "If, on the other hand, we introduce a lower threshold for the  Ik value, but still not producing a too high fragmentation, like for example 1.25kI> , we must disregard the green, dashed  links in the dendrogram in Figure 5, and obtain Figure 6, where 6 clusters are present."

### Battaglia 2014 (2)

Battaglia, Di Paola & Fazio. (2014). Cluster Analysis of Educational Data: an Example of Quantitative Study on the answers to an Open-Ended Questionnaire. Università di Palermo. [doi:10.48550/arXiv.1512.08998](https://doi.org/10.48550/arXiv.1512.08998)

`q2 · i?` · `associational · r1`

Validity check of the hierarchical partition using the Variation Ratio Criterion computed for different numbers of clusters; "The maximum value is obtained for q = 6", corroborating the six-cluster dendrogram reading.

> "In order to verify the validity of our choice  we also used the VRC (see Section II.C).  Figure 7 shows the VRC values for different numbers of clusters. The maximum value is obtained for q = 6."

## Discussion


## Related Claims
- [The k-means and hierarchical partitions of the same student sample are consistent, with the best agreement (VI = 0.28) between the four-cluster k-means solution and the six-cluster hierarchical solution](variation-of-information-method-agreement.md) — related
- [Affinity propagation clustering of gameplay attempts yielded an interpretable six-cluster solution (part.6)](affinity-propagation-six-cluster-solution.md) — related
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](six-behavioral-learner-profiles-kmeans-plus.md) — related
