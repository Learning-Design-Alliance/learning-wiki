---
type: claim
title: A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts
description: A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts
id: svm-outperforms-dt-rf-cognitive-engagement-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: gorgun-2022
    resource: "https://doi.org/10.5281/zenodo.6853149"
    title: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149"
    author: "Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The SVM classifier achieved 71% accuracy (K = .61) on the full prediction task and significantly outperformed both the decision tree and random forest classifiers. [→ Gorgun 2022](#gorgun-2022)

## Evidence

### Gorgun 2022

Gorgun, G., Yildirim-Erbasli, S. N., & Demmans Epp, C. (2022). Predicting cognitive engagement in online course discussion forums. Proceedings of the 15th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.6853149

`q2 · i?` · `design · r2`

Test-set evaluation of three classifiers trained on 104 Coh-Metrix indicators plus three contextual features, using 10-fold cross-validation with accuracy, precision, recall, F1, and Cohen's Kappa. The SVM reached "substantial agreement between the predicted and human-assigned labels" with K = .61.

> "The support vector machine classifier outperformed both the decision tree (McNemar'sχ2 = 61.31, p< .001) and the random forest (McNemar'sχ2 = 19.04, p< .001) models on the full prediction task. The SVM model's Kappa value (.61) suggested substantial agreement between the predicted and human-assigned labels"

## Discussion


## Related Claims

- [Classifiers systematically confuse adjacent engagement levels: social with active, constructive with interactive, and interactive with active](adjacent-engagement-level-misclassification-patterns.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Discipline-general academic vocabulary (AWL use) supports cognitive engagement identification and may aid generalization across courses](awl-academic-vocabulary-supports-engagement-identification.md)
- [Cohen's kappa exhibits a paradox in which high observed agreement yields low kappa, making it unsuitable for pass/fail decision consistency](cohens-kappa-paradox-decision-consistency.md) — related
- [Scientists have imposed their values of precision, objectivity, and control on language, including attempts to build machines that use and create language as humans do](science-values-imposed-on-language.md) — a broader claim this one bears on
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021 — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [Conflict with a machine-learning decision support system's output induces deeper reflection than confirmation](conflict-seed-induces-deeper-reflection.md) — related
- [Agent-generated descriptions significantly improve prediction of student dropout in a lesson, outperforming all other measured approaches](agent-descriptions-improve-dropout-prediction.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — reports the opposite
- [SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark](svm-regressors-outperformed-other-regressors.md) — related
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%](eeg-stage-classification-over-80.md) — related
- [On one graphical differentiation item, eye tracking data predicted students' specific difficulties as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
