---
type: claim
title: "GPT-4o identifies learners' thought-process step statuses more accurately from code than from natural-language descriptions, with the largest gap for sequence-change errors"
description: "GPT-4o identifies learners' thought-process step statuses more accurately from code than from natural-language descriptions, with the largest gap for sequence-change errors"
id: gpt4o-code-vs-natural-language-step-status-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: shuai-ma-2025
    title: Shuai Ma 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GPT-4o identifies learners' thought-process step statuses more accurately from code than from natural-language descriptions, with the largest gap for sequence-change errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GPT-4o's status evaluation is more accurate on code-based inputs than natural-language step descriptions, especially for sequence-change errors (70% vs 100% accuracy). [→ Shuai Ma 2025](#shuai-ma-2025)

## Evidence

### Shuai Ma 2025

Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025. DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-Decomposition. In CHI Conference on Human Factors in Computing Systems (CHI '25). https://doi.org/10.1145/3706598.3713748

`q2 · i?` · `causal · r1`

Technical evaluation on a dataset of 175 error-laden step trees built from 25 easy-level LeetCode problems with seven expert-created error types, compared against expert-annotated ground truth. Sequence-change errors from natural language yielded 70% accuracy (FPR 36%, FNR 24%) versus 100% accuracy from code.

> "For sequence change errors, GPT's accuracy drops to 70% with an F1 score of 72% from natural language descriptions, with a False Positive Rate (FPR) of 36% and a False Negative Rate (FNR) of 24%. In contrast, code-based evaluations achieve 100% accuracy and F1 scores."

## Discussion


## Related Claims
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related
- [GPT-4o prompted only with SRL theory references generates a codebook accurately representing most key elements of both foundational SRL theories](gpt4o-theory-references-codebook-covers-srl-theories.md) — related
