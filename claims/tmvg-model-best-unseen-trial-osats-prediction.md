---
type: claim
title: "A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85"
description: "A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85"
id: tmvg-model-best-unseen-trial-osats-prediction
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

# A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Model TMVG, using features from all four sensor types, achieved the best testing performance of six regression models, predicting summed scores within 4 points 89% of the time and correlating 0.85 with reviewer scores. [→ Oquendo Yousi A. 2017](#oquendo-yousi-a-2017)

## Evidence

### Oquendo Yousi A. 2017

Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6

`q2 · i?` · `design · r2`

Leave-one-subject-out cross-validation testing of six regression tree models on 63 recorded trials from 32 trainees in a custom pediatric box trainer. The all-sensor TMVG model was best on all six testing accuracy metrics, with summed scores "within 4 points of the reviewer’s summed score 89% of the time" and correlation 0.85.

> "It predicted a summed score that was within 4 points of the reviewer’s summed score 89% of the time, and its rounded average scores were always within 1 point of the true label. The correlation between the reviewer’s scores and those of this predictive model was 0.85 for both score types."

## Discussion


## Related Claims
- [Adding tool visibility and grip angle features to tip motion features improved skill prediction, with the tip-motion-only model performing worst of the six](visibility-grip-features-improve-prediction.md) — related
- [The best model was the only one of six that predicted all rounded average OSATS scores of unseen trials within 1 point of the reviewer's scores](tmvg-rounded-average-within-one-point.md) — related
- [Most trainees who repeated the pediatric suturing task improved: 71.0% improved their summed score, 16.1% decreased, and first and second trial scores correlated R = 0.89](second-trial-improvement-pediatric-suturing.md) — related
- [Subjective gentleness ratings correlate negatively with objectively measured force on tissue during robotic suturing](gentleness-negatively-correlated-with-force.md) — related
- [Force-based parameters distinguish novices, intermediates and experts on a robotic suturing task, establishing construct validity](force-parameters-distinguish-robotic-surgery-experience-groups.md) — related
