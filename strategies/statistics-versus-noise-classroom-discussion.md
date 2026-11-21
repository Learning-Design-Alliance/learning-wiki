---
type: strategy
id: statistics-versus-noise-classroom-discussion
title: Classroom discussion of statistical error versus hardware noise when simulating on quantum devices
description: "The article devotes a section to the two primary sources of error in quantum computing experiments: statistical fluctuations from the finite number of measurement shots, and intrinsic hardware noise."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: isabella-masina-2025
    resource: "https://arxiv.org/abs/2501.01434"
    title: "Isabella Masina, Giuseppe Lo Presti, Matteo Robbiati, and Michele Grossi. (2025). Simulating Bell inequalities with Qibo. https://arxiv.org/abs/2501.01434"
    author: Isabella Masina, Giuseppe Lo Presti, Matteo Robbiati, and Michele Grossi
---

# Classroom discussion of statistical error versus hardware noise when simulating on quantum devices

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article devotes a section to the two primary sources of error in quantum computing experiments: statistical fluctuations from the finite number of measurement shots, and intrinsic hardware noise. The statistical error decreases as σstat ≈ 1/√Nshots, while the noise error is independent of Nshots; the total error is estimated by adding the two in quadrature, and equation (24) tells how many shots are needed to make the statistical error comparable to the noise error. The authors state the impact of noise and statistics "should always be emphasized in a classroom discussion, to keep a practical approach".

## Design Implications

### Context
#### Requirements
- Estimating the statistical error through standard error analysis, where the uncertainty in the measurement is inversely proportional to the square root of the number of shots
#### Constraints
- In a first approximation the noise error cannot be controlled, so the statistical error must be made comparable to the noise error

### Target Learners
- Master students in Physics
- graduate students in quantum computing courses

### Target Learning Goals
- understanding statistical aspects and noise coming from current quantum chips
- practical error analysis in quantum simulations

## Claims

- [The article argues classical simulators are better suited than real quantum hardware for teaching, citing error rates, incomplete measurement output, and limited hardware access.](../claims/classical-simulators-preferred-for-teaching-quantum-computing.md) [+W]

## Related Strategies

- [Noise exploration assignments using a noise simulator to teach quantum noise concepts](noise-exploration-assignments-strategy.md)
- [Use real-hardware experiment results that deviate from theory to motivate a discussion of quantum error correction](real-hardware-error-observation-strategy.md)

## Examples
-

## Key Sources
- Isabella Masina, Giuseppe Lo Presti, Matteo Robbiati, and Michele Grossi. (2025). Simulating Bell inequalities with Qibo. https://arxiv.org/abs/2501.01434
