---
type: design
id: part2-llm-application-modules-colab
title: Part 2 LLM application modules using efficient models within Colab constraints
description: Part 2 contains six integrated modules covering LLM foundations, platforms and development tools (Hugging Face, LangChain), prompt engineering and retrieval-augmented generation, model deployment and optimization, and...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: fang-li-2025
    resource: "https://arxiv.org/abs/2512.05167"
    title: "Fang Li. (2025). Bridging Traditional Machine Learning and Large Language Models: A Two-Part Course Design for Modern AI Education. https://arxiv.org/abs/2512.05167"
    author: Fang Li
---

# Part 2 LLM application modules using efficient models within Colab constraints

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Part 2 contains six integrated modules covering LLM foundations, platforms and development tools (Hugging Face, LangChain), prompt engineering and retrieval-augmented generation, model deployment and optimization, and model customization and fine-tuning. The course uses "efficient models such as DistilGPT-2, Phi-2, and quantized LLaMA-3.1, which operate within Colab's resource constraints" and implements RAG with FAISS vector databases of lecture notes.

## Design Implications

### Context
#### Requirements
- efficient or quantized models to fit Colab free-tier runtime limits
- checkpoints and lightweight frameworks to manage runtime limits
#### Constraints
- Colab free tier constraints affect work with larger models and datasets

### Target Learners
- students who have completed the foundational ML part

### Learning Goals
- prompt engineering
- RAG system implementation
- model deployment
- fine-tuning

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Fang Li. (2025). Bridging Traditional Machine Learning and Large Language Models: A Two-Part Course Design for Modern AI Education. https://arxiv.org/abs/2512.05167
