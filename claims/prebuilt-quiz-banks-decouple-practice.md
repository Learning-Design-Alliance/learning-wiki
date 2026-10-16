---
type: claim
title: Prebuilt quiz banks of 435 questions across 65 modules decouple practice from live generation, with warm practice-request medians of 4.8 and 5.8 ms
description: Prebuilt quiz banks of 435 questions across 65 modules decouple practice from live generation, with warm practice-request medians of 4.8 and 5.8 ms
id: prebuilt-quiz-banks-decouple-practice
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sidney-shapiro-and-joshua-lindemann-2026
    resource: "https://doi.org/10.48550/arxiv.2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sidney-shapiro-and-joshua-lindemann-2026-2
    resource: "https://arxiv.org/abs/2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prebuilt quiz banks of 435 questions across 65 modules decouple practice from live generation, with warm practice-request medians of 4.8 and 5.8 ms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The deployed banks total 435 prepared items covering 65 configured modules, and practice uses stored keys and feedback without live generation. [→ Sidney Shapiro and Joshua Lindemann 2026](#sidney-shapiro-and-joshua-lindemann-2026)
`q2 i?` A 166-request live API audit found warm medians of 4.8 ms on Node A and 5.8 ms on Node B for stored quiz operations. [→ Sidney Shapiro and Joshua Lindemann 2026 (2)](#sidney-shapiro-and-joshua-lindemann-2026-2)

## Evidence

### Sidney Shapiro and Joshua Lindemann 2026

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)

`q2 · i?` · `design · r2`

System description of quiz mode across Courses 1–6: "The 435 prepared items cover 65 configured modules", with deterministic grading against the bank and answer keys kept server-side until an attempt or reveal.

> "The 435 prepared items cover 65 configured modules, and practice uses stored keys and feedback without live generation."

### Sidney Shapiro and Joshua Lindemann 2026 (2)

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510

`q2 · i?` · `design · r2`

A separate 166-request live API audit covering all 65 module starts on each node plus warm repeats, hints, and graded answers; the section reports "Warm medians were 4.8 ms on Node A and 5.8 ms on Node B".

> "Warm medians were 4.8 ms on Node A and 5.8 ms on Node B, measured server-local."

## Discussion


## Related Claims
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
