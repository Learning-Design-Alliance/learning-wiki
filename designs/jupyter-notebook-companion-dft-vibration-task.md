---
type: design
id: jupyter-notebook-companion-dft-vibration-task
title: Interactive Jupyter notebook companion guiding students through DFT-based vibration analysis with smartphone accelerometer data
description: "The article describes a Jupyter notebook that \"acts as a personal guide to the students throughout the experimental task\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: p-pirinen-2023
    resource: "https://arxiv.org/abs/2306.08436"
    title: "P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. https://arxiv.org/abs/2306.08436"
    author: P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac
---

# Interactive Jupyter notebook companion guiding students through DFT-based vibration analysis with smartphone accelerometer data

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a Jupyter notebook that "acts as a personal guide to the students throughout the experimental task". It introduces sampling rate and signal length via a sine wave, applies a DFT to a sine, adds noise, and asks students to add frequency components. It discusses aliasing, demonstrates data handling for datasets with thousands of points, and has students build their own analysis code by copying and modifying notebook examples.

## Design Implications

### Context
#### Requirements
- Students need some prior experience in uncertainty analysis, data representation, and data analysis, and had encountered Python programming before
#### Constraints
- Other aspects of digital signal processing, such as windowing or noise reduction, are not necessary for the investigations of this experimental task

### Target Learners
- beyond-first-year university physics students

### Learning Goals
- basic digital signal processing
- applying the discrete Fourier transform to authentic data
- Python programming for data analysis

### Claims
- 

## Related Designs

- [Three co-existing recitation task types: smartphone experimental, programming, and standard recitation tasks](three-task-types-recitation-mechanics.md)

## Examples
-

## Key Sources
- P. Pirinen, P. Klein, S. Z. Lahme, A. Lehtinen, L. Rončević, and A. Susac. (2023). Learning digital signal processing using an interactive Jupyter notebook and smartphone accelerometer data. https://arxiv.org/abs/2306.08436
