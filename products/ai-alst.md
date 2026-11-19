---
type: product
id: ai-alst
title: AI-ALST
description: AI-ALST is an AI-supported pronunciation tutoring system for Moroccan Arabic learners that uses word-specific audio classification to detect pronunciation errors.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# AI-ALST

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
AI-ALST is an AI-supported pronunciation tutoring system for Moroccan Arabic learners that uses word-specific audio classification to detect pronunciation errors.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AI-ALST attention BiLSTM pronunciation detection architecture**: AI-ALST's pronunciation tutoring engine trains one binary detection model per word. As the article describes it, "the detection model consists of several parts: an MFCC feature extraction layer, a BiLSTM layer combining forward and backward LSTM, an attention layer, and an output layer with a cost-based strategy for dealing with class-imbalanced audio data." Audio is converted to the first 20 MFCC dimensions; the attention layer weights audio frames by learned importance, and the cost-based strategy gives larger training weights to the minority class. Predictions threshold at p ≥ 0.5 for wrong pronunciation, trained with binary cross-entropy and Adam. (Shao et al. (2022))

### Claims
- [Attention BiLSTM outperforms plain BiLSTM on Moroccan Arabic pronunciation error detection across the four evaluation metrics](../claims/attention-bilstm-beats-bilstm-pronunciation-detection.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Shao, S., Alharir, S., Hariri, S., Satam, P., Shiri, S., & Mbarki, A. (2022). AI-based Arabic Language and Speech Tutor. IEEE conference paper. https://ieeexplore.ieee.org. [doi:10.1109/aiccsa56895.2022.10017924](https://doi.org/10.1109/aiccsa56895.2022.10017924)
