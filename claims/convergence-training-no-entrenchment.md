---
type: claim
title: Language models showed substantial L1 loss from before to after longer L1 training to convergence, in one group with no comparison group
description: Language models showed substantial L1 loss from before to after longer L1 training to convergence, in one group with no comparison group.
id: convergence-training-no-entrenchment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: ionut-constantinescu-2025
    resource: "https://doi.org/10.1162/tacl_a_00725"
    title: "Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2025). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. Originally published 2024. [doi:10.1162/tacl_a_00725](https://doi.org/10.1162/tacl_a_00725)"
    author: Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Language models showed substantial L1 loss from before to after longer L1 training to convergence, in one group with no comparison group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` L1 performance in the SEQUENTIAL condition showed a substantial loss from before to after 48 epochs of L1 training, in one group with no comparison group. [→ Ionut Constantinescu 2025](#ionut-constantinescu-2025)

## Evidence

### Ionut Constantinescu 2025

Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2025). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. Originally published 2024. [doi:10.1162/tacl_a_00725](https://doi.org/10.1162/tacl_a_00725)

`q2 · i?` · `causal · r1`

Experiment 3 trained models to convergence (48 epochs per language, one run per condition, no SEQUENTIAL-INTERLEAVED). The paper reports "a substantial loss in L1 performance in the SEQUENTIAL condition" despite the longer training.

> "We still see a substantial loss in L1 performance in the SEQUENTIAL condition, indicating that longer L1 training does not lead to entrenchment, though these PPL scores are for fi and de, and thus are not directly comparable to the en from other experiments."

## Discussion


## Related Claims
- [Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period](lms-catastrophic-l1-attrition-sequential.md) — related
- [Language models show no critical period for L2 acquisition: delayed L2 exposure does not improve L2 performance](lms-no-critical-period-l2-acquisition.md) — related
- [Late-learned L2 lexical representations are parasitic on L1: the later L2 is learned, the less well organized and more fragmented its representations](late-l2-parasitic-entrenched-representations.md) — related
