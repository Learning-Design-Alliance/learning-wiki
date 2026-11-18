---
type: claim
title: Finite time steps produce a measurable numerical offset and turn-to-turn oscillations in the extracted perihelion motion, which students use to estimate simulation error
description: Finite time steps produce a measurable numerical offset and turn-to-turn oscillations in the extracted perihelion motion, which students use to estimate simulation error
id: timestep-numerical-error-offset-oscillations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: c-körber-2018
    resource: "https://doi.org/10.1088/1361-6552/aac487"
    title: "C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. [doi:10.1088/1361-6552/aac487](https://doi.org/10.1088/1361-6552/aac487)"
    author: C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: c-körber-2018-2
    resource: "https://doi.org/10.1088/1361-6552/aac487"
    title: "C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. [doi:10.1088/1361-6552/aac487](https://doi.org/10.1088/1361-6552/aac487)"
    author: C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Finite time steps produce a measurable numerical offset and turn-to-turn oscillations in the extracted perihelion motion, which students use to estimate simulation error

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For sufficiently small time steps delta-theta is approximately constant and depends solely on beta, but it deviates from zero even for alpha = 0 = beta, an offset the article takes as an error estimate. [→ C. Körber 2018](#c-korber-2018)
`q2 i?` For large time steps the perihelion motion oscillates between discrete values at different turns, indicating the time step is too large. [→ C. Körber 2018 (2)](#c-korber-2018-2)

## Evidence

### C. Körber 2018

C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. [doi:10.1088/1361-6552/aac487](https://doi.org/10.1088/1361-6552/aac487)

`q2 · i?` · `design · r2`

Numerical stability study shown in Figure 4 (Sec. 5): perihelion motion over the first 10 turns for several time steps and beta values, all with alpha = 0. The offset at alpha = 0 = beta serves as an estimate of the simulation error.

> "As expected,δΘ is approximately constant for suﬃciently small time-steps∆t and its value depends solely onβ. However, contrary to the correct resultδΘ deviates from zero forα = 0 =β for all∆t."

### C. Körber 2018 (2)

C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. [doi:10.1088/1361-6552/aac487](https://doi.org/10.1088/1361-6552/aac487)

`q2 · i?` · `design · r2`

The article explains the oscillations arise because the perihelion finder selects the closest point among discretized time steps, sometimes before and sometimes after the true perihelion; precision improves as the time step shrinks. Figure 2b shows a trajectory failing to reproduce the physical orbit for a doubled time step.

> "Furthermore, one can observe that for large time-steps the values of the perihelion motion oscillate between discrete values at diﬀerent turns."

## Discussion


## Related Claims
- [The spring exercise lets students demonstrate interactively that the half-cycle time of harmonic motion does not depend on amplitude, even under Euler-Cromer integration](spring-exercise-period-amplitude-independence.md) — related
