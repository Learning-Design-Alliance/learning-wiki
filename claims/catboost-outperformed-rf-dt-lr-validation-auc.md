---
type: claim
title: ClickTree with the CatBoost classifier achieved higher validation AUC than Random Forest, Decision Tree and Logistic Regression on the same features.
description: ClickTree with the CatBoost classifier achieved higher validation AUC than Random Forest, Decision Tree and Logistic Regression on the same features.
id: catboost-outperformed-rf-dt-lr-validation-auc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: rohani-2024
    resource: "https://doi.org/10.48550/arXiv.2403.14664"
    title: "Rohani, N., Rohani, B., & Manataki, A. (2024). ClickTree: A Tree-based Method for Predicting Math Students' Performance Based on Clickstream Data. [doi:10.48550/arXiv.2403.14664](https://doi.org/10.48550/arXiv.2403.14664)"
    author: "Rohani, N., Rohani, B., & Manataki, A."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# ClickTree with the CatBoost classifier achieved higher validation AUC than Random Forest, Decision Tree and Logistic Regression on the same features.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On validation data, ClickTree (CatBoost) reached 80% AUC versus 76% for Random Forest, 74% for Decision Tree and 69% for Logistic Regression. [→ Rohani 2024](#rohani-2024)

## Evidence

### Rohani 2024

Rohani, N., Rohani, B., & Manataki, A. (2024). ClickTree: A Tree-based Method for Predicting Math Students' Performance Based on Clickstream Data. [doi:10.48550/arXiv.2403.14664](https://doi.org/10.48550/arXiv.2403.14664)

`q2 · i?` · `associational · r2`

Comparison of classification methods applied to the same extracted clickstream features, reported in the results section. The article states ClickTree "achieved an AUC of 80% on the validation data" while the three alternatives reached 76%, 74% and 69%; the authors attribute the advantage to CatBoost handling categorical features.

> "The ClickTree method achieved an AUC of 80% on the validation data, while Random Forest, Decision Tree, and Logistic Regression achieved AUC values of 76%, 74%, and 69%, respectively."

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest](catboost-best-f1-programme-completion.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
- [Random Forest is the best-performing classification model for predicting postgraduate public health students' CGPA category, with 71.43% accuracy and AUC 0.87](random-forest-best-classifier-ap.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [The ClickTree method achieved an AUC of 0.78844 on test data and ranked second in the EDM Cup 2023.](clicktree-auc-078844-ranked-second-edmcup2023.md) — related
