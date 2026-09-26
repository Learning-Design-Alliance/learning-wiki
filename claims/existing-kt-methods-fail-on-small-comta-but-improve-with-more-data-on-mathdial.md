---
type: claim
title: Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.
description: Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.
id: existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial
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

# Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` On CoMTA, all existing KT methods almost completely fail, unable to outperform the majority-class baseline (Acc. 57.83±5.08, AUC 50.0±0.00, F1 58.87±29.70). [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i?` On MathDial, which has 21x more data than CoMTA, existing KT methods perform significantly better, against a majority baseline Acc. of 52.64. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?`

CoMTA results of the benchmark comparison with 5-fold cross-validation: existing methods "almost completely fail, unable to outperform the simple baseline of predicting the majority class label", which scores Acc. of 57.83±5.08, AUC of 50.0±0.00, and F1 of 58.87±29.70.

> "On CoMTA, we see that all existing KT methods almost completely fail, unable to outperform the simple baseline of predicting the majority class label (which corresponds to an Acc. of 57.83±5.08, AUC of 50.0±0.00, and F1 of 58.87±29.70)."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?`

MathDial results of the same comparison: "existing KT methods perform significantly better" with 21x more data; the majority baseline gets an Acc. of 52.64 since class labels are balanced. No effect size is printed.

> "On MathDial, which has 21x more data than CoMTA, we see that existing KT methods perform significantly better (for reference, the majority baseline only gets an Acc. of 52.64 since class labels are balanced)."

## Discussion


## Related Claims
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md)
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related
