---
type: claim
title: "Second-order transitional probabilities are learned: response times to the third item decrease during learning and increase when sequences are switched"
description: "Second-order transitional probabilities are learned: response times to the third item decrease during learning and increase when sequences are switched"
id: second-order-tp-learned-switch-phase
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
  - id: lazartigues-laura-2021-2
    resource: "https://doi.org/10.1371/journal.pone.0246826"
    title: "Lazartigues Laura, Mathy Fabien, Lavigne Frédéric. (2021). Statistical learning of unbalanced exclusive-or temporal sequences in humans. PLoS ONE. https://doi.org/10.1371/journal.pone.0246826"
    author: Lazartigues Laura, Mathy Fabien, Lavigne Frédéric
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Second-order transitional probabilities are learned: response times to the third item decrease during learning and increase when sequences are switched

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` RTTT2 decreased significantly across learning blocks. [→ Lazartigues Laura 2021](#lazartigues-laura-2021)
`q3 i?` RTTT2 increased significantly in the switch phase, showing second-order TP was learned over whole triplets, not just pairs. [→ Lazartigues Laura 2021 (2)](#lazartigues-laura-2021-2)

## Evidence

### Lazartigues Laura 2021

Lazartigues Laura, Mathy Fabien, Lavigne Frédéric. (2021). Statistical learning of unbalanced exclusive-or temporal sequences in humans. PLoS ONE. https://doi.org/10.1371/journal.pone.0246826

`q3 · i?` · `causal · r2`

Mixed-model analysis of transition times to the third dot in the 38-participant touchscreen experiment; the authors state this "supports the idea that learning impacted RTTT2".

> "the mixed model 2 in Table 3 showed a significant decrease of RTTT2 as a function of block number during the learning phase (F(1,14514) = 600.5, p <.001)"

### Lazartigues Laura 2021 (2)

Lazartigues Laura, Mathy Fabien, Lavigne Frédéric. (2021). Statistical learning of unbalanced exclusive-or temporal sequences in humans. PLoS ONE. https://doi.org/10.1371/journal.pone.0246826

`q3 · i?` · `causal · r2`

In the switch phase the third dots were permuted between sequences, resetting second-order TP while preserving all pairs and first-order TPs; the increase in TT2 led the authors to conclude "second-order TPs were actually learned (and not only first-order TPs) to influence RTTT2".

> "Further, RTTT2 significantly increased in the switch phase compared to the last block of the learning phase (F(1,2831) = 730.4, p <.001)."

## Discussion


## Related Claims
- [Model comparison by AIC shows first-order TP, not frequency, accounts for learning of the third-item transition times](aic-first-order-tp-beats-frequency-model.md) — related
- [First-order TP and block number interact on third-item response times, showing sequences are not learned equally despite equal second-order TPs](block-tp-interaction-third-item.md) — related
- [Second-order TP is extracted only when first-order TP is high enough: the lowest-TP sequence showed no switch cost and the slowest third-item times](low-first-order-tp-precludes-second-order-tp.md) — a narrower finding that bears on this claim
- [Response times to the second item decrease across learning blocks and are slowest for the lowest first-order TP early in learning](tt1-decreases-blocks-lowest-tp-slowest.md) — related
