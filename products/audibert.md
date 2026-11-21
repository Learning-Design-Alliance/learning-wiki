---
type: product
id: audibert
title: AudiBERT
description: AudiBERT is a study-developed multimodal audio-text classification architecture combining BERT and Wav2Vec2.0 encoders to diagnose collaborative problem-solving subskills from students’ verbal and audio data.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# AudiBERT

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
AudiBERT is a study-developed multimodal audio-text classification architecture combining BERT and Wav2Vec2.0 encoders to diagnose collaborative problem-solving subskills from students’ verbal and audio data.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AudiBERT multimodal audio-text classification model applied to CPS diagnosis**: AudiBERT is a multimodal classification architecture the study applies to CPS diagnosis, combining text and audio encodings. It involves "an audio-textual dual self-attentive framework that captures interdependence between different parts of speech in audio and textual form", using BERT as the text encoder and Wav2Vec2.0 as the audio encoder, with embeddings processed through separate BiLSTM networks and fused by concatenation. (Kester Wong et al. (2025))

### Claims
- [AudiBERT outperformed BERT on F1 in both dimensions, while BERT performed better on accuracy, precision and recall in the affective dimension](../claims/audibert-vs-bert-f1-accuracy-tradeoff.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. https://arxiv.org/abs/2504.15093
