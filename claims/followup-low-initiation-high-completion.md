---
type: claim
title: "Follow-up support shows low initiation but reliable completion: the bottleneck is noticing and composing the question, not the AI's ability to answer"
description: "Follow-up support shows low initiation but reliable completion: the bottleneck is noticing and composing the question, not the AI's ability to answer"
id: followup-low-initiation-high-completion
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: followup-funnel
    title: followup-funnel
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Follow-up support shows low initiation but reliable completion: the bottleneck is noticing and composing the question, not the AI's ability to answer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Across 140 result-screen runs, students opened the follow-up interface 14 times (10.0%) and submitted 12 follow-up questions (8.6%), but all 12 submitted follow-ups reached first content. [→ followup-funnel](#followup-funnel)

## Evidence

### followup-funnel

Harry Feng, Yuan Tian, and Erica Zhao. 2026. From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments. https://arxiv.org/abs/2607.01692

`q2 · i?` · `design · r3`

Telemetry funnel analysis from the 12-day field deployment (7,379 backend events across 104 valid sessions). The article reports "students opened the follow-up interface 14 times (10.0%)" and that all 12 submitted questions reached first content, so the bottleneck was initiation.

> "Across 140 result-screen runs, students opened the follow-up interface 14 times (10.0%) and submitted 12 follow-up questions (8.6%, Figure 7)."

## Discussion


## Related Claims
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
- [System reliability and latency acted as a prerequisite bottleneck: 56.4% of started solves completed, with a 32.0-second average latency and 68.5-second p90](solve-funnel-latency-bottleneck.md) — related
- [Distress and depression screening improved detection but did not reliably enhance psychological or medical outcomes when follow-up pathways were absent](screening-without-followup-insufficient.md) — related
