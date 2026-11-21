---
type: claim
title: Source-free domain adaptation methods that succeed in computer vision underperform direct application of pre-trained models for retention prediction
description: Source-free domain adaptation methods that succeed in computer vision underperform direct application of pre-trained models for retention prediction
id: sfda-underperforms-in-retention-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: chengyuan-yao-2025
    title: Chengyuan Yao 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Source-free domain adaptation methods that succeed in computer vision underperform direct application of pre-trained models for retention prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SFDA techniques (SHOT, TENT, Pseudo-Labeling) were not as effective in predicting student retention rates, with many adaptation methods underperforming directly applying the pre-trained models without any adaptation. [→ Chengyuan Yao 2025](#chengyuan-yao-2025)

## Evidence

### Chengyuan Yao 2025

Chengyuan Yao, Carmen Cortez, and Renzhe Yu. 2025. Towards Fair and Privacy-Aware Transfer Learning for Educational Predictive Modeling: A Case Study on Retention Prediction in Community Colleges. In LAK25: The 15th International Learning Analytics and Knowledge Conference (LAK 2025), March 03–07, 2025, Dublin, Ireland. ACM, New York, NY, USA, 17 pages. https://doi.org/10.1145/3706468.3706567

`q2 · i?` · `design · r2`

Evaluation of three SFDA benchmark methods (SHOT, TENT, Pseudo-Labeling) versus Direct Transfer across target institutions, shown as Test AUC distributions in Fig. 8; "many of these adaptation methods underperformed" direct application.

> "that SFDA techniques that have demonstrated considerable success in computer vision tasks were not as effective in predicting student retention rates. In fact, many of these adaptation methods underperformed compared to directly applying the pre-trained models without any adaptation."

## Discussion


## Related Claims
- [Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification](few-shot-llama-underperforms-trained-models.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
