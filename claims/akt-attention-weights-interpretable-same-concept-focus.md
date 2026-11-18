---
type: claim
title: "AKT's learned attention weights are interpretable, operating at multiple time scales and focusing on past practices of the same concept"
description: "AKT's learned attention weights are interpretable, operating at multiple time scales and focusing on past practices of the same concept"
id: akt-attention-weights-interpretable-same-concept-focus
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
sources:
  - id: aritra-ghosh-2020
    title: Aritra Ghosh 2020
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: aritra-ghosh-2020-2
    title: Aritra Ghosh 2020 (2)
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# AKT's learned attention weights are interpretable, operating at multiple time scales and focusing on past practices of the same concept

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q1`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Visualized attention heads each operate on their own time scale, with attention windows of different widths. [→ Aritra Ghosh 2020](#aritra-ghosh-2020)
`q1 i?` AKT predicts a learner's response by focusing more on previous practices of the current concept than on immediate-past practices of another concept. [→ Aritra Ghosh 2020 (2)](#aritra-ghosh-2020-2)

## Evidence

### Aritra Ghosh 2020

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q1 · i?` · `design · r2`

Case study visualizing knowledge-retriever attention weights for one learner's 20 consecutive practice questions across three attention heads on ASSISTments2009; "each attention head operates on its own time scale."

> "We see that each attention head operates on its own time scale: they all have attention windows of different widths."

### Aritra Ghosh 2020 (2)

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q1 · i?` · `design · r2`

Case study of normalized attention weights for one learner across three consecutive time steps on ASSISTments2009; AKT focuses "more on previous practices on this concept" than on another concept practiced in the immediate past.

> "We see that AKT predicts their response to the current question by focusing more on previous practices on this concept (both in the immediate past and further back) than practices on another concept also in the immediate past."

## Discussion


## Related Claims
- [Injecting the collaborative prior redistributes AKT's attention from local recency bias toward long-range dependencies](mbp-kt-attention-recency-to-long-range.md) — related
- [AKT's learned Rasch difficulty parameters order questions within a concept and match intuitive difficulty levels](akt-learned-difficulty-parameters-match-intuition.md) — related
- [The survey reports, citing Pu and Becker, that removing students' repeated interactions on the same exercises reduced AKT's performance to close to that of DKVMN.](attentive-knowledge-tracing-benefits-from-repeated-interactions.md) — related
