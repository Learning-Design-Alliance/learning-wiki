---
type: strategy
id: run-structural-check-before-release-or-analysis-commitment
title: Run the structural check on a synthetic dataset, using only permutations of itself, before release or before committing to a line of analysis
description: The article recommends its surrogate-based structural check as a cheap, early screening step for synthetic educational datasets.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: inoue-2026
    resource: "https://arxiv.org/abs/2609.27265"
    title: "Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265"
    author: "Inoue, H., & Yasutake, K"
---

# Run the structural check on a synthetic dataset, using only permutations of itself, before release or before committing to a line of analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends its surrogate-based structural check as a cheap, early screening step for synthetic educational datasets. Because the computation "needs a synthetic dataset and permutations of itself", a data custodian can run it before release and a researcher before committing to an analysis, flagging synthetic cohorts whose weekly structure is implausibly flat without touching real data. It reaches part of what epistemic precision reaches, but only afterwards.

## Design Implications

### Context
#### Requirements
- A synthetic dataset of the learner-by-week shape and the ability to generate permutations of it; no real-data access is needed for the surrogate comparison
#### Constraints
- Reading the size of the gap, as in Table 2, needs a real reference
- The check examines one structural property rather than the researcher's actual conclusions
- Establishing that it is informative elsewhere would require further datasets and further synthesis mechanisms

### Target Learners
- lower-secondary school learners whose study-habit logs are shared through synthetic-data platforms

### Target Learning Goals
- trustworthy secondary use of learning-platform data for research on temporal cohort structure

## Claims

- [Real cohorts separate from marginal-preserving surrogates of themselves in all four years, while three of four synthetic cohorts do not](../claims/real-cohorts-separate-from-marginal-surrogates-synthetic-do-not.md) [+W]
- [In a control experiment on data of known construction, the check is calibrated, can be passed, and separability from marginals is not fidelity](../claims/structural-check-calibrated-passable-separability-not-fidelity.md) [+W]
- [Synthetic cohorts place week-to-week change in the term's examination weeks, which real cohorts do not](../claims/synthetic-cohorts-misplace-examination-week-structure.md) [+W]
- [Synthetic cohorts reproduce the level and shape of the weekly β0 partition but vary 2.6–4.9 times less across the term than real cohorts at a common working point](../claims/synthetic-cohorts-understate-weekly-beta0-variation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)
