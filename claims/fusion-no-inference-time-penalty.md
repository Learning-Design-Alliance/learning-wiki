---
type: claim
title: Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)
description: Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)
id: fusion-no-inference-time-penalty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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
---

# Adding the linguistic neural network to a transformer does not significantly change inference time (p = 0.244)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A paired t-test on inference time found no statistically significant difference between unimodal and multimodal approaches. [→ Jordan J. Bird 2024](#jordan-j-bird-2024)

## Evidence

### Jordan J. Bird 2024

Jordan J. Bird. (2024). What Differentiates Educational Literature? A Multimodal Fusion Approach of Transformers and Computational Linguistics. arXiv preprint. https://arxiv.org/abs/2411.17593 [doi:10.48550/arxiv.2411.17593](https://doi.org/10.48550/arxiv.2411.17593)

`q2 · i?` · `design · r2`

Paired t-test across the five validation metrics including inference time; only inference time failed to reach significance (p = 0.244). The article reports no effect size, so the magnitude of any time difference is untested.

> "Furthermore, the paired t-test for inference time ( p = 0 .244) shows that there is no statistically significant difference, suggesting that the addition of the artificial neural network does not have a considerable impact on processing time."

## Discussion


## Related Claims
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — related
- [Neural networks on linguistic features classify Key Stages poorly, with deeper networks performing worse; the best (one hidden layer, 175 ReLU) reached F1 = 0.392](linguistic-ann-weak-deeper-worse.md) — related
- [BERT was the best unimodal text classifier for Key Stage classification with an F1 score of 0.75](bert-best-unimodal-f1-075.md) — related
- Frontal EEG spectral activity shows no statistically significant differences across AI interaction modes or between with-AI and no-AI conditions — related
