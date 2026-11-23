---
type: strategy
id: empirical-domain-evaluation-for-model-selection
title: Select AI models for physics tasks by empirical evaluation on the specific domain, not by general benchmarks or price
description: Since the lighter Gemini 3 Flash slightly outperformed the larger Gemini 3 Pro across both temperature configurations tested, the authors recommend that instructors and students not assume a more advanced or expensive...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2026
    resource: "https://github.com/etufino/LLMs-performances"
    title: "Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. https://github.com/etufino/LLMs-performances"
    author: Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss
---

# Select AI models for physics tasks by empirical evaluation on the specific domain, not by general benchmarks or price

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 associational), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Since the lighter Gemini 3 Flash slightly outperformed the larger Gemini 3 Pro across both temperature configurations tested, the authors recommend that instructors and students not assume a more advanced or expensive model is more reliable for physics tasks. Model selection should be guided by empirical evaluation on the specific domain, consistent with the cost–performance analysis of Polverini and Gregorcic showing higher-priced models do not always yield better results on physics concept inventories.

## Design Implications

### Context
#### Requirements
- Domain-specific empirical evaluation of candidate models on the target task type
#### Constraints
- Cross-model accuracy comparisons in this study carry a configuration asymmetry, since GPT-5.2 ran with reasoning disabled while the Gemini models operated with full reasoning enabled

### Target Learners
- university physics students and instructors

### Target Learning Goals
- reliable use of AI chatbots for conceptual physics study and tutoring

## Claims

- [The lighter Gemini 3 Flash slightly outperforms the larger Gemini 3 Pro across temperature configurations, an inverse-scaling pattern](../claims/inverse-scaling-flash-beats-pro-crci.md) [+W]
- [All three models show severe, item-specific failures, with Q16 (fluid on inclined plane with friction) difficult for every model and GPT-5.2 scoring 0% on Q4](../claims/item-specific-complete-llm-failures.md) [+W]
- [Frontier LLMs outperform the student average on most CRCI items, with mean accuracies of 97.0% (Gemini 3 Flash), 88.6% (Gemini 3 Pro) and 73.3% (GPT-5.2) versus 61.5% for students](../claims/llms-outperform-students-on-crcl.md) [+W]
- [LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance](../claims/model-specific-llm-error-profiles-csat.md) [+W]

## Related Strategies

- [Develop unified physics benchmarks and language-specific evaluations for LLMs](unified-physics-benchmarks-for-llm-evaluation.md)

## Examples
-

## Key Sources
- Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. https://github.com/etufino/LLMs-performances
