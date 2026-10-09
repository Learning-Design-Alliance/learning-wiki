---
type: claim
title: SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set
description: SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set
id: svm-rf-consistent-bias-classification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: josmario-albuquerque-2026
    resource: "https://doi.org/10.18608/jla.2026.8905"
    title: "Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905"
    author: Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the independent test set, SVM achieved an F1-score of 0.71 and RF 0.70 for bias classification, with SVM and the stacked model both reaching the highest accuracy (0.75). [→ Josmario Albuquerque 2026](#josmario-albuquerque-2026)

## Evidence

### Josmario Albuquerque 2026

Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905

`q2 · i?` · `design · r2`

Evaluation of fine-tuned classifiers on a held-out 20% test set (69 samples; 15 biased, 54 not biased) after training with SMOTE oversampling and stratified K-fold cross-validation; the table reports "the highest accuracy (0.75)" for STK and SVM.

> "the stacked model (STK) and the SVM model both achieved the highest accuracy (0.75), with similar performance in terms of F1-score (0.71 for SVM vs. 0.69 for STK). RF and XGB models also performed comparably, with F1-scores of 0.70 and 0.69, respectively."

## Discussion


## Related Claims
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set](naive-bayes-highest-precision-bias-detection.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
