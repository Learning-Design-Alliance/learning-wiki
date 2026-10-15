---
type: claim
title: For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it
description: For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it
id: transformer-ablation-oversampling-freezing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zsolt-csibi-2026
    resource: "https://doi.org/10.48550/arxiv.2605.02402"
    title: "Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402 [doi:10.48550/arxiv.2605.02402](https://doi.org/10.48550/arxiv.2605.02402)"
    author: Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both oversampling and data augmentation are associated with higher average transformer performance, with relative gains of 22% and 26% overall respectively, while freezing the backbone decreased overall performance by 12%. [→ Zsolt Csibi 2026](#zsolt-csibi-2026)

## Evidence

### Zsolt Csibi 2026

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402 [doi:10.48550/arxiv.2605.02402](https://doi.org/10.48550/arxiv.2605.02402)

`q2 · i?` · `design · r2`

Transformer ablation (Table 5) averaged over the 2 transformer models and hyperparameter settings, reporting ROS at 0.6029 overall (22%↑), backtranslation at 0.6412 (26%↑) and freeze encoder at 0.4786 (-12%↓) relative to baseline. The article states "freezing the backbone during training significantly decreased the performance".

> "However, freezing the backbone during training significantly decreased the performance of the models, which shows the importance of full fine-tuning when adapting transformer models to specific tasks."

## Discussion


## Related Claims
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — related
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models](transformers-better-minority-class-sensitivity.md) — related
- Removing unsupervised pre-training hurts performance across all tasks, causing a 14.8% decrease relative to the full model — related
