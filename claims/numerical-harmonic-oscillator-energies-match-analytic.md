---
type: claim
title: Numerically computed harmonic-oscillator energies match the analytic formula within rounding error
description: Numerically computed harmonic-oscillator energies match the analytic formula within rounding error
id: numerical-harmonic-oscillator-energies-match-analytic
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: moderate
newest_evidence: 2007
recheck_by: 2010
sources:
  - id: r-garcia-2007
    resource: "https://doi.org/10.48550/arXiv.0704.1622"
    title: "R. Garcia, A. Zozulya, and J. Stickney. (2007). MATLAB codes for teaching quantum physics: Part 1. https://arxiv.org/abs/0704.1622"
    author: R. Garcia, A. Zozulya, and J. Stickney
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Numerically computed harmonic-oscillator energies match the analytic formula within rounding error

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the potential U = ½·100·x², the three lowest energies computed numerically (4.99969, 14.9984, 24.9959) agree, within rounding error, with the analytic formula E = ℏω(n + ½) with ω = 10 rad/s. [→ R. Garcia 2007](#r-garcia-2007)

## Evidence

### R. Garcia 2007

R. Garcia, A. Zozulya, and J. Stickney. (2007). MATLAB codes for teaching quantum physics: Part 1. https://arxiv.org/abs/0704.1622 [doi:10.48550/arXiv.0704.1622](https://doi.org/10.48550/arXiv.0704.1622)

`q2 · i?` · `design · r2`

Numerical result shown in Fig. 1 from Program 4, which solves the time-independent Schrödinger equation for the harmonic oscillator potential using sparse matrices. The quoted energies match the analytic oscillator spectrum, serving as a validation example students can check.

> "The corresponding energies displayed within the ﬁgure legend, 4.99969, 14.9984 and 24.9959, are, within rounding error, precisely those expected from Eq. (7) for the three lowest-energy modes"

## Discussion


## Related Claims
- [Simulated double-well superposition shows probability density oscillating between wells at the predicted period](double-well-oscillation-matches-predicted-period.md) — related
- [Truncated diagonalization reproduces the harmonic oscillator ground state wave function with excellent agreement, converging by a truncation of N = 20 basis states](ho-ground-state-wavefunction-convergence-n20.md) — related
- [Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy](matrix-diagonalization-square-well-basis-low-lying-eigenvalues.md) — related
