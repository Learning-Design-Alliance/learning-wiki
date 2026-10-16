---
type: strategy
id: five-moment-q-learning-lesson-plan
title: A 50-minute five-moment lesson plan maps each teaching moment to a specific interface affordance
description: "The tool ships with a 50-minute lesson plan structured around five moments — stepping through ignorance, the first goal, convergence, hyperparameter experiments, and reward design — 'each mapped to a specific interfac..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: jueng-2026
    resource: "https://arxiv.org/abs/2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802"
    author: Jueng, Ekkachai
---

# A 50-minute five-moment lesson plan maps each teaching moment to a specific interface affordance

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The tool ships with a 50-minute lesson plan structured around five moments — stepping through ignorance, the first goal, convergence, hyperparameter experiments, and reward design — 'each mapped to a specific interface affordance.' Moments use single-step mode, ×100 training, and editable rewards; the reward-design moment has students check pit-seeking behavior against the optimal policy to distinguish under-exploration from a broken objective.

## Design Implications

### Context
#### Requirements
- Requires the tool's single-step mode, ×100 training mode, editable reward values, and the Bellman panel.
#### Constraints
- Learning gains have not been measured; the authors deliberately deferred a classroom study with pre/post concept inventory and usability instruments.

### Target Learners
- undergraduate machine-learning students

### Target Learning Goals
- understanding why exploration is needed
- observing backward value propagation from the goal
- designing and diagnosing reward functions

## Claims

- [Hyperparameter sweeps reproduce the lesson's claims: γ = 0 never solves the task while ε = 1 still converges](../claims/hyperparameter-sweeps-reproduce-lesson-claims.md) [+W]

## Related Strategies

- [Structuring Lessons](structuring_lessons.md)
- [Time Management In Instruction](time-management-in-instruction.md)

## Examples
-

## Key Sources
- Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802. [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)
