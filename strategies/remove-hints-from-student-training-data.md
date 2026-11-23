---
type: strategy
id: remove-hints-from-student-training-data
title: Remove hint strings and few-shot demonstrations from student training data to force internalization
description: A training strategy in which the student is fine-tuned on successful retrieval-augmented teacher trajectories from which the hint block and few-shot examples have been stripped.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: humaid-ibrahim-2025
    resource: "https://arxiv.org/abs/2510.01375"
    title: "Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. https://arxiv.org/abs/2510.01375"
    author: Humaid Ibrahim, Nikolai Rozanov, Marek Rei
---

# Remove hint strings and few-shot demonstrations from student training data to force internalization

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A training strategy in which the student is fine-tuned on successful retrieval-augmented teacher trajectories from which the hint block and few-shot examples have been stripped. The article removes the hint block "to prevent copying", so the student must learn behaviors that substitute for explicit hints rather than memorizing the text, letting the agent reproduce teacher behavior without hints at inference. Few-shot demonstrations are excluded because they are fixed across tasks and do not reflect the agent's actual decision process.

## Design Implications

### Context
#### Requirements
- Successful teacher trajectories generated with retrieval-augmented hints
- LoRA fine-tuning on the serialized trajectories with hint strings removed
#### Constraints
- Applied with one-shot retrieval at episode start only; the approach was not tested with mid-episode retrieval

### Target Learners
- LLM agent students (7B and 14B instruction-tuned backbones)

### Target Learning Goals
- Internalizing retrieval-derived guidance so it no longer requires runtime hints

### Affordances
- Failure Driven Retrieval Distillation Pipeline

## Claims

- [Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success](../claims/distilled-models-fewer-tokens-than-rag.md) [+W]
- [Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop](../claims/distilled-students-highest-success-without-retrieval.md) [+W]
- [Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop](../claims/small-models-hints-scale-dependent.md) [~W]

## Related Strategies

- [Use retrieval-augmented generation over a curated domain corpus as a resource-efficient alternative to fine-tuning for specializing LLMs in niche domains](rag-curated-corpus-domain-specialization.md)

## Examples
-

## Key Sources
- Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. https://arxiv.org/abs/2510.01375
