---
type: claim
title: API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility
description: API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility
id: api-versus-custom-gpt-complementary-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: abreu-m-2026
    resource: "https://doi.org/10.1088/1361-6552/ae8110"
    title: "Abreu M, Suárez A, Stari C and Martí A C. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. Originally published 2025. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)"
    author: Abreu M, Suárez A, Stari C and Martí A C.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# API-based evaluation is efficient for large-scale processing but struggles with graphical content, while customized ChatGPT gives more contextualized feedback with lower reproducibility

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The two interaction modalities showed complementary strengths: the API mode was efficient but weak on graphics, and the custom mode was contextualized but less reproducible. [→ Abreu M 2026](#abreu-m-2026)

## Evidence

### Abreu M 2026

Abreu M, Suárez A, Stari C and Martí A C. (2026). Exploring the potential of ChatGPT for feedback and evaluation in experimental physics. Originally published 2025. [doi:10.1088/1361-6552/ae8110](https://doi.org/10.1088/1361-6552/ae8110)

`q2 · i?` · `design · r2`

Comparative discussion of the two evaluation modalities applied to approximately 50 laboratory reports from the 2024 Experimental Physics I course. The article states the API approach "proved efficient for large-scale processing" while the customized interaction generated "more contextualized feedback, though with lower reproducibility".

> "the API-based approach proved efficient for large-scale processing but struggled with graphical and mathematical content, whereas the customized ChatGPT interaction generated more contextualized feedback, though with lower reproducibility."

## Discussion


## Related Claims
- [API-based evaluation fails on graphical and mathematical content because the model cannot parse images, tables, graphs and embedded equations](chatgpt-api-cannot-parse-figures-equations.md) — a narrower finding that bears on this claim
- [The customized Physics Instructor GPT gives balanced formal feedback and can offer conceptually nuanced technical observations, but with greater variability](custom-gpt-balanced-context-sensitive-feedback.md) — a narrower finding that bears on this claim
- [The customized ChatGPT can accurately process graphical information when images are submitted directly through the interface](custom-gpt-direct-image-submission-accurate.md) — related
- [GPT-4 struggles with diagrammatical and graphical questions, though it can describe visual content accurately in prose.](gpt4-diagrammatic-question-weakness.md) — related
- [Switching from reference-based to contextual evaluation prompts improved GenAI grading accuracy](contextual-evaluation-prompt-improvement.md) — related
- [In API-based evaluation, ChatGPT consistently assesses the formal and structural aspects of physics laboratory reports](chatgpt-api-consistent-formal-assessment.md) — related
