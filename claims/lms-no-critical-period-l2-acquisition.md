---
type: claim
title: "Language models show no critical period for L2 acquisition: delayed L2 exposure does not improve L2 performance"
description: "Language models show no critical period for L2 acquisition: delayed L2 exposure does not improve L2 performance"
id: lms-no-critical-period-l2-acquisition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: ionut-constantinescu-2025
    resource: "https://doi.org/10.1162/tacl_a_00725"
    title: "Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2025). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. Originally published 2024. [doi:10.1162/tacl_a_00725](https://doi.org/10.1162/tacl_a_00725)"
    author: Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Language models show no critical period for L2 acquisition: delayed L2 exposure does not improve L2 performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Final L2 performance is worse (or at least not different) in the INTERLEAVED condition than in the SEQUENTIAL condition, the opposite of the human age-of-exposure pattern. [→ Ionut Constantinescu 2025](#ionut-constantinescu-2025)

## Evidence

### Ionut Constantinescu 2025

Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2025). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. Originally published 2024. [doi:10.1162/tacl_a_00725](https://doi.org/10.1162/tacl_a_00725)

`q2 · i?` · `causal · r2`

Simulation experiments training GPT-2 and RoBERTa from scratch on German–English and Finnish–English pairs (600M tokens per language, 6 or 48 epochs) across five training schedules. The paper reports that "final performance in L2 is worse (or at least not different) in the INTERLEAVED than in the SEQUENTIAL condition".

> "In experiments 1 and 3 (Figs. 2 and 4), we consistently find that final performance in L2 is worse (or at least not different) in the INTERLEAVED than in the SEQUENTIAL condition."

## Discussion


## Related Claims
- [Language models showed substantial L1 loss from before to after longer L1 training to convergence, in one group with no comparison group](convergence-training-no-entrenchment.md) — related
- [Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period](lms-catastrophic-l1-attrition-sequential.md) — related
- [Distributed practice benefits L2 learning, and one review argues that spreading it over years can be worse than over months](distributed-practice-limits-l2.md) — related
- [Simultaneous and sequential DLL learners show opposite vocabulary patterns in English versus the home language](simultaneous-sequential-vocabulary-differences.md) — related
