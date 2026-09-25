---
type: principle
id: recency-adjustment-over-static-learning-rate
title: Apply a recency adjustment to Bayesian knowledge-estimation updates instead of a static learning rate
description: "The paper's concluding recommendation is that student-model designers consider replacing a static learning rate with a recency adjustment to Bayesian updates, because this \"can lead to better properties of knowledge e..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: agarwal-2020
    resource: "https://educationaldatamining.org/edm2020/"
    title: "Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/"
    author: "Agarwal, D., Baker, R.S., & Muraleedharan, A"
---

# Apply a recency adjustment to Bayesian knowledge-estimation updates instead of a static learning rate

> **Principle** · [All principles](index.md)

## Description
The paper's concluding recommendation is that student-model designers consider replacing a static learning rate with a recency adjustment to Bayesian updates, because this "can lead to better properties of knowledge estimation, compared to using a static learning rate". It also proposes treating latent knowledge as a multistate variable rather than 2 states, leading to smoother updates in the learning level estimate. The recommendation rests on the model's demonstrated estimation properties rather than prediction gains.

## Design Implications

### Context
#### Requirements
- The recency weight quantum R must be learned from data during model fitting
#### Constraints
- Prediction quality on held-out data was similar to, not better than, classic BKT on most datasets

### Target Learners
- Students in intelligent tutoring systems using mastery learning

### Target Learning Objectives
- Accurate, interpretable real-time estimation of student knowledge level

### Claims
- [Recency Weights Capture Learning And Forgetting From Data](../claims/recency-weights-capture-learning-and-forgetting-from-data.md) [+M]
- [Ms Bkt Estimates Fluctuate Less Than Bkt](../claims/ms-bkt-estimates-fluctuate-less-than-bkt.md) [+M]
- [Ms Bkt Performs Similarly To Classic Bkt On Holdout Data](../claims/ms-bkt-performs-similarly-to-classic-bkt-on-holdout-data.md) [~M]

## Related Principles
- 

## Examples
-

## Key Sources
- Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/
