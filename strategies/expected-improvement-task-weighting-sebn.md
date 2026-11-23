---
type: strategy
id: expected-improvement-task-weighting-sebn
title: Weight candidate training tasks by expected improvement in estimated success rate between generations
description: "After each generation of rollouts, estimate base competency parameters by maximum likelihood, infer each candidate environment's success rate, and reweight the task distribution toward environments where the estimated..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: vincent-hsiao-2025
    resource: "https://arxiv.org/abs/2502.15662"
    title: "Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau. 2025. Automating Curriculum Learning for Reinforcement Learning using a Skill-Based Bayesian Network. Proc. of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025). https://arxiv.org/abs/2502.15662"
    author: Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau
---

# Weight candidate training tasks by expected improvement in estimated success rate between generations

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
After each generation of rollouts, estimate base competency parameters by maximum likelihood, infer each candidate environment's success rate, and reweight the task distribution toward environments where the estimated success rate changed most from the previous generation, with a smoothing factor for stability. The authors "choose a fitness function where the fitness of the environment is a function of the difference between the current estimated success rate and the estimated success rate on the last generation's SEBN," following the competence-progress idea of Stout and Barto. The curriculum is agnostic to the learning algorithm, requiring only rollout observations.

## Design Implications

### Context
#### Requirements
- A set of candidate tasks with environment features and targets
- Rollout data each generation to update competency estimates
- For large environment design spaces, an approximate search procedure such as the adapted KL-search with Weighted Mini-bucket Elimination
#### Constraints
- The sample-search procedure is not guaranteed to find environments with the largest heuristic difference, so sub-optimal environments can enter the curriculum

### Target Learners
- reinforcement learning agents

### Target Learning Goals
- faster learning and more robust policies on target tasks

### Affordances
- Sebn Skill Environment Bayesian Network

## Claims

- [SEBN-guided curricula produce more robust policies that reach success more quickly than other curricula in continuous control and robotics environments](../claims/sebn-curricula-outperform-baselines-continuous-robotics.md) [+W]
- [SEBN-guided curriculum learning curves show much higher variance than other methods due to approximate candidate search](../claims/sebn-curriculum-higher-variance.md) [-W]
- [In robosuite Door, SEBN-guided curriculum policies transfer to an unseen heavy door environment, obtaining a reward of 240 versus 150 without a curriculum](../claims/sebn-robosuite-heavy-door-transfer.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Vincent Hsiao, Mark Roberts, Laura M. Hiatt, George Konidaris, and Dana Nau. 2025. Automating Curriculum Learning for Reinforcement Learning using a Skill-Based Bayesian Network. Proc. of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025). https://arxiv.org/abs/2502.15662
