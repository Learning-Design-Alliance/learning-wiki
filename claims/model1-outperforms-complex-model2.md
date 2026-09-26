---
type: claim
title: The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture
description: The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture
id: model1-outperforms-complex-model2
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

# The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · `i1` small

## Subclaims
`q3 i?` Model 1 achieved higher best validation, private evaluation, and second-best public AUC than the more complex Model 2, which the authors suggest may indicate overfitting. [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/

`q3 · i1`

Results section comparison of four architectures evaluated with 10-fold cross-validation and public/private evaluation AUCs (Table 4). Model 1's private AUC was 0.79083 versus Model 2's 0.78617; the authors state "Model 1 outperforms Model 2 despite the latter’s greater complexity".

> "Model 1 outperforms Model 2 despite the latter’s greater complexity, including a broader layer width in its MLP for problem embeddings and additional heads in the Transformer Encoder."

## Discussion


## Related Claims
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
- [Embedding pretraining outperforms end-to-end training in DynEmb, avoiding the overfitting that end-to-end training exhibits](embedding-pretraining-beats-end-to-end-training-dynemb.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](transformer-kt-first-place-edm-cup-2023.md) — related
