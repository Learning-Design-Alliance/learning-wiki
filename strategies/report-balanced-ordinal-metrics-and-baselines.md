---
type: strategy
id: report-balanced-ordinal-metrics-and-baselines
title: Report class-balanced ordinal metrics alongside sensor-free baselines and label distributions in engagement-sensing studies
description: "Because engagement labels skew toward engaged states, the article encourages engagement-sensing studies \"to report both measures alongside label distributions, per-class results, and constant baselines\": balanced 1-of..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: sidharth-anupkrishnan-2026
    resource: "https://arxiv.org/abs/2609.26569"
    title: "Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569"
    author: Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen
---

# Report class-balanced ordinal metrics alongside sensor-free baselines and label distributions in engagement-sensing studies

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because engagement labels skew toward engaged states, the article encourages engagement-sensing studies "to report both measures alongside label distributions, per-class results, and constant baselines": balanced 1-off accuracy and macro-MAE, each giving equal class weight. This prevents frequent ratings from dominating evaluation and makes a within-one score interpretable alongside error magnitude and a sensor-free reference such as the mode baseline.

## Design Implications

### Context
#### Requirements
- Class-balanced averaging so performance on rarer disengaged states is not masked by majority classes
- Sensor-free baselines (mode, rounded mean, random distribution) recomputed within each fold as label-only reference points
#### Constraints
- Model selection should also reflect the intended response, since tracking graded changes and triggering a binary alert require different evaluations

### Target Learners
- researchers evaluating engagement-sensing models

### Target Learning Goals
- valid evaluation of engagement prediction across unevenly distributed rating levels

## Claims

- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](../claims/e3sense-head-confined-engagement-prediction.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569
