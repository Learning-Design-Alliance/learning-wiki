---
type: strategy
id: model-based-responder-selection-strategy
title: Model-based individualized diagnostics to select responders before training
description: Before training, collect pre-test reading speed and one training-session lexical decision block; extract participant-level features from linear mixed models (random slope estimates of lexical categorization uncertaint...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: benjamin-gagl-klara-gregorová-2024
    resource: "https://doi.org/10.1038/s41539-024-00237-7"
    title: "Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7"
    author: "Benjamin Gagl & Klara Gregorová"
---

# Model-based individualized diagnostics to select responders before training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Before training, collect pre-test reading speed and one training-session lexical decision block; extract participant-level features from linear mixed models (random slope estimates of lexical categorization uncertainty, OLD20, lexicality, plus incoming reading speed and week) and apply the trained prediction pipeline to decide who should train. The article shows this "individualized diagnostic procedure" predicted outcomes with r = 0.69 in the best pipeline and "allow[s] focusing training resources on responders only." The procedure is described as efficient at relatively low cost.

## Design Implications

### Context
#### Requirements
- Data from the pre-training reading speed assessment and the first training session only.
- Linear mixed models with crossed random effects (participant and stimulus) to extract per-participant random slope estimates.
- Consensus nested leave-one-out cross-validation for feature selection and hyperparameter tuning to limit overfitting.
#### Constraints
- Requires independent-sample evaluation to fully rule out overfitting; training week significantly moderates predictions; more complex machine learning methods may need datasets larger than 100 participants and would reduce interpretability.

### Target Learners
- adult non-native German language learners with slow reading speed

### Target Learning Goals
- reading speed improvement
- efficient allocation of training resources

### Affordances
- Lexical Categorization Model Lcm

## Claims

- [LCM-related features, especially lexical categorization uncertainty, are the most important word-characteristic predictors of training success](../claims/lcm-features-essential-prediction.md) [+W]
- [Training response times rise with lexical categorization uncertainty and fall across sessions, but a reduction of the uncertainty effect across sessions appears only in Experiment 1](../claims/uncertainty-effect-training-sessions-mixed.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7
