---
type: claim
title: The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set
description: The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set
id: naive-bayes-highest-precision-bias-detection
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

# The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Among the evaluated classifiers, naive Bayes demonstrated the highest precision (0.75 on the test set), making it suitable when precision in bias detection is prioritized. [→ Josmario Albuquerque 2026](#josmario-albuquerque-2026)

## Evidence

### Josmario Albuquerque 2026

Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905

`q2 · i?` · `design · r2`

Test-set evaluation of fine-tuned models on the 69-sample held-out portion of the OER dataset; the results section reports that naive Bayes "demonstrated the highest precision (0.75 on the test set)", though its overall accuracy was low (0.49 per Table 8).

> "In contrast, the naive Bayes (NB) model demonstrated the highest precision (0.75 on the test set)."

## Discussion


## Related Claims
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
