---
type: claim
title: "Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results"
description: "Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results"
id: estimated-human-baseline-50-percent-cdpk
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Based on results of more than 25,000 teachers from 2017 to 2021, the mean expected score of a human trainee teacher on the CDPK benchmark is estimated at approximately 50%. [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i?` · `design · r2`

Estimation from aggregate subject- and year-level results of Chilean teachers on ECEP exams, allocating each benchmark question the average accuracy of its source paper; four methods all produced estimates around 50%. Question-level human results were not available, so this is an estimate only.

> "Based on the results of more than 25,000 teachers from 2017 to 2021, the mean expected score of a human trainee teacher would be expected to be approximately 50% on The Pedagogy Benchmark."

## Discussion


## Related Claims
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Accuracy-cost value frontier: at $0.10 per million tokens, CDPK performance rose from 50% (April 2024) to 82% (June 2025)](cdpk-value-frontier-rapid-cost-performance-improvement.md) — related
- [SEND and CDPK benchmark results correlate highly (r = 0.94), but higher-performing models do relatively better on general pedagogy than SEND](send-cdpk-correlation-and-reversal.md) — related
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
