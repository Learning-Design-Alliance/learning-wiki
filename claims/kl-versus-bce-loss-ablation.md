---
type: claim
title: "KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other"
description: "KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other"
id: kl-versus-bce-loss-ablation
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

# KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` An ablation comparing the KL-based set loss to binary cross-entropy for course prediction found grade prediction within 1-2% for both MAE and MSE. [→ Paul Savala 2026](#paul-savala-2026)

## Evidence

### Paul Savala 2026

Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409

`q2 · i?` · `design · r2`

Ablation study reported in the training section comparing the novel KL-divergence course-set loss against binary cross-entropy. The article notes "grade prediction within 1-2% of each other" and suggests BCE is a reasonable alternative, while arguing KL has learning-analytics-aligned benefits.

> "we ran an ablation study comparing the above loss function to binary cross entry for course prediction, and noted grade prediction within 1-2% of each other between the two models for both MAE and MSE."

## Discussion


## Related Claims
- [Jointly predicting courses and grades reduces grade-prediction MAE by 46.4% versus an identical Transformer that predicts grades only](joint-course-grade-prediction-halves-mae.md) — related
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
