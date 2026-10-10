---
type: claim
title: Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV
description: Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV
id: lms-traces-predict-ai-assisted-cheating-risk
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: akçapınar-2026
    resource: "https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    title: "Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    author: Akçapınar, G.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` LMS behaviors from the first eight weeks of the semester meaningfully predict students' risk of AI-assisted cheating in the final exam, with Logistic Regression achieving the best performance (Accuracy = 73.1%). [→ Akçapınar 2026](#akcapnar-2026)

## Evidence

### Akçapınar 2026

Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics

`q2 · i?` · `associational · r2`

LOOCV evaluation (52 folds, fold-specific preprocessing and Mann-Whitney U feature selection) of four classifiers on 27 candidate LMS features from 52 first-year undergraduates. "Logistic Regression achieved the highest AUC and Balanced Accuracy (0.763 and 0.718, respectively)"; raw Accuracy was 0.731 versus a majority-class baseline of 0.558.

> "Logistic Regression achieved the highest AUC and Balanced Accuracy (0.763 and 0.718, respectively). Naive Bayes produced a similar AUC of 0.760, whereas Random Forest and Gradient Boosting performed less well."

## Discussion


## Related Claims
- [Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity](cheating-risk-threshold-sensitivity-tradeoff.md) — related
- [High-risk students disproportionately scored 80 or above on the final exam (13 of 23), while no low-risk student did](high-risk-students-high-final-scores.md) — related
- [Simple classifiers (Logistic Regression, Naive Bayes) outperformed tree-based models on this small dataset](simple-classifiers-beat-tree-based-cheating-risk.md) — a narrower finding that bears on this claim
- [Course-module views, assignment submissions, and video-access days are the most stable predictors, all lower in the high-risk group (Cliff's delta values from 0.50 to 0.60)](stable-lms-features-lower-in-high-risk-group.md) — a narrower finding that bears on this claim
- [A 20% suspicious-question labeling threshold partitions 52 students into 23 high-risk (44.2%) and 29 low-risk, robustly across nearby cut-offs](bimodal-suspicious-behavior-labeling-44-percent-high-risk.md) — related
- [Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy](cross-semester-at-risk-prediction-high-accuracy.md) — related
- [Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining](cross-semester-auc-decline-without-retraining.md) — related
- [Logistic Regression and linear-kernel SVM achieve the highest accuracy (99%) among five classifiers predicting student withdrawal/cancellation at SISTC](lr-linear-svm-highest-accuracy-dropout-prediction.md) — related
