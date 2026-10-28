---
type: strategy
id: shap-explainable-eye-tracking-personalized-vr-learning
title: Use SHAP-based explainable ML on eye-tracking data to identify gender-specific attention patterns and inform personalized learning support in VR educational environments.
description: The article demonstrates a methodology combining eye-tracking data collection in immersive VR, machine learning classification, and SHAP explainability to investigate gender differences in learning behavior.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: gao-2023
    resource: "https://doi.org/10.1007/s40593-022-00316-z"
    title: "Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z"
    author: "Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E"
---

# Use SHAP-based explainable ML on eye-tracking data to identify gender-specific attention patterns and inform personalized learning support in VR educational environments.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article demonstrates a methodology combining eye-tracking data collection in immersive VR, machine learning classification, and SHAP explainability to investigate gender differences in learning behavior. This approach provides "a fundamental methodology for future studies aimed at investigating gender differences using eye movement information not only in CT but also in other learning activities in immersive VR environments." The insights can inform adaptive tutoring systems and VR classroom design tailored to different learner needs.

## Design Implications

### Context
#### Requirements
- Access to eye-tracking hardware integrated in VR headsets
- Sufficient sample size for ML model training
- Ethical approval for collecting sensitive demographic data
#### Constraints
- Gender is a protected attribute and should be handled carefully in commercial applications
- Results reflect aggregated visual search behavior rather than responses to specific lesson content

### Target Learners
- K-12 students in VR-based learning environments

### Target Learning Goals
- Computational thinking skills development

## Claims

- [Eye movement features collected during a VR computational thinking lesson are discriminative for gender classification, with all five ML models performing above the 50% chance level.](../claims/eye-movements-discriminative-gender-classification-vr-ct.md) [+W]
- [Girls directed more visual attention to instructional content (virtual teacher and screen) while boys distributed attention more broadly including to virtual peer learners.](../claims/gender-differences-visual-attention-vr-classroom.md) [+W]
- [Head movement frequency was the single most informative feature, with more head movements associated with classification as male.](../claims/head-movement-rate-most-informative-gender-feature.md) [+W]
- [HMD-related and fixation-related features contribute more to gender classification than saccade-related and pupil-related features, with hmdMoveRate being the most informative single feature.](../claims/hmd-fixation-features-most-informative-gender-classification.md) [+W]
- [SHAP-based feature selection improved LightGBM gender classification accuracy from 65.5% to 70.8% using the top 24 eye movement features.](../claims/shap-feature-selection-improves-gender-classification.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gao, H., Hasenbein, L., Bozkir, E., Göllner, R., & Kasneci, E. (2023). Exploring Gender Differences in Computational Thinking Learning in a VR Classroom: Developing Machine Learning Models Using Eye-Tracking Data and Explaining the Models. International Journal of Artificial Intelligence in Education, 33, 929-954. https://doi.org/10.1007/s40593-022-00316-z
