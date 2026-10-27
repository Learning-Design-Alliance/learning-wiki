---
type: claim
title: Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies
description: Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies
id: cluster-instance-sampling-minimizes-grading-work
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: rebecka-weegar-peter-idestam-almquist-2024
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: rebecka-weegar-peter-idestam-almquist-2024-2
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The two strategies sampling single answers from clusters (cluster centroid, random cluster instance) required the least manual work for training data and corrections; full-cluster strategies required substantially more work. [→ Rebecka Weegar · Peter Idestam-Almquist 2024](#rebecka-weegar-peter-idestam-almquist-2024)
`q2 i?` Adding more training data did not always reduce total workload; for cluster centroid, combined grading and correcting effort was lowest with only ten training answers. [→ Rebecka Weegar · Peter Idestam-Almquist 2024 (2)](#rebecka-weegar-peter-idestam-almquist-2024-2)

## Evidence

### Rebecka Weegar · Peter Idestam-Almquist 2024

Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1

`q2 · i?` · `design · r2`

Numerical evaluation across six sampling strategies and sample sizes 10-100 (Fig. 4, Random Forest classifier, 20 clusters per question). Changing the number of clusters to 10, 30, and 40 gave similar results, with more variation between strategies than between cluster counts.

> "The least manual work for labeling training data and correcting incorrect scores ( nt + nc ) was required for the two strategies where clustering was applied and single answers were sampled from each cluster, the cluster centroid strategy, and the random cluster instance strategy."

### Rebecka Weegar · Peter Idestam-Almquist 2024 (2)

Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1

`q2 · i?` · `design · r2`

Results on sample sizes: larger samples raised classification accuracy but sometimes increased total workload, since extra training instances did not always yield a proportional drop in misclassifications.

> "But it was also clear that adding more training data sometimes increased the overall workload, in terms of grading and correcting. Sampling additional training instances did not always give to a corresponding decrease in the number of misclassifications."

## Discussion


## Related Claims
- [K-Means++ clustering of self-reported behavioral proxies yields six distinct, stable learner profiles (k = 6, Silhouette = 0.62)](six-behavioral-learner-profiles-kmeans-plus.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
- [Clustering and score suggestions each individually reduced average grading time per answer by 69%, and combining them gave the largest reduction of 73%](clustering-plus-score-suggestions-reduce-grading-time.md) — related
