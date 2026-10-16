---
type: claim
title: Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction
description: Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction
id: logistic-regression-poor-svm-moderate-physiological-exam-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lala-yamazaki-and-ramchandra-rimal-2026
    resource: "https://doi.org/10.48550/arxiv.2606.14960"
    title: "Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960 [doi:10.48550/arxiv.2606.14960](https://doi.org/10.48550/arxiv.2606.14960)"
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

# Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r1` · `q2`

## Subclaims
`q2 i?` Logistic regression exhibited the lowest mean accuracy (0.4243) of all models, struggling with the dataset's non-linear and multivariate complexity. [→ Lala Yamazaki and Ramchandra Rimal 2026](#lala-yamazaki-and-ramchandra-rimal-2026)
`q2 i?` SVM achieved moderate mean accuracy of 0.7374 on the same task. [→ Lala Yamazaki and Ramchandra Rimal 2026 (2)](#lala-yamazaki-and-ramchandra-rimal-2026-2)

## Evidence

### Lala Yamazaki and Ramchandra Rimal 2026

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960 [doi:10.48550/arxiv.2606.14960](https://doi.org/10.48550/arxiv.2606.14960)

`q2 · i?` · `associational · r1`

Test-set comparison of tuned models; the article reports logistic regression "demonstrates the lowest performance with mean metrics below 0.42" (Table 5: accuracy 0.4243 ± 0.0000), attributing this to inability to capture complex interactions.

> "Logistic regression demonstrates the lowest performance with mean metrics below 0.42, making it ill-suited for handling the dataset's complexity."

### Lala Yamazaki and Ramchandra Rimal 2026 (2)

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960

`q2 · i?` · `associational · r1`

Same test-set comparison; the article reports SVM "exhibit moderate performance with mean metrics around 0.74" (Table 5: accuracy 0.7374 ± 0.0000, deterministic across runs).

> "Meanwhile, SVM exhibit moderate performance with mean metrics around 0.74."

## Discussion


## Related Claims
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — related
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — reports the opposite
- Logistic Regression and linear-kernel SVM achieve the highest accuracy (99%) among five classifiers predicting student withdrawal/cancellation at SISTC — related
- [Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses](multivariate-features-improve-accuracy-over-eda-only-benchmark.md) — related
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
