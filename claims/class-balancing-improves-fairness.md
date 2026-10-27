---
type: claim
title: Class balancing techniques improved fairness in education prediction tasks, with over-sampling also improving accuracy
description: Class balancing techniques improved fairness in education prediction tasks, with over-sampling also improving accuracy
id: class-balancing-improves-fairness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: jamiu-adekunle-idowu-2024
    resource: "https://doi.org/10.1007/s40593-023-00389-4"
    title: "Jamiu Adekunle Idowu. (2024). Debiasing Education Algorithms. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00389-4"
    author: Jamiu Adekunle Idowu
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Class balancing techniques improved fairness in education prediction tasks, with over-sampling also improving accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Eight of 11 class balancing techniques improved fairness in at least two of three prediction tasks; TomekLink and SMOTE-TomekLink improved fairness across all three tasks, while accuracy was almost exclusively improved by over-sampling techniques. [→ Jamiu Adekunle Idowu 2024](#jamiu-adekunle-idowu-2024)

## Evidence

### Jamiu Adekunle Idowu 2024

Jamiu Adekunle Idowu. (2024). Debiasing Education Algorithms. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00389-4

`q2 · i?` · `review · r2`

As reported in the review, S2 (Sha et al., 2022) tested 11 class balancing techniques (four under-sampling, four over-sampling, four hybrid) on forum post classification, dropout prediction, and performance prediction tasks across three datasets, with class balancing on training sets to ensure gender parity.

> "The study revealed that eight of the 11 class balancing techniques improved fairness in at least two of the three prediction tasks. Particularly, TomekLink and SMOTE-TomekLink improved fairness across all the three tasks. Meanwhile, compared to fairness improvement, accuracy was almost exclusively improved by over-sampling techniques."

## Discussion


## Related Claims
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — reports the opposite
- [Calibrated Equalized Odds Post-processing showed lower balanced accuracy and higher EOD than the preprocessing techniques DIR and RW in student performance prediction](cpp-postprocessing-accuracy-fairness-tradeoff.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — reports the opposite
- [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD, with effectiveness varying by demographic attribute](preprocessing-mitigation-reduces-disparities-oulad.md) — related
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
