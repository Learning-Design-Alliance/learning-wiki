---
type: research-method
id: weekly-0-structural-check-for-cohort-behavioural-reorganisation
title: Weekly β0 structural check for cohort behavioural reorganisation
description: "A structural summary of how a cohort divides in each week: learners are represented as points in a feature space, connected when Euclidean distance falls below a threshold ε, and β0 counts the connected components of the graph, read as \"the number of distinct behavioural groups the cohort forms that"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Weekly β0 structural check for cohort behavioural reorganisation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A structural summary of how a cohort divides in each week: learners are represented as points in a feature space, connected when Euclidean distance falls below a threshold ε, and β0 counts the connected components of the graph, read as "the number of distinct behavioural groups the cohort forms that week". Tracked across weeks it describes reorganisation rather than level. It requires no optimisation or random seed, is defined for disconnected graphs, and is computed identically on real and synthetic cohorts.

## Accounts
<!-- How each source describes or uses the method -->
- **Weekly β0 structural check: connected components of a weekly proximity graph over learners tracked across a term**: A structural summary of how a cohort divides in each week: learners are represented as points in a feature space, connected when Euclidean distance falls below a threshold ε, and β0 counts the connected components of the graph, read as "the number of distinct behavioural groups the cohort forms that week". Tracked across weeks it describes reorganisation rather than level. It requires no optimisation or random seed, is defined for disconnected graphs, and is computed identically on real and synthetic cohorts. (Inoue et al. (2026))

### Claims

- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](../claims/synthetic-cohorts-understate-weekly-beta0-variation.md) [+M]
- [In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity](../claims/structural-check-calibrated-passable-separability-not-fidelity.md) [+M]
- [The routine rule for selecting the graph threshold makes naive comparisons of β0 between two datasets invalid](../claims/rule-selected-thresholds-make-cross-dataset-beta0-comparison-invalid.md) [~W]
- [Partition descriptors and the component-membership–study-volume association are reproduced by the synthetic cohorts](../claims/synthetic-cohorts-reproduce-partition-descriptors-and-study-volume-association.md) [~W]
- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](../claims/real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) [+W]

## Related Research Methods
-

## Key Sources
- Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://library.apsce.net. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)
