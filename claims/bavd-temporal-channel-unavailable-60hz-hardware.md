---
type: claim
title: The temporal diversion channel is unavailable on commodity 60 Hz displays, leaving a weaker spatial-only variant
description: The temporal diversion channel is unavailable on commodity 60 Hz displays, leaving a weaker spatial-only variant
id: bavd-temporal-channel-unavailable-60hz-hardware
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gupta-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03531"
    title: "Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P. (2026). Behaviorally Adaptive Visual Diversion for Inclusive and Resilient Digital Assessment Delivery. arXiv preprint, under review at IEEE Transactions on Learning Technologies. https://arxiv.org/abs/2608.03531 [doi:10.48550/arxiv.2608.03531](https://doi.org/10.48550/arxiv.2608.03531)"
    author: "Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# The temporal diversion channel is unavailable on commodity 60 Hz displays, leaving a weaker spatial-only variant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On a 60 Hz panel the highest representable temporal frequency is 30 Hz, which sits below the critical flicker-fusion frequency and inside the photosensitivity band, so the mechanism must fall back on static spatial decoys alone with correspondingly weaker capture asymmetry. [→ Gupta 2026](#gupta-2026)

## Evidence

### Gupta 2026

Gupta, L. R., Kaur, K., Ram, D. S., & Parani, P. (2026). Behaviorally Adaptive Visual Diversion for Inclusive and Resilient Digital Assessment Delivery. arXiv preprint, under review at IEEE Transactions on Learning Technologies. https://arxiv.org/abs/2608.03531 [doi:10.48550/arxiv.2608.03531](https://doi.org/10.48550/arxiv.2608.03531)

`q1 · i?` · `theoretical · r3`

Design-constraint analysis in Section 5.1 combining WCAG 2.1 flash thresholds, photosensitivity data, and the flicker-fusion requirement; the temporal argument holds at 120 Hz and above.

> "On a 60 Hz panel the highest representable temporal frequency is 30 Hz, which sits below f_cff and inside the photosensitivity band. The temporal channel of Equation (4a) is therefore unavailable on commodity 60 Hz hardware"

## Discussion


## Related Claims

- [Theoretical results establish content fidelity, rendering stability, entropy boundedness, and integrity convergence for the BAVD model](bavd-theoretical-properties-fidelity-stability-convergence.md)
- [Accessibility attenuation buys reduced sensory burden at a measurable, monotone cost in capture resistance](bavd-attenuation-monotone-accessibility-security-tradeoff.md)
- [The additive entropy decomposition is an upper bound, not a security measure; adversary uncertainty is a conditional entropy](bavd-entropy-decomposition-upper-bound-not-security-measure.md)
