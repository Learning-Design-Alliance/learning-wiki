---
type: claim
title: "In uniformly accelerated circular motion, angular acceleration determinations from the orientation API, the gyroscope, and Tracker video analysis agree with a maximum discrepancy below 1%"
description: "In uniformly accelerated circular motion, angular acceleration determinations from the orientation API, the gyroscope, and Tracker video analysis agree with a maximum discrepancy below 1%"
id: uacm-angular-acceleration-three-methods-below-1-percent
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

# In uniformly accelerated circular motion, angular acceleration determinations from the orientation API, the gyroscope, and Tracker video analysis agree with a maximum discrepancy below 1%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` For UACM, the orientation API quadratic fit gives α = 7.58(2) rad/s², the gyroscope linear fit gives α = 7.614(8) rad/s² (R² = 0.9999), and Tracker gives α = 7.56(2) rad/s² (R² = 0.9998), with maximum discrepancy below 1%. [→ Josep Ll. Suñer 2026](#josep-ll-suner-2026)

## Evidence

### Josep Ll. Suñer 2026

Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab

`q2 · i?` · `design · r?`

Results section on UACM: quadratic fit of orientation API data over 2.7 s yields α = 7.58(2) rad/s² with R² ≈ 1; gyroscope fit gives α = 7.614(8) rad/s²; Tracker gives α = 7.56(2) rad/s². "The maximum discrepancy among the three methods is below 1%". No effect size printed.

> "The gyroscope data [Fig. 4(b)] increase linearly in time, as predicted; the linear fit ω( t) = αt + ω0 gives α = 7.614(8) rad/s 2 (R 2 = 0.9999). The difference between the two smartphone determinations is only 0.5%. Video analysis with Tracker, fitting the angular position to the same quadratic model, gives α = 7.56(2) rad/s 2 (R2 = 0.9998). The maximum discrepancy among the three methods is below 1%"

## Discussion


## Related Claims
- [Gyroscope-based angular velocity measurements are robust to slight off-center smartphone placement on the rotating platform because they depend on rotation rate about the z-axis rather than spatial position](gyroscope-robust-to-off-center-placement.md) — related
- [The smartphone records verify the rotational kinematic equations: constant angular velocity yields linear angular position in UCM, and constant angular acceleration yields linear angular velocity and quadratic angular position in UACM](smartphone-records-verify-rotational-kinematic-equations.md) — a broader claim this one bears on
- [In uniform circular motion, smartphone orientation-API and gyroscope measurements of angular velocity agree with each other within 0.1% and with independent Tracker video analysis within 0.5%](ucm-smartphone-channels-agree-within-0-5-percent.md) — related
