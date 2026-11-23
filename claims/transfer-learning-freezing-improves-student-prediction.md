---
type: claim
title: Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets
description: Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets
id: transfer-learning-freezing-improves-student-prediction
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

# Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using transfer learning notably reduces RMSE and MAE values and increases R² values for both the mathematics and Portuguese datasets compared with not using it. [→ Yan Zhao 2024](#yan-zhao-2024)

## Evidence

### Yan Zhao 2024

Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)

`q2 · i?` · `design · r2`

Numerical evaluation results shown in Figure 9 and Table 2, comparing ANN models with and without transfer learning on mathematics and Portuguese test sets. The article reports the transfer learning approach "notably reduces RMSE and MAE values and increases R ² values for both datasets"; no standardized effect size is printed.

> "The transfer learning approach notably reduces RMSE and MAE values and increases R ² values for both datasets, demonstrating its effectiveness in enhancing model prediction performance."

## Discussion


## Related Claims
- [Without transfer learning, an ANN trained on one K-means cluster generalizes poorly to the other cluster, especially for the mathematics dataset](cross-cluster-generalization-fails-without-transfer.md) — related
- [The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones](frozen-layer-count-depends-on-data-complexity-and-volume.md) — related
