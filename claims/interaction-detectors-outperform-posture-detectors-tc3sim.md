---
type: claim
title: Interaction-based affect detectors outperformed posture-based detectors, with boredom detected best and posture detectors near chance
description: Interaction-based affect detectors outperformed posture-based detectors, with boredom detected best and posture detectors near chance
id: interaction-detectors-outperform-posture-detectors-tc3sim
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: defalco-2018
    resource: "https://doi.org/10.1007/s40593-017-0152-1"
    title: "DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C. (2018). Detecting and Addressing Frustration in a Serious Game for Military Training. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0152-1"
    author: "DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: defalco-2018-2
    resource: "https://doi.org/10.1007/s40593-017-0152-1"
    title: "DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C. (2018). Detecting and Addressing Frustration in a Serious Game for Military Training. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0152-1"
    author: "DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Interaction-based affect detectors outperformed posture-based detectors, with boredom detected best and posture detectors near chance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Interaction-based detectors of affect in TC3Sim showed highly variable performance, with boredom best (Kappa = 0.469, A' = 0.848) and confusion barely above chance (Kappa = 0.056, A' = 0.552). [→ DeFalco 2018](#defalco-2018)
`q2 i?` Posture-based detectors performed only slightly better than chance, with surprise worse than chance and boredom best (Kappa = 0.109, A' = 0.528). [→ DeFalco 2018 (2)](#defalco-2018-2)

## Evidence

### DeFalco 2018

DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C. (2018). Detecting and Addressing Frustration in a Serious Game for Military Training. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0152-1

`q2 · i?` · `causal · r2`

Detector development study with 119 USMA cadets using TC3Sim; interaction-based detectors were validated with 10-fold participant-level cross-validation against BROMP field observations. The boredom detector achieved "Kappa = 0.469, A'= 0.848" while confusion performed barely above chance.

> "Performance of our interaction-based detectors was highly variable across affective states. The interaction-based detector of boredom achieved the highest performance (Kappa = 0.469, A'= 0.848) while some of the other detectors achieved very low performance."

### DeFalco 2018 (2)

DeFalco, J. A., Rowe, J. P., Paquette, L., Georgoulas-Sherry, V., Brawner, K., Mott, B. W., Baker, R. S., & Lester, J. C. (2018). Detecting and Addressing Frustration in a Serious Game for Military Training. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-017-0152-1

`q2 · i?` · `associational · r2`

Kinect posture-based detectors built from 73 posture features over the same BROMP-labeled corpus; the best posture detector (boredom, logistic regression) achieved Kappa = 0.109, A' = 0.528, and the frustration SVM achieved Kappa = 0.061, A' = 0.518.

> "In general, posture-based detectors performed only slightly better than chance, with the exception of the surprise detector, which actually performed worse than chance."

## Discussion


## Related Claims
- [During novices' first programming lesson, engagement, confusion, frustration, boredom, and curiosity are the dominant affective states, collectively accounting for approximately 73% of affect judgments](novice-programming-affect-incidence-five-dominant-states.md) — related
