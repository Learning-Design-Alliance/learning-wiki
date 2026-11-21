---
type: claim
title: Live feedback tags provided only modest adaptability gains under a five-tag turn-end schema
description: Live feedback tags provided only modest adaptability gains under a five-tag turn-end schema
id: live-feedback-tags-modest-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: bhavishya-tarun-2025
    resource: "https://doi.org/10.1109/fie63693.2025.11328658"
    title: "Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)"
    author: Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: bhavishya-tarun-2025-2
    resource: "https://doi.org/10.1109/fie63693.2025.11328658"
    title: "Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)"
    author: Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Live feedback tags provided only modest adaptability gains under a five-tag turn-end schema

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Adding live feedback tags to personalization yielded an Adaptability score of 4.55, lower than static personalization alone (5.43). [→ Bhavishya Tarun 2025](#bhavishya-tarun-2025)
`q2 i?` Feedback tags were used sparingly, with only 19 tags recorded across all turns (about 9.5% of turns). [→ Bhavishya Tarun 2025 (2)](#bhavishya-tarun-2025-2)

## Evidence

### Bhavishya Tarun 2025

Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)

`q2 · i?` · `causal · r1`

Comparative pipeline evaluation showing the Personalized + Feedback pipeline scored 4.55 on Adaptability versus 5.43 for static Personalized. Authors note tags "applied only at the end of each turn, provide limited real-time improvement."

> "The modest gain from feedback tags suggests that our five feedback tags, applied only at the end of each turn, provide limited real-time improvement."

### Bhavishya Tarun 2025 (2)

Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)

`q2 · i?` · `design · r2`

Turn-level tag counts across eight sessions show sparse engagement: Excellent 3, Very Helpful 5, Average 6, Poor 3, Terrible 2 — "only 19 tags were recorded across all turns".

> "Live feedback was used sparingly—only 19 tags were recorded across all turns (see Table III)."

## Discussion


## Related Claims
- [In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios](prompt-router-beats-static-baselines-simulation.md) — related
- [Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance](sim-to-real-strategy-shift-feynman-to-coach.md) — related
- [Static onboarding metadata personalization yields the highest adaptability scores in AI tutoring responses](static-onboarding-metadata-highest-adaptability.md) — related
