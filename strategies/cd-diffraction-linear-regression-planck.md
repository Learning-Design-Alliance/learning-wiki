---
type: strategy
id: cd-diffraction-linear-regression-planck
title: "Determine LED wavelengths by compact-disk diffraction and extract the Planck constant by linear regression of qeU* versus frequency"
description: "Participants collimate each LED's light with a torch lens, diffract it through the tracks of a peeled compact disk (constant d = 1600 nm), and measure the distance L between the central and first diffraction maxima at..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: mishonov-2021
    resource: "https://arxiv.org/abs/2106.01337"
    title: "Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R. (2021). Determination of Planck constant by LED. arXiv. https://arxiv.org/abs/2106.01337"
    author: "Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R"
---

# Determine LED wavelengths by compact-disk diffraction and extract the Planck constant by linear regression of qeU* versus frequency

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Participants collimate each LED's light with a torch lens, diffract it through the tracks of a peeled compact disk (constant d = 1600 nm), and measure the distance L between the central and first diffraction maxima at screen distance D. The wavelength follows from "λ =d sinθ" with θ = arctan(L/D), giving ν = c/λ. Then, plotting qeU* against ν, the problem says: "Perform linear regression of these points (draw a straight line which passes closest to all points according to you)", and the slope ratio hLED = ΔE/Δν estimates h, with the percent error ε = 100(X−1) against the known value.

## Design Implications

### Context
#### Requirements
- A peeled CD diffraction grating, a collimating lens, a screen, and measured U* values for each LED are required; the mean L = ½(Ll + Lr) is taken from left and right maxima.
#### Constraints
- The paper allows omitting a deviating point from the regression only if this is written down explicitly, and expects at least the correct order of magnitude for h.

### Target Learners
- high school students
- university students

### Target Learning Goals
- diffraction and wavelength measurement
- graphical linear regression as a physical method

## Claims

- [A low-cost student spectrometer built in FP measured an LED wavelength within 5 nm of the accepted value](../claims/fp-low-cost-spectrometer-within-5nm.md) [+W]

## Related Strategies

- [Measure the LED turn-on voltage U* visually through a straw waveguide using at least five repeated readings and the median](median-of-five-visual-threshold-ustar.md)
- [Replace subjective visual threshold readings with a parabolic fit of the low-current I-V curve to locate U* numerically](parabolic-fit-iv-curve-ustar.md)

## Examples
-

## Key Sources
- Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R. (2021). Determination of Planck constant by LED. arXiv. https://arxiv.org/abs/2106.01337
