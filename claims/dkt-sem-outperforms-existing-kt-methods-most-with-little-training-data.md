---
type: claim
title: DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.
description: DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.
id: dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
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
    q: 2
    i: "?"
---

# DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` DKT-Sem performs better than all existing KT methods even though it largely uses the same architecture as DKT. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i?` On MathDial, DKT-Sem outperforms existing KT methods by a smaller margin than on CoMTA, which the authors read as its greatest advantage being when little training data is given. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?`

Benchmark comparison of KT methods on CoMTA and MathDial: "DKT-Sem performs better than all existing KT methods", which the authors say emphasizes the benefit of using textual dialogue context. No effect size is printed.

> "We also see that DKT-Sem performs better than all existing KT methods, even though it largely uses the same model architecture as DKT."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?`

MathDial results of the same comparison: DKT-Sem wins "by a smaller margin than on CoMTA", which the authors interpret as indicating it has its greatest advantage when little training data is given. No test statistic is printed.

> "While DKT-Sem still outperforms existing KT methods, it does so by a smaller margin than on CoMTA, indicating DKT-Sem has its greatest advantage when little training data is given."

## Discussion


## Related Claims
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md)
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels.](llmkt-uses-dialogue-text-to-adjust-kc-mastery-estimates.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
