---
type: strategy
id: pace-assistance-separately-per-context
title: Pace curriculum assistance separately for task contexts that learn at different rates, using per-context frontiers rather than a shared schedule
description: "The article's design recommendation is to pace assistance separately for contexts that progress at different rates: \"Contexts that learn at different rates should not be forced to share a frontier.\" The implementable..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: siddharth-aphale-2026
    resource: "https://arxiv.org/abs/2607.26417"
    title: "Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. https://arxiv.org/abs/2607.26417"
    author: Siddharth Aphale, Ayushman Singh
---

# Pace curriculum assistance separately for task contexts that learn at different rates, using per-context frontiers rather than a shared schedule

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's design recommendation is to pace assistance separately for contexts that progress at different rates: "Contexts that learn at different rates should not be forced to share a frontier." The implementable recipe is a per-context frontier updated by binary success, with retreat on failure and an occasional harder-start probe on stalling frontiers. Known groups are useful when their members need roughly the same pacing; otherwise a shared frontier can fail.

## Design Implications

### Context
#### Requirements
- Restorable states ordered from easier to harder starts
- Binary rollout success as the only controller signal
#### Constraints
- Scaffolds are most useful when the learner is held back by poor access to later task stages; a directed learner can sometimes overcome the state-access problem on its own
- Conflict prevalence and level needs for longer tasks remain open

### Target Learners
- reinforcement learning agents in sparse-reward settings

### Target Learning Goals
- reaching later task stages that unassisted rollouts rarely visit

### Affordances
- Per Context Reverse Curriculum Controller

## Claims

- [Pacing granularity must match heterogeneity: pooling contexts that learn at different rates under one label collapses the hard band, which per-context pacing handles](../claims/pacing-granularity-matches-heterogeneity.md) [+M]
- [A counting construction proves that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice](../claims/synchronized-global-pacing-insufficiency.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. https://arxiv.org/abs/2607.26417
