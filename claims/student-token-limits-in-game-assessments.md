---
type: claim
title: "Student-scoped API access limits in-game assessment rendering: student tokens return no question content and no endpoints exist for posting answers"
description: "Student-scoped API access limits in-game assessment rendering: student tokens return no question content and no endpoints exist for posting answers"
id: student-token-limits-in-game-assessments
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: araz-yusubov-2026
    resource: "https://github.com/ADA-SITE-SITE4890-2023-Spring/senior-design-project-ay5-gamification-2-0-unity-bb/"
    title: "Araz Yusubov, Tangiz Alizada, Michael Bechtel. (2026). Hypergamigication Through Integrating Game Engines and Learning Management Systems: Ender's Game. https://github.com/ADA-SITE-SITE4890-2023-Spring/senior-design-project-ay5-gamification-2-0-unity-bb/"
    author: Araz Yusubov, Tangiz Alizada, Michael Bechtel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Student-scoped API access limits in-game assessment rendering: student tokens return no question content and no endpoints exist for posting answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the pilot's API testing, requests with a student token returned no question content and no endpoints existed for posting runtime student answers, limiting rendering of assessment questions in games. [→ Araz Yusubov 2026](#araz-yusubov-2026)

## Evidence

### Araz Yusubov 2026

Araz Yusubov, Tangiz Alizada, Michael Bechtel. (2026). Hypergamigication Through Integrating Game Engines and Learning Management Systems: Ender's Game. https://github.com/ADA-SITE-SITE4890-2023-Spring/senior-design-project-ay5-gamification-2-0-unity-bb/

`q2 · i?` · `design · r2`

Technical API testing during the pilot implementation: the team tested retrieving assessment details including questions and answer options. Administrator or instructor-scoped tokens returned populated question schemas, while "Requests initiated with a student token returned no question content". No effect sizes apply; this is a documented technical limitation.

> "Requests initiated with a student token returned no question content. Furthermore, there w ere no endpoints for posting runtime student answers. This limit s the possibility of rendering assessments questions in a game environment."

## Discussion


## Related Claims
- [A pilot implementation produced a working Unity package and demo game integrating Unity with Blackboard via Learn APIs](pilot-unity-blackboard-working-prototype.md) — related
