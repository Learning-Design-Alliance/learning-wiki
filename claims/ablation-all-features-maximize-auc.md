---
type: claim
title: "Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs"
description: "Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs"
id: ablation-all-features-maximize-auc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: lu-2024
    resource: "https://doi.org/10.31219/osf.io/3k7z2"
    title: "Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)"
    author: "Lu, Y., Tong, L., & Cheng, Y."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The original Model 1 had the largest best validation, public, and private evaluation AUCs, and removing all additional features produced the lowest public and private AUCs. [→ Lu 2024](#lu-2024)

## Evidence

### Lu 2024

Lu, Y., Tong, L., & Cheng, Y. (2024). Advanced Knowledge Tracing: Incorporating Process Data and Curricula Information via an Attention-Based Framework for Accuracy and Interpretability. Journal of Educational Data Mining, 16(2). https://osf.io/mdpzc/ [doi:10.31219/osf.io/3k7z2](https://doi.org/10.31219/osf.io/3k7z2)

`q3 · i? · the article prints no effect size for this finding` · `design · r2`

Ablation study on Model 1 (Table 5), omitting sequence-level embeddings, student/class embeddings, action features, and problem features individually and jointly. Removing all features gave private AUC 0.7802 versus 0.7908 for the original model.

> "Table 5 also shows that removing all the additional features in the table will result in both the lowest public and private evaluation AUCs, suggesting the importance of incorporating all the additional features to maximize the performance of the model."

## Discussion


## Related Claims
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters](propdec-colinear-with-student-intercept.md) — related
- Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](transformer-kt-first-place-edm-cup-2023.md) — related
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — related
