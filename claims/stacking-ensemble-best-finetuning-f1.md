---
type: claim
title: A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)
description: A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)
id: stacking-ensemble-best-finetuning-f1
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
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

# A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Among 120 evaluated stack configurations, the best-performing stack (LG, SVM, NB, KNN, XGB) achieved an F1-score of 0.88 during fine-tuning, exceeding SVM's second-highest 0.86. [→ Josmario Albuquerque 2026](#josmario-albuquerque-2026)

## Evidence

### Josmario Albuquerque 2026

Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905

`q2 · i?` · `design · r2`

Fine-tuning experiment evaluating 120 stacking combinations by F1-score during training/validation on the OER dataset; the stack "outperformed individual models such as SVM" at this stage, though on the test set STK's F1 was 0.69.

> "the best-performing stack achieved an F1-score of 0.88. This stack included LG, SVM, NB, KNN, and XGB models and outperformed individual models such as SVM, which achieved the second-highest F1-score of 0.86."

## Discussion


## Related Claims
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- [The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set](naive-bayes-highest-precision-bias-detection.md) — related
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — related
