---
type: claim
title: Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392
description: Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392
id: linguistic-ann-weak-deeper-worse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
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

# Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The best linguistic-feature neural network had one hidden layer of 175 rectified linear units with an F1 score of 0.392. [→ Jordan J. Bird 2024](#jordan-j-bird-2024)
`q2 i?` A pattern of higher network depth led to worse overall results in the linguistic-feature classifiers. [→ Jordan J. Bird 2024 (2)](#jordan-j-bird-2024-2)

## Evidence

### Jordan J. Bird 2024

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593 [doi:10.48550/arxiv.2411.17593](https://doi.org/10.48550/arxiv.2411.17593)

`q2 · i?` · `design · r2`

Random search over 500 neural network architectures of 16–256 ReLU units in 1–5 hidden layers on numerical linguistic features. The best network had 12,604 trainable parameters and the printed scores "40.2% accuracy, 0.394 precision, 0.402 recall, and an F1 score of 0.392".

> "The best neural network had one hidden layer of 175 rectified linear units, which scored 40.2% accuracy, 0.394 precision, 0.402 recall, and an F1 score of 0.392."

### Jordan J. Bird 2024 (2)

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593

`q2 · i?` · `design · r2`

Figure 11b plots F1 against inference time for the searched architectures by hidden-layer count; the authors describe the observed pattern as an interpretation of the plotted results, not a tested statistical contrast.

> "It can be observed that neural networks trained on linguistic features perform poorly, with a pattern of higher network depth that leads to worse overall results."

## Discussion


## Related Claims
- [Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly](confusion-ks4-unimodal-vs-multimodal.md) — related
- [Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)](fusion-no-inference-time-penalty.md) — related
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — related
- [AI systems relying on black-box models should not be used for high-stakes applications](black-box-ai-not-for-high-stakes-applications.md) — related
