---
type: claim
title: SEND and CDPK benchmark results correlate highly (r = 0.94), but higher-performing models do relatively better on general pedagogy than SEND
description: SEND and CDPK benchmark results correlate highly (r = 0.94), but higher-performing models do relatively better on general pedagogy than SEND
id: send-cdpk-correlation-and-reversal
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
    i: 3
    kind: design
    rigour: 3
---

# SEND and CDPK benchmark results correlate highly (r = 0.94), but higher-performing models do relatively better on general pedagogy than SEND

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2` · `i3` large

## Subclaims
`q2 i3` SEND and CDPK accuracies across models are highly correlated (r = 0.94), yet models above 60% accuracy tended to do better on general pedagogy than SEND, while for lower-performing models this was reversed. [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i3` · `design · r3`

Benchmark evaluation of models on the 220 tested SEND questions compared with their CDPK results, shown in Figure 12. The article prints the correlation coefficient r = 0.94 between the two benchmarks' accuracies and reports the performance reversal across model tiers.

> "While the results of the two benchmarks were overall quite highly correlated (𝑟 = 0.94), it's interesting that higher performing models (above60% accuracy) tended to do better on general pedagogy than SEND, while for lower performing models, this was reversed."

## Discussion


## Related Claims
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Estimated human baseline on the CDPK benchmark is approximately 50%, based on aggregate Chilean teacher exam results](estimated-human-baseline-50-percent-cdpk.md) — related
- [Lower-performing LLMs show higher variance across pedagogy subject categories and peak in Technology and General categories](low-performing-models-subject-variance-technology-general.md) — related
