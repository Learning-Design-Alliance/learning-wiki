---
type: strategy
id: parabolic-fit-iv-curve-ustar
title: "Replace subjective visual threshold readings with a parabolic fit of the low-current I-V curve to locate U* numerically"
description: "For university participants, the paper asks students to invent a numerical determination of U* from measured current-voltage characteristics at small currents (I in the range 0.1–10 µA), removing the subjectivity of t..."
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

# Replace subjective visual threshold readings with a parabolic fit of the low-current I-V curve to locate U* numerically

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For university participants, the paper asks students to invent a numerical determination of U* from measured current-voltage characteristics at small currents (I in the range 0.1–10 µA), removing the subjectivity of the human eye. It suggests: "use quadratic polynomial (parabolic) fit I =aU 2 +bU +c ... for currents in the interval I∈ (1, 10)µA and calculate the position of the minimum ˜U =−b/2a." Students then compare Ũ with the visual U* for all LEDs and present the discrepancies between the two measurement types in percent.

## Design Implications

### Context
#### Requirements
- Two multimeters (ammeter and voltmeter), a potentiometer-based adjustable voltage source, and recorded I-V data below and above 1 µA for each LED are needed.
#### Constraints
- The ammeter's internal resistance RA must be accounted for, since the LED voltage is U = UV − RA·I; a follow-up task asks students to re-derive and program the least-squares normal equations for the parabolic fit.

### Target Learners
- university students
- advanced high school students

### Target Learning Goals
- numerical data fitting
- instrumentation error correction
- objective determination of LED threshold voltage

## Related Strategies

- [Determine LED wavelengths by compact-disk diffraction and extract the Planck constant by linear regression of qeU* versus frequency](cd-diffraction-linear-regression-planck.md)
- [Measure the LED turn-on voltage U* visually through a straw waveguide using at least five repeated readings and the median](median-of-five-visual-threshold-ustar.md)

## Examples
-

## Key Sources
- Mishonov, T. M., Petkov, A. P., Andreoni, M., Petkov, E. G., Varonov, A. M., Dimitrova, I. M., Velkoska, L., & Popeski-Dimovski, R. (2021). Determination of Planck constant by LED. arXiv. https://arxiv.org/abs/2106.01337
