---
type: claim
title: Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD
description: Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD
id: ip-recourse-compact-plans-at-scale
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Full-scale IP evaluation produces 127,972 scored plans with model validity and SHACL conformance both at 1.0, a mean of 1.075 actions, and mean total cost 10.357. [→ Ngoc Luyen Le 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Le 2026

Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)

`q2 · i?` · `design · r2`

Offline full-scale IP recourse evaluation on OULAD test instances, with 127,972 plans scored offline. Model validity and SHACL conformance both reach 1.0, and the article states the generated plans "are also compact, with an average of1.075 actions".

> "The main full-scale integer-programming evaluation pro- duces127,972scored plans. Table III summarizes the results. Both model validity and SHACL conformance reach1.0. The generated plans are also compact, with an average of1.075 actions and a mean total cost of10.357."

## Discussion


## Related Claims
- [Activating availability constraints in the IP pipeline lowers SHACL conformance to 0.875 without reducing optimization cost, exposing infeasible plans](semantic-validation-exposes-infeasible-plans.md) — related
- [A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons](oulad-calibrated-logistic-regression-strong-prediction.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [The baseline and capacitated facility location formulations of school aggregation are formally equivalent](equivalent-school-aggregation-formulations.md) — related
