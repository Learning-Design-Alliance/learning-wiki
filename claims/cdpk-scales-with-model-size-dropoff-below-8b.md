---
type: claim
title: CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters
description: CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters
id: cdpk-scales-with-model-size-dropoff-below-8b
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: lelièvre-2025
    resource: "https://arxiv.org/abs/2506.18710"
    title: "Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710"
    author: "Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Among open-weight models with known parameter counts, CDPK accuracy scales with size; the Pareto efficiency frontier shows a sharp drop-off below around 8B parameters, though at 7B parameters performance still spans over 20 percentage points (46% to 66%). [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i?` · `associational · r2`

Numerical analysis of CDPK accuracy against parameter count for open-weight models only, shown in Figure 9. The article reports the sharp drop-off below around 8B parameters and the 46%–66% range at 7B parameters; the largest model is not the best performing although the smallest is the worst.

> "The Pareto efficiency frontier shows a sharp drop-off below around 8B parameters. However, even at 7B parameters there is a range of performance of over 20 percentage points (from 46% to 66%)."

## Discussion


## Related Claims
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Accuracy-cost value frontier: at $0.10 per million tokens, CDPK performance rose from 50% (April 2024) to 82% (June 2025)](cdpk-value-frontier-rapid-cost-performance-improvement.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1](llama-guard-scaling-trend-education-classification.md) — related
- [VietEduQwen achieves 87.02% accuracy on the 2025 Vietnamese National High School Examination, a 6.10-percentage-point gain over the base Qwen3-8B model](vieteduqwen-87-exam-accuracy-gain-over-qwen3-8b.md) — related
