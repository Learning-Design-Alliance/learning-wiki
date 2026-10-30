---
type: claim
title: SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses
description: SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses
id: sgd-classifier-filtering-outperformed-linguistic-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00418-w"
    title: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w"
    author: "Morris, W., Holmes, L., Choi, J. S., & Crossley, S."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The SGD classifier on a TF-IDF document-term matrix was more precise than explicitly defined language features at filtering low-scoring responses without removing high-scoring ones. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated Scoring of Constructed Response Items in Math Assessment Using Large Language Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00418-w

`q2 · i?` · `design · r2`

The article compared two filtering methods for balancing class labels: explicit linguistic features (e.g., language probability, word count) and an SGD logistic classifier on a document-term matrix. The article reports that the linguistic-feature method "removed non-negligible portions of high-scoring responses" and that the SGD classifier "performed better."

> "Our other method of classifying low-scoring responses, the SGD classifier on a document-term matrix for items with data imbalances, performed better."

## Discussion


## Related Claims
- [Class balance and score distribution matter more than overall sample size for training accurate scoring models](class-balance-more-important-than-sample-size.md) — related
- [Data augmentation with Coedit-XL paraphrasing and targeted filtering improved model performance on imbalanced items](coedit-xl-augmentation-improved-imbalanced-item-scoring.md) — a broader claim this one bears on
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — related
- [Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392](linguistic-ann-weak-deeper-worse.md) — related
