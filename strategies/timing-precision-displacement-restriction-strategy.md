---
type: strategy
id: timing-precision-displacement-restriction-strategy
title: "Restrict initial pendulum displacement according to timing precision: 10° for photodiode, 15° for accelerometer, no restriction below 45° for stopwatch"
description: The article derives data-driven restrictions on maximum initial angular displacement when using the small angle approximation, matched to the timing instrument.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: matthew-heffernan-2022
    resource: "https://arxiv.org/abs/2104.08621"
    title: "Matthew Heffernan. (2022). How about that Bayes: Bayesian techniques and the simple pendulum. https://arxiv.org/abs/2104.08621"
    author: Matthew Heffernan
---

# Restrict initial pendulum displacement according to timing precision: 10° for photodiode, 15° for accelerometer, no restriction below 45° for stopwatch

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article derives data-driven restrictions on maximum initial angular displacement when using the small angle approximation, matched to the timing instrument. It recommends that "displacements with more precise timing±O(0.001) s should be restricted to 10◦" while "displacements with less precise timing commensurate with stopwatches and human reaction times should not be restricted below 45 ◦", with accelerometer timing (±O(0.01) s) at 15°. Table IV summarizes: photodiode (±~0.005 s) 10°, accelerometer (±~0.02 s) 15°, stopwatch (±√2(0.250) s) 45°.

## Design Implications

### Context
#### Requirements
- Knowledge of the timing instrument's precision to select the appropriate displacement restriction
#### Constraints
- The stopwatch guidance means stopwatch timing is insufficiently precise to detect the approximation's breakdown below 45°, not that larger displacements are more accurate
- Restrictions are derived under idealized, maximally-restrictive assumptions about measurement counts

### Target Learners
- students in introductory physics teaching laboratories

### Target Learning Goals
- choosing appropriate experimental conditions when investigating pendulum period dependence on initial angular displacement

## Related Strategies

- [Three-stage hybrid laboratory activity combining analytical pendulum analysis with ANN modeling](three-stage-hybrid-ann-pendulum-lab-activity.md)

## Examples
-

## Key Sources
- Matthew Heffernan. (2022). How about that Bayes: Bayesian techniques and the simple pendulum. https://arxiv.org/abs/2104.08621
