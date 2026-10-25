---
type: claim
title: Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays
description: Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays
id: shallow-ml-best-overall-hungarian-reflection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The best shallow model (SMOTEBoost + Qwen3 embeddings + decision tree with 12 maximum depth) achieved 0.7176 overall score averaged over accuracy, F1 and ROC-AUC across 5 folds. [→ Zsolt Csibi 2026](#zsolt-csibi-2026)

## Evidence

### Zsolt Csibi 2026

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402 [doi:10.48550/arxiv.2605.02402](https://doi.org/10.48550/arxiv.2605.02402)

`q2 · i?` · `design · r2`

5-fold cross-validated experiment on the Hungarian essay dataset comparing shallow models with balancing techniques and engineered features. The best SMOTEBoost configuration reached "an average score of 0.7176" with 0.7089 accuracy, 0.6808 F1 and 0.7633 ROC-AUC.

> "This model achieved an average score of 0.7176(averaged over the 3 metrics), with 0.7089 mean accuracy (with 0.0263 standard deviation), 0.6808 mean F1-score (with 0.0309 standard deviation) and 0.7633 mean ROC-AUC score (with 0.0285 standard deviation) averaged over the 5 folds."

## Discussion


## Related Claims
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — reports the opposite
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — related
- [Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models](transformers-better-minority-class-sensitivity.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — related
