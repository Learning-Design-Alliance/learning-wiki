---
type: claim
title: DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success
description: DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success
id: dmo-gru-lowest-regression-error-highest-r2
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: li-c-2025
    resource: "https://doi.org/10.1007/s44163-025-00401-x"
    title: "Li C, Yin W. (2025). Interactive online learning method for students based on artificial intelligence. Discover Artificial Intelligence 5:201. https://doi.org/10.1007/s44163-025-00401-x"
    author: Li C, Yin W.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` DMO-GRU minimizes prediction errors better than the compared models and has the highest R2 score, indicating it accounts for a greater amount of variance in student performance outcomes. [→ Li C 2025](#li-c-2025)

## Evidence

### Li C 2025

Li C, Yin W. (2025). Interactive online learning method for students based on artificial intelligence. Discover Artificial Intelligence 5:201. https://doi.org/10.1007/s44163-025-00401-x

`q2 · i?` · `design · r2`

Regression comparison across Linear Regression, Random Forest, SVR, XGBoost and DMO-GRU (Table 3, Fig. 9) shows DMO-GRU with "lower MAE and RMSE values" (2.70 and 3.40) and the highest R2 score (0.92), versus XGBoost at 3.50, 4.70 and 0.87.

> "DMO-GRU has a better ability to minimize prediction mistakes, as evidenced by its lower MAE and RMSE values."

## Discussion


## Related Claims
- [The DMO-GRU model achieves the best classification results among the compared models, with 91.2% accuracy, 90.8% F1-score, 90.1% precision and 92.5% recall](dmo-gru-best-classification-results.md) — related
- [DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM](dmo-gru-faster-training-time.md) — related
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
