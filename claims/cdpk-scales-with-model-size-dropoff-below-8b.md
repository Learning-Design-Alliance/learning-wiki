---
type: claim
title: CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters
description: CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters
id: cdpk-scales-with-model-size-dropoff-below-8b
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lelièvre-2025
    resource: "https://doi.org/10.48550/arxiv.2506.18710"
    title: "Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710 [doi:10.48550/arxiv.2506.18710](https://doi.org/10.48550/arxiv.2506.18710)"
    author: "Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among open-weight models with known parameter counts, CDPK accuracy scales with size; the Pareto efficiency frontier shows a sharp drop-off below around 8B parameters, though at 7B parameters performance still spans over 20 percentage points (46% to 66%). [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710 [doi:10.48550/arxiv.2506.18710](https://doi.org/10.48550/arxiv.2506.18710)

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
- [Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone](model-family-beats-parameter-count-for-tutoring-quality.md) — related
- [Model size is not the primary factor in outcome-prediction performance](model-size-not-primary-outcome-prediction-factor.md) — reports the opposite
- [Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs](llm-scale-does-not-predict-tutor-safety.md) — related
- Model size did not correspond to higher scores in secondary science; small open-weight models outperformed significantly larger ones — reports the opposite
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](adaptation-gains-grow-with-model-capacity.md) — a narrower finding that bears on this claim
- [The domain-specialized 32-billion-parameter model surpasses significantly larger general-purpose models such as Qwen3-235B-A22B-Thinking (86.63%) and Qwen2.5-72B-Instruct (78.60%) on the CDPK Benchmark](domain-specialized-32b-outperforms-larger-models.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
- [Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points](capability-boundaries-and-universal-failures-academiclaw.md) — related
