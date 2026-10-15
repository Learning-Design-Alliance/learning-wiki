---
type: claim
title: Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request
description: Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request
id: load-test-100-concurrent-users-30-second-response
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: zaki-kurdya-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05842"
    title: "Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad. (2026). Taklif.AI: LLM-Powered Platform for Interest-Based Personalized College Assignments. https://arxiv.org/abs/2605.05842 [doi:10.48550/arxiv.2605.05842](https://doi.org/10.48550/arxiv.2605.05842)"
    author: Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` In performance testing simulating 100 concurrent users generating assignments simultaneously, the platform yielded an average end-to-end response time of 30 seconds per request with no significant resource bottlenecks detected. [→ Zaki Kurdya 2026](#zaki-kurdya-2026)

## Evidence

### Zaki Kurdya 2026

Zaki Kurdya, Mohammed Zuqlam, Salem Amassi, Shady Telbany, Motaz Saad. (2026). Taklif.AI: LLM-Powered Platform for Interest-Based Personalized College Assignments. https://arxiv.org/abs/2605.05842 [doi:10.48550/arxiv.2605.05842](https://doi.org/10.48550/arxiv.2605.05842)

`q1 · i?` · `design · r2`

System performance (load) testing of the serverless architecture, including LLM inference via Groq's optimized Llama 3.3 70B endpoint. The scenario "simulating 100 concurrent users" produced the 30-second average response time; the serverless architecture auto-scales and LiteLLM reroutes requests on provider latency. No effect size is printed.

> "A scenario simulating 100 concurrent users generating assignments simultaneously yielded an average end-to-end response time of 30 seconds per request"

## Discussion


## Related Claims
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
- [In preliminary user acceptance testing, 84% of participants rated Taklif.AI's personalization feature as beneficial](uat-84-percent-rate-personalization-beneficial.md) — related
- [Asynchronous concurrent execution bounds overall latency to approximately the slowest individual model's inference time](async-concurrency-latency-bounded-by-slowest-model.md) — related
