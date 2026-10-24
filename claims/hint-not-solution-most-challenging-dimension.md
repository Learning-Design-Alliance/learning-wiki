---
type: claim
title: "Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models"
description: "Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models"
id: hint-not-solution-most-challenging-dimension
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-17
recheck_by: 2029
sources:
  - id: h-chad-lane-2026
    resource: "https://doi.org/10.1145/3770761.3777333"
    title: "H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench [doi:10.1145/3770761.3777333](https://doi.org/10.1145/3770761.3777333)"
    author: H. Chad Lane, Bryson Kageler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-17 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models varied widely in guiding students without giving away answers: gpt-oss:20b and olmo-3:7b scored 6% by consistently providing direct solutions, while gemma-4:31b, gemma3:27b, and nemotron-3-super reached 81%. [→ H. Chad Lane 2026](#h-chad-lane-2026)

## Evidence

### H. Chad Lane 2026

H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench [doi:10.1145/3770761.3777333](https://doi.org/10.1145/3770761.3777333)

`q2 · i?` · `design · r2`

Per-criterion scoring of the 8 debugging questions in Trial 2 (Table 2), judged by Claude Sonnet 4 with hybrid review. The lowest scorers "consistently provide direct solutions"; the discussion attributes gpt-oss:20b's 6% to a helpfulness compulsion that completes next steps for the student. No effect sizes are printed.

> "Hint_not_solution, which measures whether a model can guide a student toward a solution without giving it away, is the most challenging dimension. Scores range from 6% (gpt-oss:20b and olmo-3:7b, which consistently provide direct solutions) to 81%"

## Discussion

## Related Claims

- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](persistence-costs-concentrated-among-direct-solution-users.md) — the general claim this finding bears on, with the studies behind it
- [Unguarded answer-giving AI harmed unaided exam performance while a guarded version of the same model erased the harm (Bastani et al., 2025, as reported)](gpt4-access-harms-learning-after-withdrawal.md) — related
- [AI assistance reduces persistence: persistence costs concentrate among learners who used AI for direct solutions, not hints](ai-assistance-persistence-costs-direct-solutions.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided](models-struggle-acknowledging-debugging-progression.md) — related
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](gpt4-feedback-66-percent-targeted-35-percent-flawed.md) — related
- [Preference explanations favoring LearnLM more often cite staying on topic, challenging the learner, and not giving away answers](learnlm-preference-explanation-themes.md) — related
- [GPT-generated hints are moderately accessible by automated readability metrics (mean CAREC 0.128, mean CML2RI 3.95)](gpt-hints-moderately-accessible-readability.md) — related
