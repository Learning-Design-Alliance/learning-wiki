---
type: strategy
id: tunable-leniency-parameters-credit-decisions
title: Provide tunable leniency parameters (impact, sim_threshold, lo_threshold) to align automated credit decisions with institutional policy
description: The aggregation module exposes three parameters that decision-making authorities adjust to control how lenient automated credit decisions are.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: dhivya-chandrasekaran-and-vijay-mago-2021
    resource: "https://arxiv.org/abs/2104.01955"
    title: "Dhivya Chandrasekaran and Vijay Mago. (2021). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. https://arxiv.org/abs/2104.01955"
    author: Dhivya Chandrasekaran and Vijay Mago
---

# Provide tunable leniency parameters (impact, sim_threshold, lo_threshold) to align automated credit decisions with institutional policy

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The aggregation module exposes three parameters that decision-making authorities adjust to control how lenient automated credit decisions are. The article states "Three important tunable parameters are provided to adjust the level of leniency oﬀered by the decision-making authority in providing credits namely, 'impact', 'sim_threshold', and 'lo_threshold'" — governing the contribution ratio of the two similarities, the similarity value above which learning outcomes count as similar, and the proportion of learning outcomes needing similar counterparts. Higher values mean less leniency.

## Design Implications

### Context
#### Requirements
- The three-pass model producing taxonomic and semantic similarity grids
#### Constraints
- Increasing the impact of taxonomic similarity to a higher percentage reduces the overall similarity decision to only two or three action words

### Target Learners
- Administrators and articulation committees at receiving institutions

### Target Learning Goals
- Flexible, transparent transfer credit decisions matching institutional leniency norms

### Affordances
- [Three Pass Learning Outcome Similarity Model](../research-methods/three-pass-learning-outcome-similarity-method-for-automated-transfer-credit-assessment.md)

## Claims

- [Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators](../claims/lo-threshold-tuning-matches-annotator-leniency.md) [+W]
- [Human annotators converge on a similarity threshold above 7 of 10 before offering transfer credit](../claims/annotators-require-similarity-above-7-for-credit.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Dhivya Chandrasekaran and Vijay Mago. (2021). Automating Transfer Credit Assessment in Student Mobility - A Natural Language Processing-based Approach. https://arxiv.org/abs/2104.01955
