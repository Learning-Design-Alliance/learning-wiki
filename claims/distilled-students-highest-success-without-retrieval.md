---
type: claim
title: Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop
description: Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop
id: distilled-students-highest-success-without-retrieval
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
    rigour: 1
  - id: humaid-ibrahim-2025-2
    resource: "https://doi.org/10.48550/arXiv.2510.01375"
    title: "Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)"
    author: Humaid Ibrahim, Nikolai Rozanov, Marek Rei
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On ALFWorld, distillation exceeds RAG at 14B (91.04% vs 82.09%) and improves over both base and SFT. [→ Humaid Ibrahim 2025](#humaid-ibrahim-2025)
`q2 i?` On WebShop, distillation matches or exceeds RAG while delivering higher scores with comparable or lower token cost. [→ Humaid Ibrahim 2025 (2)](#humaid-ibrahim-2025-2)

## Evidence

### Humaid Ibrahim 2025

Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)

`q2 · i?` · `causal · r1`

Main performance results (Table 4) on ALFWorld with Qwen-2.5 14B and 7B Instruct backbones, averaged across ReAct and StateAct agents. The 14B distilled model reaches "91.04% vs. 82.09%" success over RAG, with base at 79.85% and SFT at 85.45%.

> "In ALFWorld, distillation exceeds RAG at 14B (91.04% vs. 82.09%) and improves over both base and SFT; at 7B it recovers most of the retrieval gains without requiring hints."

### Humaid Ibrahim 2025 (2)

Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)

`q2 · i?` · `causal · r1`

Main performance results (Table 4) on WebShop: 14B distilled score 72.40 vs RAG 67.08 and base 60.87; 7B distilled 61.04 vs base 60.87. Success rates are 43.5% (14B) and 22.5% (7B) for distilled models.

> "In WebShop, distillation matches or exceeds RAG while delivering higher scores with comparable or lower token cost."

## Discussion


## Related Claims
- [Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success](distilled-models-fewer-tokens-than-rag.md) — related
- [Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop](small-models-hints-scale-dependent.md) — related
