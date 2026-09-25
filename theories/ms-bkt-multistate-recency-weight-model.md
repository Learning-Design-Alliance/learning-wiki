---
type: theory
title: "MS-BKT: a multistate knowledge tracing model with data-driven recency weights replacing the learning rate"
description: "MS-BKT is a knowledge tracing architecture that keeps BKT's HMM structure but makes two changes: the knowledge node expands from 2 to 21 states, and a recency weight parameter R replaces the transition probability p(T..."
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

# MS-BKT: a multistate knowledge tracing model with data-driven recency weights replacing the learning rate

> **Theory** · [All theories](index.md)

## Description
MS-BKT is a knowledge tracing architecture that keeps BKT's HMM structure but makes two changes: the knowledge node expands from 2 to 21 states, and a recency weight parameter R replaces the transition probability p(T), so that "weight increases incrementally by a fixed quantum R for each new attempt" with the optimal value learned from data. Knowledge is updated per state via Bayes' rule and estimated by the MAP mode of the posterior, with parameters fit by Expectation Maximization. The authors position it as retaining BKT's parameter interpretability while balancing recent and historical data.

## Design Implications

### Context
#### Requirements
- Requires estimating the free recency parameter R and other parameters from data during model fitting
#### Constraints
- The choice of 21 states was made as granular enough with manageable calculation overhead; the authors note the number of states can be explored further, including a continuous distribution function

### Target Learners
- K-12 students practicing tagged skills in intelligent tutoring systems

### Target Learning Objectives
- Real-time estimation of student mastery of a skill to drive adaptive learning

### Claims
- [Recency Weights Capture Learning And Forgetting From Data](../claims/recency-weights-capture-learning-and-forgetting-from-data.md) [+M]
- [Ms Bkt Estimates Fluctuate Less Than Bkt](../claims/ms-bkt-estimates-fluctuate-less-than-bkt.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/
