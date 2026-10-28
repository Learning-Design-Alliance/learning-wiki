---
type: design
id: cognitive-tutor-partially-observable-planning
title: Intelligent cognitive tutor for planning in partially observable environments
description: An intelligent tutoring system that teaches MGPO-discovered planning strategies through interactive practice with metacognitive feedback.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: heindrich-2025
    resource: "https://doi.org/10.1007/s40593-025-00493-7"
    title: "Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7"
    author: "Heindrich, L., Consul, S., & Lieder, F"
---

# Intelligent cognitive tutor for planning in partially observable environments

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An intelligent tutoring system that teaches MGPO-discovered planning strategies through interactive practice with metacognitive feedback. "To teach people the planning strategies discovered by MGPO, we developed a cognitive tutor" that presents learners with highlighted planning-action choices, provides feedback on suboptimal selections with delay penalties proportional to the VOC difference, and demonstrates the optimal strategy through step-by-step videos. Unlike prior tutors using dynamic programming with cached Q-values, this tutor computes VOC values online via MGPO, enabling application to large, partially observable environments where pre-computing feedback is infeasible.

## Design Implications

### Context
#### Requirements
- The MGPO algorithm for online VOC computation
- A set of precomputed observation samples for the environment
#### Constraints
- Delay penalty uses a fixed 0.05 VOC threshold rather than exact Q-value differences
- Premature termination triggers a delay penalty rather than actual termination when MGPO would continue planning

### Target Learners
- adult online learners

### Learning Goals
- planning strategies
- metacognitive skill
- resource-rational information search

### Claims
- [Tutor Improves Human Planning Partially Observable](../claims/tutor-improves-human-planning-partially-observable.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Heindrich, L., Consul, S., & Lieder, F. (2025). An Intelligent Tutor for Planning in Large Partially Observable Environments. International Journal of Artificial Intelligence in Education, 35, 3095–3127. https://doi.org/10.1007/s40593-025-00493-7
