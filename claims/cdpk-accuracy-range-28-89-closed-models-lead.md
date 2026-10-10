---
type: claim
title: "LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard"
description: "LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard"
id: cdpk-accuracy-range-28-89-closed-models-lead
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
    kind: design
    rigour: 2
---

# LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 97 tested LLMs, CDPK accuracy spans 28% (Llama-3.2 1B) to 89% (Gemini 2.5 Pro), and 9 of the top 10 models are closed-weight models from OpenAI, Google and Anthropic. [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i?` · `design · r2`

Benchmark evaluation of 97 LLMs on the 899 tested CDPK questions using a fixed few-shot prompt and exact-match accuracy with 95% bootstrap confidence intervals. The article reports accuracies "from 28% (Llama-3.2 1B) to 89%" and that closed-source models dominate the top of the leaderboard.

> "Accuracies range from 28% (Llama-3.2 1B) to 89% for the current leader, Google's Gemini 2.5 Pro model. Closed-source models dominate at the top of the leaderboard (Figure 6), with 9 out of the top 10 being closed models from OpenAI, Google and Anthropic."

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results](estimated-human-baseline-50-percent-cdpk.md) — related
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — related
