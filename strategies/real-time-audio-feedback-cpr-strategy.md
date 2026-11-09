---
type: strategy
id: real-time-audio-feedback-cpr-strategy
title: Provide real-time audio feedback during CPR training, supplemented with visualisations and end-of-session dashboards
description: "Participants' answers to the desired-feedback question point to what future tutor implementations should offer: \"The most mentioned was real-time audio (five times), then real-time visualisations, dashboards at the en..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
sources:
  - id: di-mitri-daniele-2019
    resource: "https://doi.org/10.3390/s19143099"
    title: "Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099"
    author: Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik
---

# Provide real-time audio feedback during CPR training, supplemented with visualisations and end-of-session dashboards

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (3 for, 2 against) · 3 studies (1 causal, 1 review, 1 design), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
Participants' answers to the desired-feedback question point to what future tutor implementations should offer: "The most mentioned was real-time audio (five times), then real-time visualisations, dashboards at the end and haptic vibrations or augmented reality visuals". Respondents also reported that during execution "there is little awareness of the perceived performance", motivating immediate rather than retrospective feedback. The authors plan to use these principles in follow-up studies of the Multimodal Tutor for CPR alongside a run-time feedback engine capturing data in real time.

## Design Implications

### Context
#### Requirements
- A run-time feedback engine ensuring multimodal data are captured in real-time and that feedback is timely
#### Constraints
- Recommendations derive from a single questionnaire of 14 advanced students; no feedback intervention was tested in this study

### Target Learners
- CPR trainees, including medical students and public/workplace learners

### Target Learning Goals
- Timely correction of chest compression mistakes during practice

## Claims

- [Real-time audio feedback from the CPR Tutor is followed by a short-term decrease in Error Rates across all five target CPR classes within 10 seconds](../claims/cpr-tutor-short-term-error-rate-decrease.md) [+M]
- [Sessions with CPR Tutor feedback showed no significant difference in overall mistake frequency compared with control sessions without feedback](../claims/cpr-tutor-no-overall-mistake-frequency-reduction.md) [-M]
- [An augmented-reality CPR training application did not improve CPR quality compared with a standard audio-visual feedback manikin](../claims/ar-cpr-training-no-improvement-over-manikin.md) [-M]
- [Multimodal sensor data can classify standard CPR training mistakes on compression rate, depth and release with over 70% accuracy compared to a ResusciAnne manikin baseline](../claims/multimodal-data-detect-standard-cpr-mistakes.md) [+M]
- [Multimodal data can detect additional CPR training mistakes not tracked by commercial manikins — locked arms and incorrect body weight — with over 93% accuracy](../claims/multimodal-detect-additional-cpr-mistakes.md) [+M]

## Related Strategies

- [Iterate real-time tutor feedback based on user questionnaires: add explanations, positive feedback, session summaries and pause warnings](cpr-tutor-questionnaire-driven-feature-improvements.md)
- [Use gaze-based automated strategy identification for teacher dashboards and personalized feedback in online statistics learning](gaze-based-teacher-dashboards-feedback.md)

## Examples
-

## Key Sources
- Di Mitri Daniele, Schneider Jan, Specht Marcus, Drachsler Hendrik. (2019). Detecting Mistakes in CPR Training with Multimodal Data and Neural Networks. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143099
