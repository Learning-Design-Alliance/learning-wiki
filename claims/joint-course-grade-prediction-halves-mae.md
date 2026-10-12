---
type: claim
title: "Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only"
description: "Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only"
id: joint-course-grade-prediction-halves-mae
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A Transformer trained to predict both next-semester course sets and grades achieved MAE 0.1339 versus 0.2496 for a grades-only Transformer, a 46.4% reduction, on a held-out 10% test set. [→ Paul Savala 2026](#paul-savala-2026)

## Evidence

### Paul Savala 2026

Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409

`q2 · i?` · `design · r2`

Single-institution experiment training models on 5326 students across 18 semesters, testing on a held-out 10% of students. The results section reports that TRACE achieved a "mean absolute error of 0.1339, a 46.4% reduction" versus the grades-only variant, with MSE 3.5 times lower (0.0392 vs 0.1400).

> "The TRACE model achieved a mean absolute error of 0.1339, a 46.4% reduction compared to the ‘OnlyGradesTransformer‘’s MAE of 0.2496, and a mean squared error 3.5 times lower."

## Discussion


## Related Claims
- [Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction](course-prediction-metrics-auxiliary-task.md) — a broader claim this one bears on
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
- [Removing student major from the input marginally improves TRACE performance, suggesting major is recoverable from course history](major-ablation-no-predictive-signal.md) — related
