---
type: claim
title: Performance loss from extended context persists even when retrieved context is highly relevant and built from the evaluation dataset itself
description: Performance loss from extended context persists even when retrieved context is highly relevant and built from the evaluation dataset itself
id: high-quality-retrieval-still-noise
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

# Performance loss from extended context persists even when retrieved context is highly relevant and built from the evaluation dataset itself

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Even with a document database built directly from the MMLU evaluation items and retrieval limited to the most similar question pairs, small models remain sensitive to extended context irrespective of its informational quality. [→ Juan Segundo Hevia 2025](#juan-segundo-hevia-2025)

## Evidence

### Juan Segundo Hevia 2025

Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. [doi:10.48550/arXiv.2510.06255](https://doi.org/10.48550/arXiv.2510.06255)

`q2 · i?` · `design · r2`

Numerical benchmark (Table 4) testing the standard pipeline over a knowledge base constructed from MMLU biology questions themselves, with k=1 versus k=2 context; SmolLM2 1.7B drops from 58.81% at k=1 to 30.84% at k=2, showing loss even with high-quality retrieval.

> "Notably, even when the retrieved context is highly relevant and closely aligned with the input question, the loss in performance persists. These findings suggest that small models are particularly sensitive to extended contexts, irrespective of their informational quality when handling factual tasks."

## Discussion


## Related Claims
- [Accuracy drops when RAG context is added even when the correct answer is supplied in the prompt, for both letter and text answer formats](context-as-noise-answer-given.md) — related
- [Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication](fabrication-despite-successful-retrieval.md) — related
- [Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model](rag-context-reduces-small-model-accuracy.md) — a narrower finding that bears on this claim
