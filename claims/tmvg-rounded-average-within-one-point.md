---
type: claim
title: "The best model was the only one of six that predicted all rounded average OSATS scores of unseen trials within 1 point of the reviewer's scores"
description: "The best model was the only one of six that predicted all rounded average OSATS scores of unseen trials within 1 point of the reviewer's scores"
id: tmvg-rounded-average-within-one-point
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

# The best model was the only one of six that predicted all rounded average OSATS scores of unseen trials within 1 point of the reviewer's scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Model TMVG predicted rounded average OSATS scores within 1 point for every testing trial, the only model of the six to do so. [→ Oquendo Yousi A. 2017](#oquendo-yousi-a-2017)

## Evidence

### Oquendo Yousi A. 2017

Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6

`q2 · i?` · `design · r2`

Testing-set evaluation of the six regression models via leave-one-subject-out cross-validation. The TMVG model "predicted all rounded average scores within 1 point of the reviewer-generated scores", while other models showed uneven per-score classification accuracy.

> "This model was the only model of the six that predicted all rounded average scores within 1 point of the reviewer-generated scores."

## Discussion


## Related Claims
- [A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85](tmvg-model-best-unseen-trial-osats-prediction.md) — related
