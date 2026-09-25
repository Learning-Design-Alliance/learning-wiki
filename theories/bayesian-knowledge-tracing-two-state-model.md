---
type: theory
title: Bayesian Knowledge Tracing (Two-State Hidden Markov Model)
description: The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (gue...
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

# Bayesian Knowledge Tracing (Two-State Hidden Markov Model)

> **Theory** · [All theories](index.md)

## Description
The survey describes Bayesian Knowledge Tracing (BKT), introduced by Corbett and Anderson, as a special case of the Hidden Markov Model with learning parameters (transition, forgetting) and performance parameters (guess, slip) plus an initial mastery probability. "BKT operates within a two-state student modeling framework: knowledge is either learned or unlearned, and there is no forgetting once a student has mastered the knowledge." Dynamic Bayesian knowledge tracing extends it to model hierarchies and relationships among knowledge concepts jointly.

## Design Implications

### Context
#### Requirements
- Per-knowledge-concept parameters: initial probability of mastery, transition probability, guessing probability and slipping probability
- Observed correct/incorrect answers used to update the posterior probability of mastery
#### Constraints
- Standard BKT models the parameters of each knowledge concept independently, although the survey notes knowledge concepts are hierarchical and closely related
- Fundamental models such as BKT often overlook forgetting

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims
- [Bkt Overestimates Accuracy After A Day Elapses](../claims/bkt-overestimates-accuracy-after-a-day-elapses.md) [-W]
- [Individualized Bkt Reduces Questions Needed For Mastery](../claims/individualized-bkt-reduces-questions-needed-for-mastery.md) [+W]

## Related Theories
- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)
- Mastery Learning

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
