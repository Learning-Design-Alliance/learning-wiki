---
type: claim
title: "During development testing, Taklif.AI guardrails rejected roughly 12% of interests, 8% of input documents, and 3% of generated assignments"
description: "During development testing, Taklif.AI guardrails rejected roughly 12% of interests, 8% of input documents, and 3% of generated assignments"
id: guardrails-rejection-rates-development-testing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: zaki-kurdya-2026
    resource: "https://arxiv.org/abs/2605.05842"
    title: "Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad. (2026). Taklif.AI: LLM-Powered Platform for Interest-Based Personalized College Assignments. https://arxiv.org/abs/2605.05842"
    author: Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# During development testing, Taklif.AI guardrails rejected roughly 12% of interests, 8% of input documents, and 3% of generated assignments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Across approximately 200 development-phase test inputs, interest guardrails rejected about 12% of submitted interests (including prompt injection attempts), assignment guardrails rejected about 8% of input documents, and output guardrails flagged about 3% of generated assignments. [→ Zaki Kurdya 2026](#zaki-kurdya-2026)

## Evidence

### Zaki Kurdya 2026

Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad. (2026). Taklif.AI: LLM-Powered Platform for Interest-Based Personalized College Assignments. https://arxiv.org/abs/2605.05842

`q1 · i?` · `design · r2`

Development-phase guardrails testing with approximately 200 test inputs. Interest guardrails rejected "approximately 12% of submitted interests", assignment guardrails about 8% of input documents (e.g., lecture notes, syllabi), and output guardrails flagged about 3% of generated assignments. No effect size is printed.

> "Theinterest guardrailsrejected approximately 12% of submitted interests, including single-character inputs, profanity, non-interest terms (e.g., “nothing,” “I don’t know”), and attempted prompt injection attacks"

## Discussion


## Related Claims
- [Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information](project-reports-exceed-bart-token-limit.md) — related
- [In preliminary user acceptance testing, 84% of participants rated Taklif.AI's personalization feature as beneficial](uat-84-percent-rate-personalization-beneficial.md) — related
