---
type: claim
title: "Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings"
description: "Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings"
id: temperature-construct-type-interaction-coding
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
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

# Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Pairings at mid-range temperatures produced the highest reliability for constructs with higher theoretical coherence, such as Self-efficacy (κ = 0.798) and Prior KSAs (κ = 0.741). [→ Ober 2026](#ober-2026)
`q2 i?` Pairings involving higher temperature settings generally produced lower reliability, with notable exceptions for constructs with low operational clarity. [→ Ober 2026 (2)](#ober-2026-2)

## Evidence

### Ober 2026

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Pairwise reliability analysis by construct across temperature pairings. Self-efficacy peaked at moderate temperature pairings (κ = 0.798) and Prior KSAs at higher pairings (κ = 0.741), patterns the authors align with their dimensional analysis.

> "Self-efficacy achieved its highest pairwise reliability in the ChatGPT4o/temperature=0.3 vs. ChatGPT4o/temperature=0.7 comparison ( κ = 0.798, 90.8% agreement), while Prior KSA s performed best in ChatGPT4o/temperature=0.7 vs. ChatGPT4o/temperature=1 pairings (κ = 0.741, 88.06% agreement)"

### Ober 2026 (2)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Pairwise reliability analysis across temperature settings. Higher-temperature pairings generally produced lower reliability except for low-clarity constructs; the abstract Prior KSAs construct showed its strongest performance (κ = 0.809) in higher-temperature mini-model pairings.

> "In further contrast, pairings involving model configurations with higher temperature settings generally produced lower reliability, with notable exceptions for constructs with low operational clarity"

## Discussion


## Related Claims
- [Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement](construct-clarity-predicts-coding-agreement.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — reports the opposite
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
