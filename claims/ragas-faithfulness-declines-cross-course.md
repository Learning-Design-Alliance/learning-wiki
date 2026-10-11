---
type: claim
title: "RAGAS Faithfulness declines with curriculum distance from LEA's original course (0.685 to 0.499), while Answer Relevancy and Context Precision remain broadly stable across courses"
description: "RAGAS Faithfulness declines with curriculum distance from LEA's original course (0.685 to 0.499), while Answer Relevancy and Context Precision remain broadly stable across courses"
id: ragas-faithfulness-declines-cross-course
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: rumble-2026
    resource: "https://arxiv.org/abs/2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: rumble-2026-2
    resource: "https://arxiv.org/abs/2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# RAGAS Faithfulness declines with curriculum distance from LEA's original course (0.685 to 0.499), while Answer Relevancy and Context Precision remain broadly stable across courses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Faithfulness declined from 0.685 (CMP511) through 0.609 (CMP202) to 0.499 (PSY555), carried by the significant cross-domain drop at PSY555 rather than the non-significant cross-level step to CMP202. [→ Rumble 2026](#rumble-2026)
`q2 i?` Answer Relevancy (0.875-0.935) and Context Precision (0.877-0.901) were comparatively stable across the three courses. [→ Rumble 2026 (2)](#rumble-2026-2)

## Evidence

### Rumble 2026

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370

`q2 · i?` · `design · r2`

RAGAS evaluation of 660 questions across three courses using LEA's live Chat Mode pipeline, with Kruskal-Wallis and pairwise Mann-Whitney tests on non-normal bounded scores. The Faithfulness gradient is attributed to generation logic tuned to the original course.

> "Faithfulness, by contrast, declines across the three courses, from 0.685 (CMP511) through 0.609 (CMP202) to 0.499 (PSY555); as the pairwise tests below establish, this decline is carried by the significant cross-domain drop at PSY555 rather than by the non-significant cross-level step to CMP202."

### Rumble 2026 (2)

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370

`q2 · i?` · `design · r2`

The same RAGAS cross-course evaluation found the system "consistently retrieves topically relevant material and generates on-topic responses" regardless of whether content is technical STEM or discursive psychology text.

> "Answer Relevancy and Context Precision are comparatively stable across domains (0.875–0.935 and 0.877–0.901 respectively), with only a modest decline for PSY555 on Answer Relevancy"

## Discussion


## Learner Variables
- [Domain Context](../learner-variables/domain-context.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [LEA's course-agnostic architecture was operationalised across three courses with no changes to the orchestrator, mastery tracker, or scaffolding engine](orchestration-layer-generalises-knowledge-layer-adapts.md) — a broader claim this one bears on
- [Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding](course-blind-code-question-generation-failure.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related
