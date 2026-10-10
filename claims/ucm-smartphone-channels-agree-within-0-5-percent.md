---
type: claim
title: "In uniform circular motion, smartphone orientation-API and gyroscope measurements of angular velocity agree with each other within 0.1% and with independent Tracker video analysis within 0.5%"
description: "In uniform circular motion, smartphone orientation-API and gyroscope measurements of angular velocity agree with each other within 0.1% and with independent Tracker video analysis within 0.5%"
id: ucm-smartphone-channels-agree-within-0-5-percent
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
---

# In uniform circular motion, smartphone orientation-API and gyroscope measurements of angular velocity agree with each other within 0.1% and with independent Tracker video analysis within 0.5%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` For UCM, the orientation API linear fit gives ω = 6.110(5) rad/s (R² = 0.9999) and the gyroscope mean gives ω = 6.10(8) rad/s, differing by 0.1%, while Tracker video analysis gives ω = 6.13(2) rad/s, agreeing with both to better than 0.5%. [→ Josep Ll. Suñer 2026](#josep-ll-suner-2026)

## Evidence

### Josep Ll. Suñer 2026

Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab

`q2 · i?` · `design · r?`

Results section reports the UCM analysis: orientation API fit ω = 6.110(5) rad/s (R² = 0.9999), gyroscope mean ω = 6.10(8) rad/s, and Tracker video analysis ω = 6.13(2) rad/s (R² = 0.9986). The two smartphone values "differ by only 0.1%" and video analysis agrees "to better than 0.5%". No effect size is printed.

> "The two values differ by only 0.1%, well within the quoted uncertainties, confirming the internal consistency of the browser's sensor-fusion pipeline. As a fully independent external check, video analysis of the motion with Tracker 14 gives ω = 6.13(2) rad/s (R 2 = 0.9986), in agreement with both smartphone measurements to better than 0.5%"

## Discussion


## Related Claims
- [Gyroscope-based angular velocity measurements are robust to slight off-center smartphone placement on the rotating platform because they depend on rotation rate about the z-axis rather than spatial position](gyroscope-robust-to-off-center-placement.md) — related
- [The smartphone records verify the rotational kinematic equations: constant angular velocity yields linear angular position in UCM, and constant angular acceleration yields linear angular velocity and quadratic angular position in UACM](smartphone-records-verify-rotational-kinematic-equations.md) — a broader claim this one bears on
- [In uniformly accelerated circular motion, angular acceleration determinations from the orientation API, the gyroscope, and Tracker video analysis agree with a maximum discrepancy below 1%](uacm-angular-acceleration-three-methods-below-1-percent.md) — related
