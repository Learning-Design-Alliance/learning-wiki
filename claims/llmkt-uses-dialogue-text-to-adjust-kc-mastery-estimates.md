---
type: claim
title: "In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels."
description: "In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels."
id: llmkt-uses-dialogue-text-to-adjust-kc-mastery-estimates
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: weak
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 1
    i: "?"
  - id: alexander-scarlatos-2024-2
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 1
    i: "?"
---

# In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels.

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q1` argument or single case

## Subclaims
`q1 i?` LLMKT excels in cases when it relies on textual information, rather than correctness labels, to adjust its KC mastery estimates. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q1 i?` LLMKT tends to predict low mastery when a KC is seen for the first time in a dialogue. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q1 · i?`

Qualitative case study of one CoMTA test-set dialogue (Table 3): "LLMKT excels in cases when it relies on textual information"; the model appeared to estimate the second tutor question as harder than the first despite overlapping KC labels.

> "LLMKT excels in cases when it relies on textual information, rather than correctness labels, to adjust its KC mastery estimates."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q1 · i?`

Qualitative analysis observation: LLMKT "tends to predict low mastery when a KC is seen for the first time in a dialogue", which the authors suggest may reflect students not reacting well to tutors shifting to new KCs mid-way.

> "We also found that LLMKT tends to predict low mastery when a KC is seen for the first time in a dialogue, possibly through observing that students do not react well to the tutor shifting to new KCs mid-way through the dialogue."

## Discussion


## Related Claims
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md)
