---
type: claim
title: "Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task."
description: "Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task."
id: dialogue-kt-performance-is-relatively-low-compared-to-standard-kt
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
    q: 2
    i: "?"
  - id: alexander-scarlatos-2024-2
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 1
    i: "?"
---

# Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q1`–`q2`

## Subclaims
`q2 i?` Performance of all KT methods is relatively low on dialogueKT, with a maximum of around 76% AUC for student turn correctness prediction. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q1 i?` The authors attribute the difficulty partly to student behavior in dialogues being more unpredictable than in traditional KT, given many diverse types of student responses. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?`

Benchmark comparison across both datasets: performance is "relatively low on the dialogueKT task, with a maximum of around 76% AUC", which the article contrasts with standard KT methods surpassing 80% AUC on some datasets.

> "Finally, we see that performance of all KT methods is relatively low on the dialogueKT task, with a maximum of around 76% AUC for student dialogue turn correctness prediction."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q1 · i?`

Authors' explanation of the low performance, not a tested result: "student behavior in dialogues is more unpredictable compared to traditional KT". A first stated reason is that CoMTA dialogues are short, with only 4-5 labeled turn pairs on average.

> "Second, student behavior in dialogues is more unpredictable compared to traditional KT, since there can be many diverse types of student responses to tutor turns."

## Discussion


## Related Claims
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md)
