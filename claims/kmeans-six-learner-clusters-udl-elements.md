---
type: claim
title: K-means clustering on EFA-derived features yields six learner groups with distinct usage patterns of UDL-guided elements
description: K-means clustering on EFA-derived features yields six learner groups with distinct usage patterns of UDL-guided elements
id: kmeans-six-learner-clusters-udl-elements
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: marvin-roski-2024
    resource: "https://doi.org/10.1016/j.compedu.2024.105028"
    title: "Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring. (2024). Learning analytics and the Universal Design for Learning (UDL): A clustering approach. Computers & Education 214 (2024) 105028. https://doi.org/10.1016/j.compedu.2024.105028"
    author: Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# K-means clustering on EFA-derived features yields six learner groups with distinct usage patterns of UDL-guided elements

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using silhouette score, BIC and AIC, the optimal k-means solution had six clusters, with a silhouette score of 0.506 and cluster sizes ranging from 7 to 226 learners. [→ Marvin Roski 2024](#marvin-roski-2024)

## Evidence

### Marvin Roski 2024

Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring. (2024). Learning analytics and the Universal Design for Learning (UDL): A clustering approach. Computers & Education 214 (2024) 105028. https://doi.org/10.1016/j.compedu.2024.105028

`q2 · i?` · `associational · r2`

Unsupervised k-means clustering (scikit-learn defaults, ten initializations, maximum 300 iterations) was run on four weighted-sum-score features derived from the EFA factors for 384 learners. The silhouette score for the six clusters was 0.506; the largest cluster contained 226 learners (58.9%) and the smallest 7 (1.8%).

> "When comparing the silhouette score and BIC/AIC at different numbers of clusters, the silhouette score shows a maximum at k = 6, and the BIC/AIC shows a minimum at the same number of clusters"

## Discussion


## Related Claims
- [The six clusters differ substantially in usage duration of UDL-guided elements, with the small Cluster 2 investing particularly more time than Cluster 1](cluster-usage-duration-differences.md) — related
- [The largest cluster of learners invests minimally in the platform and shows almost no gain in conceptual knowledge](cluster1-minimal-investment-no-knowledge-gain.md) — related
- [Exploratory factor analysis of 384 learners' log data identifies four factors in usage of UDL-guided elements, indicating learners remain consistent in decisions such as video vs. text and tasks with or without help](efafour-factors-udl-usage-consistency.md) — related
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](six-behavioral-learner-profiles-kmeans-plus.md) — related
- [K-means clustering of K–8 students' platform trace data yields seven distinct engagement profiles](seven-engagement-profiles-k8-elearning.md) — related
