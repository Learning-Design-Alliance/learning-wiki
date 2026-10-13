---
type: product
id: kt4eqg
title: KT4EQG
description: KT4EQG is a personalized question-generation system combining knowledge tracing, large-language-model generation, reinforcement learning, and an alignment verifier, developed by Xinyi Gao et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# KT4EQG

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 7 claims (7 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 7 claims rest on one study

## Description
KT4EQG is a personalized question-generation system combining knowledge tracing, large-language-model generation, reinforcement learning, and an alignment verifier, developed by Xinyi Gao et al.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **KT4EQG system with released code**: KT4EQG is an implemented personalized question generation system combining the KT2 knowledge tracer, a QWEN3-8B-based question generator trained with SFT and GRPO reinforcement learning, and an alignment verifier built on ALL-MINILM-L6-V2. The paper notes "Code available at https://github.com/UCSB-NLP-Chang/KT4EQG". The system was evaluated on XES3G5M and MOOCRADAR across six knowledge modules, with training on 8 NVIDIA H100 GPUs and the verifier trained on a single RTX 3090 Ti. (Xinyi Gao et al. (2026))

### Claims

- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](../claims/alignment-rl-improves-concept-alignment.md) [+W]
- [KT4EQG achieves the highest exam score across all practice-round counts, while methods without effective concept selection show only marginal gains as rounds increase](../claims/consistent-gains-across-practice-rounds.md) [+W]
- [Without alignment training, generated questions collapse to similar content regardless of the intended knowledge concept, whereas KT4EQG questions spread across many verified KCs](../claims/alignment-training-prevents-question-collapse.md) [+W]
- [Providing baselines with oracle knowledge-concept selection substantially improves their performance, identifying concept selection as a key bottleneck, though baselines with oracle KCs still trail KT4EQG](../claims/concept-selection-bottleneck-baselines.md) [+W]
- [KT4EQG remains competitive when evaluated with alternative knowledge tracers (BKT and DKT), though its advantage varies across modules](../claims/kt4eqg-competitive-under-alternative-tracers.md) [+W]
- [KT4EQG's education-value objective produces an adaptive KC-selection policy: weaker students are given better-mastered concepts and stronger students progressively more challenging ones](../claims/adaptive-kc-selection-policy.md) [+W]
- [KT4EQG achieves the highest exam score across all knowledge modules on both XES3G5M and MOOCRADAR, outperforming all question-generation baselines](../claims/kt4eqg-highest-exam-score-all-modules.md) [+W]

## Related Products and Programmes

- [DeepTutor](deeptutor.md)

## Key Sources
- Xinyi Gao, Qiucheng Wu, Lu Ding, Q. Vera Liao, Kaizhi Qian, Ying Xu, Shiyu Chang, Yang Zhang. (2026). KT4EQG: Personalized Exercise Question Generation via Knowledge Tracing. Preprint. Under review. https://arxiv.org/abs/2605.23933
