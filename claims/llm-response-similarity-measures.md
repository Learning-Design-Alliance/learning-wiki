---
type: claim
title: Gemini-1.5-flash and Coral were the most semantically consistent across repeated prompts, and ChatGPT4.0 the most lexically consistent by cosine similarity
description: Gemini-1.5-flash and Coral were the most semantically consistent across repeated prompts, and ChatGPT4.0 the most lexically consistent by cosine similarity
id: llm-response-similarity-measures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: keisuke-sato-2024
    resource: "https://doi.org/10.48550/arXiv.2407.05308"
    title: "Keisuke Sato. (2024). Exploring the Educational Landscape of AI: Large Language Models' Approaches to Explaining Conservation of Momentum in Physics. A Preprint. [doi:10.48550/arXiv.2407.05308](https://doi.org/10.48550/arXiv.2407.05308)"
    author: Keisuke Sato
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Gemini-1.5-flash and Coral were the most semantically consistent across repeated prompts, and ChatGPT4.0 the most lexically consistent by cosine similarity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Gemini-1.5-flash and Coral showed the highest LSA similarities (0.338636 and 0.335099 respectively), and ChatGPT4.0 the highest cosine similarity. [→ Keisuke Sato 2024](#keisuke-sato-2024)

## Evidence

### Keisuke Sato 2024

Keisuke Sato. (2024). Exploring the Educational Landscape of AI: Large Language Models' Approaches to Explaining Conservation of Momentum in Physics. A Preprint. [doi:10.48550/arXiv.2407.05308](https://doi.org/10.48550/arXiv.2407.05308)

`q2 · i?` · `design · r2`

Similarity analysis using cosine, Jaccard, LSA, and Levenshtein measures over all pairs of the 50 responses per model. The article reports "Gemini-1.5-ﬂash and Coral exhibited the highest LSA similarities (0.338636 and 0.335099 respectively)"; ChatGPT4.0's cosine similarity was highest and Gemini-1.5-pro's Levenshtein distance greatest.

> "Gemini-1.5-ﬂash and Coral exhibited the highest LSA similarities (0.338636 and 0.335099 respectively), indicating more consistent semantic content across their responses."

## Discussion


## Related Claims
- [ChatGPT4.0 and Gemini-1.5-flash showed the most consistent response lengths, while ChatGPT3.5 was the most variable across repeated prompts](llm-response-consistency-cv.md) — related
- [Personalized responses remain semantically grounded in the shared knowledge base while varying in surface-level expression and structure](semantic-grounding-with-surface-variation.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
