---
type: claim
title: The additive entropy decomposition is an upper bound, not a security measure; adversary uncertainty is a conditional entropy
description: The additive entropy decomposition is an upper bound, not a security measure; adversary uncertainty is a conditional entropy
id: bavd-entropy-decomposition-upper-bound-not-security-measure
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
    rigour: 2
---

# The additive entropy decomposition is an upper bound, not a security measure; adversary uncertainty is a conditional entropy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`

## Subclaims
`q1 i?` By sub-additivity of joint Shannon entropy, the four-component sum upper-bounds the joint entropy with equality only under mutual independence, which the generator contradicts by construction; what an adversary faces is the residual conditional entropy given the captured stream. [→ Gupta 2026](#gupta-2026)

## Evidence

### Gupta 2026

Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P. (2026). Behaviorally Adaptive Visual Diversion for Inclusive and Resilient Digital Assessment Delivery. arXiv preprint, under review at IEEE Transactions on Learning Technologies. https://arxiv.org/abs/2608.03531

`q1 · i?` · `theoretical · r2`

Analytical correction (Equations 11a-11b, Theorem 3): decoy placement is drawn conditionally on item layout, making diversion and spatial terms dependent, so conflating the decomposition with security would let a system look secure because it is merely busy; the composite retains a human-factors auditing role.

> "Marginal entropy is not the quantity a security claim rests on. What an adversary faces is the residual uncertainty about the field after observing the captured stream without holding the key"

## Discussion


## Related Claims
- [Theoretical results establish content fidelity, rendering stability, entropy boundedness, and integrity convergence for the BAVD model](bavd-theoretical-properties-fidelity-stability-convergence.md) — related
- [Accessibility attenuation buys reduced sensory burden at a measurable, monotone cost in capture resistance](bavd-attenuation-monotone-accessibility-security-tradeoff.md) — related
