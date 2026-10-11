---
type: claim
title: Standardized repair and source-verification gating produced structurally complete, source-traceable feedback for most generated messages
description: Standardized repair and source-verification gating produced structurally complete, source-traceable feedback for most generated messages
id: repair-and-source-gating-feedback-completeness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shihao-wang-2026
    resource: "https://arxiv.org/abs/2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: shihao-wang-2026-2
    resource: "https://arxiv.org/abs/2609.29874"
    title: "Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874"
    author: Shihao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Standardized repair and source-verification gating produced structurally complete, source-traceable feedback for most generated messages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` After repair and deterministic reference gating, 519 of 544 newly generated messages (95.4%) contained all required components, while 25 required further structural review. [→ Shihao Wang 2026](#shihao-wang-2026)
`q2 i?` The source-verification gate identified exact code matches in 16 of 544 outputs (2.9%) and removed 484 unverifiable source references. [→ Shihao Wang 2026 (2)](#shihao-wang-2026-2)

## Evidence

### Shihao Wang 2026

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874

`q2 · i?` · `design · r2`

Paired generation experiment producing 544 F1–F4 messages for 136 cases with a constant language model and deterministic decoding. "After repair and deterministic reference gating, 519 outputs (95.4%) contained all required components"; final completeness rates ranged from 92.6% to 97.1% across conditions.

> "After repair and deterministic reference gating, 519 outputs (95.4%) contained all required components, while 25 required further structural review."

### Shihao Wang 2026 (2)

Shihao Wang. (2026). A Risk-Adaptive and Evidence-Constrained Framework for Generative AI Feedback in Programming Education. https://arxiv.org/abs/2609.29874

`q2 · i?` · `design · r2`

Automated source checks across the four within-case conditions. "The source-veriﬁcation gate identiﬁed exact code matches" in 16 of 544 outputs (2.9%), and the gate removed 484 unverifiable source references so only exact matches were retained.

> "The source-veriﬁcation gate identiﬁed exact code matches in 5 F1, 4 F2, 2 F3, and 5 F4 messages, totaling 16 of 544 outputs (2.9%)."

## Discussion


## Related Claims
- [Conservative manual verification identified 30 hallucinated references across 14 papers in 2025 and 2026 computing education venues](30-hallucinated-references-14-papers-csed.md) — related
- [Automated verification of AI-drafted content produced mixed results: strong accuracy and integrity scores but only 5 of 10 chapters meeting the pedagogical-progression bar](verification-layer-one-mixed-results.md) — related
