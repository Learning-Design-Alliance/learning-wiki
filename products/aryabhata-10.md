---
type: product
id: aryabhata-10
title: Aryabhata 1.0
description: A 7B-parameter, text-only mathematics reasoning model released by Ritvik Rastogi and collaborators on Hugging Face for step-by-step, exam-focused problem solving.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Aryabhata 1.0

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A 7B-parameter, text-only mathematics reasoning model released by Ritvik Rastogi and collaborators on Hugging Face for step-by-step, exam-focused problem solving.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Four-stage post-training pipeline: model merging, domain-aligned data curation, rejection-sampled curriculum SFT, and RLVR**: The article organizes its method as a four-stage pipeline: "The overall process can be categorized in the following four stages" — linear model merging of three Qwen-based 7B models, curation of a domain-aligned JEE question corpus, supervised fine-tuning on best-of-4 rejection-sampled verified chain-of-thought traces ordered as a curriculum, and reinforcement learning with verifiable rewards using an A2C objective with group-relative advantage estimation. The authors state their approach builds on prior math-LLM work "by merging models for hybrid capabilities (symbolic fluency + coherent CoT), followed by rejection-sampled SFT and RL with verifiable rewards, preserving both performance and efficiency in a compact model". (Ritvik Rastogi et al. (2025))

### Claims
- [Aryabhata 1.0 achieves 86.0% accuracy on the JEE Main 2025 January session and 90.2% on the April session with roughly 2K tokens per response](../claims/aryabhata-jee-main-2025-accuracy.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Ritvik Rastogi, Sachin Dharashivkar, Sandeep Varma. (2025). Aryabhata: An exam-focused language model for JEE Math. arXiv. https://arxiv.org/abs/2508.08665
