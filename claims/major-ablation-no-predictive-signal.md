---
type: claim
title: Removing student major from the input marginally improves TRACE performance, suggesting major is recoverable from course history
description: Removing student major from the input marginally improves TRACE performance, suggesting major is recoverable from course history
id: major-ablation-no-predictive-signal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: paul-savala-2026
    resource: "https://arxiv.org/abs/2608.13409"
    title: "Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409"
    author: Paul Savala
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing student major from the input marginally improves TRACE performance, suggesting major is recoverable from course history

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A TRACE variant with major removed achieved MSE 0.0360 vs 0.0392 and MAE 0.1327 vs 0.1339, marginally better than the full model. [→ Paul Savala 2026](#paul-savala-2026)

## Evidence

### Paul Savala 2026

Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409

`q2 · i?` · `design · r2`

Feature-ablation analysis in which a TRACE variant was trained with student major removed from the input. The article reports "marginally improved performance" and interprets major as largely recoverable from early course selections, adding redundancy and overfitting risk.

> "This ablation resulted in marginally improved performance (MSE: 0.0360 vs. 0.0392; MAE: 0.1327 vs. 0.1339), suggesting that major provides no additional predictive signal beyond course history and may introduce slight redundancy."

## Discussion


## Related Claims
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — related
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
