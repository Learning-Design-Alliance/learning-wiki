---
type: design
id: oulad-snapshot-recourse-evaluation-protocol
title: OULAD snapshot evaluation protocol with leakage-excluded presentation-level split
description: The evaluation protocol constructs two snapshots per eligible student per assessment, at t = d-14 and t = d-7 before the due day, using only information available up to snapshot time; post-t interactions and assessmen...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: ngoc-luyen-le-2026
    resource: "https://arxiv.org/abs/2608.17618"
    title: "Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618"
    author: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
---

# OULAD snapshot evaluation protocol with leakage-excluded presentation-level split

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The evaluation protocol constructs two snapshots per eligible student per assessment, at t = d-14 and t = d-7 before the due day, using only information available up to snapshot time; post-t interactions and assessments are excluded. Features include "aggregated click counts by activity type over rolling 7-, 14-, and 28-day windows", availability-alignment features, prior assessment history, time-to-deadline variables, and immutable learner descriptors. Data are split at the module-presentation level (15 train, 2 validation, 5 test presentations) to avoid leakage across closely related offerings, with pass defined as score >= 40.

## Design Implications

### Context
#### Requirements
- Snapshots must exclude post-t information to avoid leakage
- Splits at module-presentation level to avoid leakage across related offerings
#### Constraints
- Early assessments that would induce negative snapshot times are handled during preprocessing

### Target Learners
- Open University students in the OULAD dataset

### Learning Goals
- next-assessment pass/fail prediction and recourse generation

### Claims
- [Oulad Calibrated Logistic Regression Strong Prediction](../claims/oulad-calibrated-logistic-regression-strong-prediction.md) [+M]
- [Ip Recourse Compact Plans At Scale](../claims/ip-recourse-compact-plans-at-scale.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618
