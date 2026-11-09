---
type: claim
title: Adding tool visibility and grip angle features to tip motion features improved skill prediction, with the tip-motion-only model performing worst of the six
description: Adding tool visibility and grip angle features to tip motion features improved skill prediction, with the tip-motion-only model performing worst of the six
id: visibility-grip-features-improve-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-09
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: oquendo-yousi-a-2017
    resource: "https://doi.org/10.1007/s00464-017-5873-6"
    title: "Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6"
    author: Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding tool visibility and grip angle features to tip motion features improved skill prediction, with the tip-motion-only model performing worst of the six

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models TMV and TMG outperformed Model TM on all accuracy measures, indicating visibility and grip features carried information absent from tip motion data alone. [→ Oquendo Yousi A. 2017](#oquendo-yousi-a-2017)

## Evidence

### Oquendo Yousi A. 2017

Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6

`q2 · i?` · `design · r2`

Comparison of six regression models on leave-one-subject-out testing data from 63 trials. Model TM (time plus tip motion) tested worst of the six, and the authors report it had the largest training-to-testing performance decrease, which they attribute to overfitting.

> "Models TMV and TMG both performed better than Model TM in all measures of accuracy, showing that the visibility and grip features added important information that was not provided by the tip motion data."

## Discussion


## Related Claims
- [A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85](tmvg-model-best-unseen-trial-osats-prediction.md) — related
