---
type: claim
title: Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction
description: Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction
id: course-prediction-metrics-auxiliary-task
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the test set TRACE course prediction reached P=0.5076, R=0.4090, F1=0.4432, far above a random-selection precision of approximately 0.014. [→ Paul Savala 2026](#paul-savala-2026)

## Evidence

### Paul Savala 2026

Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409 [doi:10.48550/arxiv.2608.13409](https://doi.org/10.48550/arxiv.2608.13409)

`q2 · i?` · `design · r2`

Evaluation of the auxiliary course-prediction task on the held-out test set. The article reports "P= 0.5076,R= 0.4090,F1 = 0.4432" and notes random selection of 5 courses from the 360-course catalog would yield precision of approximately 0.014, indicating substantial predictive signal despite imperfect predictions.

> "we computed standard classification metrics for the TRACE model on the test set (P= 0.5076,R= 0.4090,F1 = 0.4432)."

## Discussion


## Related Claims
- [On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52](cased-challenge-methods-near-random-chance.md) — related
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — a narrower finding that bears on this claim
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
