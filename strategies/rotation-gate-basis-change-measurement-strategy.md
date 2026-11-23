---
type: strategy
id: rotation-gate-basis-change-measurement-strategy
title: Measure arbitrary spin directions on quantum hardware by applying rotation gates that map the desired eigenvectors onto the computational basis
description: "Because the platform permits computational-basis measurement only, the article teaches a general method for measuring any spin direction: apply unitary rotation operators that map the eigenvectors of the desired measu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: jed-brody-2021
    resource: "https://doi.org/10.1119/10.0001967"
    title: "Jed Brody, and Gavin Guzman. (2021). Calculating spin correlations with a quantum computer. American Journal of Physics 89, 35 (2021). https://doi.org/10.1119/10.0001967"
    author: Jed Brody, and Gavin Guzman
---

# Measure arbitrary spin directions on quantum hardware by applying rotation gates that map the desired eigenvectors onto the computational basis

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because the platform permits computational-basis measurement only, the article teaches a general method for measuring any spin direction: apply unitary rotation operators that map the eigenvectors of the desired measurement operator onto j0i and j1i, then read the outcome frequencies. The expectation value is then the fraction of 00 and 11 results minus the fraction of 01 and 10 results. The article notes that "The IBM Quantum Experience allows measurements in the computational basis only," making this rotation technique essential for measuring along arbitrary Bloch-sphere directions.

## Design Implications

### Context
#### Requirements
- Students must determine the rotation operator from geometric considerations, e.g., Ry(−p/2) maps the x-axis eigenvectors onto the z axis, and Rz(−phi) followed by Ry(−p/2) handles the x-y plane
#### Constraints
- Applies within the platform's computational-basis-only measurement restriction

### Target Learners
- undergraduate physics students

### Target Learning Goals
- unitary operations for basis transformations
- measuring observables other than the computational basis

## Related Strategies

- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Use the free cloud-accessible IBM quantum computers to run simple classroom experiments illustrating nonclassical features of quantum mechanics](ibm-quantum-experience-classroom-experiments-strategy.md)

## Examples
-

## Key Sources
- Jed Brody, and Gavin Guzman. (2021). Calculating spin correlations with a quantum computer. American Journal of Physics 89, 35 (2021). https://doi.org/10.1119/10.0001967
