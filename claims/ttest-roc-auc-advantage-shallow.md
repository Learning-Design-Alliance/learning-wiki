---
type: claim
title: T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model
description: T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model
id: ttest-roc-auc-advantage-shallow
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: zsolt-csibi-2026
    resource: "https://arxiv.org/abs/2605.02402"
    title: "Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402"
    author: Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 5 folds, differences in Accuracy (t = −0.0464, p = 0.9652), Weighted F1 (t = 0.2862, p = 0.7889) and Macro-F1 (t = −0.9815, p = 0.3819) were not significant, while ROC-AUC differed significantly (t = 5.5053, p = 0.0053) favouring the shallow model. [→ Zsolt Csibi 2026](#zsolt-csibi-2026)

## Evidence

### Zsolt Csibi 2026

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402

`q2 · i?` · `design · r2`

Statistical significance section comparing the best shallow model (SMOTEBoost + Qwen3 embeddings) and the best transformer (PULI-BERT-Large with backtranslation and cross-entropy) via T-test across 5 folds. The ROC-AUC difference was "statistically significant" favouring the shallow model.

> "In contrast, a statistically significant difference was found for ROC-AUC (t =5.5053, p =0.0053), where the shallow model achieved higher scores than the transformer model."

## Discussion


## Related Claims
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [Hungarian transformer models achieve slightly lower overall score (about 68%) but better minority-class sensitivity than shallow models](transformers-better-minority-class-sensitivity.md) — reports the opposite
