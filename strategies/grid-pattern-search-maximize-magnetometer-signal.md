---
type: strategy
id: grid-pattern-search-maximize-magnetometer-signal
title: Grid-pattern iterative search over position and two rotation axes to locate the absolute maximum magnetometer signal
description: "This procedure teaches students an empirical optimization routine: with data recording running, they slide the earbud on the phone screen alternating between x- and y-direction searches to \"walk\" to a local two-dimens..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: glen-d-gillen-and-katharina-gillen-2021
    resource: "https://www.ngdc.noaa.gov/geomag/magfield.shtml"
    title: "Glen D. Gillen and Katharina Gillen. (2021). Magnetic Field Experiments Using a Phone. Physics Department, California Polytechnic State University, San Luis Obispo. https://www.ngdc.noaa.gov/geomag/magfield.shtml"
    author: Glen D. Gillen and Katharina Gillen
---

# Grid-pattern iterative search over position and two rotation axes to locate the absolute maximum magnetometer signal

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
This procedure teaches students an empirical optimization routine: with data recording running, they slide the earbud on the phone screen alternating between x- and y-direction searches to "walk" to a local two-dimensional maximum, then fine-tune the earbud's tilt about axes parallel to x and then y to reach the absolute maximum reading. The manual describes this as "walking" your way to a local two-dimensional maximum using a grid-pattern-style of searching. The found location and angle are reused as the starting point for maximizing the signal at every subsequent spacer distance.

## Design Implications

### Context
#### Requirements
- The Phyphox magnetometer running in Absolute mode while data collection continues
- Repeated re-optimization of position and angle at each new distance before recording the maximum field value
#### Constraints
- On phones that auto-deactivate the magnetometer at high fields, the search must be done with a spacer in place or by moving the phone under stationary earbud and pages

### Target Learners
- introductory undergraduate physics students

### Target Learning Goals
- systematic multivariable experimental optimization
- locating magnetic field sensor position within a phone

## Related Strategies

- [Estimate a skill's minimum BKT-BF RSS a priori from dim, n, and percent_correct before running the full grid search](estimate-minimum-rss-from-skill-variables.md)
- [Use counted sheets of paper as precision spacers to vary earbud-to-sensor distance below ruler resolution](paper-sheet-spacers-submillimeter-distance-precision.md)

## Examples
-

## Key Sources
- Glen D. Gillen and Katharina Gillen. (2021). Magnetic Field Experiments Using a Phone. Physics Department, California Polytechnic State University, San Luis Obispo. https://www.ngdc.noaa.gov/geomag/magfield.shtml
