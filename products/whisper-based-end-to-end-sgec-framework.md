---
type: product
id: whisper-based-end-to-end-sgec-framework
title: Whisper-based end-to-end SGEC framework
description: A Whisper-based end-to-end system developed by Mengjie Qian et al.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Whisper-based end-to-end SGEC framework

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A Whisper-based end-to-end system developed by Mengjie Qian et al. that maps L2 English learner speech directly to grammatically corrected transcriptions and derives edit-based feedback by comparison with fluent transcriptions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Whisper-based end-to-end SGEC framework mapping learner speech directly to grammatically corrected transcriptions**: The article develops an end-to-end spoken grammatical error correction framework in which a single Whisper-based model "directly map learner speech to grammatically corrected transcriptions", replacing the traditional cascaded ASR-then-disfluency-then-GEC pipeline that is "prone to error propagation". Learner feedback is then derived by comparing the corrected transcription with a fluent transcription from Whisperflt. The framework is enhanced with pseudo-labeling, prompt conditioning, reference alignment, and edit-confidence filtering, and the article argues Whisper's transcription-focused training "closely aligns with the core structure of SGEC" relative to general-purpose multimodal LLMs. (Mengjie Qian et al. (2025))

### Claims
- [With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines](../claims/e2e-whisper-large-v2-sgec-outperforms-pipelines.md) [+M]
- [Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added](../claims/pseudo-labeled-data-sgec-model-size-moderates.md) [+M]
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](../claims/prompt-conditioned-sgec-improves-feedback-precision.md) [+M]
- [Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality](../claims/reference-alignment-boosts-sgec-feedback-f05.md) [+M]
- [Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline](../claims/edit-confidence-filtering-improves-feedback-f05.md) [+M]
- [Current multimodal LLMs underperform fine-tuned Whisper for spoken grammar correction: LoRA-tuned Qwen2-Audio reaches 13.7% WER (2.6% absolute worse than Whispergec) and zero-shot Voxtral scores F0.5 of 23.69 versus the 43.10 partial-cascaded baseline](../claims/multimodal-llms-underperform-whisper-sgec.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2025). End-to-End Spoken Grammatical Error Correction. arXiv. https://arxiv.org/abs/2506.18532
