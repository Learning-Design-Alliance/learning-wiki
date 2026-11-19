---
type: strategy
id: choose-privacy-loss-epsilon-tradeoff
title: Specify the privacy loss epsilon by balancing efficiency tolerance, expected outcome levels, and regulatory privacy standards
description: "When deploying an RP-RCT, investigators must choose the FRR parameters r and r', which jointly determine the privacy loss epsilon and the statistical efficiency of treatment-effect estimation."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: manjusha-kancharla-and-hyunseung-kang-2021
    resource: "https://arxiv.org/abs/2112.02452"
    title: "Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. https://arxiv.org/abs/2112.02452"
    author: Manjusha Kancharla and Hyunseung Kang
---

# Specify the privacy loss epsilon by balancing efficiency tolerance, expected outcome levels, and regulatory privacy standards

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 design, 1 theoretical), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
When deploying an RP-RCT, investigators must choose the FRR parameters r and r', which jointly determine the privacy loss epsilon and the statistical efficiency of treatment-effect estimation. The article recommends that investigators "specify ϵ based on (a) their tolerance for loss in eﬃciency at the expense of more privacy" and on expected outcome levels and regulatory standards. In the UW-Madison application the team chose epsilon = 2, tolerating roughly a 50% increase in standard error relative to a standard RCT.

## Design Implications

### Context
#### Requirements
- Knowledge of expected control and treatment outcome levels, potentially from subject-matter experts during planning
- Awareness of recommended data privacy standards from relevant regulatory bodies
#### Constraints
- Any finite epsilon implies the RP-RCT estimator is strictly less efficient than the standard RCT estimator

### Target Learners
- students in online courses with sensitive outcome data

### Target Learning Goals
- credible program evaluation while protecting student data privacy

## Claims

- [The RP-RCT difference-in-means estimator is never as asymptotically efficient as the standard RCT estimator when privacy is guaranteed](../claims/rp-rct-efficiency-cost-of-privacy.md) [+W]
- [ε=2.0 provides the best privacy–utility balance, while ε=0.5 introduces excessive noise that degrades performance below baseline on ASSIST09](../claims/privacy-budget-epsilon-tradeoff-cognitive-diagnosis.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. https://arxiv.org/abs/2112.02452
