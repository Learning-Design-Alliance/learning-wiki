---
type: claim
title: "Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models"
description: "Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models"
id: hint-not-solution-most-challenging-dimension
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

# Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Models varied widely in guiding students without giving away answers: gpt-oss:20b and olmo-3:7b scored 6% by consistently providing direct solutions, while gemma-4:31b, gemma3:27b, and nemotron-3-super reached 81%. [→ H. Chad Lane 2026](#h-chad-lane-2026)

## Evidence

### H. Chad Lane 2026

H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench

`q2 · i?` · `design · r2`

Per-criterion scoring of the 8 debugging questions in Trial 2 (Table 2), judged by Claude Sonnet 4 with hybrid review. The lowest scorers "consistently provide direct solutions"; the discussion attributes gpt-oss:20b's 6% to a helpfulness compulsion that completes next steps for the student. No effect sizes are printed.

> "Hint_not_solution, which measures whether a model can guide a student toward a solution without giving it away, is the most challenging dimension. Scores range from 6% (gpt-oss:20b and olmo-3:7b, which consistently provide direct solutions) to 81%"

## Discussion


## Related Claims
- [Unguarded answer-giving AI harmed unaided exam performance while a guarded version of the same model erased the harm (Bastani et al., 2025, as reported)](guarded-ai-placement-prevents-unaided-exam-harm.md) — related
- [AI assistance reduces persistence: persistence costs concentrate among learners who used AI for direct solutions, not hints](ai-assistance-persistence-costs-direct-solutions.md) — related
- [Review reports a field experiment in which GPT access improved supported practice but was followed by poorer unaided test performance, mitigated by a guarded tutor](gpt-access-supported-practice-poorer-unaided-test.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided](models-struggle-acknowledging-debugging-progression.md) — related
