---
type: claim
title: "LEA's course-agnostic architecture was operationalised across three courses with no changes to the orchestrator, mastery tracker, or scaffolding engine"
description: "LEA's course-agnostic architecture was operationalised across three courses with no changes to the orchestrator, mastery tracker, or scaffolding engine"
id: orchestration-layer-generalises-knowledge-layer-adapts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rumble-2026
    resource: "https://doi.org/10.48550/arxiv.2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370 [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LEA's course-agnostic architecture was operationalised across three courses with no changes to the orchestrator, mastery tracker, or scaffolding engine

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Deployment across three courses spanning two disciplines and two academic levels required only course-specific RAG and KC artifacts, with no changes to the orchestrator, mastery tracker, or scaffolding engine. [→ Rumble 2026](#rumble-2026)

## Evidence

### Rumble 2026

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370 [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)

`q2 · i?` · `design · r2`

Deployment methodology across CMP511 (MSc computing), CMP202 (UG computing), and PSY555 (MSc social science), each onboarded through the identical three-stage pipeline. The authors summarise the design claim as "the orchestration layer generalises; the knowledge layer adapts."

> "This design was tested through deployment across three courses spanning two disciplines and two academic levels (Table 3); each required only course-specific RAG and KC artifacts, with no changes to the orchestrator, mastery tracker, or scaffolding engine."

## Discussion


## Related Claims
- [Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding](course-blind-code-question-generation-failure.md) — reports the opposite
- [Over two semesters the LearnAI deployment reached 18 courses (293 enrolled students) and 35 co-creation clients who produced 36 portfolio websites and over 20 deployed applications](learnai-reach-artifacts-two-semesters.md) — related
- [RAGAS Faithfulness declines with curriculum distance from LEA's original course (0.685 to 0.499), while Answer Relevancy and Context Precision remain broadly stable across courses](ragas-faithfulness-declines-cross-course.md) — a narrower finding that bears on this claim
- [In a graduate QIS course pilot, the specialized Spoke-and-Wheel architecture showed no task-boundary failures across 75 student interactions, though no controlled comparison against the prototype was run](itas-specialization-no-task-boundary-failures.md) — related
- [Many agentic multi-agent implementations remain at prototype or conceptual stage with limited large-scale deployment and empirical validation](agentic-multi-agent-systems-lack-empirical-validation.md) — related
- [Class size, course level, and discipline did not explain significant variation in how achievement gaps changed under active learning](class-size-level-discipline-not-significant-moderators.md) — related
