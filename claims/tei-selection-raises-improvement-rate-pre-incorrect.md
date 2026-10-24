---
type: claim
title: "TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base"
description: "TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base"
id: tei-selection-raises-improvement-rate-pre-incorrect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tei-selection-1
    resource: "https://doi.org/10.48550/arxiv.2605.30666"
    title: tei-selection-1
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# TEI@N inference-time selection raises the improvement rate on pre-incorrect math scenarios from 59.0% to 81.9% at N=8 over Greedy on a frozen DeepSeek-R1-8B base

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` At N=8, TEI@N reaches an 81.9% improvement rate versus Greedy's 59.0% (+22.9pp) on pre-incorrect scenarios, with no training and no external judge. [→ tei-selection-1](#tei-selection-1)

## Evidence

### tei-selection-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666 [doi:10.48550/arxiv.2605.30666](https://doi.org/10.48550/arxiv.2605.30666)

`q2 · i?` · `causal · r2`

Block-grouped selection experiment on the pre-incorrect subset of 1,000 in-domain BigMath tutoring scenarios (n=363 pre-incorrect), 20 random repeats per N, DeepSeek-R1-8B base. "TEI@𝑁 reaches81.9%versus Greedy59 .0%(+22.9pp)"; no effect size printed.

> "At𝑁= 8, TEI@𝑁 reaches81.9%versus Greedy59 .0%(+22.9pp). The gap is stable across𝑁 ; DTR@𝑁 trails TEI@𝑁 by13to15pp at every𝑁, and Random@𝑁never exceeds Greedy."

## Discussion


## Related Claims
- [On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost](tei4-beats-dtr4-and-greedy-same-base.md) — related
- [TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model](tei4-selects-deliberation-rich-candidates.md) — related
