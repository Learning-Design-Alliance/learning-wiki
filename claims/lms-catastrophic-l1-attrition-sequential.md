---
type: claim
title: Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period
description: Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period
id: lms-catastrophic-l1-attrition-sequential
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

# Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the SEQUENTIAL condition, LMs rapidly lose L1 knowledge after L2 exposure begins, with final L1 perplexity indicating they forget almost everything learned before. [→ Ionut Constantinescu 2025](#ionut-constantinescu-2025)
`q2 i?` Continued L1 exposure in the SEQUENTIAL-INTERLEAVED condition completely mitigates L1 loss. [→ Ionut Constantinescu 2025](#ionut-constantinescu-2025)

## Evidence

### Ionut Constantinescu 2025

Ionut Constantinescu, Tiago Pimentel, Ryan Cotterell, Alex Warstadt. (2025). Investigating Critical Period Effects in Language Acquisition through Neural Language Models. arXiv. Originally published 2024. [doi:10.1162/tacl_a_00725](https://doi.org/10.1162/tacl_a_00725)

`q2 · i?` · `causal · r2`

Experiment 2 reversed the language order (English as L1, German/Finnish as L2) so all three benchmarks could track L1 across training. The paper reports LMs "rapidly lose the knowledge acquired from L1 learning after L2 exposure is started".

> "In this condition, LMs rapidly lose the knowledge acquired from L1 learning after L2 exposure is started. The final L1 perplexity values indicate that, in the end, the LMs forget almost everything that they have learned before."

## Discussion


## Related Claims
- [Catastrophic forgetting is prevalent when fine-tuning LLMs, risking loss of general knowledge in customized educational models](catastrophic-forgetting-llm-fine-tuning.md) — related
- [Language models showed substantial L1 loss from before to after longer L1 training to convergence, in one group with no comparison group](convergence-training-no-entrenchment.md) — related
- [L1–L2 relatedness affects L2 perplexity but not BLiMP grammatical performance unless plasticity is reduced](language-relatedness-ppl-not-blimp.md) — related
- [Language models show no critical period for L2 acquisition: delayed L2 exposure does not improve L2 performance](lms-no-critical-period-l2-acquisition.md) — related
