---
type: strategy
id: square-well-basis-matrix-diagonalization-instruction-strategy
title: Teach quantum bound states by embedding arbitrary potentials in an infinite square well basis and solving truncated matrix diagonalization problems
description: "This is a concrete instructional recipe: students set up the Hamiltonian matrix Eq."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
sources:
  - id: f-marsiglio-2008
    resource: "https://arxiv.org/abs/0806.3051"
    title: "F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051"
    author: F. Marsiglio
---

# Teach quantum bound states by embedding arbitrary potentials in an infinite square well basis and solving truncated matrix diagonalization problems

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (6 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
This is a concrete instructional recipe: students set up the Hamiltonian matrix Eq. (9) using the familiar infinite square well eigenfunctions as a basis, truncate at N states, and feed the matrix to an eigenvalue solver in standard software. The article frames it as equipping students so that "This paper should equip students to obtain the low lying bound states of any one-dimensional short range potential." Analytical evaluation of integrals is not even required, and the potential need not be defined analytically.

## Design Implications

### Context
#### Requirements
- A basis set of infinite square well eigenfunctions within which any single-particle potential can be embedded
- A truncation cutoff N and access to an eigenvalue/eigenvector solver or software packages
#### Constraints
- Low-lying states are obtained accurately, but convergence is slow for potentials with short length scales, requiring large numbers of basis states

### Target Learners
- undergraduate students learning quantum mechanics for the first time

### Target Learning Goals
- obtain low-lying bound states and wave functions of arbitrary one-dimensional short-range potentials using matrix mechanics

## Claims

- [Truncated diagonalization reproduces the harmonic oscillator ground state wave function with excellent agreement, converging by a truncation of N = 20 basis states](../claims/ho-ground-state-wavefunction-convergence-n20.md) [+W]
- [Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy](../claims/matrix-diagonalization-square-well-basis-low-lying-eigenvalues.md) [+W]
- [Convergence of the truncated diagonalization degrades for potentials with short length scales: narrow wells require increasingly many basis states, with a delta function ground state still about 10% off at N = 100](../claims/short-length-scale-potentials-require-large-basis.md) [~W]
- [For a step potential, matrix-mechanics eigenvalues converge to the analytical infinite square well results at both low energies (width a/2) and high energies (width a shifted by v0/2)](../claims/step-potential-eigenvalues-low-high-energy-convergence.md) [+W]
- [Numerically computed harmonic-oscillator energies match the analytic formula within rounding error](../claims/numerical-harmonic-oscillator-energies-match-analytic.md) [+W]
- [Simulated double-well superposition shows probability density oscillating between wells at the predicted period](../claims/double-well-oscillation-matches-predicted-period.md) [+W]
- [Numerical exercises empower beginning quantum students to solve real problems without analytic solutions](../claims/computational-aspect-empowers-quantum-students.md) [+W]

## Related Strategies

- [Incorporate numerical calculation into introductory quantum courses to counteract abstraction-driven misconceptions](incorporate-numerical-calculation-in-quantum-courses.md)

## Examples
-

## Key Sources
- F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051
