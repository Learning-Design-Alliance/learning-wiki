---
type: claim
title: Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset
description: Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset
id: simple-classifiers-beat-tree-based-cheating-risk
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: akçapınar-2026
    resource: "https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    title: "Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    author: Akçapınar, G.
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Logistic Regression and Naive Bayes performed better than Random Forest and Gradient Boosting in this dataset, suggesting simple classifiers were competitive under small-sample conditions. [→ Akçapınar 2026](#akcapnar-2026)

## Evidence

### Akçapınar 2026

Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics

`q2 · i?` · `associational · r1`

Out-of-sample comparison of four classifiers (linear, probabilistic, bagging-based, boosting-based) under LOOCV in Table I. "Random Forest and Gradient Boosting performed less well" (AUC 0.720 and 0.646) than Logistic Regression (0.763) and Naive Bayes (0.760).

> "Logistic Regression achieved the highest AUC and Balanced Accuracy (0.763 and 0.718, respectively). Naive Bayes produced a similar AUC of 0.760, whereas Random Forest and Gradient Boosting performed less well."

## Discussion


## Related Claims
- [Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV](lms-traces-predict-ai-assisted-cheating-risk.md) — a broader claim this one bears on
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — reports the opposite
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set](naive-bayes-highest-precision-bias-detection.md) — related
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](college-offtrack-classified-90-percent-accuracy.md) — related
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — reports the opposite
- [Logistic Regression and linear-kernel SVM achieve the highest accuracy (99%) among five classifiers predicting student withdrawal/cancellation at SISTC](lr-linear-svm-highest-accuracy-dropout-prediction.md) — related
- [Question and observed-coverage features retrospectively predict high-divergence questions with AUC 0.774, but the model is not validated for new-query routing](retrospective-prediction-high-divergence-questions-auc-077.md) — related
