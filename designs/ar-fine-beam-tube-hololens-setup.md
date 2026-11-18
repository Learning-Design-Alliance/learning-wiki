---
type: design
id: ar-fine-beam-tube-hololens-setup
title: AR-augmented fine beam tube experiment with HoloLens-based hybrid measurement
description: A digitally enhanced lab experiment for determining the electron charge-to-mass ratio in which students use Microsoft HoloLens smartglasses to record measurement data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: o-bodensiek-2019
    resource: "https://pubs.aip.org/aip/ptt"
    title: "O. Bodensiek, D. Sonntag, N. Wendorff, G. Albuquerque, and M. Magnor. (2019). Augmenting the fine beam tube: From hybrid measurements to magnetic field visualization. The Physics Teacher 57. https://pubs.aip.org/aip/ptt"
    author: O. Bodensiek, D. Sonntag, N. Wendorff, G. Albuquerque, and M. Magnor
---

# AR-augmented fine beam tube experiment with HoloLens-based hybrid measurement

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A digitally enhanced lab experiment for determining the electron charge-to-mass ratio in which students use Microsoft HoloLens smartglasses to record measurement data. Acceleration voltage and coil current are gathered by a USB-connected single board computer and shown as real-time numerical values on the smartglasses, and a gesture-controlled virtual ruler is moved into the beam plane to measure the circular path diameter. Values are saved to a CSV file via a record button for later analysis.

## Design Implications

### Context
#### Requirements
- A single board computer connected via USB to multimeters and power supplies establishes a wireless data link to the HoloLens.
- Light conditions must be adjusted so the weakly glowing electron beam is visible through the darkening HoloLens while the power supplies remain operable.
#### Constraints
- The article names the need to adjust light conditions as the only drawback experienced in using the AR environment for this experiment.

### Target Learners
- undergraduate physics laboratory course students

### Learning Goals
- determining the electron charge-to-mass ratio
- understanding charged particles in magnetic fields

### Claims
- Ar Fine Beam Tube Measurement Accuracy [+M]
- [Ar Measurement Series Quick Single Student](../claims/ar-measurement-series-quick-single-student.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- O. Bodensiek, D. Sonntag, N. Wendorff, G. Albuquerque, and M. Magnor. (2019). Augmenting the fine beam tube: From hybrid measurements to magnetic field visualization. The Physics Teacher 57. https://pubs.aip.org/aip/ptt
