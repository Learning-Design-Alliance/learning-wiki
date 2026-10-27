---
type: claim
title: An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy
description: An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy
id: lstm-strategy-temporal-analytics-outperforms-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2018
source_checked: 2026-10-20
recheck_by: 2021
sources:
  - id: akram-2018
    resource: "https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics"
    title: "Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J. (2018). Improving Stealth Assessment in Game-based Learning with LSTM-based Analytics. In Proceedings of the 11th International Conference on Educational Data Mining (EDM 2018). https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics"
    author: "Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The LSTM-based evidence model achieved higher predictive accuracy (64.82%) than random forest (50.43%), SVM (41.17%), and the majority-class baseline (35.71%) on held-out test data. [→ Akram 2018](#akram-2018)

## Evidence

### Akram 2018

Akram, B., Mott, B., Min, W., Boyer, K. E., Wiebe, E., & Lester, J. (2018). Improving Stealth Assessment in Game-based Learning with LSTM-based Analytics. In Proceedings of the 11th International Conference on Educational Data Mining (EDM 2018). https://scholar.google.com/scholar?q=Improving+Stealth+Assessment+in+Game-based+Learning+with+LSTM-based+Analytics

`q2 · i?` · `design · r2`

Computational evaluation on behavior trace data from 168 middle school students who completed both tests and all 11 binary tasks, with training/test split and 100 training runs averaged. The LSTM achieved "an average accuracy of 64.82%" versus RF 50.43%, SVM 41.17%, and baseline 35.71% (Table 2).

> "The results of applying this LSTM on the held -out test set achieve an average accuracy of 64.82%, an average precision of 63.88%, an average recall of 65.14%, and an F1-score of 63.68%."

## Discussion


## Related Claims

- [Adding in-game strategy features to pre-test features substantially improves LSTM-based stealth assessment accuracy](in-game-strategy-features-improve-prediction-over-pretest-only.md)
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — reports the opposite
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — reports the opposite
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — reports the opposite
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — reports the opposite
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — reports the opposite
- [Adding student attributes and autoregression improves prediction accuracy, with GP-α (τ = 1) reaching 0.711 accuracy and 0.757 F1.](attributes-autoregression-improve-response-prediction.md) — related
- [Unsupervised time-series clustering identifies low performers more accurately than SVM or decision-tree classifiers trained on two temporal statistics](unsupervised-clustering-beats-feature-classifiers.md) — related
- [On one graphical differentiation item, eye tracking data predicted students' specific difficulties as a multiclass classification problem](gaze-prediction-specific-math-difficulties-multiclass.md) — related
- [Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)](keystroke-classification-weak-auc.md) — related
- [Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82](random-forest-slightly-better-for-answer-classification.md) — related
