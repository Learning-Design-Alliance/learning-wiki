---
type: design
id: crank-slider-geometric-kinematic-model
title: Geometric crank-slider kinematic model predicting non-sinusoidal cart motion
description: "A closed-form model derived from mechanism geometry: cart position x(t) = R cos(ωt + φ) + √(L² − R² sin²(ωt + φ)), differentiated to give velocity and acceleration."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: josep-ll-suñer-2026
    resource: "https://www.upv.es"
    title: "Josep Ll. Suñer, Rod Milbrandt, Juan C. Castro-Palacio, Alfonso Merchante, Francisco M. Muñoz-Peréz, Juan A. Monsoriu. (2026). Bringing Engineering into the Physics Lab: Exploring Crank-Slider Dynamics with Smartphones. https://www.upv.es"
    author: Josep Ll. Suñer, Rod Milbrandt, Juan C. Castro-Palacio, Alfonso Merchante, Francisco M. Muñoz-Peréz, Juan A. Monsoriu
---

# Geometric crank-slider kinematic model predicting non-sinusoidal cart motion

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A closed-form model derived from mechanism geometry: cart position x(t) = R cos(ωt + φ) + √(L² − R² sin²(ωt + φ)), differentiated to give velocity and acceleration. Because the connecting rod has finite length, the motion is nonlinear and departs from simple harmonic motion; the article states that "this departure from simple harmonic motion becomes more noticeable as the ratio R/L increases." The treatment "requires only trigonometry and differentiation and is therefore accessible to students enrolled in a calculus-based introductory physics course."

## Design Implications

### Context
#### Requirements
- Knowledge of the geometric parameters R (crank radius) and L (rod length)
- constant angular velocity of the motor
- a phase angle φ accounting for the crank's initial position
#### Constraints
- The model assumes the crank rotates at constant angular velocity and neglects effects not included in the geometric derivation

### Target Learners
- calculus-based introductory physics students

### Learning Goals
- mathematical modeling from geometric considerations
- testing theoretical predictions against experimental measurements

### Claims
- Crank Slider Video Model Fit R2 095 [+M]
- [Crank Slider Accelerometer Fit Agreement Video](../claims/crank-slider-accelerometer-fit-agreement-video.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Josep Ll. Suñer, Rod Milbrandt, Juan C. Castro-Palacio, Alfonso Merchante, Francisco M. Muñoz-Peréz, Juan A. Monsoriu. (2026). Bringing Engineering into the Physics Lab: Exploring Crank-Slider Dynamics with Smartphones. https://www.upv.es
