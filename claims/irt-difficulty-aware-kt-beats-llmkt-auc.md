---
type: claim
title: An IRT-based difficulty-aware conversational KT framework improves AUC over the LLMKT baseline on both QATD2k and MathDial
description: An IRT-based difficulty-aware conversational KT framework improves AUC over the LLMKT baseline on both QATD2k and MathDial
id: irt-difficulty-aware-kt-beats-llmkt-auc
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: shuyan-huang-2026
    resource: "https://arxiv.org/abs/2605.01097"
    title: "Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097"
    author: Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An IRT-based difficulty-aware conversational KT framework improves AUC over the LLMKT baseline on both QATD2k and MathDial

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Explicitly modeling student ability, item difficulty, and IRT-based prediction improves AUC from 64.89 to 65.25 on QATD2k and from 75.99 to 76.59 on MathDial over LLMKT. [→ Shuyan Huang 2026](#shuyan-huang-2026)

## Evidence

### Shuyan Huang 2026

Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097

`q2 · i?` · `design · r2`

Quantitative comparison on two tutor-student dialogue datasets (QATD2k: 1,573 train/393 test dialogues; MathDial: 2,235 train/588 test) shows the proposed framework "improves AUC from 64.89 to 65.25 (+0.36) on QATD2k" and to 76.59 on MathDial, with the best accuracy and AUC in Table 1. No effect size is printed.

> "our framework improves AUC from 64.89 to 65.25 (+0.36) on QATD2k and from 75.99 to 76.59 (+0.60) on Math- Dial"

## Discussion


## Related Claims
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related
