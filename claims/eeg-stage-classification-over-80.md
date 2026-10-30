---
type: claim
title: "Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%"
description: "Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%"
id: eeg-stage-classification-over-80
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-26
recheck_by: 2028
sources:
  - id: hui-xie-2025
    resource: "https://doi.org/10.1038/s41539-025-00376-5"
    title: "Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen. (2025). EEG analysis of brain dynamics in a simulated multi-task and multi-stage learning environment. npj Science of Learning. https://doi.org/10.1038/s41539-025-00376-5"
    author: "Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-26 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SVM and neural network models classified the three learning stages with testing accuracies of 82.6% and 81.8% from 84 EEG features. [→ Hui Xie 2025](#hui-xie-2025)

## Evidence

### Hui Xie 2025

Hui Xie, Chunli Jia, Yanxia Luo, Jiangshan He, Zexiao Dong, Dan Liang, Ziqi Ren, Mingzhe Jiang, Xinbo Gao & Xueli Chen. (2025). EEG analysis of brain dynamics in a simulated multi-task and multi-stage learning environment. npj Science of Learning. https://doi.org/10.1038/s41539-025-00376-5

`q2 · i?` · `associational · r1`

Classification of learning stage from 10-s EEG segments (84 relative-PSD features, 14 channels, six bands; 7,544 samples), trained in MATLAB with 10-fold cross-validation. Five models were compared; KNN reached 80.4% test accuracy.

> "The two models with better classification results are the support vector machine (SVM) and neural network (NN) models, with testing accuracies of 82.6% and 81.8%."

## Discussion


## Related Claims
- [EEG average amplitude differs significantly across learning stages within each task, and across tasks at Stages 1 and 3, during a semester-long course](eeg-amplitude-stage-task-differences.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Relative PSD shows stage- and task-specific band patterns, including higher high-beta in Stage 3 of labs and quizzes](relative-psd-band-stage-patterns.md) — related
- [On one graphical differentiation item, eye tracking data predicted students' specific difficulties as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](roberta-svm-most-accurate-scoring-pisa.md) — related
