---
type: theory
id: ms-bkt-multistate-recency-weight-model
moved_from: [method/recency-adjustment-over-static-learning-rate]
title: "MS-BKT: a multistate knowledge tracing model with data-driven recency weights replacing the learning rate"
description: "MS-BKT is a knowledge tracing architecture that keeps BKT's HMM structure but makes two changes: the knowledge node expands from 2 to 21 states, and a recency weight parameter R replaces the transition probability p(T..."
status: review
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
> **Evidence** · no claims cited

## Description
MS-BKT is a knowledge tracing architecture that keeps BKT's HMM structure but makes two changes: the knowledge node expands from 2 to 21 states, and a recency weight parameter R replaces the transition probability p(T), so that "weight increases incrementally by a fixed quantum R for each new attempt" with the optimal value learned from data. Knowledge is updated per state via Bayes' rule and estimated by the MAP mode of the posterior, with parameters fit by Expectation Maximization. The authors position it as retaining BKT's parameter interpretability while balancing recent and historical data.

## Design Implications

### Context
#### Requirements
- Requires estimating the free recency parameter R and other parameters from data during model fitting
- The recency weight quantum R must be learned from data during model fitting
#### Constraints
- The choice of 21 states was made as granular enough with manageable calculation overhead; the authors note the number of states can be explored further, including a continuous distribution function
- Prediction quality on held-out data was similar to, not better than, classic BKT on most datasets

### Target Learners
- K-12 students practicing tagged skills in intelligent tutoring systems
- Students in intelligent tutoring systems using mastery learning

### Target Learning Objectives
- Real-time estimation of student mastery of a skill to drive adaptive learning
- Accurate, interpretable real-time estimation of student knowledge level

### Claims

## Related Theories

- [Two hypotheses for the meaning of Spectral BKT's intermediate states: a stages-of-mastery account and a mastery-by-metacognition interaction account](spectral-bkt-intermediate-state-hypotheses.md)
- [Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment](bkt-mastery-updating-model.md)

## Examples
-

## Key Sources
- Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/

<!-- merged 2026-10-20 from methods/recency-adjustment-over-static-learning-rate ("Apply a recency adjustment to Bayesian knowledge-estimation updates instead of a static learning rate"), an isolated part of this page (maintainer 2026-10-20: fold approved): its body as it stood. Its bullets this page lacked were added above.

# Apply a recency adjustment to Bayesian knowledge-estimation updates instead of a static learning rate

> **Design Method** · [All design methods](index.md)
> **Evidence** · no claims cited

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

## Related Principles
- 

## Examples
-

## Key Sources
- Agarwal, D., Baker, R.S., & Muraleedharan, A. (2020). Dynamic knowledge tracing through data driven recency weights. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org/edm2020/
-->
