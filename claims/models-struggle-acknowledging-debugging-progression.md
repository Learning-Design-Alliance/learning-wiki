---
type: claim
title: "Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided"
description: "Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided"
id: models-struggle-acknowledging-debugging-progression
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: h-chad-lane-2026
    resource: "https://github.com/InviteInstitute/CSTutorBench"
    title: "H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench"
    author: H. Chad Lane, Bryson Kageler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the six iterative debugging questions, acknowledges_progression scores ranged from 8% to 67%, indicating most models fail to build on the student's prior attempts. [→ H. Chad Lane 2026](#h-chad-lane-2026)

## Evidence

### H. Chad Lane 2026

H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench

`q2 · i?` · `design · r2`

Trial 2 per-criterion scoring of the 6 debugging_iterative questions, judged by Claude Sonnet 4 with hybrid review. Each entry provides 2–3 code snapshots of the student's self-directed fix attempts, and the dedicated criterion evaluates whether the response recognizes and builds on these prior attempts. No effect sizes are printed.

> "acknowledges_progression(scored on 6 iterative debugging questions) ranged from 8% to 67%, indicating that most models struggle to engage meaningfully with a student’s prior attempts even when that history is provided as context."

## Discussion


## Related Claims
- [Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models](hint-not-solution-most-challenging-dimension.md) — related
- [Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness](student-context-personalization-improves-tutor-metrics.md) — related
