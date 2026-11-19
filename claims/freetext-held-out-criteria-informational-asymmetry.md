---
type: claim
title: Held-out grading criteria create an informational asymmetry between the LLM evaluator and the student
description: Held-out grading criteria create an informational asymmetry between the LLM evaluator and the student
id: freetext-held-out-criteria-informational-asymmetry
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: matelsky-2023
    resource: "https://doi.org/10.48550/arXiv.2308.02439"
    title: "Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P. (2023). A large language model-assisted education tool to provide feedback on open-ended responses. arXiv preprint. [doi:10.48550/arXiv.2308.02439](https://doi.org/10.48550/arXiv.2308.02439)"
    author: "Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P."
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Held-out grading criteria create an informational asymmetry between the LLM evaluator and the student

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The intermediary server supplies the LLM with rubric information hidden from the student, which the authors describe as a useful asymmetry between evaluator and student. [→ Matelsky 2023](#matelsky-2023)

## Evidence

### Matelsky 2023

Matelsky, J. K., Parodi, F., Liu, T., Lange, R. D., & Kording, K. P. (2023). A large language model-assisted education tool to provide feedback on open-ended responses. arXiv preprint. [doi:10.48550/arXiv.2308.02439](https://doi.org/10.48550/arXiv.2308.02439)

`q2 · i?` · `design · r1`

Design description from the Approach section: the server pairs the student response with instructor criteria that are "not revealed to the student," forming the LLM payload. This is a definitional/design claim about the system, not a tested result.

> "A distinctive feature of our system is the intermediary server which equips the large language model with 'held-out' information, such as a rubric for correct responses, accessible only to the LLM and instructor, and not to the student."

## Discussion


## Related Claims
- [Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form](open-weight-proprietary-rubric-equivalence.md) — related
- [LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other](llm-short-answer-graders-can-reach-human-rater-agreement.md) — related
