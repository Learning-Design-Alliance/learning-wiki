---
type: design
id: on-premise-oer-knowledge-base-assistant-system
title: On-premise OER-based AI knowledge-base assistant system for computer science education
description: A three-subsystem architecture comprising an LMS Layer, a Knowledge Base Layer with structured extraction and a FAISS vector index, and an AI Inference Layer with curriculum alignment and model optimization modules.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: shen-x-2026
    resource: "https://doi.org/10.3389/fpsyg.2026.1843444"
    title: "Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444"
    author: Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B
---

# On-premise OER-based AI knowledge-base assistant system for computer science education

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A three-subsystem architecture comprising an LMS Layer, a Knowledge Base Layer with structured extraction and a FAISS vector index, and an AI Inference Layer with curriculum alignment and model optimization modules. The article states that "all components operate entirely on-premise on a consumer-grade GPU (RTX 3060, 12 GB VRAM), with no external API calls". It ingests 82 open-licensed Markdown documents (~347,000 tokens) from MIT OpenCourseWare, OpenStax, CS50 and WikiCS, and serves student queries via retrieval-augmented generation with quantized Qwen-7B or DeepSeek-MoE models.

## Design Implications

### Context
#### Requirements
- Openly licensed OER documents (Creative Commons or OSI-compatible) as the knowledge corpus
- A consumer-grade GPU with at least 12 GB VRAM for deployment
#### Constraints
- The article characterizes it as a knowledge-base assistant rather than a validated intelligent tutor; no controlled learner study was conducted
- Evaluation dataset drawn from English-medium OER platforms; multilingual extension is future work

### Target Learners
- introductory undergraduate computer science students

### Learning Goals
- factual recall, concept explanation, and multi-hop reasoning about introductory computer science topics

### Claims
- [Deepseek Moe Ours Strongest Accuracy Balance](../claims/deepseek-moe-ours-strongest-accuracy-balance.md) [+M]
- [Nf4 Quantization Vram Reduction](../claims/nf4-quantization-vram-reduction.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444
