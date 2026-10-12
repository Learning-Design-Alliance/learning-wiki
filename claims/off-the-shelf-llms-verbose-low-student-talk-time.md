---
type: claim
title: "Off-the-shelf LLM tutors are more verbose than human tutors, leaving students only 5-15% of talk time versus close to 30% in human tutoring"
description: "Off-the-shelf LLM tutors are more verbose than human tutors, leaving students only 5-15% of talk time versus close to 30% in human tutoring"
id: off-the-shelf-llms-verbose-low-student-talk-time
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: janos-perczel-2025
    resource: "https://arxiv.org/abs/2510.05087"
    title: "Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087"
    author: Janos Perczel, Jin Chow, and Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Off-the-shelf LLM tutors are more verbose than human tutors, leaving students only 5-15% of talk time versus close to 30% in human tutoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In benchmark simulations, off-the-shelf models leave students 5-15% of talk time while human tutors leave students close to 30%. [→ Janos Perczel 2025](#janos-perczel-2025)

## Evidence

### Janos Perczel 2025

Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087

`q2 · i?` · `design · r2`

Benchmarking study (Fig. 6) comparing human tutors from 80,000 hours of Polygence data with state-of-the-art LLMs from OpenAI, Google, Anthropic, Meta, and XAI using the fine-tuned student model protocol. Human tutors also speak only 72 words per turn versus 150-300 for most models.

> "In Fig. 6(a), we find that in human-to-human tutor-led dialogues students speak close to 30% of the time. Off-the-shelf models are typically more verbose than humans, leaving only 5-15% of talk time to students."

## Discussion


## Related Claims
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
