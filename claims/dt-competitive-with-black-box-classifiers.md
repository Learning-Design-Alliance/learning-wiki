---
type: claim
title: Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability
description: Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability
id: dt-competitive-with-black-box-classifiers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: vincent-zhang-2025
    resource: "https://doi.org/10.1007/s40593-025-00510-9"
    title: "Vincent Zhang, Bryn Jeffries, Irena Koprinska. (2025). A Machine Learning Approach for Predicting Student Progress in Online Programming Education. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00510-9"
    author: Vincent Zhang, Bryn Jeffries, Irena Koprinska
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LR, RF and SVM performed slightly better than DTs, with SVM best at 83.9-94.4% accuracy, but SVM and RF are black-box and SVM and LR were slow to train. [→ Vincent Zhang 2025](#vincent-zhang-2025)

## Evidence

### Vincent Zhang 2025

Vincent Zhang, Bryn Jeffries, Irena Koprinska. (2025). A Machine Learning Approach for Predicting Student Progress in Online Programming Education. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00510-9

`q2 · i?` · `associational · r2`

Comparison reported in the Results section across the same four-course module-level evaluation: DTs versus Logistic Regression, Random Forest and Support Vector Machine, all with Weka default settings. The article reports SVM "achieved 83.9-94.4 accuracy" while noting the interpretability and training-speed trade-off.

> "The machine learning methods used for comparison - LR, RF and SVM, performed slightly better than DTs, e.g. the best performing method SVM achieved 83.9-94.4 accuracy, 0.84-0.94 precision, 0.84-0.94 recall and 0.87-0.94 F1 score. These methods however lack interpretability, and SVM and LR were also slow to train which limits their applicability for our case study."

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — reports the opposite
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — reports the opposite
- [Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction](logistic-regression-poor-svm-moderate-physiological-exam-prediction.md) — related
- [Shallow machine learning with SMOTE oversampling and Qwen3 embeddings achieves the best overall reflection-classification performance (0.7176) on Hungarian essays](shallow-ml-best-overall-hungarian-reflection.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [AI systems relying on black-box models should not be used for high-stakes applications](black-box-ai-not-for-high-stakes-applications.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — reports the opposite
- [SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark](svm-regressors-outperformed-other-regressors.md) — related
- [CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance](feature-selection-reduces-tree-size-maintains-accuracy.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — reports the opposite
- [Machine learning models classify the three learning stages from EEG features with over 80% test accuracy, SVM highest at 82.6%](eeg-stage-classification-over-80.md) — related
- [Subcortical but not cortical activation-trajectory parameters classify BDNF genotype above chance in an exploratory decision-tree analysis](subcortical-trajectories-classify-bdnf-genotype.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
- [A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set](decision-tree-explanation-quality-f1-80.md) — related
- [The discourse personalization hint-selection model achieves the highest cross-validated accuracy (86.71%) and F1 (84.81%), significantly above all other models](discourse-personalization-hint-selection-best-cv.md) — related
- [SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time](smoteenn-denoising-higher-accuracy.md) — related
