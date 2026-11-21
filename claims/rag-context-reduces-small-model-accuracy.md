---
type: claim
title: Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model
description: Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model
id: rag-context-reduces-small-model-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: juan-segundo-hevia-2025
    resource: "https://doi.org/10.48550/arXiv.2510.06255"
    title: "Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. [doi:10.48550/arXiv.2510.06255](https://doi.org/10.48550/arXiv.2510.06255)"
    author: Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Including RAG-retrieved textbook context before processing user queries does not improve accuracy and appears to reduce it, with particularly notable declines for SmolLM2 1.7B (33.04% with RAG vs 41.00% without). [→ Juan Segundo Hevia 2025](#juan-segundo-hevia-2025)

## Evidence

### Juan Segundo Hevia 2025

Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. [doi:10.48550/arXiv.2510.06255](https://doi.org/10.48550/arXiv.2510.06255)

`q2 · i?` · `design · r2`

Benchmark evaluation of quantized SmolLM 135M, SmolLM2 135M and SmolLM2 1.7B on college and high-school biology MMLU tasks with and without RAG context; Table 1 prints SmolLM2 1.7B at 33.04% with RAG versus 41.00% without. The article reports the decline is "particularly notable" for the larger model.

> "Table 1 reveals that the inclusion of the RAG component prior to processing user queries does not lead to an improvement in accuracy. On the contrary, it appears to reduce accuracy, with particularly notable declines observed in the larger model."

## Discussion


## Related Claims
- [Accuracy drops when RAG context is added even when the correct answer is supplied in the prompt, for both letter and text answer formats](context-as-noise-answer-given.md) — a broader claim this one bears on
- [Performance loss from extended context persists even when retrieved context is highly relevant and built from the evaluation dataset itself](high-quality-retrieval-still-noise.md) — a broader claim this one bears on
- [Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline](rag-grounding-near-perfect-correctness.md) — related
- [Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication](fabrication-despite-successful-retrieval.md) — related
