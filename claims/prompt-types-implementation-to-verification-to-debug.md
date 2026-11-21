---
type: claim
title: "Student prompt types shifted from implementation-driven (2023, 42.67% Code Implementation) to verification-driven (2024, 52.25% Code Verification) to a balanced debug–verify–implement pattern (2025, 36.18% Error Message Interpretation)"
description: "Student prompt types shifted from implementation-driven (2023, 42.67% Code Implementation) to verification-driven (2024, 52.25% Code Verification) to a balanced debug–verify–implement pattern (2025, 36.18% Error Messa..."
id: prompt-types-implementation-to-verification-to-debug
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: boxuan-ma-2026
    resource: "https://doi.org/10.1145/3862769"
    title: "Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi. (2026). Three Years with Classroom AI in Introductory Programming: Shifts in Student Awareness, Interaction, and Performance. [doi:10.1145/3862769](https://doi.org/10.1145/3862769)"
    author: "Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: boxuan-ma-2026-2
    resource: "https://doi.org/10.1145/3862769"
    title: "Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi. (2026). Three Years with Classroom AI in Introductory Programming: Shifts in Student Awareness, Interaction, and Performance. [doi:10.1145/3862769](https://doi.org/10.1145/3862769)"
    author: "Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Student prompt types shifted from implementation-driven (2023, 42.67% Code Implementation) to verification-driven (2024, 52.25% Code Verification) to a balanced debug–verify–implement pattern (2025, 36.18% Error Message Interpretation)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Coded prompt-type distributions changed markedly across cohorts: Code Implementation dominated in 2023 (42.67%), Code Verification in 2024 (52.25%), and Error Message Interpretation rose to 36.18% in 2025. [→ Boxuan Ma 2026](#boxuan-ma-2026)
`q2 i?` By 2025, Error Message Interpretation rose to 36.18% while Code Verification (23.27%) and Code Implementation (17.28%) remained substantial, indicating a more iterative debug–verify–implement workflow. [→ Boxuan Ma 2026 (2)](#boxuan-ma-2026-2)

## Evidence

### Boxuan Ma 2026

Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi. (2026). Three Years with Classroom AI in Introductory Programming: Shifts in Student Awareness, Interaction, and Performance. [doi:10.1145/3862769](https://doi.org/10.1145/3862769)

`q2 · i?` · `associational · r1`

Thematic coding of stratified-sampled student–AI dialogue logs (Fig. 4), with prompt types coded using established codebooks (Cohen's κ .88 for student-prompt coding). The article reports Code Implementation dominated 2023 prompts at "42.67%"; descriptive percentages only.

> "In2023,students’promptsweredominatedbyCodeImplementationprompts (42.67%), indicating an implementation-driven pattern in which learners primar- ily asked the AI to help write or complete code."

### Boxuan Ma 2026 (2)

Boxuan Ma, Huiyong Li, Gen Li, Li Chen, Cheng Tang, Atsushi Shimada, and Shin'ichi Konomi. (2026). Three Years with Classroom AI in Introductory Programming: Shifts in Student Awareness, Interaction, and Performance. [doi:10.1145/3862769](https://doi.org/10.1145/3862769)

`q2 · i?` · `associational · r1`

Same coded dialogue-log analysis (Fig. 4), 2025 cohort. The article reports "Error MessageInterpretationroseto 36.18%" with Code Verification and Code Implementation remaining substantial; descriptive percentages only.

> "Error MessageInterpretationroseto 36.18%,while Code Verification (23.27%) and Code Implementation (17.28%) remained substantial."

## Discussion


## Related Claims
- [CS2 learners jumped directly into implementation without querying any learning support about the algorithm, and GenAI queries shifted toward debugging](learners-skip-pre-implementation-support-queries.md) — related
- [Prompting technique distribution shifts in teams, driven by students reporting no technique at all](prompting-technique-disengagement-in-teams.md) — related
- [Transition Network Analysis shows interaction workflows became structurally more iterative and dense across cohorts, from sparse short episodes (2023) to verification-centered loops (2024) to the densest, most strategy-mixed networks (2025)](tna-workflows-denser-more-iterative.md) — possibly the same claim (merge candidate)
