---
type: claim
title: "In simulation, LEA met or exceeded targets in Chat and Tutor modes while Quiz Mode's KC Alignment Score fell below target"
description: "In simulation, LEA met or exceeded targets in Chat and Tutor modes while Quiz Mode's KC Alignment Score fell below target"
id: lea-simulation-evaluation-results
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: rumble-2026
    resource: "https://doi.org/10.48550/arxiv.2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370 [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: rumble-2026-2
    resource: "https://doi.org/10.48550/arxiv.2607.13370"
    title: "Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370. [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)"
    author: Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# In simulation, LEA met or exceeded targets in Chat and Tutor modes while Quiz Mode's KC Alignment Score fell below target

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` Chat Mode achieved 100% retrieval success and M=0.880 generated answer quality, both exceeding target. [→ Rumble 2026](#rumble-2026)
`q1 i?` Quiz Mode's KC Alignment Score averaged M=0.751, below the 0.80 target, with thematic analysis suggesting prompt phrasing favoured recall over higher-order reasoning. [→ Rumble 2026 (2)](#rumble-2026-2)

## Evidence

### Rumble 2026

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370 [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)

`q1 · i?` · `design · r2`

Simulation-based testing with synthetic learner agents across 14,143 interactions, scored with an LLM-as-a-Judge framework against course content. Chat Mode exceeded both retrieval and answer-quality targets.

> "Chat Mode achieved 100% retrieval success andM= 0.880 generated answer quality (95% CI [0.879, 0.882]), both exceeding target."

### Rumble 2026 (2)

Rumble, T., Zarrin, J., Lovell, P. G., Falconer, R. (2026). Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System. arXiv. https://arxiv.org/abs/2607.13370. [doi:10.48550/arxiv.2607.13370](https://doi.org/10.48550/arxiv.2607.13370)

`q1 · i?` · `design · r2`

The same simulation evaluation found Quiz Mode below its 0.80 target on KC Alignment; the authors' thematic analysis of feedback logs attributed this to prompt phrasing favouring recall over higher-order reasoning.

> "Quiz Mode's KC Alignment Score averagedM= 0.751
(95% CI [0.745, 0.757]), below target, with thematic analysis [53] of feedback logs
suggesting prompt phrasing favoured recall over higher-order reasoning."

## Discussion


## Related Claims
- [Quiz mode's course-blind Python question generation was the only cross-course failure requiring a code change during onboarding](course-blind-code-question-generation-failure.md) — related
- [In an exploratory pilot (n=8), students rated LEA's usability, Chat Mode, Quiz Mode, learning outcomes, and trust positively, with Chat Mode the strongest performer](lea-pilot-positive-usability-chat-quiz-trust.md) — related
- [A question-repetition bug in Quiz Mode, reported by 2/8 pilot participants, was a defect simulation-based evaluation could not identify](quiz-repetition-bug-simulation-blind-spot.md) — related
- [Tutor Mode's adaptive responsiveness was overestimated by simulation: only 3/8 pilot participants agreed LEA adapted appropriately when they expressed uncertainty](simulation-overestimated-tutor-adaptiveness.md) — reports the opposite
