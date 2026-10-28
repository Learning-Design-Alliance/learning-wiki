---
type: strategy
id: future-work-affective-embeddings-and-end-to-end-training
title: Exploit affective and behavioral clickstream attributes via unsupervised embeddings and end-to-end training for career prediction.
description: "Future work proposes using \"unsupervised feature embedding methods\" such as \"a variational auto-encoder to encode the clickstream record to an embedded feature vector\" to leverage unused affective-state and disengaged..."
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

# Exploit affective and behavioral clickstream attributes via unsupervised embeddings and end-to-end training for career prediction.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
Future work proposes using "unsupervised feature embedding methods" such as "a variational auto-encoder to encode the clickstream record to an embedded feature vector" to leverage unused affective-state and disengaged-behavior attributes, and merging the two-fold pipeline into "end-to-end training" so the model "can automatically learn the latent representation of the necessary processing steps to map students' clickstream data to their career choices."

## Design Implications

### Context
#### Requirements
- Requires clickstream attributes beyond skill and correctness, such as affective states and disengaged behaviors, and an embedding or end-to-end model architecture
#### Constraints
- 

### Target Learners
- middle school students

### Target Learning Goals
- STEM career prediction

## Claims

- [Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.](../claims/combined-dkt-knowledge-state-features-improve-stem-job-prediction.md) [+W]
- [DKT+ knowledge states discriminate STEM from non-STEM students better than DKT knowledge states for the majority of mathematical skills.](../claims/dkt-plus-knowledge-state-better-discrimination-than-dkt.md) [+W]
- [LDA projection visualizations show knowledge-state features separate STEM and non-STEM classes better than student-profile features.](../claims/lda-projection-knowledge-state-separates-classes-better-than-profile.md) [+W]
- [The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.](../claims/overfitting-from-small-labeled-set-and-high-dimensionality.md) [+W]
- [Recursive feature elimination mitigates overfitting and improves STEM/non-STEM prediction performance, with LR-DKT&SP performing best after RFE.](../claims/rfe-mitigates-overfitting-in-stem-job-prediction.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256
