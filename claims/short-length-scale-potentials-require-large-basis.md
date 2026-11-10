---
type: claim
title: "Convergence of the truncated diagonalization degrades for potentials with short length scales: narrow wells require increasingly many basis states, with a delta function ground state still about 10% off at N = 100"
description: "Convergence of the truncated diagonalization degrades for potentials with short length scales: narrow wells require increasingly many basis states, with a delta function ground state still about 10% off at N = 100"
id: short-length-scale-potentials-require-large-basis
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
    rigour: 2
  - id: f-marsiglio-2008-2
    resource: "https://arxiv.org/abs/0806.3051"
    title: "F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051"
    author: F. Marsiglio
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Convergence of the truncated diagonalization degrades for potentials with short length scales: narrow wells require increasingly many basis states, with a delta function ground state still about 10% off at N = 100

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1`–`r2` · `q2`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ground state energy convergence is rapid for wide finite wells but slow for narrow wells, because confined wave functions contain very small spatial variations describable only by high-energy basis states. [→ F. Marsiglio 2008](#f-marsiglio-2008)
`q2 i?` For the delta function potential, even a cutoff of N = 100 leaves the ground state energy about 10% from the converged result, and the wave function cusp remains slightly missed even at N = 200. [→ F. Marsiglio 2008 (2)](#f-marsiglio-2008-2)

## Evidence

### F. Marsiglio 2008

F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051 [doi:10.48550/arXiv.0806.3051](https://doi.org/10.48550/arXiv.0806.3051)

`q2 · i?` · `design · r2`

Numerical study of finite square wells of varying width b at fixed bV0 (Fig. 4, V00 = −5E(0)1): results are "insensitive to the cutoﬀ for b ≈a, while for low values of b, there is considerable variation." Even a 3×3 matrix is accurate down to b ≈ 0.5a, but finite N results peel off as width decreases.

> "The results are insensitive to the cutoﬀ for b ≈a, while for low values of b, there is considerable variation."

### F. Marsiglio 2008 (2)

F. Marsiglio. (2008). The harmonic oscillator in quantum mechanics: A third way. arXiv preprint. https://arxiv.org/abs/0806.3051 [doi:10.48550/arXiv.0806.3051](https://doi.org/10.48550/arXiv.0806.3051)

`q2 · i?` · `design · r1`

Delta function potential limit (Fig. 5 and Fig. 4(b)): "the result at b = 0 is oﬀ from the N → ∞ result by about 10%" at N = 100, and even at N = 200 the computed wave function "still misses (though only slightly) the cusp at the centre." The article attributes this to very small spatial variations requiring very high energy basis states.

> "For example, even with a cutoﬀ of N = 100, meaning that unperturbed states with energy as high as 10000 are included, the result at b = 0 is oﬀ from the N → ∞ result by about 10%."

## Discussion


## Related Claims
- [Truncated diagonalization reproduces the harmonic oscillator ground state wave function with excellent agreement, converging by a truncation of N = 20 basis states](ho-ground-state-wavefunction-convergence-n20.md) — related
- [Truncated matrix diagonalization in an infinite square well basis reproduces low-lying harmonic oscillator eigenvalues accurately, with deviations beginning near a computable crossover energy](matrix-diagonalization-square-well-basis-low-lying-eigenvalues.md) — related
- [For a step potential, matrix-mechanics eigenvalues converge to the analytical infinite square well results at both low energies (width a/2) and high energies (width a shifted by v0/2)](step-potential-eigenvalues-low-high-energy-convergence.md) — a narrower finding that bears on this claim
