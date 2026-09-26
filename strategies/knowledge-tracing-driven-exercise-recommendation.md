---
type: strategy
id: knowledge-tracing-driven-exercise-recommendation
title: Knowledge-Tracing-Driven Exercise Recommendation
description: "The survey's first application area uses traced knowledge states to choose learning resources automatically."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# Knowledge-Tracing-Driven Exercise Recommendation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The survey's first application area uses traced knowledge states to choose learning resources automatically. "Given the inferred knowledge states, one common strategy is selecting the next exercise that will best advance students’ knowledge acquisition." Examples include the BKT-sequence algorithm, which returns the exercise whose predicted score is closest to the expected score, a DKVMN extension recommending exercises in SPOCs, and a BKT video model for evaluating video resources.

## Design Implications

### Context
#### Requirements
- A KT model estimating each student's current knowledge state per knowledge concept
- Predicted scores for candidate exercises, matched against an expected score that depends on the current knowledge state
#### Constraints
- The survey says existing solutions mainly assign non-mastered exercises, which it calls reasonable but too broad to advance learning effectively

### Target Learners
- Students in intelligent tutoring systems and Small Private Online Courses

### Target Learning Goals
- Knowledge acquisition and learning efficiency through appropriately difficult exercises

## Related Strategies
- [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- [Knowledge Tracing Learner Modeling Task](../theories/knowledge-tracing-learner-modeling-task.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
