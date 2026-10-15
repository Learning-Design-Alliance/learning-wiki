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
