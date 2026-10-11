---
type: claim
title: The pipeline generated grounded questions about complex multimodal diagrams, citing visual evidence
description: The pipeline generated grounded questions about complex multimodal diagrams, citing visual evidence
id: grounded-multimodal-diagram-questions
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: salsman-2026
    resource: "https://arxiv.org/abs/2605.26428"
    title: "Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428"
    author: Salsman, J.
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: salsman-2026-2
    resource: "https://arxiv.org/abs/2605.26428"
    title: "Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428"
    author: Salsman, J.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The pipeline generated grounded questions about complex multimodal diagrams, citing visual evidence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`

## Subclaims
`q1 i?` For a mean-pooling slide the system generated a question on sentence encoding with the answer grounded as taking the element-wise max or mean of all hidden states (Fidelity 5, Coverage 5). [→ Salsman 2026](#salsman-2026)
`q1 i?` For an LSTM diagram in the Neural Constituency Parsing deck, the system generated questions on bidirectional routing citing horizontal arrows between boxes as visual evidence (Fidelity 5). [→ Salsman 2026 (2)](#salsman-2026-2)

## Evidence

### Salsman 2026

Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428

`q1 · i?` · `design · r2`

Qualitative case observation in the Results section on the Self-Attention and Transformers deck, describing a mean-pooling slide interpreted as a conceptual stepping stone toward attention. The quoted scores are the system's own fidelity and coverage judgments.

> "the system generated a question asking how "Sentence encoding" is computed, correctly identifying the answer as "taking the element-wise max or mean of all hidden states" (Fidelity: 5, Coverage: 5)."

### Salsman 2026 (2)

Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428

`q1 · i?` · `design · r2`

Qualitative case observation in the Results section on the Neural Constituency Parsing deck, where the system mapped visual cues in an LSTM unit diagram to the concept of bidirectional context gathering. The Fidelity score is the system's own judgment.

> "the system correctly generated questions addressing how bidirectional routing works, accurately citing "horizontal arrows pointing left and right between the boxes" as evidence for how context is gathered across the sequence (Fidelity: 5)."

## Discussion


## Related Claims
- [The pipeline feasibly produces coherent, synchronized educational videos from textbook queries, integrating retrieval, image generation, animation, and speech](feasible-synchronized-video-generation-from-textbook-queries.md) — related
- [The reconciliation phase filters non-instructional slides by zero-budgeting administrative and transition slides](reconciliation-zero-budgets-structural-slides.md) — related
