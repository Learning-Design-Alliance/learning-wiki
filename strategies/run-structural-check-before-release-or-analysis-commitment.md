---
type: strategy
id: run-structural-check-before-release-or-analysis-commitment
title: Run the structural check on a synthetic dataset, using only permutations of itself, before release or before committing to a line of analysis
description: The article recommends its surrogate-based structural check as a cheap, early screening step for synthetic educational datasets.
status: draft
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
> **Evidence** · no claims cited

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

## Related Strategies
- 

## Examples
-

## Key Sources
- Inoue, H., & Yasutake, K. (2026). What Fidelity Metrics Miss: A Structural Check on Synthetic Educational Data. Proceedings of the 34th International Conference on Computers in Education. Asia-Pacific Society for Computers in Education. https://arxiv.org/abs/2609.27265. [doi:10.48550/arxiv.2609.27265](https://doi.org/10.48550/arxiv.2609.27265)
