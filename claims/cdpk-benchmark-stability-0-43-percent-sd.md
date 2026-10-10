---
type: claim
title: "The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs"
description: "The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs"
id: cdpk-benchmark-stability-0-43-percent-sd
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

# The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Running the 899 CDPK questions 20 times on a subset of 8 models yielded a maximum standard deviation of accuracy of 0.43%, indicating the test procedure and scores are robust and repeatable. [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i?` · `design · r2`

Stability experiment in which the 899 CDPK questions were run 20 times on a subset of 8 models sampled across the obtained accuracy range, to evaluate benchmark robustness given stochastic LLM decoding. The article reports the maximum standard deviation of accuracy as 0.43%.

> "Over these 8 models the maximum standard deviation of accuracy (over the 20 runs) was 0.43%. This shows that our test procedure and result scores are robust and repeatable."

## Discussion


## Related Claims
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
- [SEND and CDPK benchmark results correlate highly (r = 0.94), but higher-performing models do relatively better on general pedagogy than SEND](send-cdpk-correlation-and-reversal.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [Accuracy-cost value frontier: at $0.10 per million tokens, CDPK performance rose from 50% (April 2024) to 82% (June 2025)](cdpk-value-frontier-rapid-cost-performance-improvement.md) — related
- [Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results](estimated-human-baseline-50-percent-cdpk.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
