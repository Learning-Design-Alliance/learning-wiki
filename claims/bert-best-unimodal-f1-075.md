---
type: claim
title: BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75
description: BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75
id: bert-best-unimodal-f1-075
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jordan-j-bird-2024
    resource: "https://arxiv.org/abs/2411.17593"
    title: "Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593"
    author: Jordan J. Bird
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Among eight fine-tuned transformers, BERT achieved the highest unimodal F1 score of 0.75. [→ Jordan J. Bird 2024](#jordan-j-bird-2024)

## Evidence

### Jordan J. Bird 2024

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593

`q2 · i?` · `design · r2`

Results section benchmark of eight transformers (Longformer 148M parameters down to ALBERT 12M), each fine-tuned for 5 epochs on segmented text. BERT scored 0.750 accuracy, 0.751 precision, 0.750 recall and "an F1 score of 0.75" per Table 4.

> "The best single modal model overall was BERT, which had an F1 score of 0.75."

## Discussion


## Related Claims
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — related
- [Unimodal classification confuses Key Stage 4 with Key Stage 3, while the best multimodal model classifies Key Stages 4 and 5 perfectly](confusion-ks4-unimodal-vs-multimodal.md) — related
- [Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)](fusion-no-inference-time-penalty.md) — related
- [Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392](linguistic-ann-weak-deeper-worse.md) — related
