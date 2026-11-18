---
type: strategy
id: pilot-experiment-estimate-sigma-planning
title: Estimate the standard deviation in a pilot experiment before planning how many measurements to take
description: "The article recommends determining the number of measurements needed to reach a desired uncertainty of the mean only after the standard deviation has been estimated early in the measurement process, \"in a pilot experi..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: gabriel-l-a-de-sousa-george-c-cardoso-2018
    resource: "https://arxiv.org/abs/1611.03425v6"
    title: "Gabriel L. A. de Sousa & George C. Cardoso. (2018). A battery-resistor analogy for further insights on measurement uncertainties. https://arxiv.org/abs/1611.03425v6"
    author: "Gabriel L. A. de Sousa & George C. Cardoso"
---

# Estimate the standard deviation in a pilot experiment before planning how many measurements to take

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends determining the number of measurements needed to reach a desired uncertainty of the mean only after the standard deviation has been estimated early in the measurement process, "in a pilot experiment". Because the uncertainty of the mean decreases only with the square root of the number of readings, planning ahead avoids wasteful data collection. The article adds that when the noise stems from the measurement system or method, investing in better experimental conditions to lower the standard deviation reduces the uncertainty of the mean faster than accumulating readings.

## Design Implications

### Context
#### Requirements
- An early estimate of the standard deviation σ, obtained before the main data collection, so the required number of readings can be calculated.
#### Constraints
- The planning relation assumes homoscedasticity: the repeated measurements of the same quantity should come from the same probability distribution, with variances that do not change from measurement to measurement.

### Target Learners
- introductory laboratory students

### Target Learning Goals
- planning repeated measurements to reach a target uncertainty of the mean
- deciding between collecting more data and improving the apparatus

### Affordances
- [Battery Resistor Loudspeaker Analogy](../designs/battery-resistor-loudspeaker-analogy.md)

## Claims

- [Students in introductory physics labs are almost never engaged in experiment design, so they hold only a theoretical view of setup limitations and how they affect measurement uncertainty](../claims/introductory-lab-students-not-engaged-in-design.md) [-W]

## Related Strategies

- [Run a pilot study before the full experiment and be willing to restart with an improved design](pilot-study-before-full-student-experiment.md)
- [Use a revised laboratory worksheet that guides students to decide measurement duration and number, discuss uncertainty sources, and preestimate uncertainty ranges before taking data](revised-worksheet-student-designed-measurement-plan.md)

## Examples
-

## Key Sources
- Gabriel L. A. de Sousa & George C. Cardoso. (2018). A battery-resistor analogy for further insights on measurement uncertainties. https://arxiv.org/abs/1611.03425v6
