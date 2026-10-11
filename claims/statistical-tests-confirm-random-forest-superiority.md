---
type: claim
title: "Pairwise statistical tests confirm random forest's performance differences from other models are statistically significant (p < 0.05)"
description: "Pairwise statistical tests confirm random forest's performance differences from other models are statistically significant (p < 0.05)"
id: statistical-tests-confirm-random-forest-superiority
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
---

# Pairwise statistical tests confirm random forest's performance differences from other models are statistically significant (p < 0.05)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Welch's t-tests and Mann–Whitney U tests on 30 independent runs produced p-values below 0.05 in all pairwise comparisons among GRU, LSTM, logistic regression, transformer, and random forest. [→ Lala Yamazaki and Ramchandra Rimal 2026](#lala-yamazaki-and-ramchandra-rimal-2026)

## Evidence

### Lala Yamazaki and Ramchandra Rimal 2026

Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960

`q2 · i?` · `associational · r1`

Statistical analysis of 30 independent test runs per model (SVM excluded for deterministic outputs); the article reports p-values "below the 0.05 significance level in all pairwise comparisons", supporting random forest's superiority. Normality was checked with the D'Agostino and Pearson omnibus test.

> "The t-tests and Mann–Whitney U tests produced p-values below the 0.05 significance level in all pairwise comparisons, confirming that the observed performance differences were statistically significant and not likely due to chance."

## Discussion


## Related Claims
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — reports the opposite
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
