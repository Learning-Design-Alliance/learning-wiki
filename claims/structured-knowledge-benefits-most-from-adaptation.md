---
type: claim
title: Adaptation benefits structured curricular knowledge (quantities, laws, definitions) most and loosely specified entity-level knowledge least
description: Adaptation benefits structured curricular knowledge (quantities, laws, definitions) most and loosely specified entity-level knowledge least
id: structured-knowledge-benefits-most-from-adaptation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: rashid-azraf-jahin-2026
    resource: "https://doi.org/10.48550/arxiv.2610.00664"
    title: "Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)"
    author: Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Adaptation benefits structured curricular knowledge (quantities, laws, definitions) most and loosely specified entity-level knowledge least

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On Qwen3-4B Token F1 by node type, Quantity nodes show the largest relative gain (93.9%), followed by laws (56.6%) and definitions (56.1%), while Entity nodes show the smallest gain (8.7%). [→ Rashid Azraf Jahin 2026](#rashid-azraf-jahin-2026)

## Evidence

### Rashid Azraf Jahin 2026

Rashid Azraf Jahin, Saadman Sajid, Khan Raiyan Ibne Reza, Sumaiya Tabassum Nimi. (2026). PhysicsMate: A Curriculum-Grounded Bengali Benchmark for Secondary Physics QA with Small-Model Adaptation. IEEE CSDE 2026. https://arxiv.org/abs/2610.00664 [doi:10.48550/arxiv.2610.00664](https://doi.org/10.48550/arxiv.2610.00664)

`q2 · i?` · `causal · r1`

Node-type diagnostic on the 275 test questions (Table IV, Fig. 3). The authors interpret that quantities, laws and definitions have "canonical Bengali phrasings in the NCTB textbook" while entity mentions are loosely specified with multiple valid surface forms.

> "Quantity nodes show the largest relative gain (93.9%), followed by scientific laws (56.6%) and definitions (56.1%). Entity nodes show the smallest gain (8.7%)."

## Discussion


## Related Claims
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](adaptation-gains-grow-with-model-capacity.md) — related
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — related
