---
type: claim
title: "Second-order TP is extracted only when first-order TP is high enough: the lowest-TP sequence showed no switch cost and the slowest third-item times"
description: "Second-order TP is extracted only when first-order TP is high enough: the lowest-TP sequence showed no switch cost and the slowest third-item times"
id: low-first-order-tp-precludes-second-order-tp
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: lazartigues-laura-2021
    resource: "https://doi.org/10.1371/journal.pone.0246826"
    title: "Lazartigues Laura, Mathy Fabien, Lavigne Frédéric. (2021). Statistical learning of unbalanced exclusive-or temporal sequences in humans. PLoS ONE. https://doi.org/10.1371/journal.pone.0246826"
    author: Lazartigues Laura, Mathy Fabien, Lavigne Frédéric
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Second-order TP is extracted only when first-order TP is high enough: the lowest-TP sequence showed no switch cost and the slowest third-item times

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` The sequence with the lowest first-order TP (.29) had the longest RTTT2 despite second-order TP equal to 1, and its RTTT2 did not increase at the switch. [→ Lazartigues Laura 2021](#lazartigues-laura-2021)

## Evidence

### Lazartigues Laura 2021

Lazartigues Laura, Mathy Fabien, Lavigne Frédéric. (2021). Statistical learning of unbalanced exclusive-or temporal sequences in humans. PLoS ONE. https://doi.org/10.1371/journal.pone.0246826

`q3 · i?` · `causal · r2`

In the same touchscreen experiment, the three sequences with higher first-order TPs (.38, .62, .71) showed no significant RTTT2 difference (F(2,13084) = 1.06, p = .347), while the lowest-TP sequence did not show the switch increase; the authors conclude "a too low value of first-order TP might preclude processing of second-order TP".

> "the sequence with the lowest value of first-order TP (TP = .29, plain red line) exhibited the longest RTTT2 compared to the other three sequences (F(1,7243) = 43.64, p <.001). For this sequence, RTTT2 did not increase between the last block of the learning phase and the switch phase (F(1,251) = 2.9, p <.09)."

## Discussion


## Related Claims
- [Model comparison by AIC shows first-order TP, not frequency, accounts for learning of the third-item transition times](aic-first-order-tp-beats-frequency-model.md) — related
- [First-order TP and block number interact on third-item response times, showing sequences are not learned equally despite equal second-order TPs](block-tp-interaction-third-item.md) — related
- [Second-order transitional probabilities are learned: response times to the third item decrease during learning and increase when sequences are switched](second-order-tp-learned-switch-phase.md) — a broader claim this one bears on
- [Response times to the second item decrease across learning blocks and are slowest for the lowest first-order TP early in learning](tt1-decreases-blocks-lowest-tp-slowest.md) — related
