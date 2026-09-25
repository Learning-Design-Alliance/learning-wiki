---
type: principle
id: adaptive-learning-consistent-with-cognitive-structure
title: Adaptive Learning Consistent with Knowledge Level and Knowledge Structure
description: "The survey argues that because students' cognitive structures include both their knowledge level and the knowledge structure of learning items (e.g., prerequisites), \"adaptive learning should maintain consistency with..."
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

# Adaptive Learning Consistent with Knowledge Level and Knowledge Structure

> **Principle** · [All principles](index.md)

## Description
The survey argues that because students' cognitive structures include both their knowledge level and the knowledge structure of learning items (e.g., prerequisites), "adaptive learning should maintain consistency with both students’ knowledge level and the latent knowledge structure." It cites CSEAL, which uses DKT to trace knowledge states, a knowledge-structure navigation algorithm for logical learning paths, and an actor-critic algorithm to decide what to learn next.

## Design Implications

### Context
#### Requirements
- A KT model tracing each student's evolving knowledge state
- A representation of prerequisite relations among learning items to constrain learning paths
#### Constraints
- The survey states that existing adaptive learning methods often focus separately on either students' knowledge levels or the knowledge structure of learning items

### Target Learners
- Students in adaptive learning systems, including MOOCs and programming tutors

### Target Learning Objectives
- Following individualized, logically ordered learning paths until each rule or concept is mastered

### Claims
- 

## Related Principles
- [Adaptive Learning](adaptive-learning.md)
- [Mastery Learning](mastery-learning.md)
- [Knowledge Tracing Learner Modeling Task](../theories/knowledge-tracing-learner-modeling-task.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
