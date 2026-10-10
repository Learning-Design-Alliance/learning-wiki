---
type: claim
title: Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions
description: Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions
id: llm-selection-bias-against-option-d
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
    rigour: 3
---

# Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` In a four-configuration answer-position experiment, some tested models exhibited a selection bias, and contrary to prior work showing a preference for option A, some models showed a negative bias against selecting option D. [→ Lelièvre 2025](#lelievre-2025)

## Evidence

### Lelièvre 2025

Lelièvre, M., Waldock, A., Liu, M., Valdes Aspillaga, N., Mackintosh, A., Ogando Portela, M. J., Lee, J., Atherton, P., Ince, R. A. A., & Garrod, O. G. B. (2025). Benchmarking the Pedagogical Knowledge of Large Language Models. https://arxiv.org/abs/2506.18710

`q2 · i?` · `design · r3`

Controlled experiment on a subset of models with four configurations in which the correct answer was swapped into each possible position (A, B, C, D), preserving the ordering of the other options. The article reports a selection bias for some models, specifically against option D.

> "We indeed found a selection bias for some of the models tested (see Fig. 4) but contrary to [29] who showed a preference for responseA, we found that some models exhibit a negative bias against selecting optionD."

## Discussion


## Related Claims
- [A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only](llm-emotional-tone-bias-incident-words.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
