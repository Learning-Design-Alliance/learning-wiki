---
type: claim
title: Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest
description: Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest
id: boosting-highest-accuracy-logistic-lowest
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: kubsch-2025
    resource: "https://doi.org/10.1007/s10648-025-10011-9"
    title: "Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N. (2025). Self-regulated Learning in the Digitally Enhanced Science Classroom: Toward an Early Warning System. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10011-9"
    author: "Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across most CAM-dimension combinations and timepoints, boosting showed the highest F1 and logistic regression the lowest, with decision trees ranking between them. [→ Kubsch 2025](#kubsch-2025)

## Evidence

### Kubsch 2025

Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N. (2025). Self-regulated Learning in the Digitally Enhanced Science Classroom: Toward an Early Warning System. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10011-9

`q2 · i?` · `associational · r2`

Hyperparameter search results (Fig. 3) comparing four model types: multinomial logistic regression, decision trees, XGBoost boosting, and a two-layer feed-forward neural network. Neural networks performed best when only affect and metacognition were considered.

> "The highest predictive accuracy (as measured by the F1 scores; other metrics (see online supplement S1) provide equivalent results) was observed in most combinations of CAM dimensions for boosting, while logistic regression exhibited the lowest predictive accuracy in nearly all cases."

## Discussion


## Related Claims
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — reports the opposite
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — reports the opposite
- [In an AI-based early warning system, the predictive importance of CAM dimensions shifted over an instructional unit, with affect/metacognition self-reports leading early and cognitive artifacts gaining accuracy toward the end](early-warning-system-cam-predictive-importance-shifts-over-unit.md) — related
