---
type: principle
id: multi-objective-exercise-recommendation-objectives
title: "Multi-Objective Exercise Recommendation: Review and Explore, Smooth Difficulty, Engagement"
description: The survey reports three objectives proposed by Huang et al.
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

# Multi-Objective Exercise Recommendation: Review and Explore, Smooth Difficulty, Engagement

> **Principle** · [All principles](index.md)

## Description
The survey reports three objectives proposed by Huang et al. to go beyond assigning non-mastered exercises: "review and explore , smoothness of difficulty level and student engagement ." Review and explore reinforces non-mastered concepts with timely reviews while keeping opportunities to explore new knowledge; smooth difficulty keeps consecutive exercises within a small difficulty range; engagement aligns recommended exercises with student preferences. These objectives are optimized in a multi-objective deep reinforcement learning (DRE) framework.

## Design Implications

### Context
#### Requirements
- Traced knowledge states plus reward functions that capture and quantify each of the three objectives, as in the DRE framework
#### Constraints
- The survey reports only that DRE can effectively learn from learning records to optimize multiple objectives; no magnitude of learning benefit is given

### Target Learners
- Students receiving exercise recommendations in online intelligent education systems

### Target Learning Objectives
- Reviewing non-mastered concepts, exploring new knowledge, and sustaining enthusiasm during learning

### Claims
- 

## Related Principles
- [Knowledge Tracing Driven Exercise Recommendation](../strategies/knowledge-tracing-driven-exercise-recommendation.md)
- [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- [Engagement](engagement.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
