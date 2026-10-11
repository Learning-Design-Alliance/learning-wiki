---
type: claim
title: "Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding"
description: "Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding"
id: course-blind-code-question-generation-failure
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: rumble-2026
    resource: "https://arxiv.org/abs/2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Quiz mode hardcoded Python question generation with no awareness of the active course, generating Python questions for PSY555 and Python rather than C++ for CMP202. [→ Rumble 2026](#rumble-2026)

## Evidence

### Rumble 2026

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370

`q2 · i?` · `design · r2`

Deployment analysis across the three courses found one component was not course-agnostic in practice: the system generated Python code questions for PSY555, a course with no programming content. It was resolved by adding an explicit course-to-language mapping.

> "Quiz mode’s logic hard- coded Python question generation as a default (a choice originally made because Python fluency is a core objective of CMP511) and relied on generic Granular Objec- tive metadata with no awareness of which course was active."

## Discussion


## Related Claims
- [A question-repetition bug in Quiz Mode, reported by 2/8 pilot participants, was a defect simulation-based evaluation could not identify](quiz-repetition-bug-simulation-blind-spot.md) — related
- [LEA's course-agnostic architecture was operationalised across three courses with no changes to the orchestrator, mastery tracker, or scaffolding engine](orchestration-layer-generalises-knowledge-layer-adapts.md) — reports the opposite
- [In simulation, LEA met or exceeded targets in Chat and Tutor modes while Quiz Mode's KC Alignment Score fell below target](lea-simulation-evaluation-results.md) — related
- [RAGAS Faithfulness declines with curriculum distance from LEA's original course (0.685 to 0.499), while Answer Relevancy and Context Precision remain broadly stable across courses](ragas-faithfulness-declines-cross-course.md) — related
