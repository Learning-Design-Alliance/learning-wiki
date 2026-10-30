---
type: claim
title: Class balance and score distribution matter more than overall sample size for training accurate scoring models
description: Class balance and score distribution matter more than overall sample size for training accurate scoring models
id: class-balance-more-important-than-sample-size
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00418-w"
    title: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w"
    author: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Class balance and score distribution matter more than overall sample size for training accurate scoring models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors report that filtering removed upwards of 50% of 1-scoring samples from some items and markedly improved performance, suggesting class balance matters more than overall sample count. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w

`q1 · i?` · `design · r2`

This is an author interpretation based on their filtering experiments rather than a controlled comparison. The article states that filters "removed upwards of 50% of the 1-scoring samples from some items" and that this "markedly improved model performance, suggesting that class balance and the distribution of the data are more important than the overall number of samples collected."

> "we did, however, apply filters that removed upwards of 50% of the 1-scoring samples from some items (meaning that these samples were not seen by our models during training), and this markedly improved model performance, suggesting that class balance and the distribution of the data are more important than the overall number of samples collected."

## Discussion


## Related Claims
- [Data augmentation with Coedit-XL paraphrasing and targeted filtering improved model performance on imbalanced items](coedit-xl-augmentation-improved-imbalanced-item-scoring.md) — related
- [SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses](sgd-classifier-filtering-outperformed-linguistic-features.md) — related
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — reports the opposite
- [For transformer models, oversampling and backtranslation augmentation improve performance while freezing the encoder substantially decreases it](transformer-ablation-oversampling-freezing.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — reports the opposite
