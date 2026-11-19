---
type: claim
title: The sensing modules show high linearity, with calibration coefficients of determination above 0.99
description: The sensing modules show high linearity, with calibration coefficients of determination above 0.99
id: fretboard-sensors-high-linearity-r2-above-99
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: ren-2023
    resource: "https://doi.org/10.48550/arXiv.2304.06521"
    title: "Ren, Z., Hsu, C.-C., Kocabalkanli, C., Nguyen, K., Iordachita, I. I., Bastepe-Gray, S., Scott, N. (2023). Multi-Contact Force-Sensing Guitar for Training and Therapy. [doi:10.48550/arXiv.2304.06521](https://doi.org/10.48550/arXiv.2304.06521)"
    author: Ren, Z., Hsu, C.-C., Kocabalkanli, C., Nguyen, K., Iordachita, I. I., Bastepe-Gray, S., Scott, N.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The sensing modules show high linearity, with calibration coefficients of determination above 0.99

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Calibration of the 72 sensing modules against a load cell shows high linearity, with each tested module's coefficient of determination higher than 0.99. [→ Ren 2023](#ren-2023)

## Evidence

### Ren 2023

Ren, Z., Hsu, C.-C., Kocabalkanli, C., Nguyen, K., Iordachita, I. I., Bastepe-Gray, S., Scott, N. (2023). Multi-Contact Force-Sensing Guitar for Training and Therapy. [doi:10.48550/arXiv.2304.06521](https://doi.org/10.48550/arXiv.2304.06521)

`q2 · i?` · `design · r2`

Bench calibration on a custom micron-stage rig with a Sparkfun TAL220B load cell (±0.025 N accuracy) as ground truth; each of the 72 modules was loaded and unloaded between 0 and 25 N for 2 trials. The figure caption reports "The coefﬁcient of determination for each is higher than 0.99." Calibration slopes differed across modules because flexure stiffness varies with fret width.

> "Calibration results of ﬁve randomly chosen modules. The coefﬁcient of determination for each is higher than 0.99."

## Discussion


## Related Claims
- [81% of sensing modules achieve average error below 0.4 N RMSE and 90% achieve worst error below 5% FSO](fretboard-validation-error-percentages.md) — related
- [Musicians found the force-sensing fretboard's real-time visual feedback constructive to their playing despite slight sound-quality differences](musician-user-testing-positive-reception.md) — related
