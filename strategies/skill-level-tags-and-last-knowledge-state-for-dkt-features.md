---
type: strategy
id: skill-level-tags-and-last-knowledge-state-for-dkt-features
title: Use skill-level tags and last-time-step knowledge states when training DKT for downstream static models.
description: "The article adopts skill-level rather than question-level tags because \"using the question-level tag will induce sparsity in both vector representation and data density\", and extracts the knowledge state at the last i..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: yeung-2018
    resource: "https://arxiv.org/abs/1806.03256"
    title: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256"
    author: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y"
---

# Use skill-level tags and last-time-step knowledge states when training DKT for downstream static models.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article adopts skill-level rather than question-level tags because "using the question-level tag will induce sparsity in both vector representation and data density", and extracts the knowledge state at the last interaction because "the knowledge state computed from the DKT retains the information from past interactions thanks to the RNN's architecture" and ensures a fixed feature size for static machine learning models.

## Design Implications

### Context
#### Requirements
- Requires a DKT model trained with skill-level tags and extraction of the last knowledge state yT as fixed-size features
#### Constraints
- 

### Target Learners
- middle school students

### Target Learning Goals
- STEM career prediction

## Claims

- [Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.](../claims/combined-dkt-knowledge-state-features-improve-stem-job-prediction.md) [+W]
- [LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.](../claims/lda-projection-knowledge-state-separates-classes-better-than-profile.md) [+W]
- [Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.](../claims/rfe-mitigates-overfitting-in-stem-job-prediction.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256
