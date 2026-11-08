---
type: strategy
id: quantified-explainable-feedback-strategy-surgical-training
title: Provide trainees with quantified, explainable feedback (estimated GOALS scores and SHAP-derived comments) rather than raw metrics or opaque tier labels
description: "The article's questionnaire results support delivering automated feedback that is quantitative and explained: estimated GOALS scores and SHAP-based comments were rated most helpful, while \"three-tier classification an..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: ebina-koki-2025
    resource: "https://doi.org/10.1007/s00464-025-12018-3"
    title: "Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo. (2025). External validation of a motion capture-based surgical skill assessment system in laparoscopic simulation training environments. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12018-3"
    author: Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo
---

# Provide trainees with quantified, explainable feedback (estimated GOALS scores and SHAP-derived comments) rather than raw metrics or opaque tier labels

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 design), `q2`–`q3` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article's questionnaire results support delivering automated feedback that is quantitative and explained: estimated GOALS scores and SHAP-based comments were rated most helpful, while "three-tier classification and raw metrics values were deemed less instructive by participants". The authors intend to use participant feedback to revise the feedback contents to be more user-friendly, and suggest GOALS-based evaluation alone may be more appropriate for future training.

## Design Implications

### Context
#### Requirements
- An ML model predicting a quantified skill score, plus an explainable-AI layer (SHAP) linking motion metrics to the prediction
#### Constraints
- Educational effects and operating-room transfer of the feedback were not verified in this study
- Psychological acceptability of AI-based rather than surgeon-based evaluation remains to be investigated

### Target Learners
- Surgical trainees in simulation-based laparoscopic training

### Target Learning Goals
- Technical skill development through objective, understandable performance feedback

## Claims

- [Most trainees found the automated SHAP-based feedback easy to understand and were satisfied with the assessment, with GOALS scores rated most informative](../claims/automated-feedback-acceptability-questionnaire.md) [+W]
- [Three-tier classification frequently misclassifies intermediate surgeons, suggesting procedural caseload is a limited surrogate for skill in simulation training](../claims/intermediate-tier-misclassification-caseload-limitation.md) [+W]
- [The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors](../claims/mocap-goals-prediction-correlation-mae.md) [+W]
- [A motion-capture ML three-tier classification model classifies laparoscopic experience with 67.3% accuracy on a dissection task and 56.9% on a suturing task in external validation](../claims/mocap-three-tier-classification-external-validation-accuracy.md) [+W]
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](../claims/feature-importance-spread-across-many-features.md) [+W]

## Related Strategies

- [Deliver formative feedback on quantifiable, AI-derived performance metrics with actionable goals during surgical simulation practice](metric-based-formative-feedback-strategy.md)

## Examples
-

## Key Sources
- Ebina Koki, Abe Takashige, Hotta Kiyohiko, Lingbo Yan, Kamijo Chihiro, Higuchi Madoka, Kon Masafumi, Kikuchi Hiroshi, Miyata Haruka, Matsumoto Ryuji, Osawa Takahiro, Murai Sachiyo, Senoo Taku, Komizunai Shunsuke, Tsujita Teppei, Sase Kazuya, Chen Xiaoshuai, Konno Atsushi, Shinohara Nobuo. (2025). External validation of a motion capture-based surgical skill assessment system in laparoscopic simulation training environments. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12018-3
