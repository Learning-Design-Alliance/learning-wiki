---
type: claim
title: "A deterministic follow-up resolver raised intended-topic follow-up rates to 90–100% across five courses with all 400 scope checks passing, without changing the generator"
description: "A deterministic follow-up resolver raised intended-topic follow-up rates to 90–100% across five courses with all 400 scope checks passing, without changing the generator"
id: deterministic-resolver-raises-topic-checks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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
  - id: sidney-shapiro-and-joshua-lindemann-2026-3
    resource: "https://arxiv.org/abs/2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A deterministic follow-up resolver raised intended-topic follow-up rates to 90–100% across five courses with all 400 scope checks passing, without changing the generator

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Topic checks rose from 23.3–40.0% in baseline resolver preflight to 90–100% live across five courses, with all 400 scope checks passing. [→ Sidney Shapiro and Joshua Lindemann 2026](#sidney-shapiro-and-joshua-lindemann-2026)
`q2 i?` In the five-course run all 400 scope checks passed with zero API errors and each course reached the 90% follow-up target, while median per-turn latency ranged from 3.24 to 6.19 s. [→ Sidney Shapiro and Joshua Lindemann 2026 (2)](#sidney-shapiro-and-joshua-lindemann-2026-2)
`q2 i?` The 20 September router extension passed 306 focused Python tests and documented live probes on both nodes before activation. [→ Sidney Shapiro and Joshua Lindemann 2026 (3)](#sidney-shapiro-and-joshua-lindemann-2026-3)

## Evidence

### Sidney Shapiro and Joshua Lindemann 2026

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)

`q2 · i?` · `design · r2`

Multi-turn conversation evaluation with frozen fixtures of 20 dialogues and 80 turns per course; the decision summary reports topic checks rising "to 90–100% live across five courses" with the unchanged 8B generator.

> "Topic checks rose from 23.3–40.0% in baseline resolver preflight to 90–100% live across five courses; all 400 scope checks passed."

### Sidney Shapiro and Joshua Lindemann 2026 (2)

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510

`q2 · i?` · `design · r2`

The evaluation section reports the live five-course replay on Node B: "all 400 scope checks passed with zero API errors"; median per-turn latency ranged from 3.24 to 6.19 s, and Course 1's median rose from 4.92 to 5.81 s.

> "In the five-course run, all 400 scope checks passed with zero API errors, and each course reached the 90% follow-up target."

### Sidney Shapiro and Joshua Lindemann 2026 (3)

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510

`q2 · i?` · `design · r2`

The router extension evaluation used a frozen contract of 32 crossover cases plus focused checks; the section reports "306 focused Python tests and the documented live probes" passed before activation on both nodes.

> "Both nodes passed 306 focused Python tests and the documented live probes before activation."

## Discussion


## Related Claims
- [A deterministic slide-image override converts a 0/9 corpus-grounding failure into 9/10 successful slide matches on the same topic](slide-image-override-corpus-grounding-recovery.md) — related
