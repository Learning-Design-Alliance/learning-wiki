---
type: claim
title: An individualized machine-learning diagnostic using LCM-based features predicts lexical categorization training benefits with moderate-to-good accuracy
description: An individualized machine-learning diagnostic using LCM-based features predicts lexical categorization training benefits with moderate-to-good accuracy
id: ml-diagnostic-predicts-training-benefit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: benjamin-gagl-klara-gregorová-2024
    resource: "https://doi.org/10.1038/s41539-024-00237-7"
    title: "Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7"
    author: "Benjamin Gagl & Klara Gregorová"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: benjamin-gagl-klara-gregorová-2024-2
    resource: "https://doi.org/10.1038/s41539-024-00237-7"
    title: "Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7"
    author: "Benjamin Gagl & Klara Gregorová"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# An individualized machine-learning diagnostic using LCM-based features predicts lexical categorization training benefits with moderate-to-good accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Aggregating predictions across all machine-learning pipelines, the correlation between predicted and observed training effect was moderate, r = 0.58. [→ Benjamin Gagl & Klara Gregorová 2024](#benjamin-gagl-klara-gregorova-2024)
`q3 i?` The best-performing pipeline reached a predicted–observed correlation of 0.69, explaining nearly 50% of training-effect variance (R² = 0.476). [→ Benjamin Gagl & Klara Gregorová 2024 (2)](#benjamin-gagl-klara-gregorova-2024-2)

## Evidence

### Benjamin Gagl & Klara Gregorová 2024

Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7

`q3 · i?` · `causal · r2`

Prediction models were built with consensus nested leave-one-out cross-validation using pre-test reading speed and first-session data only; individual pipeline correlations ranged from −0.10 to 0.69 with a mean of 0.42. The aggregated prediction achieved r = 0.58.

> "When we aggre- gate the predicted values from all pipelines for each participant (median across 720 predictions), the correlation between pre- dicted vs. observed training effect was moderate ( r = 0.58; t(73) = 6.02, conﬁdence interval: 0.40–0.71, p < 001)."

### Benjamin Gagl & Klara Gregorová 2024 (2)

Benjamin Gagl & Klara Gregorová. (2024). Investigating lexical categorization in reading based on joint diagnostic and training approaches for language learners. npj Science of Learning 9:29. https://doi.org/10.1038/s41539-024-00237-7

`q3 · i?` · `causal · r2`

The best pipeline combined multiple regression fitting, a feature-selection cutoff of 10, and a predictor composition estimating change of lexical categorization uncertainty and OLD20 effects within the first session; it was best in 21 of 75 cross-validation loops, and its predictor composition was best in 55 of 75 loops.

> "the ﬁnal correlation of pre- dicted vs. observed lexical categorization training effects resulted in 0.69 (t(73) = 8.16, con ﬁdence interval = [0.55–0.79], p < 0.001, see Fig. 5A), explaining nearly 50% of the variance of the training effect (R2 = 0.476)."

## Discussion


## Related Claims
- [Lexical categorization training significantly increases reading speed in adult non-native German learners, replicated across three experiments](lc-training-reading-speed-gains-language-learners.md) — related
- [LCM-related features, especially lexical categorization uncertainty, are the most important word-characteristic predictors of training success](lcm-features-essential-prediction.md) — related
- [Training response times rise with lexical categorization uncertainty and fall across sessions, but a reduction of the uncertainty effect across sessions appears only in Experiment 1](uncertainty-effect-training-sessions-mixed.md) — related
- [Machine-learning-based responder selection raises mean group reading-speed gain from 23% to 43%](responder-selection-gain-23-to-43.md) — related
