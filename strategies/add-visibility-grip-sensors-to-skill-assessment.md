---
type: strategy
id: add-visibility-grip-sensors-to-skill-assessment
title: Incorporate tool visibility and grip angle sensors into motion-tracked surgical skill assessment setups
description: The article recommends that motion-analysis skill assessment systems add endoscope-based tool visibility tracking and handle-mounted flex sensors alongside standard tip motion tracking.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-09
sources:
  - id: oquendo-yousi-a-2017
    resource: "https://doi.org/10.1007/s00464-017-5873-6"
    title: "Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6"
    author: Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J
---

# Incorporate tool visibility and grip angle sensors into motion-tracked surgical skill assessment setups

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends that motion-analysis skill assessment systems add endoscope-based tool visibility tracking and handle-mounted flex sensors alongside standard tip motion tracking. The authors report that "information from both of these sensor streams significantly improved skill prediction", while adding little cost: about 500 USD for the additional visibility sensor and about 50 USD for two flex sensors, with minimal computation time relative to the full feature calculation.

## Design Implications

### Context
#### Requirements
- A camera-based endoscope view for computing tool tip visibility features and handle-mounted flex sensors calibrated per subject for grip angle measurement
#### Constraints
- Adding magnetic sensors required removing metal components from the box trainer environment to avoid transmitter interference

### Target Learners
- surgical trainees in minimally invasive surgery programs

### Target Learning Goals
- automated objective assessment of laparoscopic technical skill

## Claims

- [A regression model using all four sensor streams (time, tip motion, visibility, grip) best predicted summed OSATS scores of unseen trials, within 4 points 89% of the time with correlation 0.85](../claims/tmvg-model-best-unseen-trial-osats-prediction.md) [+W]
- [The best model was the only one of six that predicted all rounded average OSATS scores of unseen trials within 1 point of the reviewer's scores](../claims/tmvg-rounded-average-within-one-point.md) [+W]
- [Adding tool visibility and grip angle features to tip motion features improved skill prediction, with the tip-motion-only model performing worst of the six](../claims/visibility-grip-features-improve-prediction.md) [+W]

## Related Strategies

- [Integrate objective force-based assessment of tissue handling into robotic surgery training](objective-force-assessment-in-ras-training.md)
- [Develop universal objective assessment and feedback methods that go beyond time and motion to capture tissue handling and interaction forces](universal-objective-assessment-tissue-force-feedback.md)

## Examples
-

## Key Sources
- Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6
