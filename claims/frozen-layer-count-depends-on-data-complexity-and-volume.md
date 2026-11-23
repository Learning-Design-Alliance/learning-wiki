---
type: claim
title: "The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones"
description: "The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones"
id: frozen-layer-count-depends-on-data-complexity-and-volume
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
  - id: yan-zhao-2024-2
    resource: "https://doi.org/10.1109/aiea62095.2024.10692712"
    title: "Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)"
    author: Yan Zhao, Pengbo Wang, Hao Wang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the mathematics dataset, freezing more layers (the third layer) gave the best results (RMSE 4.57, MAE 3.65, R² -1.24), while for the Portuguese dataset freezing fewer layers (the first layer) was best (RMSE 2.69, MAE 2.15, R² 0.02). [→ Yan Zhao 2024](#yan-zhao-2024)
`q1 i?` The authors interpret this pattern as reflecting data complexity and target-domain data volume: freezing more layers helps prevent overfitting with small or noisy data, while freezing fewer layers allows better use of larger, simpler data. [→ Yan Zhao 2024 (2)](#yan-zhao-2024-2)

## Evidence

### Yan Zhao 2024

Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)

`q2 · i?` · `design · r2`

Numerical comparison across frozen-layer counts (1, 2, 3) in Table 2 after 100 epochs of fine-tuning. The mathematics dataset favored freezing three layers; the Portuguese dataset favored freezing one layer. No standardized effect size is printed.

> "For the mathematics dataset, the optimal results were achieved by freezing the third layer, yielding an RMSE of 4.57, MAE of 3.65, and R ² of -1.24. For the Portuguese dataset, the best results were obtained by freezing the first layer, with an RMSE of 2.69, MAE of 2.15, and R² of 0.02."

### Yan Zhao 2024 (2)

Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. [doi:10.1109/aiea62095.2024.10692712](https://doi.org/10.1109/aiea62095.2024.10692712)

`q1 · i?` · `design · r2`

Authors' interpretation (type e) of the Table 2 pattern, attributing it to target-domain data volume (Portuguese 122 entries, mathematics 64 entries) and data complexity/noise. This is the authors' explanation, not a separately tested result.

> "When the data volume is small, freezing more layers helps prevent overfitting and enhances generalization. With larger data volumes, freezing fewer layers allows the model to adequately train on new data, improving performance."

## Discussion


## Related Claims
- [Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets](transfer-learning-freezing-improves-student-prediction.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — reports the opposite
- [Single-layer sequence encoders with 768-dimensional embeddings consistently achieved the best probe performance; added transformer depth degraded results](single-layer-768-dim-encoder-best.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
