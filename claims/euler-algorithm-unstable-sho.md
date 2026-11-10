---
type: claim
title: The Euler algorithm is unstable and does not conserve energy when applied to the simple harmonic oscillator
description: The Euler algorithm is unstable and does not conserve energy when applied to the simple harmonic oscillator
id: euler-algorithm-unstable-sho
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: weak
newest_evidence: 2007
recheck_by: 2010
sources:
  - id: todd-timberlake-and-javier-e-hasbun-2007
    resource: "https://doi.org/10.48550/arXiv.0708.2498"
    title: "Todd Timberlake and Javier E. Hasbun. (2007). Computation in Classical Mechanics. https://arxiv.org/abs/0708.2498"
    author: Todd Timberlake and Javier E. Hasbun
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# The Euler algorithm is unstable and does not conserve energy when applied to the simple harmonic oscillator

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` When applied to the simple harmonic oscillator, the Euler algorithm produces a trajectory that spirals outward away from the exact solution, so total mechanical energy steadily increases. [→ Todd Timberlake and Javier E. Hasbun 2007](#todd-timberlake-and-javier-e-hasbun-2007)

## Evidence

### Todd Timberlake and Javier E. Hasbun 2007

Todd Timberlake and Javier E. Hasbun. (2007). Computation in Classical Mechanics. https://arxiv.org/abs/0708.2498 [doi:10.48550/arXiv.0708.2498](https://doi.org/10.48550/arXiv.0708.2498)

`q1 · i?` · `design · r1`

Numerical demonstration (Fig. 1a) applying the Euler algorithm to the simple harmonic oscillator with m = 1 kg, k = 1 N/m, x(0) = 1 m, v(0) = 0, and ∆t = 0.2 s; the trajectory "spirals continually outward away from the exact solution" in phase space. No effect size is reported.

> "It is clear from this result that the Euler algorithm is unstable since the trajectory produced by the algorithm spirals continually outward away from the exact solution."

## Discussion


## Related Claims
- [The Euler-Cromer algorithm is stable and conserves energy, on average, for oscillatory motion](euler-cromer-stable-conserves-energy.md) — related
