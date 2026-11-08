---
type: claim
title: Four of 270 simulator-derived performance metrics, all with negative weights, were selected by an iterative loop algorithm to drive the classification model
description: Four of 270 simulator-derived performance metrics, all with negative weights, were selected by an iterative loop algorithm to drive the classification model
id: four-metrics-selected-from-270-negative-weights
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: mirchi-n-2020
    resource: "https://doi.org/10.1371/journal.pone.0229596"
    title: "Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596"
    author: Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Four of 270 simulator-derived performance metrics, all with negative weights, were selected by an iterative loop algorithm to drive the classification model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Two safety metrics (Max Force w/ Bipolar, Rate of Bleeding) and two movement metrics (Instrument Tip Distance, Acceleration w/ Bipolar) were selected, each carrying a negative weight. [→ Mirchi N 2020](#mirchi-n-2020)

## Evidence

### Mirchi N 2020

Mirchi N, Bissonnette V, Yilmaz R, Ledwos N, Winkler-Schwartz A, Del Maestro RF. (2020). The Virtual Operative Assistant: An explainable artificial intelligence tool for simulation-based training in surgery and medicine. PLoS ONE. https://doi.org/10.1371/journal.pone.0229596

`q2 · i?` · `design · r2`

Metric generation and selection from simulator-recorded data in the framework validation study: 270 metrics were created and "Four final metrics were selected by using an iterative loop algorithm". Table 2 lists the four metrics with weights from -0.2710 to -1.4902, all negative.

> "Two-hundred and seventy metrics of performance were created using the data recorded by the simulator.[12] Four final metrics were selected by using an iterative loop algorithm previously developed by our research group."

## Discussion


## Related Claims
- [Feedback on 4 AI-selected metrics improved 3 trained metrics and generalized to 8 of 16 untrained ICEMS performance metrics](voa-metric-feedback-extended-effect-untrained-metrics.md) — related
