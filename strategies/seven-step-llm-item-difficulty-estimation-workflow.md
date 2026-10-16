---
type: strategy
id: seven-step-llm-item-difficulty-estimation-workflow
title: Seven-step workflow for testing professionals to implement LLM-based item difficulty estimation with their item pool
description: "The article offers its methods as a reusable implementation path for other testing organizations, stating: \"We provide a seven-step workflow for testing professionals who would want to implement a similar item difficu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: pooya-razavi-2025
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: Pooya Razavi, Sonya Powers
---

# Seven-step workflow for testing professionals to implement LLM-based item difficulty estimation with their item pool

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article offers its methods as a reusable implementation path for other testing organizations, stating: "We provide a seven-step workflow for testing professionals who would want to implement a similar item difficulty estimation approach with their item pool". The workflow distills the study's pipeline: SME feature elicitation, prompt development with iterative refinement, direct and feature-based LLM estimation, rescaling to the IRT scale, ensemble model training with cross-validation, and benchmark comparison on a stratified holdout sample. It is intended to streamline item development and reduce reliance on extensive field testing.

## Design Implications

### Context
#### Requirements
- An item pool with existing calibrated difficulty values (Rasch IRT parameters) for training and validation
- Access to an LLM via API with output variability controlled (temperature set to zero)
#### Constraints
- Prompt refinement on a subset of items (n = 250) continued until performance plateaued; few-shot prompts did not improve results
- Accuracy was worse for early grades, so the approach needs grade-level caution

### Target Learners
- K-5 students assessed in mathematics and reading

### Target Learning Goals
- Scalable pre-screening of item difficulty to support efficient item development and adaptive testing

## Related Strategies
- 

## Examples
-

## Key Sources
- Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015
