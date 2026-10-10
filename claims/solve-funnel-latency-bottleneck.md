---
type: claim
title: "System reliability and latency acted as a prerequisite bottleneck: 56.4% of started solves completed, with a 32.0-second average latency and 68.5-second p90"
description: "System reliability and latency acted as a prerequisite bottleneck: 56.4% of started solves completed, with a 32.0-second average latency and 68.5-second p90"
id: solve-funnel-latency-bottleneck
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: solve-funnel
    title: solve-funnel
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: solve-latency
    title: solve-latency
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# System reliability and latency acted as a prerequisite bottleneck: 56.4% of started solves completed, with a 32.0-second average latency and 68.5-second p90

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r3` · `q2`

## Subclaims
`q2 i?` Students started 149 solve attempts and 84 completed successfully (56.4%), a funnel the authors treat as combining user behavior with a system-stability event. [→ solve-funnel](#solve-funnel)
`q2 i?` Average solve latency was 32.0 seconds with p90 at 68.5 seconds, disrupting cognitive momentum and causing premature abandonment. [→ solve-latency](#solve-latency)

## Evidence

### solve-funnel

Harry Feng, Yuan Tian, and Erica Zhao. 2026. From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments. https://arxiv.org/abs/2607.01692

`q2 · i?` · `design · r3`

Telemetry funnel from the 12-day field deployment. The article cautions this "should not be interpreted as simple user disinterest" because a reliability breakdown on May 20–21 depressed completion.

> "students started 149 solve attempts, and 84 completed successfully, yielding a 56.4% completion rate."

### solve-latency

Harry Feng, Yuan Tian, and Erica Zhao. 2026. From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments. https://arxiv.org/abs/2607.01692

`q2 · i?` · `design · r3`

Latency telemetry from the same deployment; the authors state prolonged waits "directly disrupt[ed] students' cognitive momentum and caus[ed] premature abandonment."

> "the average solve latency was 32.0 seconds, with the p90 reaching 68.5 seconds."

## Discussion


## Related Claims
- [Follow-up support shows low initiation but reliable completion: the bottleneck is noticing and composing the question, not the AI's ability to answer](followup-low-initiation-high-completion.md) — related
- [Students rarely open transfer-practice cards immediately after solving; they want such problems organized into delayed, spaced wrong-book review instead](transfer-practice-timing-mismatch-delayed-review.md) — related
