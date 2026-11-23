---
type: claim
title: Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop
description: Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop
id: small-models-hints-scale-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: humaid-ibrahim-2025
    resource: "https://doi.org/10.48550/arXiv.2510.01375"
    title: "Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)"
    author: Humaid Ibrahim, Nikolai Rozanov, Marek Rei
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` 7B models gain from 26.5% to 71.3% success in ALFWorld with hints, but hints push the small model towards wrong attributes or over-constrain search in WebShop. [→ Humaid Ibrahim 2025](#humaid-ibrahim-2025)

## Evidence

### Humaid Ibrahim 2025

Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)

`q2 · i?` · `causal · r2`

Scale analysis in Results §5.1: the 14B model's higher capacity lets it better interpret hint semantics. Distillation compresses capability, matching a larger base in WebShop-7B (61.04 vs Base WebShop-14B 60.87).

> "7B models benefit dramatically from hints (26.5%→71.3%) in ALFWorld, but struggle to use them effectively at inference in WebShop. Hints push the small model towards the wrong attributes or over-constrain the search for the smaller models"

## Discussion


## Related Claims
- [Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success](distilled-models-fewer-tokens-than-rag.md) — related
- [Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop](distilled-students-highest-success-without-retrieval.md) — related
- Retrieval depth k shows diminishing returns: large hint blocks become counterproductive, with a sharp drop at k=9 in ALFWorld and reduced scores at k=6 and 9 in WebShop — related
- Injected conceptual hints consistently improve performance on logic and planning tasks across model sizes, with the largest gains in smaller models — a broader claim this one bears on
