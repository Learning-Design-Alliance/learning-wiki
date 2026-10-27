---
type: claim
title: A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)
description: A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)
id: random-forest-best-auc-flagged-problems
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-19
recheck_by: 2028
sources:
  - id: kole-norberg-2025
    resource: "https://doi.org/10.5281/zenodo.15870274"
    title: "Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274"
    author: Kole Norberg, Husni Almoubayyed, and Stephen Fancsali
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-19 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the hold-out test set, the random forest (AUC 0.75, accuracy 0.70) outperformed elastic net, XGBoost, SVM, and neural network models. [→ Kole Norberg 2025](#kole-norberg-2025)

## Evidence

### Kole Norberg 2025

Kole Norberg, Husni Almoubayyed, and Stephen Fancsali. (2025). Linguistic Features Predicting Math Word Problem Readability Among Less-Skilled Readers. Proceedings of the 18th International Conference on Educational Data Mining, Palermo, Italy. https://doi.org/10.5281/zenodo.15870274

`q2 · i?` · `associational · r2`

Model comparison on a 20% scenario-held-out test set, with 3-fold cross-validation for training. Table 1 prints Random Forest AUC 0.75, accuracy 0.70, versus Elastic Net 0.65, XGBoost 0.62, SVM 0.69, Neural Net 0.65. No effect size is printed.

> "Fit statistics for each model are provided in Table 1. The random forest had the best overall performance on the hold out test set."

## Discussion


## Related Claims
- [Flagged word problems were shorter (lower word count) but had more sentences than non-flagged problems in descriptive statistics](flagged-problems-shorter-more-sentences-descriptives.md) — related
- [4,446 of 9,421 MATHia word problems showed larger-than-expected error-rate gaps between less- and more-skilled readers and were flagged for potential readability concerns](mathia-word-problems-flagged-reading-gaps.md) — related
- [Partial dependence plots showed higher word count, more dependent clauses, and higher custom magnitude raised predicted flag probability, with non-linear relationships](partial-dependence-nonlinear-relationships.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Three word embedding methods and three classifiers were introduced to predict item quality for accessible math assessments](word-embedding-classifiers-predict-item-quality-vi.md) — a broader claim this one bears on
- Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021 — related
- Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96 — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset — reports the opposite
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
- [Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing](retrospective-prediction-high-divergence-questions-auc-077.md) — related
- [On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52](cased-challenge-methods-near-random-chance.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — reports the opposite
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Rewriting MATHia word problems for struggling readers, by human experts or LLMs, sped completion by 30% and improved mastery rate](rewritten-word-problems-faster-completion-mastery.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — reports the opposite
- [SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark](svm-regressors-outperformed-other-regressors.md) — related
- [PPB maintained comparable readability on three of four measures while increasing Flesch-Kincaid toward grade level](ppb-readability-comparable-flesch-kincaid-increased.md) — related
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](svm-rf-consistent-bias-classification.md) — related
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot](random-forest-survey-pilot-f1-0924.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
- [Eye tracking data can predict specific student difficulties in graphical differentiation tasks as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
