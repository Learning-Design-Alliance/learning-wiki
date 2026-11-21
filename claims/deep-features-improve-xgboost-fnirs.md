---
type: claim
title: XGBoost accuracy improves when trained on deep-learned representations, with CNN-GRU features yielding the highest XGBoost accuracy
description: XGBoost accuracy improves when trained on deep-learned representations, with CNN-GRU features yielding the highest XGBoost accuracy
id: deep-features-improve-xgboost-fnirs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025
    title: Shayla Sharmin and Roghayeh Leila Barmaki 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# XGBoost accuracy improves when trained on deep-learned representations, with CNN-GRU features yielding the highest XGBoost accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The highest XGBoost accuracy (69.23%) was obtained using features extracted from the hybrid CNN-GRU model, exceeding XGBoost on raw features. [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025](#shayla-sharmin-and-roghayeh-leila-barmaki-2025)

## Evidence

### Shayla Sharmin and Roghayeh Leila Barmaki 2025

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `design · r2`

Post-training analysis feeding GRU-extracted features into an XGBoost classifier. The results section reports "The highest XGBoost accuracy (69.23%) was obtained using features from the hybrid CNN-GRU model".

> "While XGBoost on raw features gave reasonable performance, its accuracy improved when applied to deep-learned representations. When we trained an XGBoost classifier using features extracted from these deep models, BiLSTM and CNN achieved an XGBoost accuracy of 66.18%, while LSTM features gave a lower accuracy of 58.82%. The highest XGBoost accuracy (69.23%) was obtained using features from the hybrid CNN-GRU model."

## Discussion


## Related Claims
- [A hybrid CNN-GRU deep learning model outperforms traditional machine learning and standalone deep models in predicting quiz performance from fNIRS signals](cnn-gru-outperforms-baselines-fnirs-performance-prediction.md) — related
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
