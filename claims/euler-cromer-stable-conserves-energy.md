---
type: claim
title: The Euler-Cromer algorithm is stable and conserves energy, on average, for oscillatory motion
description: The Euler-Cromer algorithm is stable and conserves energy, on average, for oscillatory motion
id: euler-cromer-stable-conserves-energy
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

# The Euler-Cromer algorithm is stable and conserves energy, on average, for oscillatory motion

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Updating velocity first and then position (Euler-Cromer) yields a solution that stays close to the exact simple harmonic oscillator solution and conserves energy on average. [→ Todd Timberlake and Javier E. Hasbun 2007](#todd-timberlake-and-javier-e-hasbun-2007)

## Evidence

### Todd Timberlake and Javier E. Hasbun 2007

Todd Timberlake and Javier E. Hasbun. (2007). Computation in Classical Mechanics. https://arxiv.org/abs/0708.2498 [doi:10.48550/arXiv.0708.2498](https://doi.org/10.48550/arXiv.0708.2498)

`q1 · i?` · `design · r1`

Numerical demonstration (Fig. 1b) applying the Euler-Cromer algorithm to the same simple harmonic oscillator; the article states the algorithm "is stable and conserves en- ergy, on average, for oscillatory motion" and the solution remains close to the exact solution, coinciding at every quarter period. No effect size is reported.

> "This algorithm is stable and conserves en- ergy, on average, for oscillatory motion.11 We can quickly illustrate this by applying this new algorithm to our sim- ple harmonic oscillator."

## Discussion


## Related Claims
- [The Euler algorithm is unstable and does not conserve energy when applied to the simple harmonic oscillator](euler-algorithm-unstable-sho.md) — related
