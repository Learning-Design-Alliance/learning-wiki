---
type: claim
title: XGBoost slightly outperformed a logistic regression baseline in predicting ChatGPT assignment use
description: XGBoost slightly outperformed a logistic regression baseline in predicting ChatGPT assignment use
id: xgboost-slightly-outperforms-logistic-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: surajit-das-and-aleksei-eliseev-2025
    resource: "https://doi.org/10.48550/arXiv.2508.12013"
    title: "Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)"
    author: Surajit Das and Aleksei Eliseev
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# XGBoost slightly outperformed a logistic regression baseline in predicting ChatGPT assignment use

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the same preprocessed dataset and train-test split, the Logistic Regression baseline achieved an accuracy and F1-score of 79%, slightly below the performance of XGBoost. [→ Surajit Das and Aleksei Eliseev 2025](#surajit-das-and-aleksei-eliseev-2025)

## Evidence

### Surajit Das and Aleksei Eliseev 2025

Surajit Das and Aleksei Eliseev. (2025). Predicting ChatGPT Use in Assignments: Implications for AI-Aware Assessment Design. arXiv preprint. [doi:10.48550/arXiv.2508.12013](https://doi.org/10.48550/arXiv.2508.12013)

`q2 · i?` · `associational · r1`

Baseline comparison run on the same preprocessed dataset and train-test split as the XGBoost model. The article reports the Logistic Regression model 'achieved an accuracy and F1-score of 79%, slightly below the performance of XGBoost'.

> "The Logistic Regression model achieved an accuracy and F1-score of 79%, slightly below the performance of XGBoost."

## Discussion


## Related Claims
- [An XGBoost binary classifier predicts self-reported ChatGPT use in academic assignments with 80.1% test accuracy](xgboost-binary-predicts-chatgpt-assignment-use.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91](xgboost-logreg-highest-f1-midterm-risk-prediction.md) — related
