---
type: claim
title: Elastic net logistic regression performs comparably to random forest and gradient boosting in predicting first-round Physics Olympiad success and is selected as the final model
description: Elastic net logistic regression performs comparably to random forest and gradient boosting in predicting first-round Physics Olympiad success and is selected as the final model
id: elastic-net-comparable-performance-olympiad-success
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tschisgale-2026
    resource: "https://doi.org/10.48550/arXiv.2609.35151"
    title: "Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)"
    author: "Tschisgale, P., & Neumann, K."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Elastic net logistic regression performs comparably to random forest and gradient boosting in predicting first-round Physics Olympiad success and is selected as the final model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 50 outer cross-validation folds, the elastic net (Brier 0.237, AUC 0.605) performed near-equivalently to the random forest and gradient boosting models, and was selected for parsimony. [→ Tschisgale 2026](#tschisgale-2026)

## Evidence

### Tschisgale 2026

Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)

`q2 · i?` · `associational · r1`

A model-comparison analysis trained three supervised classifiers (elastic net, random forest, gradient boosting) via 10-times repeated stratified 5-fold nested cross-validation on 282 participants, optimizing the Brier score. The article reports the elastic net was selected "due to its greater parsimony as a simple linear classifier"; Table 2 shows Brier 0.237, AUC 0.605, Cohen’s κ 0.177.

> "Given the near-equivalent performance of all three models, the elastic net was selected as the final model due to its greater parsimony as a simple linear classifier."

## Discussion


## Related Claims
- [Applying the model at a high-confidence threshold identifies 43 non-participants (3.9%) as potentially successful in the Physics Olympiad](43-potentially-successful-non-participants.md) — related
- [Mathematics skills are the dominant positive predictor of first-round success, while conventional vocational interests negatively predict success](shap-predictors-olympiad-success.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
