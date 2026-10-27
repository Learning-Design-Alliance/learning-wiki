---
type: claim
title: Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals
description: Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals
id: random-forest-highest-accuracy-physiological-exam-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: lala-yamazaki-and-ramchandra-rimal-2026
    resource: "https://doi.org/10.48550/arxiv.2606.14960"
    title: "Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960 [doi:10.48550/arxiv.2606.14960](https://doi.org/10.48550/arxiv.2606.14960)"
    author: Lala Yamazaki and Ramchandra Rimal
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The random forest model achieved the highest mean accuracy of 0.9590 with the smallest variability (0.0003) across 30 test replicates, outperforming all other models compared. [→ Lala Yamazaki and Ramchandra Rimal 2026](#lala-yamazaki-and-ramchandra-rimal-2026)

## Evidence

### Lala Yamazaki and Ramchandra Rimal 2026

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960 [doi:10.48550/arxiv.2606.14960](https://doi.org/10.48550/arxiv.2606.14960)

`q2 · i?` · `associational · r1`

Comparative evaluation of tuned machine learning models on a test set of 49,299 samples drawn from 328,655 processed observations; the article reports the random forest "achieves the highest mean metric of 0.96" across accuracy, precision, recall, and F1. Table 5 prints mean accuracy 0.9590 ± 0.0003 over 30 replicates.

> "the random forest model achieves the highest mean metric of 0.96, effectively modeling non-linear relationships and proving the best choice for this particular modeling problem."

## Discussion


## Related Claims
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — reports the opposite
- [Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction](logistic-regression-poor-svm-moderate-physiological-exam-prediction.md) — related
- [Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses](multivariate-features-improve-accuracy-over-eda-only-benchmark.md) — related
- [Pairwise statistical tests confirm random forest's performance differences from other models are statistically significant (p < 0.05)](statistical-tests-confirm-random-forest-superiority.md) — related
- [Random forest feature importance identifies EDA, ACC, and TEMP as the top three physiological predictors of exam outcomes](eda-acc-temp-top-three-predictors-exam-outcomes.md) — related
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — reports the opposite
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — reports the opposite
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](random-forest-slightly-better-for-answer-classification.md) — related
