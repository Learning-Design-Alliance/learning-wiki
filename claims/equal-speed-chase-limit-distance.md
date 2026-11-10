---
type: claim
title: For equal dog and rabbit speeds, the distance between them converges to r_min = (L2 + sqrt(L1^2 + L2^2))/2
description: For equal dog and rabbit speeds, the distance between them converges to r_min = (L2 + sqrt(L1^2 + L2^2))/2
id: equal-speed-chase-limit-distance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: weak
newest_evidence: 2009
sources:
  - id: o-i-chashchina-2009
    resource: "https://arxiv.org/abs/0711.3293"
    title: "O. I. Chashchina, Z. K. Silagadze. (2009). The dog-and-rabbit chase problem as an exercise in introductory kinematics. https://arxiv.org/abs/0711.3293"
    author: O. I. Chashchina, Z. K. Silagadze
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# For equal dog and rabbit speeds, the distance between them converges to r_min = (L2 + sqrt(L1^2 + L2^2))/2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` When V = u, the quantity r(1 - cos phi) is conserved, and as phi -> pi the separation approaches the printed limit. [→ O. I. Chashchina 2009](#o-i-chashchina-2009)

## Evidence

### O. I. Chashchina 2009

O. I. Chashchina, Z. K. Silagadze. (2009). The dog-and-rabbit chase problem as an exercise in introductory kinematics. https://arxiv.org/abs/0711.3293

`q1 · i?` · `theoretical · r3`

Analytical derivation in Section 5: working in the rabbit's frame with V = u, the article shows d/dt(r - r cos phi) = 0, evaluates the constant C from initial positions, and prints the limiting distance.

> "In the rabbit’s frame ϕ → π, when t → ∞. Hence the limit distance between the dog and the rabbit is [5] rmin = C1 − cos π = L2 + √ L21 + L22 2 ."

## Discussion


## Related Claims
- [The chase duration for a dog of speed V pursuing a rabbit of speed u is T = LV/(V^2 - u^2), derived with elementary vector kinematics](chase-duration-vector-kinematics-derivation.md) — related
- [If the rabbit adjusts its speed to keep the separation constant at L, the required speed is u(t) = V*sqrt(1 - sin^2(phi0) e^(-2Vt/L)) and the dog's trajectory is a tractrix](constant-distance-chase-tractrix-trajectory.md) — related
- [The dog's trajectory in the rabbit's frame is r = L/sin(phi) * (cot(phi/2))^(V/u), obtained by radial-tangential velocity decomposition](dog-trajectory-rabbit-frame-polar-form.md) — related
- [The dog's curve of pursuit in the laboratory frame derived via the rabbit-frame trajectory matches the result previously found in the literature](lab-frame-curve-of-pursuit-matches-literature.md) — related
