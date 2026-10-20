---
type: claim
title: TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction
description: TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction
id: trace-outperforms-lstm-gnn-xgboost
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: paul-savala-2026
    resource: "https://doi.org/10.48550/arxiv.2608.13409"
    title: "Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409 [doi:10.48550/arxiv.2608.13409](https://doi.org/10.48550/arxiv.2608.13409)"
    author: Paul Savala
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` TRACE achieved MSE approximately 30% lower and MAE approximately 15% lower than two LSTM models, MSE/MAE 15%-20% lower than a GNN, and drastically outperformed XGBoost. [→ Paul Savala 2026](#paul-savala-2026)

## Evidence

### Paul Savala 2026

Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409 [doi:10.48550/arxiv.2608.13409](https://doi.org/10.48550/arxiv.2608.13409)

`q2 · i?` · `design · r2`

Comparison experiment on the same institutional dataset (Table 1: TRACE MSE 0.0392/MAE 0.1339; EncDecLSTM 0.0530/0.1608; UniLSTM 0.0544/0.1619; GNN 0.0495/0.1640; XGBoost 1.3317/0.8818). The text reports "a MSE approximately 30% lower than the LSTM models".

> "Compared to the two LSTM models, the Transformer model shows a significant improvement, with a MSE approximately 30% lower than the LSTM models, and a MAE approximately 15% lower."

## Discussion


## Related Claims
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — related
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
- [Removing student major from the input marginally improves TRACE performance, suggesting major is recoverable from course history](major-ablation-no-predictive-signal.md) — related
- LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains — related
- [Feature-based ML models reduce next-week forecasting MAE by 22-33% over heuristic baselines for weekly minutes practiced and new skills mastered](ml-outperforms-heuristics-week-ahead-engagement-forecasting.md) — related
- [The DMO-GRU model achieves the best classification results among the compared models, with 91.2% accuracy, 90.8% F1-score, 90.1% precision and 92.5% recall](dmo-gru-best-classification-results.md) — related
- [DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success](dmo-gru-lowest-regression-error-highest-r2.md) — related
- [On the ASSISTments real-world benchmark, the proposed method achieves the best performance across all metrics, significantly outperforming all baselines](assistments-real-world-best-all-metrics.md) — related
- Replacing the transformer with a single-layer 2048-unit LSTM drops the average score by 5.6, with the LSTM winning only on MRPC — related
- [Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction](course-prediction-metrics-auxiliary-task.md) — related
