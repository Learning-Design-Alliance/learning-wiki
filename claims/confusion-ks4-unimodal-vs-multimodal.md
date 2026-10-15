---
type: claim
title: Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly
description: Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly
id: confusion-ks4-unimodal-vs-multimodal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jordan-j-bird-2024
    resource: "https://doi.org/10.48550/arxiv.2411.17593"
    title: "Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593 [doi:10.48550/arxiv.2411.17593](https://doi.org/10.48550/arxiv.2411.17593)"
    author: Jordan J. Bird
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jordan-j-bird-2024-2
    resource: "https://arxiv.org/abs/2411.17593"
    title: "Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593"
    author: Jordan J. Bird
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Key Stage 4 was the most problematic class for the unimodal BERT approach, with excerpts misinterpreted as Key Stage 3. [→ Jordan J. Bird 2024](#jordan-j-bird-2024)
`q2 i?` The best multimodal approach classified Key Stages 4 and 5 perfectly, with relatively lower confusion between Key Stages 2 and 3. [→ Jordan J. Bird 2024 (2)](#jordan-j-bird-2024-2)

## Evidence

### Jordan J. Bird 2024

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593 [doi:10.48550/arxiv.2411.17593](https://doi.org/10.48550/arxiv.2411.17593)

`q2 · i?` · `design · r2`

Normalised confusion matrix for unimodal BERT (Figure 13a) shows Key Stage 4 recall of 0.680 with 0.138 misclassified as Key Stage 3. The quoted sentence is the article's own description of that matrix.

> "The most problematic class for the unimodal approach was Key Stage 4, with several excerpts misinterpreted as Key Stage 3."

### Jordan J. Bird 2024 (2)

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593

`q2 · i?` · `design · r2`

Normalised confusion matrix for multimodal ELECTRA + ANN (Figure 13b) shows 1.000 diagonal entries for Key Stages 4 and 5 and residual KS2/KS3 confusion (e.g. 0.012 of KS3 predicted as KS2).

> "However, the best-performing multimodal approach was able to classify Key Stages 4 and 5 perfectly, with relatively lower confusion between Key Stages 2 and 3."

## Discussion


## Related Claims
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — a broader claim this one bears on
- [Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392](linguistic-ann-weak-deeper-worse.md) — related
