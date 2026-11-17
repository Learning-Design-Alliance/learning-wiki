---
type: claim
title: The pyro compressible-hydrodynamics verification tests reproduce analytic reference solutions (Sod shock tube, Sedov-Taylor blast wave, single-mode Rayleigh-Taylor)
description: The pyro compressible-hydrodynamics verification tests reproduce analytic reference solutions (Sod shock tube, Sedov-Taylor blast wave, single-mode Rayleigh-Taylor)
id: pyro-compressible-tests-match-analytic-solutions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2014
sources:
  - id: zingale-2014
    resource: "https://doi.org/10.1016/j.ascom.2014.07.003"
    title: "Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)"
    author: Zingale, M.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zingale-2014-2
    resource: "https://doi.org/10.1016/j.ascom.2014.07.003"
    title: "Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)"
    author: Zingale, M.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The pyro compressible-hydrodynamics verification tests reproduce analytic reference solutions (Sod shock tube, Sedov-Taylor blast wave, single-mode Rayleigh-Taylor)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The Sedov-Taylor blast wave angle-averaged profiles agree very well with the exact solution, though some grid effects aligned with the coordinate axes are visible. [→ Zingale 2014](#zingale-2014)
`q2 i?` A single-mode Rayleigh-Taylor calculation on a 128x384 grid is very symmetric and in good agreement with prior published results. [→ Zingale 2014 (2)](#zingale-2014-2)

## Evidence

### Zingale 2014

Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)

`q2 · i?` · `design · r2`

Numerical Sedov-Taylor blast wave simulation on a 128² grid with E = 1.0, r_init = 0.01 and γ = 1.4. Angle-averaged profiles show "very good agreement with the exact solution", with some axis-aligned grid effects.

> "We run on a 128 2 grid with a CFL number of 0.8. Figure 5 shows the various fluid quantities. We see a nice circular blast wave, but some grid effects are seen aligned with the coordinate axes. The angle-averaged data (profiles as a function of radius) are shown in Figure 6. We see very good agreement with the exact solution."

### Zingale 2014 (2)

Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)

`q2 · i?` · `design · r2`

Numerical single-mode Rayleigh-Taylor instability calculation with a 2:1 density ratio on a 128 × 384 zone grid with CFL 0.8. The article reports the result is "very symmetric" and "in good agreement" with Almgren et al. (2010).

> "Figure 7 shows the results for a 128 × 384 zone grid with a CFL of 0.8. We see that this single mode RT is very symmetric, and in good agreement with the results shown in Almgren et al. (2010)."

## Discussion


## Related Claims
-
