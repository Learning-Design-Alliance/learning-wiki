---
type: claim
title: "Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models"
description: "Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models"
id: transformers-better-minority-class-sensitivity
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

# Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Transformer models reach about 68% overall score while classifying minority reflection classes better than shallow baselines, though most minority samples are still misclassified. [→ Zsolt Csibi 2026](#zsolt-csibi-2026)

## Evidence

### Zsolt Csibi 2026

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402 [doi:10.48550/arxiv.2605.02402](https://doi.org/10.48550/arxiv.2605.02402)

`q2 · i?` · `design · r2`

Fine-tuning experiment of two Hungarian transformers (hubert-base-cc, PULI-BERT-Large) on the essay dataset with stratified 5-fold cross-validation. Confusion matrices in Fig. 5c and 5d show "improved minority-class detection for transformer models compared to shallow baselines in these settings."

> "The best results with the transformer models are around≈68% overall score averaged over accuracy, F1-score, and ROC AUC metrics. However the transformer models are able to classify the minority classes better, as the confusion matrix in Fig. 5c and Fig. 5d presents."

## Discussion


## Related Claims
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — reports the opposite
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
