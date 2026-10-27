---
type: claim
title: Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models
description: Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models
id: mmla-k8-random-forest-best-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
newest_evidence: 2025
source_checked: 2026-10-20
recheck_by: 2028
sources:
  - id: caskurlu-2025
    resource: "https://doi.org/10.18608/jla.2025.8505"
    title: "Caskurlu, S., Ocak, C., & Dai, C.-P. (2025). The Scope of Multimodal Learning Analytics in K–8: A Systematic Review. Journal of Learning Analytics, 12(2), 224–236. https://doi.org/10.18608/jla.2025.8505"
    author: "Caskurlu, S., Ocak, C., & Dai, C.-P."
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In studies comparing classifiers, random forest was chosen for best performance, including detecting guessing behaviours with motion features. [→ Caskurlu 2025](#caskurlu-2025)

## Evidence

### Caskurlu 2025

Caskurlu, S., Ocak, C., & Dai, C.-P. (2025). The Scope of Multimodal Learning Analytics in K–8: A Systematic Review. Journal of Learning Analytics, 12(2), 224–236. https://doi.org/10.18608/jla.2025.8505

`q2 · i?` · `review · r2`

The review reports that Shin et al. (2020) compared logistic regression, support vector machine, decision tree, and random forests with baseline classifiers using synthetic minority over-sampling. Similarly, in Moon et al. (2022), after testing kNN, random forest, decision tree, and logistic regression, "random forest was chosen as a classification model because it resulted in the best performance."

> "Their results showed th at random for est yielded the best performance in detecting guessing behavio urs with motion features."

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — reports the opposite
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — a narrower finding that bears on this claim
- Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021 — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — reports the opposite
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — reports the opposite
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — a narrower finding that bears on this claim
- A Random Forest classifier reached 89.09% test accuracy with 0.89 macro F1 across three stress-severity levels, exceeding an SVM comparison (88.48%) and a reported Random Forest benchmark (87.93%) on similar data — a narrower finding that bears on this claim
- [On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52](cased-challenge-methods-near-random-chance.md) — related
- In a student project on laser-drilled hole diameter detection, GPR significantly outperformed MLP in detection accuracy and training speed — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — reports the opposite
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy](cross-semester-at-risk-prediction-high-accuracy.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — reports the opposite
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](college-offtrack-classified-90-percent-accuracy.md) — related
- [Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot](random-forest-survey-pilot-f1-0924.md) — a narrower finding that bears on this claim
- [Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining](cross-semester-auc-decline-without-retraining.md) — related
- [Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.](attributes-autoregression-improve-response-prediction.md) — related
- [Machine-learning classifiers predict full student response to teacher communication in autism classrooms above random and major-class baselines.](ml-predicts-student-response-autism-communication.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
- [Eye tracking data can predict specific student difficulties in graphical differentiation tasks as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](random-forest-slightly-better-for-answer-classification.md) — related
