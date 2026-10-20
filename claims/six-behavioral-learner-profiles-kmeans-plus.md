---
type: claim
title: K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)
description: K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)
id: six-behavioral-learner-profiles-kmeans-plus
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: najem-2026
    resource: "https://doi.org/10.1007/s44217-026-02181-7"
    title: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7"
    author: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: najem-2026-2
    resource: "https://doi.org/10.1007/s44217-026-02181-7"
    title: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7"
    author: "Najem, K., Zaoui Seghroucheni, Y., & Ziti, S."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Unsupervised clustering of 12 behavioral, psychological, and environmental features identified six learner profiles ranging from Highly Engaged Achievers to At-Risk Learners. [→ Najem 2026](#najem-2026)
`q2 i?` The clustering solution was stable across 10 independent runs (mean ARI = 0.94, SD = 0.03; centroid displacement < 0.02 normalized units). [→ Najem 2026 (2)](#najem-2026-2)

## Evidence

### Najem 2026

Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7

`q2 · i?` · `associational · r2`

Secondary analysis of a 14,003-record anonymized dataset using K-Means++ (k = 6) on 12 self-reported behavioral, psychological, and environmental inputs; the article reports "six distinct learner profiles" (C0–C5), with Silhouette = 0.62 described as acceptable for educational data mining.

> "Unsupervised clustering techniques were applied to the preprocessed data set, which resulted in the identification of six distinct learner profiles, based on unique combinations of behavioral, psychological, and performance traits."

### Najem 2026 (2)

Najem, K., Zaoui Seghroucheni, Y., & Ziti, S. (2026). Behavioral clustering for adaptive learning object recommendation in higher education using learning analytics for personalized student success. Discover Education. https://doi.org/10.1007/s44217-026-02181-7

`q2 · i?` · `associational · r1`

Stability analysis over 10 independent K-Means++ runs with different random seeds; the article reports "mean Adjusted Rand Index (ARI)" of 0.94 (SD = 0.03) and centroid displacement under 0.02 normalized units.

> "Across runs, the mean Adjusted Rand Index (ARI) between pairwise cluster assignments was 0.94 (SD = 0.03), and the average centroid displacement was less than 0.02 normalized units, indicating high stability and reproducibility of the clustering solution"

## Discussion


## Related Claims

- [Under the reported settings, K-Means++ achieved the best internal clustering indices, though the K-Means baseline used a single initialization](kmeans-plus-best-benchmark.md) — possibly the same claim (merge candidate)
- [Cluster analysis identifies three stable learner profiles: Engaged and Literate, Uncritical Reliant, and Skeptical Minimal users](three-genai-learner-profiles.md) — related
- [K-means clustering of K–8 students' platform trace data yields seven distinct engagement profiles](seven-engagement-profiles-k8-elearning.md) — related
- [Exploratory K-means clustering identifies four heterogeneous student AI-user profiles differing in experience, competence, usefulness, trust, and control, but the solution's optimality and stability are not established](exploratory-four-cluster-student-ai-profiles.md) — related
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](clustering-recovers-expert-bundles.md) — related
- [Cluster analysis across both studies identifies three meta-attention knowledge profiles, including an overconfident group with a self-knowledge/strategy mismatch](makq-three-meta-attention-profiles.md) — related
- [Affinity propagation clustering of gameplay attempts yielded an interpretable six-cluster solution (part.6)](affinity-propagation-six-cluster-solution.md)
- [K-means clustering of standardized prior knowledge and final grades yields four performance profiles: Consistent Achievers, Growing Achievers, Declining Performers, and Struggling Performers](four-kmeans-achievement-trajectory-profiles.md) — related
- [Teachers' post-workshop platform engagement fell into three behavioral profiles, with most teachers showing minimal creation and browsing](three-behavioral-engagement-profiles-ai-agent-creation.md) — related
