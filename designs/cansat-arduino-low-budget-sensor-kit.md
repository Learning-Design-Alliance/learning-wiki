---
type: design
id: cansat-arduino-low-budget-sensor-kit
title: Low-budget Arduino-based sensor kit with datasheet calibration for CanSat atmospheric measurement
description: "The students built the measurement payload around three sensors on Arduino analog inputs: an MPX4115 pressure sensor, an NTC thermistor for temperature, and a Honeywell HIH-4021-003 humidity sensor for the secondary m..."
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

# Low-budget Arduino-based sensor kit with datasheet calibration for CanSat atmospheric measurement

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The students built the measurement payload around three sensors on Arduino analog inputs: an MPX4115 pressure sensor, an NTC thermistor for temperature, and a Honeywell HIH-4021-003 humidity sensor for the secondary mission. Data were logged in real time as a text file via the Cool Term serial terminal. Students produced "a calibration plot for each of the three sensors" and, using Logger Pro curve fitting, derived conversion formulas including a degree-four polynomial for the nonlinear NTC temperature sensor.

## Design Implications

### Context
#### Requirements
- Calibration using datasheet conversion tables and reference values is a preliminary step to obtain more precise measures
- the humidity sensor must be shielded from bright light because it is light sensitive
#### Constraints
- The NTC sensor has not a linear response, requiring a polynomial calibration

### Target Learners
- seventeen-year-old high school students

### Learning Goals
- sensor calibration and curve fitting
- electronics and data acquisition

### Claims
- 

## Related Designs

- [Adiabatic expansion model of the atmospheric temperature gradient, with stated scope limits](adiabatic-atmosphere-lapse-rate-model.md)
- [Low-cost Arduino sensor kit for open physics projects](arduino-low-cost-sensor-kit-open-projects.md)
- [Arduino microcontroller lab kit with sensors as a personal student-owned data-acquisition platform](arduino-lab-kit-introductory-physics.md)
- [Arduino open-project student-lab teaching unit](arduino-open-project-student-lab-unit.md)

## Examples
-

## Key Sources
- Giovanni Bindi. (2017). Improving physics with CanSat. https://arxiv.org/abs/1701.03085
