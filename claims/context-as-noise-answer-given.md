---
type: claim
title: Accuracy drops when RAG context is added even when the correct answer is supplied in the prompt, for both letter and text answer formats
description: Accuracy drops when RAG context is added even when the correct answer is supplied in the prompt, for both letter and text answer formats
id: context-as-noise-answer-given
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
    kind: causal
    rigour: 2
---

# Accuracy drops when RAG context is added even when the correct answer is supplied in the prompt, for both letter and text answer formats

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the correct multiple-choice answer is provided in the input, adding RAG context still causes a consistent and significant loss in accuracy, and SmolLM2 1.7B is as vulnerable as smaller models. [→ Juan Segundo Hevia 2025](#juan-segundo-hevia-2025)

## Evidence

### Juan Segundo Hevia 2025

Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. [doi:10.48550/arXiv.2510.06255](https://doi.org/10.48550/arXiv.2510.06255)

`q2 · i?` · `causal · r2`

Diagnostic experiment feeding MMLU biology questions with the true answer embedded, either as an option letter (Table 2) or as answer text (Table 3), with and without two retrieved RAG blocks; e.g. SmolLM 135M falls from 91.63% letter-answer-only to 26.65% with RAG context added.

> "As the tables show, in both cases there is a consistent, and significant loss in accuracy when adding the RAG component's output to the model. Contrary to what one would initial expect, the larger model (SmolLM2 1.7B) is as vulnerable to this loss in performance."

## Discussion


## Related Claims
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [Performance loss from extended context persists even when retrieved context is highly relevant and built from the evaluation dataset itself](high-quality-retrieval-still-noise.md) — related
- [Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model](rag-context-reduces-small-model-accuracy.md) — a narrower finding that bears on this claim
