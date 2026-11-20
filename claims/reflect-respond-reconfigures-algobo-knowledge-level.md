---
type: claim
title: "Knowledge-state contents reconfigure AlgoBo's MCQ performance by knowledge type"
description: "Knowledge-state contents reconfigure AlgoBo's MCQ performance by knowledge type"
id: reflect-respond-reconfigures-algobo-knowledge-level
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
    kind: causal
    rigour: 2
  - id: hyoungwook-jin-2024-2
    title: Hyoungwook Jin 2024 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Knowledge-state contents reconfigure AlgoBo's MCQ performance by knowledge type

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` With a facts-only knowledge state, AlgoBo solved conceptual questions but no Implementation questions, showing knowledge-type-specific configuration. [→ Hyoungwook Jin 2024](#hyoungwook-jin-2024)
`q2 i?` AlgoBo achieved higher MCQ scores with correct code (State 4) than with incorrect code (State 3) in its knowledge state. [→ Hyoungwook Jin 2024 (2)](#hyoungwook-jin-2024-2)

## Evidence

### Hyoungwook Jin 2024

Hyoungwook Jin, Seonghee Lee, Hyungyu Shin, and Juho Kim. 2024. Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education. Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24). https://doi.org/10.1145/3613904.3642349

`q2 · i?` · `causal · r2`

Technical evaluation of the Reflect-Respond pipeline measuring AlgoBo's performance on nine MCQs per topic across three algorithm topics under four seed knowledge states. With a facts-only state, AlgoBo 'could solve some conceptual (Understanding and Analysis) questions but none of the Implementation questions'.

> "When the knowledge state had only facts information (State 2 ), AlgoBo could solve some conceptual (Understanding and Analysis) questions but none of the Implementation questions."

### Hyoungwook Jin 2024 (2)

Hyoungwook Jin, Seonghee Lee, Hyungyu Shin, and Juho Kim. 2024. Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education. Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24). https://doi.org/10.1145/3613904.3642349

`q2 · i?` · `design · r2`

Same technical evaluation comparing knowledge states containing code. AlgoBo 'achieved higher scores when given correct code (State 4), compared to incorrect code (State 3)', and followed incorrect knowledge-state content exactly, producing wrong code and answers.

> "When the knowledge state contained code information, AlgoBo started to solve Implementation questions and achieved higher scores when given correct code (State 4), compared to incorrect code (State 3)."

## Discussion


## Related Claims
- [Correct tutoring improves AlgoBo's MCQ scores while random irrelevant conversation does not](correct-tutoring-improves-algobo-mcq-scores.md) — related
- [The training-by-content interaction is not specific to test question type, indicating transfer between skill and fact learning](no-three-way-interaction-test-question-type-transfer.md) — reports the opposite
- [The training-by-content interaction did not vary with retention interval duration in the human experiment](no-training-retention-interval-interaction.md) — related
- [Classroom testing benefits facts (g = 0.524), concept learning (g = 0.644), and knowledge application in problem solving (g = 0.453).](testing-benefits-facts-concepts-problem-solving.md) — related
