---
type: design
id: adiabatic-atmosphere-lapse-rate-model
title: Adiabatic expansion model of the atmospheric temperature gradient, with stated scope limits
description: "The article derives, from the adiabatic gas expansion of a rising air column, the lapse-rate formula dT/dh = −(γ−1)/γ · Mg/R, presented as \"an interesting application of the adiabatic gas expansion\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: giovanni-bindi-2017
    resource: "https://arxiv.org/abs/1701.03085"
    title: "Giovanni Bindi. (2017). Improving physics with CanSat. https://arxiv.org/abs/1701.03085"
    author: Giovanni Bindi
---

# Adiabatic expansion model of the atmospheric temperature gradient, with stated scope limits

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article derives, from the adiabatic gas expansion of a rising air column, the lapse-rate formula dT/dh = −(γ−1)/γ · Mg/R, presented as "an interesting application of the adiabatic gas expansion". Taking air as a poor conductor of heat so the expansion is adiabatic, and combining the hydrostatic relation dp = −ρg dh with the gas law, students obtained −9.8 °C/1000 m, larger than the international standard −6.5 °C/1000 m.

## Design Implications

### Context
#### Requirements
- Treating the rising air's expansion as adiabatic, since air is a poor conductor of heat
#### Constraints
- The model overestimates the lapse rate because it neglects the effect of water vapor condensation

### Target Learners
- seventeen-year-old high school physics students

### Learning Goals
- thermodynamics of the atmosphere
- deriving the temperature-altitude dependence

### Claims
- 

## Related Designs

- [One-dimensional polymer segment model linking configurational entropy to rubber's thermomechanics](one-dimensional-polymer-segment-model-rubber-entropy.md)
- [Low-budget Arduino-based sensor kit with datasheet calibration for CanSat atmospheric measurement](cansat-arduino-low-budget-sensor-kit.md)

## Examples
-

## Key Sources
- Giovanni Bindi. (2017). Improving physics with CanSat. https://arxiv.org/abs/1701.03085
