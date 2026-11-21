---
type: claim
title: "The GPT-4o rubric scorer aligned reasonably well with expert judgments (84.6% accuracy) and its rubric-level judgments matched TAs' final judgments 88.7% of the time"
description: "The GPT-4o rubric scorer aligned reasonably well with expert judgments (84.6% accuracy) and its rubric-level judgments matched TAs' final judgments 88.7% of the time"
id: llm-rubric-scorer-validity-84-6-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: xinyi-lu-2026
    title: Xinyi Lu 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The GPT-4o rubric scorer aligned reasonably well with expert judgments (84.6% accuracy) and its rubric-level judgments matched TAs' final judgments 88.7% of the time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The LLM-based rubric scorer achieved 84.6% classification accuracy against expert ratings, and 88.7% of its rubric-level judgments matched TAs' final judgments. [→ Xinyi Lu 2026](#xinyi-lu-2026)

## Evidence

### Xinyi Lu 2026

Xinyi Lu, Kexin Phyllis Ju, Mitchell Dudley, Larissa Sano, and Xu Wang. 2026. AI-Mediated Feedback Improves Student Revisions: A Randomized Trial with FeedbackWriter in a Large Undergraduate Course. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3791121

`q2 · i?` · `causal · r2`

Validation against a human expert who annotated 60 randomly sampled essays across 35 rubrics each (2,100 judgements, over 13 hours). The scorer achieved "a classification accuracy of 84.6% and a recall of 85.6%"; system logs separately showed 88.7% of rubric-level AI judgments matched TAs' final judgments. Accuracy is not an effect size.

> "Treating the expert ratings as the gold standard, the LLM-based rubric scorer (with GPT-4o) achieved a classification accuracy of 84.6% and a recall of 85.6%."

## Discussion


## Related Claims
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
