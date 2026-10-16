---
type: strategy
id: conservative-lora-on-attention-components-hybrid-architectures
title: Apply LoRA fine-tuning conservatively to attention components only when adapting hybrid transformer-Mamba architectures
description: Because of training instabilities reported in the literature for hybrid architectures, the authors applied LoRA only to the Gated Attention components of the hybrid Qwen3.5 model, leaving the Gated DeltaNet layers unt...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: christopher-ormerod-and-youngkoung-kim-2026
    resource: "https://arxiv.org/abs/2608.10154"
    title: "Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154"
    author: Christopher Ormerod and YoungKoung Kim
---

# Apply LoRA fine-tuning conservatively to attention components only when adapting hybrid transformer-Mamba architectures

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because of training instabilities reported in the literature for hybrid architectures, the authors applied LoRA only to the Gated Attention components of the hybrid Qwen3.5 model, leaving the Gated DeltaNet layers untouched. They state: "we conservatively applied LoRA to the attention components, knowing this would essentially affect only a quarter of the hidden layers that would be typically used to fine-tune models." This is an implementable recipe for parameter-efficient fine-tuning of hybrid models on local hardware.

## Design Implications

### Context
#### Requirements
- Knowledge of the underlying model structure to select which linear layers LoRA replaces; parameter-efficient methods such as LoRA or quantized LoRA
#### Constraints
- The authors note a better understanding of how to adapt the DeltaNet layers stably would likely improve recovery, particularly of the weakest parameters

### Target Learners
- researchers fine-tuning multimodal LLMs for educational measurement tasks

### Target Learning Goals
- parameter-efficient adaptation of LLMs for simulated-respondent item parameter estimation

## Related Strategies

- [Select LoRA rank r=8 as a balanced compromise between parameter count and performance when adapting course question-answering models under resource constraints](lora-rank-8-compromise-course-qa.md)

## Examples
-

## Key Sources
- Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154
