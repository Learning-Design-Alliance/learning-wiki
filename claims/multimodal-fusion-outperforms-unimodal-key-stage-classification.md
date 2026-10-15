---
type: claim
title: Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996
description: Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996
id: multimodal-fusion-outperforms-unimodal-key-stage-classification
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

# Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Every multimodal model outperformed all unimodal models, and the ELECTRA + ANN fusion achieved an F1 score of 0.996. [→ Jordan J. Bird 2024](#jordan-j-bird-2024)
`q2 i?` Paired t-tests show statistically significant differences between unimodal and multimodal approaches on accuracy, precision, recall and F1 (all p < 0.001). [→ Jordan J. Bird 2024 (2)](#jordan-j-bird-2024-2)

## Evidence

### Jordan J. Bird 2024

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593 [doi:10.48550/arxiv.2411.17593](https://doi.org/10.48550/arxiv.2411.17593)

`q2 · i?` · `design · r2`

Benchmark of eight fine-tuned transformers and their late fusions with the best linguistic ANN on a balanced 20,000-row Key Stage dataset (80/20 split). The article reports "an F1 score of 0.996" for ELECTRA + ANN, and that all multimodal models beat all unimodal text classifiers.

> "The overall best model was the multimodal combination of the ELECTRA text classifier and linguistics artificial neural network, which achieved an F1 score of 0.996."

### Jordan J. Bird 2024 (2)

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593

`q2 · i?` · `design · r2`

Paired t-tests compared unimodal and multimodal models on accuracy, precision, recall and F1; Table 5 prints t-statistics of 9.45 to 21.95 with p < 0.001 for all four metrics. The article reports the improvements as "statistically significant" with no effect size given.

> "The results can be observed in Table 5, which shows that these improvements in the classification metrics are statistically significant ( p < 0.05)."

## Discussion


## Related Claims
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- [Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly](confusion-ks4-unimodal-vs-multimodal.md) — a narrower finding that bears on this claim
- [Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)](fusion-no-inference-time-penalty.md) — related
- [Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392](linguistic-ann-weak-deeper-worse.md) — related
