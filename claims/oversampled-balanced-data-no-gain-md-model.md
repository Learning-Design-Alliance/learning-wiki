---
type: claim
title: Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data
description: Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data
id: oversampled-balanced-data-no-gain-md-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-25
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: psyridou-2024
    resource: "https://doi.org/10.1037/edu0000835"
    title: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835"
    author: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` An MLP trained on an oversampled, balanced training dataset (approximately 1,100 cases per group) did not perform better than the model trained on the unbalanced data. [→ Psyridou 2024](#psyridou-2024)

## Evidence

### Psyridou 2024

Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835

`q2 · i?` · `associational · r2`

Supplementary sensitivity analysis (Appendix E) in which the MD group was oversampled in the training sample to about 1,100 cases per group, the model retrained, and performance evaluated on the unchanged testing dataset. Results are reported in the online supplemental materials.

> "the model with balanced data did not perform better than the model with the unbalanced data indicating that the unbalanced data might have better represented the real -world distribution of the target variable."

## Discussion


## Related Claims
- [A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818](mlp-kindergarten-predictors-md-grade6-auc-818.md) — related
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — reports the opposite
- [A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)](six-predictor-md-model-auc-776.md) — related
