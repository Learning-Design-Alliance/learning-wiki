---
type: claim
title: "GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three"
description: "GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three"
id: gru-lowest-performing-competency-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: henderson-2020
    resource: "https://educationaldatamining.org/EDM2020/proceedings/"
    title: "Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/"
    author: "Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The GRU achieved an average R² of 0.102 across all concepts, the lowest of all models evaluated, while LSTM variants achieved the highest R² on at least one concept. [→ Henderson 2020](#henderson-2020)

## Evidence

### Henderson 2020

Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/

`q2 · i?` · `design · r2`

Held-out test set comparison of sequential deep learning models on 316 students' gameplay sequences. The GRU's "average R2 value of 0.102" was the lowest across both task types.

> "Across both single-task and multi-task models, the GRU was the lowest-performing model, achieving an average R2 value of 0.102 across all concepts."

## Discussion


## Related Claims

- [Overlapping concepts (sharing post-test questions with other concepts) yield higher student scores and higher model R², and multi-task modeling across all concepts is detrimental for these concepts](overlapping-concepts-higher-performance-multi-task-detrimental.md)
- [The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts](single-task-rf-best-average-not-universally-optimal.md)
- [The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance](fusion-transformer-lowest-worst-group-mae-smallest-gender-gap.md)
- [Adding in-game strategy features to pre-test features substantially improves LSTM-based stealth assessment accuracy](in-game-strategy-features-improve-prediction-over-pretest-only.md) — related
- [DMO-GRU attains the lowest MAE and RMSE and the highest R2 score among the compared regression models for forecasting student success](dmo-gru-lowest-regression-error-highest-r2.md) — reports the opposite
- [DMO-GRU trains faster than the deep learning baselines, with a 98 s training time versus 150 s for CNN-GRU and 138 s for LSTM](dmo-gru-faster-training-time.md) — related
- [The DMO-GRU model achieves the best classification results among the compared models, with 91.2% accuracy, 90.8% F1-score, 90.1% precision and 92.5% recall](dmo-gru-best-classification-results.md) — reports the opposite
- [Deep learning models (LSTM, GRU, transformer) achieve high and comparable accuracy (0.90–0.93) on physiological exam-outcome prediction](deep-learning-models-comparable-accuracy-physiological-exam-prediction.md) — reports the opposite
