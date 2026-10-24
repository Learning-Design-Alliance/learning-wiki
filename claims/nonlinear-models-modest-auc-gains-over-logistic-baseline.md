---
type: claim
title: Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline
description: Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline
id: nonlinear-models-modest-auc-gains-over-logistic-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ngoc-luyen-le-2026
    resource: "https://doi.org/10.48550/arxiv.2608.17618"
    title: "Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)"
    author: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the d-14 split, XGBoost and the TabTransformer-style model reach AUC 0.898, the MLP 0.895, and the BiLSTM 0.888, versus 0.884 for logistic regression. [→ Ngoc Luyen Le 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Le 2026

Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)

`q2 · i?` · `design · r2`

Supplementary offline checks on the same OULAD d-14 test split compare stronger nonlinear models against the logistic baseline. The article reports the printed AUC values and characterizes the gains as "modest relative to the calibrated logistic baseline", so logistic regression remains the reference predictor.

> "On thed−14split, XGBoost and the TabTransformer-style model reach an AUC of0.898, while the MLP reaches0.895and the BiLSTM0.888. These improvements remain modest relative to the calibrated logistic baseline."

## Discussion


## Related Claims
- [A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons](oulad-calibrated-logistic-regression-strong-prediction.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model](small-gain-from-question-level-features.md) — related
