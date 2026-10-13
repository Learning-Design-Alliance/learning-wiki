---
type: product
id: fine-tuned-gemma-e2b-offline-deployment-with-dashboard-and-conversational-interfaces
title: Fine-tuned Gemma E2B offline deployment with dashboard and conversational interfaces
description: "Chenguang Pan et al.'s offline educational-intervention-effect explanation system, combining a LoRA-adapted Gemma E2B model with dashboard and conversational interfaces for parents, students, counselors, and other stakeholders."
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Fine-tuned Gemma E2B offline deployment with dashboard and conversational interfaces

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 2 studies (2 causal), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
Chenguang Pan et al.'s offline educational-intervention-effect explanation system, combining a LoRA-adapted Gemma E2B model with dashboard and conversational interfaces for parents, students, counselors, and other stakeholders.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims

- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](../claims/lora-rank-sensitivity-architecture-dependent.md) [~W]
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](../claims/llama-prediction-range-compression.md) [+W]
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](../claims/adaptation-gains-grow-with-model-capacity.md) [~W]

## Related Products and Programmes
-

## Key Sources
- Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165
