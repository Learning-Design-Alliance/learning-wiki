---
type: claim
title: K-means with the Elbow method determines an optimal cluster count of two for both the mathematics and Portuguese datasets
description: K-means with the Elbow method determines an optimal cluster count of two for both the mathematics and Portuguese datasets
id: kmeans-elbow-optimal-two-clusters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: yan-zhao-2024
    resource: "https://doi.org/10.1109/aiea62095.2024.10692712"
    title: "Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)"
    author: Yan Zhao, Pengbo Wang, Hao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# K-means with the Elbow method determines an optimal cluster count of two for both the mathematics and Portuguese datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using the Elbow algorithm on the WCSS-versus-k plot, the optimal K value was determined to be 2 for both datasets. [→ Yan Zhao 2024](#yan-zhao-2024)

## Evidence

### Yan Zhao 2024

Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)

`q2 · i?` · `design · r2`

Preprocessing step (Figure 1): WCSS was computed for different k values and plotted; the elbow at k = 2 was chosen for both the mathematics and Portuguese datasets to produce subsets with different distributions. PCA to two dimensions was used for visualization (Figure 2).

> "Based on this method, the optimal K value was determined to be 2 for both datasets, as the gradient is highest at this point, indicating that dividing the dataset into two clusters is the most reasonable."

## Discussion


## Related Claims
- [Without transfer learning, an ANN trained on one K-means cluster generalizes poorly to the other cluster, especially for the mathematics dataset](cross-cluster-generalization-fails-without-transfer.md) — related
- [AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training](aoi-metrics-classify-novice-skill-levels-early-training.md) — related
- [Students' interactions with the EWA cluster into two patterns: one emphasising outline planning and essay structure, the other content development](ewa-two-interaction-clusters-structure-content.md) — related
- [K-means clustering of self-reported resource usage identifies four student classes, from peer-and-helproom users to students using all resources including AI everywhere](four-resource-usage-clusters-physics.md) — related
