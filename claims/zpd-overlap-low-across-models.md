---
type: claim
title: "ZPDs of different LLMs differ significantly: Z✗→✓ and Z✗→✗ examples overlap little across models while Z✓ examples are largely shared"
description: "ZPDs of different LLMs differ significantly: Z✗→✓ and Z✗→✗ examples overlap little across models while Z✓ examples are largely shared"
id: zpd-overlap-low-across-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: peng-cui-2025
    resource: "https://doi.org/10.18653/v1/2025.findings-naacl.362"
    title: "Peng Cui, Mrinmaya Sachan. (2025). Investigating the Zone of Proximal Development of Language Models for In-Context Learning. arXiv. [doi:10.18653/v1/2025.findings-naacl.362](https://doi.org/10.18653/v1/2025.findings-naacl.362)"
    author: Peng Cui, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# ZPDs of different LLMs differ significantly: Z✗→✓ and Z✗→✗ examples overlap little across models while Z✓ examples are largely shared

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Examples in Z✓ are largely shared across models, but Z✗→✓ and Z✗→✗ examples do not highly overlap, indicating each LLM has its own ZPD. [→ Peng Cui 2025](#peng-cui-2025)

## Evidence

### Peng Cui 2025

Peng Cui, Mrinmaya Sachan. (2025). Investigating the Zone of Proximal Development of Language Models for In-Context Learning. arXiv. [doi:10.18653/v1/2025.findings-naacl.362](https://doi.org/10.18653/v1/2025.findings-naacl.362)

`q2 · i?` · `causal · r2`

Overlap analysis using the averaged pairwise Overlap Coefficient across zones of different LLaMA models on GSM8K and EZStance (Table 1). The article reports Z✓ examples are largely shared while Z✗→✓ and Z✗→✗ examples do not highly overlap.

> "The results are shown in Table 1, where we can see examples in Z✓ are largely shared across various models, while examples in Z✗→✓ and Z✗→✗ do not highly overlap, indicating each LLM has its own ZPD."

## Discussion


## Related Claims
- [Teacher-agent comparisons show backbone-dependent patterns consistent with ZPD-informed adaptation](teacher-agent-backbone-dependent-zpd-patterns.md) — related
- [A ZPD-based curriculum prioritizing challenging yet learnable examples improves fine-tuning convergence and performance, consistent with shared learnability between ICL and fine-tuning](zpd-curriculum-improves-finetuning.md) — related
- [Human learners' knowledge states subsume weaker learners' nearly perfectly, while LLMs show substantially lower and more fragmented subsumption](llms-lack-coherent-knowledge-subsumption.md) — related
