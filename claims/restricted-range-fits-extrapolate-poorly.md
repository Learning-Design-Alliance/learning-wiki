---
type: claim
title: Extrapolating from parameters fitted to a restricted range of between-session intervals produces worse predictions than time-variant fits
description: Extrapolating from parameters fitted to a restricted range of between-session intervals produces worse predictions than time-variant fits
id: restricted-range-fits-extrapolate-poorly
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: maarten-van-der-velde-2026
    resource: "https://doi.org/10.1038/s41539-026-00447-1"
    title: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1"
    author: "Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Extrapolating from parameters fitted to a restricted range of between-session intervals produces worse predictions than time-variant fits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models fitted only to 0–10 minute or 23.5–24.5 hour intervals predicted recall worse out-of-sample than any of the time-variant model fits. [→ Maarten van der Velde 2026](#maarten-van-der-velde-2026)

## Evidence

### Maarten van der Velde 2026

Maarten van der Velde, Florian Sense, Jelmer P. Borst & Hedderik van Rijn. (2026). Explaining forgetting at different timescales requires a time-variant forgetting function. npj Science of Learning. https://doi.org/10.1038/s41539-026-00447-1

`q2 · i?` · `associational · r2`

Cross-validated comparison of models fitted to restricted interval ranges (0–10 minutes, reflecting within-session intervals, or around 24 hours) against time-variant fits. The article reports "clear evidence that extrapolating from parameters ﬁtted to a restricted range... produces worse model predictions."

> "We found clear evidence that extrapolating from parameters ﬁtted to a restricted range of between-session intervals (0–10 min or 24 hours; Fig.2b) produces worse model predictions than any of the time-variant model ﬁts."

## Discussion


## Related Claims
- [In 5-fold cross-validation, multi-bin time-variant model fits outperform single-bin fits, with diminishing returns beyond a 5-bin split and further gains from differentiating by learner and amount of practice](cross-validation-favors-time-variant-fits.md) — related
- [Optimal ACT-R parameter values change systematically and predictably with the length of the between-session interval](parameters-vary-systematically-with-interval.md) — a broader claim this one bears on
- [Allowing ACT-R memory parameters to vary with the between-session interval produces a strong fit between model and recall data across timescales](time-variant-parameters-capture-retention-across-timescales.md) — a broader claim this one bears on
- [A single time-invariant ACT-R forgetting function cannot simultaneously capture recall accuracy on short and long between-session intervals](single-forgetting-function-fails-across-timescales.md) — a narrower finding that bears on this claim
