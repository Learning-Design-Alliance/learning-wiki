---
type: claim
title: "A linear support vector machine using 4 performance metrics classified skilled versus novice participants in a virtual reality brain tumor resection task with 92% accuracy, 100% sensitivity and 82% specificity"
description: "A linear support vector machine using 4 performance metrics classified skilled versus novice participants in a virtual reality brain tumor resection task with 92% accuracy, 100% sensitivity and 82% specificity"
id: svm-classifies-skilled-novice-vr-neurosurgery-92-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2020
source_checked: 2026-11-08
recheck_by: 2023
sources:
  - id: mirchi-n-2020
    resource: "https://doi.org/10.1371/journal.pone.0229596"
    title: "Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596"
    author: Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A linear support vector machine using 4 performance metrics classified skilled versus novice participants in a virtual reality brain tumor resection task with 92% accuracy, 100% sensitivity and 82% specificity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · checked against its sources 2026-11-08 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Leave-one-out cross-validated classification of skilled and novice participants achieved 92% accuracy with 100% sensitivity and 82% specificity. [→ Mirchi N 2020](#mirchi-n-2020)

## Evidence

### Mirchi N 2020

Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596

`q2 · i?` · `design · r2`

Framework validation study: 50 participants (28 skilled: staff neurosurgeons, fellows, PGY4-6 residents; 22 novice: junior residents and medical students) performed a subpial tumor resection on the NeuroVR simulator. "the leave-one-out cross-validation accuracy was 92% (sensitivity: 100%; specificity: 82%)". No skilled participant was misclassified; 4 novices were classified as skilled.

> "The metrics were normalized by calculating the z-scores and a support vector machine algorithm was trained using this data and the leave-one-out cross-validation accuracy was 92% (sensitivity: 100%; specificity: 82%)."

## Discussion


## Related Claims
- [Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%](eeg-stage-classification-over-80.md) — related
- [Functional connectivity among six task-difficulty-sensitive ROIs classifies HMA versus LMA individuals at 70.49% accuracy, with PI–MCC, HPC–precuneus and TPJ–NAc edges most diagnostic](functional-connectivity-classifies-math-anxiety.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
