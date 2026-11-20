---
type: design
id: undergraduate-homodyne-detection-setup
title: Pre-aligned optical homodyne detection setup for undergraduate quadrature measurement
description: "A laboratory optical setup implementing homodyne detection for measuring quadratures of light: a stable 633nm He-Ne laser with power close to 0.5 mW split by a beam splitter, beams recombined at a second beam splitter..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: juan-rafael-álvarez-2023
    resource: "https://arxiv.org/abs/2310.17525"
    title: "Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia. (2023). Measuring Wigner functions of quantum states of light in the undergraduate laboratory. arXiv. https://arxiv.org/abs/2310.17525"
    author: Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia
---

# Pre-aligned optical homodyne detection setup for undergraduate quadrature measurement

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A laboratory optical setup implementing homodyne detection for measuring quadratures of light: a stable 633nm He-Ne laser with power close to 0.5 mW split by a beam splitter, beams recombined at a second beam splitter with half-wave plates for polarization matching, two 30mm focal-length lenses focusing onto silicon photodiodes (Thorlabs FDS100), and a dove prism on a piezo-electric platform to scan the local oscillator phase. The article notes "the created experimental setup remains in the laboratory and is the one used by students in the quantum optics class." Data are recorded with an oscilloscope taking ten thousand points over 2 seconds per PZT position.

## Design Implications

### Context
#### Requirements
- A pre-aligned optical setup so students can control the piezoelectric and perform quadrature measurements within two-hour shifts
#### Constraints
- The He-Ne laser implementation limits which states can be measured; more exotic states are emulated via simulation rather than experimentally

### Target Learners
- undergraduate and early graduate physics students

### Learning Goals
- measuring optical quadratures via homodyne detection and reconstructing Wigner functions experimentally

### Claims
- [Students Reconstruct Wigner Vacuum Coherent States](../claims/students-reconstruct-wigner-vacuum-coherent-states.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia. (2023). Measuring Wigner functions of quantum states of light in the undergraduate laboratory. arXiv. https://arxiv.org/abs/2310.17525
