---
type: claim
title: In a restrictive mastery-based online learning system, a purely theory-based distance metric produced better module-level trace clusters than data-driven and hybrid metrics
description: In a restrictive mastery-based online learning system, a purely theory-based distance metric produced better module-level trace clusters than data-driven and hybrid metrics
id: theory-based-distance-metric-outperforms-data-driven-clustering
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: tom-zhang-2022
    resource: "https://doi.org/10.1145/3506860.3506887"
    title: Tom Zhang 2022
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a restrictive mastery-based online learning system, a purely theory-based distance metric produced better module-level trace clusters than data-driven and hybrid metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The theory-based method outperformed data-driven and hybrid distance methods on average silhouette and interpretability for module-level clustering. [→ Tom Zhang 2022](#tom-zhang-2022)

## Evidence

### Tom Zhang 2022

Tom Zhang, Michelle Taub, and Zhongzhou Chen. 2022. A Multi-level Trace Clustering Analysis Scheme for Measuring Students' Self-Regulated Learning Behavior in a Mastery-Based Online Learning Environment. In LAK22: 12th International Learning Analytics and Knowledge Conference (LAK22). ACM, New York, NY, USA. [doi:10.1145/3506860.3506887](https://doi.org/10.1145/3506860.3506887)

`q2 · i?` · `design · r2`

Comparison of three distance-metric strategies for hierarchical agglomerative clustering of 5960 module-level traces from 26 OLM modules, evaluated by average silhouette. The theory-based method reached "a local maximum average silhouette of over 0.8 at 7 clusters" while the data-driven method peaked at 0.7 and the hybrid method showed no local maximum under 10 clusters.

> "The theory-based method outperformed the other two methods with a local maximum average silhouette of over 0.8 at 7 clusters. The purely data-driven method had a local maximum of 0.7 at three clusters, while the average silhouette of the hybrid method did not reach a local maximum in under 10 clusters."

## Discussion


## Related Claims
- [Data-driven and hybrid trace clustering failed to separate study from no-study traces and normal from short attempts in a restrictive system](data-driven-clustering-fails-restrictive-systems.md) — possibly the same claim (merge candidate)
- [A hybrid K-Means/HDBSCAN clustering method outperforms K-Means and HDBSCAN alone on silhouette score and Davies-Bouldin Index for physics strategy essays](hybrid-clustering-outperforms-kmeans-hdbscan-essays.md) — related
