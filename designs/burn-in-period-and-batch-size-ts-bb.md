---
type: design
id: burn-in-period-and-batch-size-ts-bb
title: Burn-in period and batch size parameters for balancing statistical inference and optimization in adaptive experiments
description: Two tunable parameters of the TS-BB adaptive experimentation engine.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: ilya-musabirov-2024
    resource: "https://doi.org/10.1145/3660650.3660659"
    title: "Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659"
    author: Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams
---

# Burn-in period and batch size parameters for balancing statistical inference and optimization in adaptive experiments

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size

## Description
Two tunable parameters of the TS-BB adaptive experimentation engine. The burn-in period sets "the first𝑘 cases (or batches) to be served using uniform random assignment instead of Thompson Sampling" while still updating distributions, and the batch size "regulates the minimal number of data points collected by the adaptive experimentation engine before updating the parameters". In the case study, "the burn-in period was set at 100" and "The batch size was set to 10".

## Design Implications

### Context
#### Requirements
- An adaptive experimentation engine running TS-BB that records rewards and updates arm distributions as cases arrive.
#### Constraints
- A reasonable burn-in period can only "partially alleviate" the early- vs. late-comer problem, by "preventing premature swings to a condition preferred by early-comers until reasonable evidence is gathered".

### Target Learners
- CS1 students completing online homework problems

### Learning Goals
- Less biased samples for null hypothesis significance testing
- Reducing noise and computational effort in arm updates

### Claims
- [Adaptive Bandit Reallocates Majority To Better Condition](../claims/adaptive-bandit-reallocates-majority-to-better-condition.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659
