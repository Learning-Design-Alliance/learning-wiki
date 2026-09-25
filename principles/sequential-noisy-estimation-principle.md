---
type: principle
id: sequential-noisy-estimation-principle
title: Use stochastic approximation for sequential parameter estimation when observations are noisy and each observation is costly
description: The article supports using the Robbins-Monro procedure in settings where a parameter must be estimated sequentially from noisy observations, as in adaptive measurement of learner ability.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: wolff-1970
    resource: "https://eric.ed.gov/?id=ED051258"
    title: "Wolff, Hans. (1970). On Stochastic Approximation. https://eric.ed.gov/?id=ED051258"
    author: Wolff, Hans
---

# Use stochastic approximation for sequential parameter estimation when observations are noisy and each observation is costly

> **Principle** · [All principles](index.md)

## Description
The article supports using the Robbins-Monro procedure in settings where a parameter must be estimated sequentially from noisy observations, as in adaptive measurement of learner ability. Because the procedure updates after each observation, it suits contexts where observations are costly and convergence must be guaranteed. The article's contribution is the condition the iteration coefficients must satisfy for such sequential estimation to converge.

## Design Implications

### Context
#### Requirements
- Iteration coefficients chosen to satisfy the article's necessary and sufficient convergence condition
#### Constraints
- The guarantee is mathematical; the article reports no instructional trial of the procedure

### Target Learners
- learners undergoing sequential or adaptive assessment

### Target Learning Objectives
- accurate estimation of learner ability or learning parameters

### Claims
- Convergence Condition Stochastic Approximation [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Wolff, Hans. (1970). On Stochastic Approximation. https://eric.ed.gov/?id=ED051258
