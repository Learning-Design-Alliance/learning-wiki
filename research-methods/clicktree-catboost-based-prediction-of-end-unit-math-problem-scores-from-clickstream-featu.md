---
type: research-method
id: clicktree-catboost-based-prediction-of-end-unit-math-problem-scores-from-clickstream-featu
title: "ClickTree: CatBoost-based prediction of end-unit math problem scores from clickstream features"
description: ClickTree is a tree-based methodology that predicts whether a student successfully answers a problem in an end-unit math assignment from ASSISTments clickstream data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# ClickTree: CatBoost-based prediction of end-unit math problem scores from clickstream features

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
ClickTree is a tree-based methodology that predicts whether a student successfully answers a problem in an end-unit math assignment from ASSISTments clickstream data. It extracts features at assignment level (action counts), student level (action counts), in-unit average action counts, problem-level average action counts, a problem-weighted in-unit average, and problem-level performance, plus categorical features and the first 32 principal components of the Bert embedding of problem text. The CatBoost classifier, using Ordered Target Statistics to handle categorical features without target leakage, is trained on these features. The code is available at the authors' Kaggle notebook.

## Accounts
<!-- How each source describes or uses the method -->
- **ClickTree: a CatBoost-based method predicting end-unit math problem scores from multi-level clickstream features**: ClickTree is a tree-based methodology that predicts whether a student successfully answers a problem in an end-unit math assignment from ASSISTments clickstream data. It extracts features at assignment level (action counts), student level (action counts), in-unit average action counts, problem-level average action counts, a problem-weighted in-unit average, and problem-level performance, plus categorical features and the first 32 principal components of the Bert embedding of problem text. The CatBoost classifier, using Ordered Target Statistics to handle categorical features without target leakage, is trained on these features. The code is available at the authors' Kaggle notebook. (Rohani et al. (2024))

### Claims
- [The ClickTree method achieved an AUC of 0.78844 on test data and ranked second in the EDM Cup 2023.](../claims/clicktree-auc-078844-ranked-second-edmcup2023.md) [+M]
- [ClickTree with the CatBoost classifier achieved higher validation AUC than Random Forest, Decision Tree and Logistic Regression on the same features.](../claims/catboost-outperformed-rf-dt-lr-validation-auc.md) [+M]

## Related Research Methods
-

## Key Sources
- Rohani, N., Rohani, B., & Manataki, A. (2024). ClickTree: A Tree-based Method for Predicting Math Students' Performance Based on Clickstream Data. https://arxiv.org/abs/2403.14664. [doi:10.48550/arxiv.2403.14664](https://doi.org/10.48550/arxiv.2403.14664)
