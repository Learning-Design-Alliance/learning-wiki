---
type: claim
title: "Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses"
description: "Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses"
id: multivariate-features-improve-accuracy-over-eda-only-benchmark
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lala-yamazaki-and-ramchandra-rimal-2026
    resource: "https://arxiv.org/abs/2606.14960"
    title: "Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960"
    author: Lala Yamazaki and Ramchandra Rimal
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: lala-yamazaki-and-ramchandra-rimal-2026-2
    resource: "https://arxiv.org/abs/2606.14960"
    title: "Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960"
    author: Lala Yamazaki and Ramchandra Rimal
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`

## Subclaims
`q2 i?` Prior work using nine engineered EDA-only features reached a maximum accuracy of 80% for the final exam; this study reports obtaining superior results with 96% accuracy by using all useful collected features. [→ Lala Yamazaki and Ramchandra Rimal 2026](#lala-yamazaki-and-ramchandra-rimal-2026)
`q2 i?` The study's stated initiatives include obtaining superior results with 96% accuracy over the prior 80%. [→ Lala Yamazaki and Ramchandra Rimal 2026 (2)](#lala-yamazaki-and-ramchandra-rimal-2026-2)

## Evidence

### Lala Yamazaki and Ramchandra Rimal 2026

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960

`q2 · i?` · `associational · r1`

The article describes the benchmark Wearable Exam Stress Dataset analyses, which used only skin electrical conductance from EDA; the review of prior work reports those studies "achieving a maximum accuracy of 80% for the final exam".

> "Nine engineered features derived from EDA were then used as input features to predict exam grades, achieving a maximum accuracy of 80% for the final exam [11]."

### Lala Yamazaki and Ramchandra Rimal 2026 (2)

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960

`q2 · i?` · `associational · r1`

The article's introduction lists its research initiatives, including "obtaining superior results with 96% accuracy over 80% previously" by leveraging the full multivariate recordings rather than EDA alone.

> "(f) obtaining superior results with 96% accuracy over 80% previously."

## Discussion


## Related Claims
- [Random forest feature importance identifies EDA, ACC, and TEMP as the top three physiological predictors of exam outcomes](eda-acc-temp-top-three-predictors-exam-outcomes.md) — related
- [Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction](logistic-regression-poor-svm-moderate-physiological-exam-prediction.md) — related
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — related
