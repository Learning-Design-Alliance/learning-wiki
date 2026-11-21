---
type: design
id: ilp-llm-explanation-pipeline
title: ILP + LLM explanation generation and scoring pipeline
description: "The article develops an explanation pipeline combining Inductive Logic Programming with large language models in three stages: learning, explanation, and scoring."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: lun-ai-2025
    resource: "https://arxiv.org/abs/2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. https://arxiv.org/abs/2509.00961"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
---

# ILP + LLM explanation generation and scoring pipeline

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article develops an explanation pipeline combining Inductive Logic Programming with large language models in three stages: learning, explanation, and scoring. An ILP system (Hopper, using Learning from Failures) learns Prolog programs from episodes; multiple coding LLMs (Qwen2.5 Coder 14B, StarCoder V2 15B) interpret the programs, and a reasoning LLM summarises the interpretations into a consensus explanation, inspired by the debate strategy; LLM judges (DeepSeek R1, Claude Sonnet 3.7, o3-mini) score candidates, optionally using expert-written references. The pipeline "produces a set of natural language explanations" with human intervention only during scoring, avoiding expert-written templates.

## Design Implications

### Context
#### Requirements
- ILP learning episodes as input, configured coding and reasoning LLMs, and human expert double-checking of top-ranking answers before use in teaching
#### Constraints
- LLM judges do not replace human evaluations; the authors retain expert evaluation for ethics concerns and value technical correctness over LLM judged scores in final selection

### Target Learners
- Adult learners without a technical background studying explanations of learned strategies

### Learning Goals
- Teaching active learning strategies for fault diagnosis that transfer across isomorphic domains

### Claims
- [Llm Judges Rate Pipeline Explanations Higher](../claims/llm-judges-rate-pipeline-explanations-higher.md) [+M]
- [Llm Pipeline Explanations No Advantage Over Self Learning](../claims/llm-pipeline-explanations-no-advantage-over-self-learning.md) [-M]

## Related Designs
- 

## Examples
-

## Key Sources
- Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. https://arxiv.org/abs/2509.00961
