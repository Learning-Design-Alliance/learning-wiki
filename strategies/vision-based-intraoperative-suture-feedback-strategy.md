---
type: strategy
id: vision-based-intraoperative-suture-feedback-strategy
title: Use video-based, system-independent suture metrics to deliver intraoperative feedback in surgical training
description: The authors propose that if a robust quantitative relationship between stitch placement and mechanical resistance is established, computer-vision systems could provide on-screen intraoperative feedback on suture quali...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: spagnulo-r-2025
    resource: "https://doi.org/10.1007/s00464-025-12441-6"
    title: "Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A. (2025). From precision to strength: computer vision for suture quality assessment—an ex vivo pilot study. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12441-6"
    author: Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A
---

# Use video-based, system-independent suture metrics to deliver intraoperative feedback in surgical training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors propose that if a robust quantitative relationship between stitch placement and mechanical resistance is established, computer-vision systems could provide on-screen intraoperative feedback on suture quality, augmenting surgeon perception and supporting skill progression in simulation environments. They stress that "assessment protocols should be system-independent, functioning without additional sensors or hardware that may impede clinical adoption". The present pilot is an early step: correlations exist, but spatial metrics alone predicted burst pressure poorly.

## Design Implications

### Context
#### Requirements
- A robust, well-powered quantitative relationship between stitch placement and pressure resistance must first be established
- Integration of structured assessment protocols into training and intraoperative workflows
#### Constraints
- Current spatial metrics are insufficient as standalone indicators of suture quality; complementary biomechanical and contextual metrics are needed

### Target Learners
- surgical trainees at beginner through expert levels in minimally invasive surgery

### Target Learning Goals
- technical suturing skill development
- objective skill assessment and progression tracking

## Claims

- [An XGBoost model on spatial metrics fails to predict burst pressure, indicating spatial metrics alone are insufficient standalone indicators of suture quality](../claims/xgboost-spatial-metrics-poor-burst-prediction.md) [-W]

## Related Strategies

- [Validate automated video analytics and reach metric consensus before widespread adoption in surgical training](validate-video-analytics-before-adoption.md)
- [Provide trainees with quantified, explainable feedback (estimated GOALS scores and SHAP-derived comments) rather than raw metrics or opaque tier labels](quantified-explainable-feedback-strategy-surgical-training.md)
- [Prototype AI feedback system showing surgeons their skill strengths and weaknesses quantitatively](ai-feedback-prototype-strengths-weaknesses.md)

## Examples
-

## Key Sources
- Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A. (2025). From precision to strength: computer vision for suture quality assessment—an ex vivo pilot study. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12441-6
