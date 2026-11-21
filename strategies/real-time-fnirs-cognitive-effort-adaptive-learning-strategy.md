---
type: strategy
id: real-time-fnirs-cognitive-effort-adaptive-learning-strategy
title: Build real-time cognitive effort estimation systems using live fNIRS data and dynamic model outputs to support adaptive learning
description: The authors propose extending their post-hoc cognitive effort estimation into a real-time system that estimates cognitive effort during learning using live fNIRS data and dynamic model outputs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025
    resource: "https://doi.org/10.1145/3747327.3764901"
    title: "Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901"
    author: Shayla Sharmin and Roghayeh Leila Barmaki
---

# Build real-time cognitive effort estimation systems using live fNIRS data and dynamic model outputs to support adaptive learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 associational, 1 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors propose extending their post-hoc cognitive effort estimation into a real-time system that estimates cognitive effort during learning using live fNIRS data and dynamic model outputs. They state their "lightweight CNN-GRU model is suitable for real-time deployment" and envision personalized educational setups that dynamically adapt to learners' cognitive states, supporting adaptive learning systems grounded in neural feedback.

## Design Implications

### Context
#### Requirements
- Real-time performance prediction and availability of fNIRS data for a given time window
#### Constraints
- Real-time implementation was beyond this study's scope; cognitive effort was estimated post-hoc

### Target Learners
- learners in classroom and remote educational settings

### Target Learning Goals
- adapting learning materials to learners' cognitive states in real time

## Claims

- [A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals](../claims/cnn-gru-outperforms-baselines-fnirs-performance-prediction.md) [+W]
- [XGBoost accuracy improves when trained on deep-learned representations, with CNN-GRU features yielding the highest XGBoost accuracy](../claims/deep-features-improve-xgboost-fnirs.md) [+W]
- [Interpretability analysis indicates LPFC activity contributed significantly to the model's performance prediction](../claims/lpfc-dominates-fnirs-performance-prediction.md) [+W]
- [RNE and RNI computed from predicted scores closely match actual cognitive effort values, with Pearson r > 0.94 across tested participants](../claims/predicted-rne-rni-match-actual-trends.md) [+W]
- [Traditional machine learning models show mixed results predicting quiz performance from fNIRS, with Random Forest achieving the highest recall and Neural Network and LightGBM the lowest test accuracy](../claims/traditional-ml-mixed-fnirs-quiz-prediction.md) [+W]

## Related Strategies

- [Prioritize standardized fNIRS methods, ecologically valid learning settings, and evaluation of real-time neural adaptation feasibility](prioritize-standardized-methods-and-ecological-validity-fnirs-gils.md)
- [Prioritize construct-to-data mappings, multimodal validation, ethical implementation, and cross-disciplinary collaboration for domain-specific adaptive systems](domain-specific-adaptivity-research-priorities.md)

## Examples
-

## Key Sources
- Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901
