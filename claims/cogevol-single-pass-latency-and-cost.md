---
type: claim
title: Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than flagship models
description: Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than...
id: cogevol-single-pass-latency-and-cost
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: cogevol-team-2026
    resource: "https://arxiv.org/abs/2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: cogevol-team-2026-2
    resource: "https://arxiv.org/abs/2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than flagship models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`

## Subclaims
`q2 i?` Over a seven-day live-traffic window the production models completed 180k slide generations at a median of 17s and 40k interactive pages at 59s. [→ CogEvol Team 2026](#cogevol-team-2026)
`q2 i?` At public list prices CogEvol-27B delivers near-flagship quality at 15–22× lower per-artifact API cost than Claude Opus 4.8 or GPT-5.4, and CogEvol-4B at ~100× lower. [→ CogEvol Team 2026 (2)](#cogevol-team-2026-2)

## Evidence

### CogEvol Team 2026

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

Production serving-database statistics (successful calls, seven-day window, August 2026) for the models serving OpenMAIC traffic. The report states these "are production numbers, not laboratory ones", with slides emitting ~1.8k output tokens and pages ~9k.

> "the production models behind these medians—same architecture and parameter count as CogEvol-27B, and therefore the same serving speed—completed 180k slide generations at a median (P95) of 17s (26s) and 40k interactive pages at 59s (107s)."

### CogEvol Team 2026 (2)

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

Cost comparison computed from token usage on the identical benchmark runs at public list prices (Figure 1b); the report frames cost as deciding "who gets to use the technology" for under-resourced users.

> "at public list prices, CogEvol-27B delivers near-flagship quality at 15–22× lower per-artifact API cost than Claude Opus 4.8 or GPT-5.4, and CogEvol-4B at∼100× lower."

## Discussion


## Related Claims
- [On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities](cogevol-benchmark-no-flagship-leads-both-modalities.md) — related
- [A deployment-hardening rehearsal with 50 distinct learner accounts recorded 50 completed sessions, 50 successful board pulls and 50 denials of student analytics access, with a median API session time of 3.064 s](hardening-rehearsal-50-sessions-and-access-denials.md) — related
