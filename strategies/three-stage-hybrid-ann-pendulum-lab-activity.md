---
type: strategy
id: three-stage-hybrid-ann-pendulum-lab-activity
title: Three-stage hybrid laboratory activity combining analytical pendulum analysis with ANN modeling
description: "The article proposes a structured classroom implementation blending theoretical concepts, experimental investigation, and data-driven modeling across \"an activity of 2-3 laboratory sessions\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: saralasrita-mohanty-2026
    resource: "https://arxiv.org/abs/2503.23506"
    title: "Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2026). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. https://arxiv.org/abs/2503.23506"
    author: Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty
---

# Three-stage hybrid laboratory activity combining analytical pendulum analysis with ANN modeling

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a structured classroom implementation blending theoretical concepts, experimental investigation, and data-driven modeling across "an activity of 2-3 laboratory sessions". In stage one, students perform the compound pendulum experiment and record time periods for different effective lengths and small angular displacements. In stage two, they analyse the data conventionally to determine g including uncertainty estimation. In stage three, they train an ANN on the same dataset and compare its predictions with the analytical results, forming the basis for discussion of model reliability, generalisation, and limitations.

## Design Implications

### Context
#### Requirements
- Structured guidelines and simplified code frameworks so the focus remains on conceptual understanding rather than technical complexity
- Additional instructional support for students with varying familiarity with programming and machine learning
#### Constraints
- Proposed for second/third-year undergraduate laboratory courses on oscillatory systems or experimental methods; students may have varying levels of programming and machine-learning familiarity

### Target Learners
- second/third-year undergraduate physics and engineering students

### Target Learning Goals
- experimental data acquisition and uncertainty analysis
- ANN-based modeling of experimental data
- critical evaluation of theory-driven versus data-driven approaches

### Affordances
- [Ann Architecture Data Driven Approximator](../designs/ann-architecture-data-driven-approximator.md)

## Claims

- [ANN prediction accuracy depends on hidden-node count, with 9 hidden nodes optimal and larger or smaller configurations showing overfitting or underfitting](../claims/hidden-node-count-ann-overfitting-underfitting.md) [+W]
- [Validation MSE reaches its minimum at epoch 127, and early stopping there prevents overfitting](../claims/early-stopping-validation-minimum-epoch-127.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2026). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. https://arxiv.org/abs/2503.23506
