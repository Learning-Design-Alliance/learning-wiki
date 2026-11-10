---
type: strategy
id: eye-tracking-real-time-formative-feedback-laparoscopic-training
title: Integrate AOI-dependent eye-tracking and motion metrics into training sessions for real-time formative feedback and personalized training
description: The authors recommend integrating CV-DL-extracted AOI-dependent and motion metrics into training sessions so novices receive real-time feedback on where to look and how to allocate attention, rather than being evaluat...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: khanfar-aseel-f-2025
    resource: "https://doi.org/10.1007/s00464-025-12369-x"
    title: "Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x"
    author: Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett
---

# Integrate AOI-dependent eye-tracking and motion metrics into training sessions for real-time formative feedback and personalized training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 review, 1 associational), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The authors recommend integrating CV-DL-extracted AOI-dependent and motion metrics into training sessions so novices receive real-time feedback on where to look and how to allocate attention, rather than being evaluated only after a session. They state metrics "have great potential to be integrated into training sessions to provide novices with real-time feedback on where to look" and that ML models can predict skill levels to "customize and adapt their training program." This addresses FLS box trainers' lack of real-time objective assessment and personalization.

## Design Implications

### Context
#### Requirements
- Requires a validated CV-DL model to extract AOI-dependent metrics automatically during training, plus ML models trained on those metrics to classify trainee skill levels.
#### Constraints
- The article states findings are specific to the peg transfer task, derive from a single-institution small sample without expert participants, and that further validation in large-scale multi-institution studies is necessary.

### Target Learners
- Novice surgeons (medical students and residents in early laparoscopic training)

### Target Learning Goals
- Laparoscopic psychomotor skill acquisition
- Visual attention guidance (fixating relevant objects rather than tools)

## Claims

- [AOI-dependent eye-tracking and motion metrics classify novices into High and Mid-Low skill levels during early-stage peg transfer training](../claims/aoi-metrics-classify-novice-skill-levels-early-training.md) [+W]
- [Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors](../claims/random-forest-predicts-visual-behavior-levels.md) [+W]
- [More-skilled novices fixate more on objects and less on tools, with slower tool speed, than less-skilled novices](../claims/skilled-novices-object-fixation-pattern.md) [+W]
- [Cognitive and behavioral metrics via EEG and eye-tracking with machine learning predicted surgical training outcomes with 72.5% accuracy](../claims/eeg-eye-metrics-ml-predict-training-outcomes.md) [+W]

## Related Strategies

- [Integrate the validated iVR simulator into early orthopedic training as a platform for deliberate practice with individualized feedback, pending longitudinal confirmation](ivr-deliberate-practice-platform-early-orthopedic-training.md)
- [Use GPT-4 few-shot rephrasing of incorrect trainee responses to deliver corrective explanatory feedback at scale](gpt4-rephrase-incorrect-responses-feedback-strategy.md)
- [Use gaze tracking as a feedback tool to alert students and instructors to key moments in simulation learning](gaze-tracking-feedback-simulation-debriefing.md)
- [Use eye-tracking feedback and gradually increasing case complexity to train targeted visual search and cognitive-load management in ECG education](eye-tracking-feedback-ecg-visual-strategy-training.md)
- [Use simulated real-world tasks as a platform for deliberate practice and risk-perception training with cognitive-state monitoring](real-world-sim-deliberate-practice-strategy.md)

## Examples
-

## Key Sources
- Khanfar Aseel F., Motamedi Sanaz, Safford Shawn D., Moore Jason, Menold Jessica, Miller Scarlett. (2025). From gaze to proficiency: deep learning-driven prediction of novice performance in laparoscopic training using AOI-dependent metrics. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12369-x
