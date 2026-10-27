---
type: claim
title: In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1
description: In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1
id: shallow-ablation-balancing-embeddings
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
  - id: zsolt-csibi-2026-2
    resource: "https://arxiv.org/abs/2605.02402"
    title: "Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402"
    author: Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models without class balancing achieved better results in every metric than models with class balancing on this dataset. [→ Zsolt Csibi 2026](#zsolt-csibi-2026)
`q2 i?` Semantic embeddings improved ROC-AUC significantly while accuracy and F1 were better without them. [→ Zsolt Csibi 2026 (2)](#zsolt-csibi-2026-2)

## Evidence

### Zsolt Csibi 2026

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402 [doi:10.48550/arxiv.2605.02402](https://doi.org/10.48550/arxiv.2605.02402)

`q2 · i?` · `design · r2`

Ablation study (Table 2) averaging 5-fold cross-validated results over shallow models with and without class balancing, oversampling and semantic embeddings. The article attributes the pattern to models learning the class distribution well without additional techniques.

> "One finding is that the models without class balancing achieved better results in every metric compared to the models with class balancing."

### Zsolt Csibi 2026 (2)

Zsolt Csibi, Kristian Fenech, Mónika Sándor, Mónika Serfőző, Kinga Gyöngy. (2026). Automatic Reflection Level Classification in Hungarian Student Essays. https://arxiv.org/abs/2605.02402

`q2 · i?` · `design · r2`

Same shallow-model ablation (Table 2). The article reports embeddings helped models "distinguish between the classes better" while accuracy and F1 favoured non-embedding settings.

> "The usage of semantic embeddings improved the ROC-AUC scores of the models significantly, however the accuracy and F1-scores were better without using semantic embeddings."

## Discussion


## Related Claims
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — reports the opposite
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [T-tests show no significant shallow-vs-transformer difference in accuracy, weighted F1 or macro-F1, but a significant ROC-AUC advantage for the shallow model](ttest-roc-auc-advantage-shallow.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — related
- [Class balancing techniques improved fairness in education prediction tasks, with over-sampling also improving accuracy](class-balancing-improves-fairness.md) — reports the opposite
