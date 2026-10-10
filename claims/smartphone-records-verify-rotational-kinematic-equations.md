---
type: claim
title: "The smartphone records verify the rotational kinematic equations: constant angular velocity yields linear angular position in UCM, and constant angular acceleration yields linear angular velocity and quadratic angular position in UACM"
description: "The smartphone records verify the rotational kinematic equations: constant angular velocity yields linear angular position in UCM, and constant angular acceleration yields linear angular velocity and quadratic angular..."
id: smartphone-records-verify-rotational-kinematic-equations
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: josep-ll-suñer-2026
    resource: "https://smartphysics.webs.upv.es/rotation-lab"
    title: "Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab"
    author: Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí
    q: 2
    i: "?"
    kind: design
    rigour: "?"
  - id: josep-ll-suñer-2026-2
    resource: "https://smartphysics.webs.upv.es/rotation-lab"
    title: "Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab"
    author: Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# The smartphone records verify the rotational kinematic equations: constant angular velocity yields linear angular position in UCM, and constant angular acceleration yields linear angular velocity and quadratic angular position in UACM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r?` · `q2`

## Subclaims
`q2 i?` In UCM the angular velocity is approximately constant and the angle grows linearly in time; in UACM the angular velocity increases linearly and the angle exhibits quadratic evolution, as expected for constant angular acceleration. [→ Josep Ll. Suñer 2026](#josep-ll-suner-2026)
`q2 i?` The orientation API angular position over 4.1 s fits θ(t) = ωt + θ0 with R² = 0.9999, confirming the linear behavior expected for UCM. [→ Josep Ll. Suñer 2026 (2)](#josep-ll-suner-2026-2)

## Evidence

### Josep Ll. Suñer 2026

Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab

`q2 · i?` · `design · r?`

Descriptive analysis of application screenshots during both experiments: only the azimuth angle and corresponding angular velocity component take significant values, while other series stay close to zero. The quote states the observed kinematic patterns for both motions.

> "For UCM [Fig. 2(a)] the angular velocity is approximately constant and the angle grows linearly in time, whereas for UACM [Fig. 2(b)] the angular velocity increases linearly and the angle exhibits the characteristic quadratic evolution of motion with constant angular acceleration."

### Josep Ll. Suñer 2026 (2)

Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab

`q2 · i?` · `design · r?`

Results section, UCM: linear fit of orientation-API angular position over a 4.1 s interval gives ω = 6.110(5) rad/s with R² = 0.9999; the gyroscope needs no fit and its mean is ω = 6.10(8) rad/s. Uncertainties obtained with spreadsheet LINEST, AVERAGE and STDEV functions.

> "Figure 3(a) shows the angular position obtained from the orientation API over an analyzed interval of 4.1 s, together with the linear fit θ(t) = ωt + θ0. The slope directly yields the angular velocity, ω = 6.110(5) rad/s, with a coefficient of determination R 2 = 0.9999, confirming the excellent linear behavior expected for UCM."

## Discussion


## Related Claims
- [Gyroscope-based angular velocity measurements are robust to slight off-center smartphone placement on the rotating platform because they depend on rotation rate about the z-axis rather than spatial position](gyroscope-robust-to-off-center-placement.md) — related
- [In uniformly accelerated circular motion, angular acceleration determinations from the orientation API, the gyroscope, and Tracker video analysis agree with a maximum discrepancy below 1%](uacm-angular-acceleration-three-methods-below-1-percent.md) — a narrower finding that bears on this claim
- [In uniform circular motion, smartphone orientation-API and gyroscope measurements of angular velocity agree with each other within 0.1% and with independent Tracker video analysis within 0.5%](ucm-smartphone-channels-agree-within-0-5-percent.md) — a narrower finding that bears on this claim
