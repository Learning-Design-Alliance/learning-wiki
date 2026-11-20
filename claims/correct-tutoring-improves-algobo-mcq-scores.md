---
type: claim
title: "Correct tutoring improves AlgoBo's MCQ scores while random irrelevant conversation does not"
description: "Correct tutoring improves AlgoBo's MCQ scores while random irrelevant conversation does not"
id: correct-tutoring-improves-algobo-mcq-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: hyoungwook-jin-2024
    title: Hyoungwook Jin 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: hyoungwook-jin-2024-2
    title: Hyoungwook Jin 2024 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Correct tutoring improves AlgoBo's MCQ scores while random irrelevant conversation does not

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Random irrelevant conversations did not significantly increase AlgoBo's MCQ scores, indicating persistence of the configured knowledge level. [→ Hyoungwook Jin 2024](#hyoungwook-jin-2024)
`q2 i?` Correct tutoring significantly improved AlgoBo's MCQ scores across Understanding, Implementation, and Analysis question types. [→ Hyoungwook Jin 2024 (2)](#hyoungwook-jin-2024-2)

## Evidence

### Hyoungwook Jin 2024

Hyoungwook Jin, Seonghee Lee, Hyungyu Shin, and Juho Kim. 2024. Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education. Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24). https://doi.org/10.1145/3613904.3642349

`q2 · i?` · `design · r2`

Technical evaluation of persistence: random conversations teaching arithmetic, translation, and classification were run on a facts-only state with Reflection enabled, and MCQ scores were compared before and after. No significant score increase was observed across conversation lengths.

> "We did not observe any significant increase in the scores, confirming that the persistence of knowledge levels is robust regardless of the length of random conversations."

### Hyoungwook Jin 2024 (2)

Hyoungwook Jin, Seonghee Lee, Hyungyu Shin, and Juho Kim. 2024. Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education. Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24). https://doi.org/10.1145/3613904.3642349

`q2 · i?` · `design · r2`

Technical evaluation of adaptability on State 2 seeds: tutoring conversations taught three pieces of information mapping to Understanding, Implementation, and Analysis. Correct tutoring 'significantly improved MCQ scores' across all three question types relative to the start.

> "Correct tutoring significantly improved MCQ scores (compare the difference between the "At the start" and "After Correct tutoring" columns in Table 4) across Understanding, Implementation, and Analysis."

## Discussion


## Related Claims
- [Knowledge-state contents reconfigure AlgoBo's MCQ performance by knowledge type](reflect-respond-reconfigures-algobo-knowledge-level.md) — related
- [The tutor-access learning gain was concentrated in conceptual depth of written answers rather than multiple-choice scores](tutor-gain-concentrated-in-written-reasoning-depth.md) — related
- [Access to a structured conversational AI tutor increased post-test content scores over a no-AI holdout with ambient consumer AI available](structured-ai-tutor-raises-post-test-scores-field-experiment.md) — a broader claim this one bears on
- [Curiosity-modulated tutoring produces roughly 2.4× more conversational turns than baseline under fixed time budgets](curiosity-modulation-increases-conversational-turns.md) — related
