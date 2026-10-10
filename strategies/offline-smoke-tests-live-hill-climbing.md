---
type: strategy
id: offline-smoke-tests-live-hill-climbing
title: Use offline evaluations as smoke tests and live experiments for hill climbing
description: "The article recommends a three-step strategy for any hill-climbing change: \"(1) Conduct offline evals to make sure that the change is ok to show to users."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: udeshi-2026
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M
---

# Use offline evaluations as smoke tests and live experiments for hill climbing

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends a three-step strategy for any hill-climbing change: "(1) Conduct offline evals to make sure that the change is ok to show to users. This includes spot-checking threads from the eval datasets (2) Run a live experiment for 1-2 weeks (3) If the experiment shows improvements in metrics, launch the change." Offline hill climbing was abandoned because primary metrics rely on user actions that cannot be computed in single-turn offline evals, datasets are hard to maintain, and offline metrics saturated quickly.

## Design Implications

### Context
#### Requirements
- A live experiments platform sharing the same AI Component overrides spec as offline eval specs, with feature-flag management supporting thread- or user-level diversion and orthogonal traffic slices
#### Constraints
- Offline evaluation datasets are of O(100) and saturate quickly, with confidence intervals too wide to measure lift beyond roughly 80%

### Target Learners
- K-12 students using AI tutoring features at scale

### Target Learning Goals
- Improving AI tutoring quality metrics such as next-item correctness and cognitive engagement

## Related Strategies
- 

## Examples
-

## Key Sources
- Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home
