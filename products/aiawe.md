---
type: product
id: aiawe
title: AiAWE
description: AiAWE is an open-source Django platform developed by John Maurice Gayed and collaborators for real-time and batch automated essay scoring, custom-rubric feedback, and formative writing support.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# AiAWE

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
AiAWE is an open-source Django platform developed by John Maurice Gayed and collaborators for real-time and batch automated essay scoring, custom-rubric feedback, and formative writing support.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AiAWE open-source automated writing evaluation platform**: AiAWE is a Django web application, publicly accessible at https://app.awade.gec.waseda.ac.jp, that serves students and educators with "real-time essay scoring, rubric-referenced qualitative feedback, batch processing, and custom-rubric configuration." It runs llama.cpp inference of a Q4_K_M-quantised LoRA-adapted Gemma-3-27B model on a single RTX 3090, with average inference latency below two seconds per essay. Educator-facing features include batch user creation via Excel upload, batch essay processing (batches of over 1,000 essays in a single run), admin-defined custom rubric configurations with temperature settings, and token-based authentication with per-model daily request quotas. An experimental AWADE mode runs the base Gemma model without a LoRA adapter against instructor-defined rubrics for formative feedback. (John Maurice Gayed (2026))

### Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](../claims/gemma-27b-lora-beats-gpt35-essay-scoring.md) [+M]
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](../claims/lora-rank-sensitivity-architecture-dependent.md) [~W]

## Related Products and Programmes
-

## Key Sources
- John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801
