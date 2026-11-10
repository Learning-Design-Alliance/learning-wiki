---
type: claim
title: Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy
description: Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy
id: matrix-diagonalization-square-well-basis-low-lying-eigenvalues
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: weak
newest_evidence: 2008
recheck_by: 2011
sources:
  - id: f-marsiglio-2008
    resource: "https://doi.org/10.48550/arXiv.0806.3051"
    title: "F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051"
    author: F. Marsiglio
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q2`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For a harmonic oscillator potential embedded in an infinite square well, numerically converged eigenvalues (N = 400) agree excellently with analytical harmonic oscillator results for low-lying states, and begin to deviate at the crossover energy where the potential reaches the well walls. [→ F. Marsiglio 2008](#f-marsiglio-2008)

## Evidence

### F. Marsiglio 2008

F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051 [doi:10.48550/arXiv.0806.3051](https://doi.org/10.48550/arXiv.0806.3051)

`q2 · i?` · `design · r1`

Numerical diagonalization of the harmonic oscillator embedded in an infinite square well (Fig. 1, truncation N = 400, ¯hω/E(0)1 = 50) shows that "The low lying states are well described by the harmonic oscillator eigenvalues." The article prints a crossover formula Ecross/E(0)1 = (π2/16)(¯hω/E(0)1)2, giving Ecross/E(0)1 ≈ 1550 for this example, where results begin to deviate.

> "The low lying states are well described by the harmonic oscillator eigenvalues. The harmonic oscillator potential becomes truncated by the inﬁnite square well at an energy given by the value of the potential at x = a"

## Discussion


## Related Claims
- [Numerical exercises empower beginning quantum students to solve real problems without analytic solutions](computational-aspect-empowers-quantum-students.md) — related
- [Simulated double-well superposition shows probability density oscillating between wells at the predicted period](double-well-oscillation-matches-predicted-period.md) — related
- [Truncated diagonalization reproduces the harmonic oscillator ground state wave function with excellent agreement, converging by a truncation of N = 20 basis states](ho-ground-state-wavefunction-convergence-n20.md) — related
- [Convergence of the truncated diagonalization degrades for potentials with short length scales: narrow wells require increasingly many basis states, with a delta function ground state still about 10% off at N = 100](short-length-scale-potentials-require-large-basis.md) — related
- [Numerically computed harmonic-oscillator energies match the analytic formula within rounding error](numerical-harmonic-oscillator-energies-match-analytic.md) — related
- [For a step potential, matrix-mechanics eigenvalues converge to the analytical infinite square well results at both low energies (width a/2) and high energies (width a shifted by v0/2)](step-potential-eigenvalues-low-high-energy-convergence.md) — a narrower finding that bears on this claim
