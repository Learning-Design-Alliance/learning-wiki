---
type: research-method
id: races-reward-aligned-consistent-essay-scoring-framework
title: RACES (Reward-Aligned Consistent Essay Scoring) framework
description: "RACES (Reward-Aligned Consistent Essay Scoring) is a unified AES framework that \"integrates LoRA-based parameter-efficient fine-tuning, reward modeling, and PPO with KL regularization\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# RACES (Reward-Aligned Consistent Essay Scoring) framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (3 for, 3 mixed) · 4 studies (2 causal, 2 design), `q2` · 1 of 4 report an effect size · 6 claims rest on one study

## Description
RACES (Reward-Aligned Consistent Essay Scoring) is a unified AES framework that "integrates LoRA-based parameter-efficient fine-tuning, reward modeling, and PPO with KL regularization". It runs an offline inference–feedback–optimization loop: LoRA SFT establishes basic score-label mapping with standardized prompts; a reward model learns ranking preferences between preferred proxy responses and harder negative samples; PPO with KL divergence and critic constraints optimizes the policy while limiting distribution drift. Alignment is proxy-based, using LLM-generated feedback rather than human-written comments.

## Accounts
<!-- How each source describes or uses the method -->
- **RACES: a reward-aligned, consistency-regularized framework for LLM-based automated essay scoring**: RACES (Reward-Aligned Consistent Essay Scoring) is a unified AES framework that "integrates LoRA-based parameter-efficient fine-tuning, reward modeling, and PPO with KL regularization". It runs an offline inference–feedback–optimization loop: LoRA SFT establishes basic score-label mapping with standardized prompts; a reward model learns ranking preferences between preferred proxy responses and harder negative samples; PPO with KL divergence and critic constraints optimizes the policy while limiting distribution drift. Alignment is proxy-based, using LLM-generated feedback rather than human-written comments. (Zhenxin Zhang et al. (2026))

### Claims

- [RACES configurations improve QWK essay-scoring agreement over evaluated pretrained baselines on ASAP 2.0, with LLaMA2-7B-based configurations slightly outperforming Qwen2.5-Instruct-7B-based ones](../claims/races-improves-qwk-over-evaluated-baselines.md) [+M]
- [Mistral-7B reward model outperforms GPT2-XL on Hit@k ranking and Pairwise Accuracy for proxy preference discrimination, at higher computational cost](../claims/mistral-reward-model-beats-gpt2-xl.md) [+M]
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](../claims/judge-anchoring-raises-human-agreement.md) [+W]
- [After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines](../claims/races-auxiliary-feedback-simcse-gains.md) [~W]
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](../claims/model-size-and-lora-rank-joint-effects.md) [~W]
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](../claims/lora-finetuning-llm-grader-parity.md) [~W]

## Related Research Methods
-

## Key Sources
- Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8
