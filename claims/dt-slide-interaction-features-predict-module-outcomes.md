---
type: claim
title: Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses
description: Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses
id: dt-slide-interaction-features-predict-module-outcomes
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

# Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` DTs with and without feature selection achieved 85.2-90.7% accuracy, 0.88-0.92 precision, 0.78-0.98 recall and 0.83-0.92 F1 across all four courses, considerably surpassing the majority-class baseline. [→ Vincent Zhang 2025](#vincent-zhang-2025)

## Evidence

### Vincent Zhang 2025

Vincent Zhang, Bryn Jeffries, Irena Koprinska. (2025). A Machine Learning Approach for Predicting Student Progress in Online Programming Education. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00510-9

`q2 · i?` · `associational · r2`

Evaluation on log data from four large-scale online programming courses (approximately 35,000 enrolled students), with a separate DT model per module and 10-fold stratified cross-validation. The article reports "85.2-90.7% accuracy" for DTs with and without feature selection, all surpassing the majority-class baseline.

> "The DTs with and without feature selection show consistently high predictive performance on all courses - 85.2-90.7% accuracy, precision of 0.88-0.92 precision, 0.78-0.98 recall and 0.83-0.92 F1 score. All DTs considerably surpass the majority class baseline."

## Discussion


## Related Claims
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance](feature-selection-reduces-tree-size-maintains-accuracy.md) — related
- [Completion of prior problem slides is the most critical predictor of completing a module's final exercise, consistent with the doer effect](problem-slide-completion-top-predictor-doer-effect.md) — a narrower finding that bears on this claim
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
