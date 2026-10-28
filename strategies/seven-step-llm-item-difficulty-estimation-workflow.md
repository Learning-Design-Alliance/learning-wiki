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
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

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

## Claims

- [Direct LLM estimation accuracy varies by grade, performing worse for early grades; math grade K was worse than the dummy regressor and math grade 1 showed no significant prediction](../claims/direct-llm-accuracy-varies-by-grade-early-grades-worse.md) [~W]
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](../claims/direct-llm-estimation-beats-dummy-regressor-k5-items.md) [+W]
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](../claims/feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) [+W]
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](../claims/feature-importance-spread-across-many-features.md) [+W]
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](../claims/llm-features-add-value-beyond-item-metadata.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015
