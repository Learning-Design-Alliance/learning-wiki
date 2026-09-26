---
type: claim
title: "Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs"
description: "Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs"
id: ablation-all-features-maximize-auc
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: lu-2024
    resource: "https://osf.io/mdpzc/"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/"
    author: "Lu, Y., Tong, L., & Cheng, Y."
    q: 3
    i: 1
---

# Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · `i1` small

## Subclaims
`q3 i?` The original Model 1 had the largest best validation, public, and private evaluation AUCs, and removing all additional features produced the lowest public and private AUCs. [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/

`q3 · i1`

Ablation study on Model 1 (Table 5), omitting sequence-level embeddings, student/class embeddings, action features, and problem features individually and jointly. Removing all features gave private AUC 0.7802 versus 0.7908 for the original model.

> "Table 5 also shows that removing all the additional features in the table will result in both the lowest public and private evaluation AUCs, suggesting the importance of incorporating all the additional features to maximize the performance of the model."

## Discussion


## Related Claims
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters](propdec-colinear-with-student-intercept.md) — related
- [Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets](time-window-features-null-for-lr-boost-nonlinear.md) — related
