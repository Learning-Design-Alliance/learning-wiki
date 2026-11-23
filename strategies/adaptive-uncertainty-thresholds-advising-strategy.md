---
type: strategy
id: adaptive-uncertainty-thresholds-advising-strategy
title: Use adaptive uncertainty thresholds instead of fixed domain-specific thresholds for advising decisions
description: "The article's algorithms determine uncertainty thresholds dynamically from previously observed uncertainty values rather than fixing them per domain."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: sahir-2022
    resource: "https://arxiv.org/abs/2204.07254"
    title: "Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). https://arxiv.org/abs/2204.07254"
    author: Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor
---

# Use adaptive uncertainty thresholds instead of fixed domain-specific thresholds for advising decisions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's algorithms determine uncertainty thresholds dynamically from previously observed uncertainty values rather than fixing them per domain. As printed: "we use adaptive uncertainty thresholds to avoid tuning domain-specific uncertainty thresholds to enable scalability of our methods." Percentile values (p1 = 70 for the student, p2 = 90 for the model of the teacher) are computed over an uncertainty buffer with a minimum window size of 200, so the same hyperparameters are kept across all five Atari domains.

## Design Implications

### Context
#### Requirements
- An uncertainty buffer with a minimum window size (set to 200) to ensure enough data for accurate threshold estimates
#### Constraints
- The authors note fixed percentile values could be extended to a dynamic schedule, since a lower percentile for the student's uncertainty would not capture states for which the student is genuinely uncertain

### Target Learners
- reinforcement learning student agents across domains

### Target Learning Goals
- decide when to request teacher advice without per-domain threshold tuning

### Affordances
- Dual Uncertainty Advice Collection Reuse Framework

## Related Strategies

- [Set difficulty-specific intervention times based on when prediction quality exceeds a fixed threshold](difficulty-specific-intervention-times.md)
- [Teachers adaptively review the top-n students by model confidence instead of using fixed-threshold binary predictions](top-n-confidence-review-strategy.md)

## Examples
-

## Key Sources
- Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). https://arxiv.org/abs/2204.07254. [doi:10.48550/arxiv.2204.07254](https://doi.org/10.48550/arxiv.2204.07254)
