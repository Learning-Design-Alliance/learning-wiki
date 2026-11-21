---
type: design
id: ofi-3x3-coupler-arctangent-demodulation-system
title: Optic fiber interferometry (OFI) measurement system with 3×3 coupler and arctangent phase demodulation for directional sub-micrometer displacement tracking
description: "The OFI system integrates a narrow-linewidth 1550 nm fiber laser, a 1×2 fiber coupler splitting reference and probe beams, a probe-arm collimator mounted on the vibrating object, and a 3×3 fiber coupler producing \"thr..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: wang-m-2024
    resource: "https://doi.org/XXXX/XXXX"
    title: "Wang M, Zhou M, Ji H, Lan T. (2024). Utilizing Optic Fiber Interferometry in Forced Vibration Experimentation for Educational Purposes. https://doi.org/XXXX/XXXX"
    author: Wang M, Zhou M, Ji H, Lan T
---

# Optic fiber interferometry (OFI) measurement system with 3×3 coupler and arctangent phase demodulation for directional sub-micrometer displacement tracking

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The OFI system integrates a narrow-linewidth 1550 nm fiber laser, a 1×2 fiber coupler splitting reference and probe beams, a probe-arm collimator mounted on the vibrating object, and a 3×3 fiber coupler producing "three output signals with a fixed 120°  phase difference, facilitating high-precision phase demodulation for directional displacement detection". Three photodetector outputs feed an arctangent algorithm (Equation 9) that computes phase and hence displacement x = φfλ/2π, resolving both magnitude and direction. The article uses it in a forced-vibration teaching experiment for undergraduates and optics-focused graduate students.

## Design Implications

### Context
#### Requirements
- Basic training in interferometric diagnostics, including optical alignment, data acquisition, and signal analysis, before conducting the experiment
- Precise alignment of the collimated beam via a kinematic mount
#### Constraints
- Equation (9) is valid only for single-frequency vibration signals; with multiple vibration components of comparable amplitude, phase calculation errors may increase

### Target Learners
- undergraduate physics majors with foundational mechanics and optics training
- optics-focused graduate students

### Learning Goals
- forced vibration theory and resonance
- interferometric measurement principles and phase-displacement relationships

### Claims
- Ofi Natural Frequency 855Hz Matches Theory [+M]
- Ofi Power Spectrum Peak Matches Driving Frequency [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Wang M, Zhou M, Ji H, Lan T. (2024). Utilizing Optic Fiber Interferometry in Forced Vibration Experimentation for Educational Purposes. https://doi.org/XXXX/XXXX
