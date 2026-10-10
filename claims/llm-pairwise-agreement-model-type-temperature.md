---
type: claim
title: Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases
description: Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases
id: llm-pairwise-agreement-model-type-temperature
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-2
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Within-model type pairs showed 3.3–4.0% higher agreement than cross-model pairs at the same temperature (H2a supported). [→ Ober 2026](#ober-2026)
`q2 i?` Within each model type, agreement decreased monotonically as temperature difference increased (H2b supported). [→ Ober 2026 (2)](#ober-2026-2)

## Evidence

### Ober 2026

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Pairwise Cohen's κ and percent agreement comparisons between LLM configurations on the full chat log dataset. Same-base-model pairs (κ = 0.876) exceeded cross-model pairs (κ = 0.841), supporting H2a.

> "Within-model type pairs showed 3.3–4.0% higher agreement than cross-model pairs at the same temperature (e.g., ChatGPT4o/temperature=0 vs. ChatGPT4o/temperature=0.3: κ = 0.876; ChatGPT4o/temperature=0 vs. ChatGPT4o-mini/temperature=0: κ = 0.841)"

### Ober 2026 (2)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Pairwise reliability analysis across temperature settings within each model type. The article reports agreement "decreased monotonically as temperature difference increased," with lower-temperature pairings producing the highest inter-model reliability.

> "Within each model type, agreement decreased monotonically as temperature difference increased ( H2b supported ). In addition, pairings consisting of model configurations with lower temperature settings consistently produced the highest inter-model reliability across most constructs"

## Discussion


## Related Claims
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](human-human-agreement-lower-than-llm-llm.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [Lowering an LLM's temperature setting is one lever for improving output consistency](lowering-temperature-improves-llm-consistency.md) — related
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](moderate-cross-model-agreement-solvability.md) — a narrower finding that bears on this claim
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions](assertion-cross-model-agreement-moderate-median-0401.md) — related
