---
type: design
id: raspberry-pi-gsr-hr-physiological-collection-system
title: Wearable GSR and heart rate physiological collection system on Raspberry Pi
description: "The article built a physiological signal collection system from a Grove GSR sensor and a Grove ear-clip heart rate sensor installed on a Raspberry Pi, plus a GUI-based JavaFX application that \"collects voice frequenci..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: tseng-2022
    resource: "https://rec.chass.ncku.edu.tw/application/search?combine=110-174"
    title: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2022). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. https://rec.chass.ncku.edu.tw/application/search?combine=110-174"
    author: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R"
---

# Wearable GSR and heart rate physiological collection system on Raspberry Pi

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article built a physiological signal collection system from a Grove GSR sensor and a Grove ear-clip heart rate sensor installed on a Raspberry Pi, plus a GUI-based JavaFX application that "collects voice frequencies, volumes, heart rates, and GSR values", keeping only heart rate and GSR values in this research. Sampling rates were 0.3 samples/second for GSR and 1.1 samples/second for heart rate.

## Design Implications

### Context
#### Requirements
- The sensors must be attached to participants before the experimental task so signals can be collected and saved to a local disk during the session.
#### Constraints
- The application collected voice frequencies and volumes but this research kept only the heart rate values and GSR values.

### Target Learners
- university electrical engineering students

### Learning Goals
- assessment of Big Five personality traits to inform personalized programming instruction

### Claims

- [Physiological Gsr Hr Variance Predict Extraversion](../claims/physiological-gsr-hr-variance-predict-extraversion.md) [+M]
- [No effective prediction model was found for emotional stability or openness, though tendencies were observed](../claims/no-effective-model-emotional-stability-openness.md) [~W]
- [Heart rate variance predicts agreeableness and conscientiousness levels, with Random Forest OOB errors of 27.59% and 24.14%](../claims/hr-variance-predicts-agreeableness-conscientiousness.md) [+W]

## Related Designs

- [Multi-modal sensing framework with pressure-instrumented laryngoscope and biometric vest](multimodal-sensing-laryngoscope-biometrics.md)
- [Use ultra-brief affective prompts to enrich the psychological interpretability of passive physiological data at minimal participant burden](ultra-brief-affective-prompts-interpretability.md)

## Examples
-

## Key Sources
- Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2022). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. https://rec.chass.ncku.edu.tw/application/search?combine=110-174
