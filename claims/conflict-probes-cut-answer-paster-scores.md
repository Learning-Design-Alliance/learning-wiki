---
type: claim
title: "Adding conflict probes cut the answer-paster persona's scores from 4/6 + 1 to 0–1/6 in most later runs"
description: "Adding conflict probes cut the answer-paster persona's scores from 4/6 + 1 to 0–1/6 in most later runs"
id: conflict-probes-cut-answer-paster-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: byungmoon-cho-2026
    resource: "https://doi.org/10.48550/arXiv.2610.22949"
    title: "Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)"
    author: Byungmoon Cho
    q: 1
    i: "?"
    kind: design
    rigour: 3
---

# Adding conflict probes cut the answer-paster persona's scores from 4/6 + 1 to 0–1/6 in most later runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Before conflict probes were added (version 3) the answer-paster scored 4/6 + 1; after they were added (versions 5–8) it scored 0–1/6 + 0 in four of six runs, with two version-7 runs at 3/6 + 0. [→ Byungmoon Cho 2026](#byungmoon-cho-2026)

## Evidence

### Byungmoon Cho 2026

Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)

`q1 · i?` · `design · r3`

Scripted simulation comparison across agent versions: two rules worked together — each paste drew an own-words request (5.7), and the student's own words then met a conflict or Hold probe. "Neither accusation nor detection was involved." No effect size is printed.

> "Before conflict probes were added, at version 3, the answer-paster, which pasted an answer and then switched to its own words, scored 4/6 + 1. After they were added, on versions 5–8, it scored 0–1/6 + 0 in four of six runs; the other two, both on version 7, scored 3/6 + 0."

## Discussion


## Related Claims
- [Under versions 7–8, scripted personas produced distinct score profiles, with the self-corrector earning full bonus and the caver none](personas-distinct-score-profiles.md) — related
- [In the first full round on version 8, routing, summary-line consistency, and the own-example question were each correct in 5 of 5 runs, and all three prompt-injection attempts were refused](structural-reliability-five-of-five.md) — related
