---
type: claim
title: DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM
description: DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM
id: dmo-gru-faster-training-time
status: review
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

# DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` DMO-based hyperparameter tuning yielded a 98 s training time, faster than CNN-GRU (150 s) and LSTM (138 s), while traditional models were less accurate despite being faster. [→ Li C 2025](#li-c-2025)

## Evidence

### Li C 2025

Li C, Yin W. (2025). Interactive online learning method for students based on artificial intelligence. Discover Artificial Intelligence 5:201. https://doi.org/10.1007/s44163-025-00401-x

`q2 · i?` · `design · r2`

The Results section's comparative analysis reports training times from Table 2: DMO-GRU at 98 s versus CNN-GRU at 150 s and LSTM at 138 s, described as "better efficiencies" from DMO-based hyperparameter tuning.

> "It also proved that DMO-based hyperparameter tuning led to better efficiencies, with a 98 s training time as compared to CNN-GRU (150 s) and LSTM (138 s)."

## Discussion


## Related Claims
- [The DMO-GRU model achieves the best classification results among the compared models, with 91.2% accuracy, 90.8% F1-score, 90.1% precision and 92.5% recall](dmo-gru-best-classification-results.md) — related
- [DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success](dmo-gru-lowest-regression-error-highest-r2.md) — related
