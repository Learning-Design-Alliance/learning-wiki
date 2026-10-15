---
type: claim
title: Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction
description: Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction
id: deep-learning-models-comparable-accuracy-physiological-exam-prediction
status: draft
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

# Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r1` · `q2`

## Subclaims
`q2 i?` LSTM achieved a mean accuracy of 0.9299, GRU 0.9185, and the adapted transformer 0.9039, with the transformer performing comparably to the recurrent models. [→ Lala Yamazaki and Ramchandra Rimal 2026](#lala-yamazaki-and-ramchandra-rimal-2026)

## Evidence

### Lala Yamazaki and Ramchandra Rimal 2026

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960 [doi:10.48550/arxiv.2606.14960](https://doi.org/10.48550/arxiv.2606.14960)

`q2 · i?` · `associational · r1`

Test-set evaluation over 30 replicates of tuned deep learning models; the article reports GRU and LSTM "mean performance metrics of 0.92 and 0.93" and Table 5 prints accuracies of 0.9185 (GRU) and 0.9299 (LSTM).

> "The GRU and LSTM models yield reliable results, with mean performance metrics of 0.92 and 0.93, respectively, demonstrating excellent generalization to unseen data."

### Lala Yamazaki and Ramchandra Rimal 2026 (2)

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960

`q2 · i?` · `associational · r1`

Same comparative test evaluation; the article reports the transformer's "slightly lower mean metric of approximately 0.90" (Table 5: accuracy 0.9039 ± 0.0081), describing it as versatile on tabular data though slightly below GRU and LSTM.

> "The transformer model has a slightly lower mean metric of approximately 0.90, but it shows versatility by obtaining dependable performance in modeling the tabular data."

## Discussion


## Related Claims
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — reports the opposite
- [Pairwise statistical tests confirm random forest's performance differences from other models are statistically significant (p < 0.05)](statistical-tests-confirm-random-forest-superiority.md) — reports the opposite
- [Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction](logistic-regression-poor-svm-moderate-physiological-exam-prediction.md) — related
- [Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses](multivariate-features-improve-accuracy-over-eda-only-benchmark.md) — related
