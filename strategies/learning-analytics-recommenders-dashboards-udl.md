---
type: strategy
id: learning-analytics-recommenders-dashboards-udl
title: Use cluster-derived usage patterns to drive machine-learning recommender systems and educator/learner dashboards for individualized support
description: "The article proposes that identifying usage-pattern clusters is a starting point for individualized learning support: recommender systems could suggest, for example, more advanced tasks without assistance, while dashb..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
sources:
  - id: marvin-roski-2024
    resource: "https://doi.org/10.1016/j.compedu.2024.105028"
    title: "Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring. (2024). Learning analytics and the Universal Design for Learning (UDL): A clustering approach. Computers & Education 214 (2024) 105028. https://doi.org/10.1016/j.compedu.2024.105028"
    author: Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring
---

# Use cluster-derived usage patterns to drive machine-learning recommender systems and educator/learner dashboards for individualized support

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article proposes that identifying usage-pattern clusters is a starting point for individualized learning support: recommender systems could suggest, for example, more advanced tasks without assistance, while dashboards give educators and learners insight into the learning process. Clustering lets teachers "see immediately if one group tends to under-utilize learning opportunities", and learners can receive cluster-based feedback to improve self-regulated learning.

## Design Implications

### Context
#### Requirements
- Log-file data capturing usage of UDL-guided elements that require a learner decision, plus clustering of usage patterns to form actionable groups
#### Constraints
- The results do not provide insight into learning outcomes of individual learners based on their usage patterns, nor do they imply the best learning path through the platform for each learner

### Target Learners
- Ninth- and tenth-grade inclusive chemistry learners (K-12)

### Target Learning Goals
- Conceptual knowledge of ion bonding
- Self-regulated learning

## Claims

- [K-means clustering on EFA-derived features yields six learner groups with distinct usage patterns of UDL-guided elements](../claims/kmeans-six-learner-clusters-udl-elements.md) [+W]
- [Clusters differ in learner characteristics: Cluster 2 and 5 differ in chemistry self-concept and interest, Cluster 0 shows higher reading ability, and Cluster 1 shows below-average post-test scores](../claims/cluster-learner-characteristic-differences.md) [+W]
- [The six clusters differ substantially in usage duration of UDL-guided elements, with the small Cluster 2 investing particularly more time than Cluster 1](../claims/cluster-usage-duration-differences.md) [+W]
- [The largest cluster of learners invests minimally in the platform and shows almost no gain in conceptual knowledge](../claims/cluster1-minimal-investment-no-knowledge-gain.md) [+W]
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](../claims/six-behavioral-learner-profiles-kmeans-plus.md) [+W]

## Related Strategies

- [Use early-session timing signals, interpreted relative to proficiency, to identify students needing adaptive support](early-session-timing-signals-target-adaptive-support.md)
- [Use clustering of LMS interaction patterns to identify at-risk students early.](cluster-lms-patterns-to-identify-at-risk-students.md)

## Examples
-

## Key Sources
- Marvin Roski, Ratan Sebastian, Ralph Ewerth, Anett Hoppe, Andreas Nehring. (2024). Learning analytics and the Universal Design for Learning (UDL): A clustering approach. Computers & Education 214 (2024) 105028. https://doi.org/10.1016/j.compedu.2024.105028
