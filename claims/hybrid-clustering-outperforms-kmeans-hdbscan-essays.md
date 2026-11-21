---
type: claim
title: A hybrid K-Means/HDBSCAN clustering method outperforms K-Means and HDBSCAN alone on silhouette score and Davies-Bouldin Index for physics strategy essays
description: A hybrid K-Means/HDBSCAN clustering method outperforms K-Means and HDBSCAN alone on silhouette score and Davies-Bouldin Index for physics strategy essays
id: hybrid-clustering-outperforms-kmeans-hdbscan-essays
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: winter-allen-2025
    resource: "https://doi.org/10.48550/arXiv.2504.08904"
    title: "Winter Allen, N. Sanjay Rebello. (2025). Exploring the Feasibility of Employing a Hybrid Machine Learning Method to Unpack Student Reasoning Patterns in Physics Essays. [doi:10.48550/arXiv.2504.08904](https://doi.org/10.48550/arXiv.2504.08904)"
    author: Winter Allen, N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A hybrid K-Means/HDBSCAN clustering method outperforms K-Means and HDBSCAN alone on silhouette score and Davies-Bouldin Index for physics strategy essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the same set of student strategy essays, the hybrid method achieved the highest silhouette score (0.417) and lowest Davies-Bouldin Index (0.172), outperforming K-Means (SS 0.045, DBI 3.844) and HDBSCAN (SS 0.087, DBI 1.808). [→ Winter Allen 2025](#winter-allen-2025)

## Evidence

### Winter Allen 2025

Winter Allen, N. Sanjay Rebello. (2025). Exploring the Feasibility of Employing a Hybrid Machine Learning Method to Unpack Student Reasoning Patterns in Physics Essays. [doi:10.48550/arXiv.2504.08904](https://doi.org/10.48550/arXiv.2504.08904)

`q2 · i?` · `design · r2`

Numerical evaluation of three clustering methods (K-Means, HDBSCAN, hybrid) on the same 1018 cleaned essay responses, reported in Table 2. The hybrid method's SS of 0.417 and DBI of 0.172 exceeded K-Means (0.045, 3.844) and HDBSCAN (0.087, 1.808); the article states the hybrid "outperforms both methods substantially".

> "Finally, the hybrid method outperforms both methods substantially, with the highest SS and lowest DBI."

## Discussion


## Related Claims
- [Under the reported settings, K-Means++ achieved the best internal clustering indices, though the K-Means baseline used a single initialization](kmeans-plus-best-benchmark.md) — related
- [In a restrictive mastery-based online learning system, a purely theory-based distance metric produced better module-level trace clusters than data-driven and hybrid metrics](theory-based-distance-metric-outperforms-data-driven-clustering.md) — related
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](six-behavioral-learner-profiles-kmeans-plus.md) — related
- [k-means and k-medoids clustering merged conceptually distinct mechanistic reasoning types, making them less effective than HDBSCAN for this data](kmeans-kmedoids-merged-distinct-reasoning-types.md) — related
