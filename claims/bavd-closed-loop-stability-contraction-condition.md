---
type: claim
title: The closed-loop adaptation law is stable only when the adaptation gain is small relative to behavioural responsiveness
description: The closed-loop adaptation law is stable only when the adaptation gain is small relative to behavioural responsiveness
id: bavd-closed-loop-stability-contraction-condition
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: gupta-2026
    resource: "https://arxiv.org/abs/2608.03531"
    title: "Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P. (2026). Behaviorally Adaptive Visual Diversion for Inclusive and Resilient Digital Assessment Delivery. arXiv preprint, under review at IEEE Transactions on Learning Technologies. https://arxiv.org/abs/2608.03531"
    author: "Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# The closed-loop adaptation law is stable only when the adaptation gain is small relative to behavioural responsiveness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`

## Subclaims
`q1 i?` With a first-order lag on intensity and Lipschitz behavioural response, the closed loop is a contraction whenever the product of the adaptation coefficient and the two Lipschitz constants is below one, yielding a unique equilibrium. [→ Gupta 2026](#gupta-2026)

## Evidence

### Gupta 2026

Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P. (2026). Behaviorally Adaptive Visual Diversion for Inclusive and Resilient Digital Assessment Delivery. arXiv preprint, under review at IEEE Transactions on Learning Technologies. https://arxiv.org/abs/2608.03531

`q1 · i?` · `theoretical · r3`

Analytical derivation (Equations 9a-9b, Theorem 5) using the Banach fixed-point theorem: the lag rate-limits intensity so a behavioural jump produces a ramp rather than a step, making the flash-rate constraint enforceable at the intensity level.

> "If g is Lipschitz with constant Lg and the behavioural response to on-screen intensity is Lipschitz with constant LB, the closed loop is a contraction whenever β Lg LB < 1"

## Discussion


## Related Claims
- [Theoretical results establish content fidelity, rendering stability, entropy boundedness, and integrity convergence for the BAVD model](bavd-theoretical-properties-fidelity-stability-convergence.md) — related
