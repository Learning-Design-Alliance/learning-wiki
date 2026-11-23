---
type: design
id: led-threshold-photon-energy-relation
title: "Photon-energy account of LED threshold voltage: hν = qeU* + A with an approximately constant band-gap offset A"
description: "The EPO8 method rests on relating the smallest voltage U* at which an LED emits visible light to the photon energy of its emitted light."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: mishonov-2021
    resource: "https://arxiv.org/abs/2106.01337"
    title: "Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R. (2021). Determination of Planck constant by LED. arXiv. https://arxiv.org/abs/2106.01337"
    author: "Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R"
---

# Photon-energy account of LED threshold voltage: hν = qeU* + A with an approximately constant band-gap offset A

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The EPO8 method rests on relating the smallest voltage U* at which an LED emits visible light to the photon energy of its emitted light. The problem states: "Those energies are related to photon energies by the equation hν =qeU∗ +A." Plotting qeU* against the diffraction-measured frequency ν for LEDs of different colors and performing a linear regression yields the Planck constant as the slope. The framework assumes: "the parameter A is weakly dependent of the chemical compound of the LED semiconductor therefore is almost constant."

## Design Implications

### Context
#### Requirements
- Wavelengths of all LEDs must be measured independently by diffraction so frequencies ν = c/λ are known before the linear regression.
#### Constraints
- The estimation relies on the approximation that A is nearly constant across different LED semiconductor compounds; the paper asks university students to evaluate whether inaccuracies in ΔU* and Δθ or this constant-A approximation give the larger uncertainty.

### Target Learners
- high school students
- university students

### Learning Goals
- determining the Planck constant
- understanding photon energy and semiconductor light emission

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R. (2021). Determination of Planck constant by LED. arXiv. https://arxiv.org/abs/2106.01337
