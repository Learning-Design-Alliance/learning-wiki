---
type: strategy
id: selective-loss-masking-llm-finetuning
title: Use selective loss masking when fine-tuning generative LLMs on classification tasks
description: When adapting generative LLMs to classification tasks, all output tokens typically contribute to the loss, introducing noise.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: max-norris-2026
    resource: "https://arxiv.org/abs/2511.02599"
    title: "Max Norris, Kobi Gal and Sahan Bulathwela. (2026). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. https://arxiv.org/abs/2511.02599"
    author: Max Norris, Kobi Gal and Sahan Bulathwela
---

# Use selective loss masking when fine-tuning generative LLMs on classification tasks

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When adapting generative LLMs to classification tasks, all output tokens typically contribute to the loss, introducing noise. NTKT masks all tokens except those spelling Correct or Incorrect, enclosed in <cr>...</cr> tags, computing loss only at those positions while non-target tokens still participate in attention. This "simplifies optimization by aligning the supervision signal with the task".

## Design Implications

### Context
#### Requirements
- Target outcome tokens must be unambiguously locatable in the sequence, e.g. via XML-style tags
#### Constraints
- 

### Target Learners
- students modelled by adaptive learning systems

### Target Learning Goals
- accurate prediction of student response correctness for personalisation

## Related Strategies
- 

## Examples
-

## Key Sources
- Max Norris, Kobi Gal and Sahan Bulathwela. (2026). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. https://arxiv.org/abs/2511.02599
