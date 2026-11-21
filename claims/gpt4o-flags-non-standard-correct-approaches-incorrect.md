---
type: claim
title: GPT-4o sometimes incorrectly judges non-standard but correct solution approaches as wrong, flagging correct solutions as incorrect in five of 25 tasks
description: GPT-4o sometimes incorrectly judges non-standard but correct solution approaches as wrong, flagging correct solutions as incorrect in five of 25 tasks
id: gpt4o-flags-non-standard-correct-approaches-incorrect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: shuai-ma-2025
    title: Shuai Ma 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o sometimes incorrectly judges non-standard but correct solution approaches as wrong, flagging correct solutions as incorrect in five of 25 tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GPT mistakenly flagged correct solutions as incorrect when they deviated from common approaches in its training data, in five out of 25 tasks. [→ Shuai Ma 2025](#shuai-ma-2025)

## Evidence

### Shuai Ma 2025

Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025. DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-Decomposition. In CHI Conference on Human Factors in Computing Systems (CHI '25). https://doi.org/10.1145/3706598.3713748

`q2 · i?` · `causal · r2`

In the technical evaluation against expert-annotated ground truth, the authors observed that GPT "mistakenly flagged correct solutions as incorrect" for non-standard approaches, for example marking a correct sorting-based solution as incorrect because it was not the most optimal approach.

> "In five out of 25 tasks, GPT mistakenly flagged correct solutions as incorrect simply because they deviated from the common approaches in its training data."

## Discussion


## Related Claims
- [GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements](gpt4-feedback-plausible-but-misleading.md) — related
- [GPT-4 grading shows high score variability across repeated rounds, especially for numerical correctness](gpt4-grading-score-variability.md) — related
