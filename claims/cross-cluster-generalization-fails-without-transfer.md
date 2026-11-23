---
type: claim
title: Without transfer learning, an ANN trained on one K-means cluster generalizes poorly to the other cluster, especially for the mathematics dataset
description: Without transfer learning, an ANN trained on one K-means cluster generalizes poorly to the other cluster, especially for the mathematics dataset
id: cross-cluster-generalization-fails-without-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# Without transfer learning, an ANN trained on one K-means cluster generalizes poorly to the other cluster, especially for the mathematics dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predictive performance on the source cluster0 test set is significantly better than on the target cluster1, with the mathematics dataset showing a negative R² of -3.11 on cluster1. [→ Yan Zhao 2024](#yan-zhao-2024)

## Evidence

### Yan Zhao 2024

Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)

`q2 · i?` · `design · r2`

Numerical results in Table 1 (evaluation metrics without transfer learning): mathematics cluster1 RMSE 6.20, MAE 4.76, R² -3.11 versus cluster0 RMSE 4.79, MAE 3.67, R² -0.03. The article states the model's performance on cluster0 is "significantly better than on cluster1".

> "for cluster1, although the Portuguese dataset maintains relatively low RMSE and MAE values, the mathematics dataset shows significantly higher RMSE and MAE values, and the R² value is negative, indicating poor predictive performance on this subset."

## Discussion


## Related Claims
- [Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets](transfer-learning-freezing-improves-student-prediction.md) — related
- [K-means with the Elbow method determines an optimal cluster count of two for both the mathematics and Portuguese datasets](kmeans-elbow-optimal-two-clusters.md) — related
