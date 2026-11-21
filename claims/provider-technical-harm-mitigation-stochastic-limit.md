---
type: claim
title: Edtech providers actively mitigate technical harms, but the stochastic nature of LLMs prevents guaranteed harm-free outputs
description: Edtech providers actively mitigate technical harms, but the stochastic nature of LLMs prevents guaranteed harm-free outputs
id: provider-technical-harm-mitigation-stochastic-limit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: emma-harvey-2025
    resource: "https://doi.org/10.1145/3706598.3713210"
    title: "Emma Harvey, Allison Koenecke, and René F. Kizilcec. (2025). \"Don't Forget the Teachers\": Towards an Educator-Centered Understanding of Harms from Large Language Models in Education. arXiv. [doi:10.1145/3706598.3713210](https://doi.org/10.1145/3706598.3713210)"
    author: Emma Harvey, Allison Koenecke, and René F. Kizilcec
    q: 2
    i: "?"
    kind: qualitative
    rigour: 3
  - id: emma-harvey-2025-2
    resource: "https://doi.org/10.1145/3706598.3713210"
    title: "Emma Harvey, Allison Koenecke, and René F. Kizilcec. (2025). \"Don't Forget the Teachers\": Towards an Educator-Centered Understanding of Harms from Large Language Models in Education. arXiv. [doi:10.1145/3706598.3713210](https://doi.org/10.1145/3706598.3713210)"
    author: Emma Harvey, Allison Koenecke, and René F. Kizilcec
    q: 2
    i: "?"
    kind: qualitative
    rigour: 3
---

# Edtech providers actively mitigate technical harms, but the stochastic nature of LLMs prevents guaranteed harm-free outputs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · qualitative `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All interviewed edtech providers were aware of and attempting to account for technical LLM harms using human oversight and technical guardrails. [→ Emma Harvey 2025](#emma-harvey-2025)
`q2 i?` Most providers acknowledged their mitigations could not guarantee outputs free of toxic or biased content, privacy violations, or hallucinations, so many limited LLM use instead. [→ Emma Harvey 2025 (2)](#emma-harvey-2025-2)

## Evidence

### Emma Harvey 2025

Emma Harvey, Allison Koenecke, and René F. Kizilcec. (2025). "Don't Forget the Teachers": Towards an Educator-Centered Understanding of Harms from Large Language Models in Education. arXiv. [doi:10.1145/3706598.3713210](https://doi.org/10.1145/3706598.3713210)

`q2 · i?` · `qualitative · r3`

Interview findings from six edtech provider participants (T1-T6) whose tools each report at least 10,000 active student users. Providers reported human oversight via moderation teams and educator chat-log review, plus guardrails such as toxicity detectors, personal-information filtering, and retrieval-augmented generation.

> "All of the edtech providers we interviewed were aware of and a ttempting to account for the technical LLM harms identiﬁed by Bender et al. [5] and Weidin ger et al. [80]."

### Emma Harvey 2025 (2)

Emma Harvey, Allison Koenecke, and René F. Kizilcec. (2025). "Don't Forget the Teachers": Towards an Educator-Centered Understanding of Harms from Large Language Models in Education. arXiv. [doi:10.1145/3706598.3713210](https://doi.org/10.1145/3706598.3713210)

`q2 · i?` · `qualitative · r3`

Provider interview findings (§4.1). Because mitigations could not guarantee harm-free outputs, providers limited LLM use by generating static human-reviewed content, restricting LLM agents to adult users, and limiting live-chat context windows. No effect size is reported.

> "most of the edtech providers we interviewed ac knowl- edged that, due to the inherently stochastic nature of LLMs, their mitigations could not guarantee LLM outputs that were free of toxic or biased content, privacy violations, or hallucinations (T1–T4, T6)."

## Discussion


## Related Claims
- [Edtech providers focus primarily on technical harms while educators are most concerned about broader-impact harms of LLM-based edtech](provider-educator-harm-conception-gap.md) — related
- [Most edtech providers do not explore harms arising from human-LLM interactions such as academic dishonesty](providers-neglect-human-llm-interaction-harms.md) — related
- [Panelists strongly agreed human oversight must remain central in academic decisions involving GenAI, with clear accountability assignments](human-oversight-central-genai-academic-decisions.md) — related
- [Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics](tutor-harm-subject-dependent-mitigations.md) — related
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — related
