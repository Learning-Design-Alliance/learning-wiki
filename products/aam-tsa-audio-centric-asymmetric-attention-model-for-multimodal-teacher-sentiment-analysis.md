---
type: product
id: aam-tsa-audio-centric-asymmetric-attention-model-for-multimodal-teacher-sentiment-analysis
title: "AAM-TSA: audio-centric asymmetric attention model for multimodal teacher sentiment analysis"
description: AAM-TSA is a multimodal sentiment-analysis model developed by Zhiyi Duan et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# AAM-TSA: audio-centric asymmetric attention model for multimodal teacher sentiment analysis

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
AAM-TSA is a multimodal sentiment-analysis model developed by Zhiyi Duan et al. that fuses textual, audio, video-description, and instructional-information features to classify teacher emotions in classroom recordings.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AAM-TSA: audio-centric asymmetric attention model for multimodal teacher sentiment analysis**: AAM-TSA is a four-module multimodal sentiment model built on the premise that teacher emotional expression is audio-centric. It extracts features from text (RoBERTa), audio (HuBERT), LLM-generated video descriptions, and instructional information embeddings; applies asymmetric cross-modal attention in which non-audio modalities query audio key-value pairs while audio queries text; fuses text, audio, and video features through softmax-normalized gated weights before concatenating instructional information; and classifies eight emotions. The authors state the design enables "differentiated cross-modal feature fusion and precise emotional classification". (Zhiyi Duan et al. (2025))

### Claims
- [AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark](../claims/aam-tsa-outperforms-multimodal-baselines-t-med.md) [+M]
- [Audio is the core carrier of teacher emotional expression: audio-only features outperform text-only and video-description-only variants](../claims/audio-core-carrier-teacher-emotion-t-med.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2025). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. https://arxiv.org/abs/2512.20548
