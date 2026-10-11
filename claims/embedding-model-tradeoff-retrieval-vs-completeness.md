---
type: claim
title: General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance
description: General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance
id: embedding-model-tradeoff-retrieval-vs-completeness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: ronghua-xu-2026
    resource: "https://arxiv.org/abs/2608.08163"
    title: "Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163"
    author: Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across two embedding models and two LLMs, nomic-embed-text:v1.5 showed better retrieval performance, while MedEmbed-large-v0.1 provided more domain-specific medical information achieving higher answer completeness and relevance. [→ Ronghua Xu 2026](#ronghua-xu-2026)

## Evidence

### Ronghua Xu 2026

Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163

`q2 · i?` · `design · r2`

Comparison of four model-embedding configurations in Table IV (context recall, answer relevance, answer completeness) using the RAGAS framework on the 52-question expert dataset. The article concludes both approaches produce high-quality answers, with domain-specific embedding increasing quality for medical queries.

> "The results demonstrate that nomic-embed-text:v1.5 has better retrieval performance, while MedEmbed-large-v0.1 can provide more domain-specific and concrete medical information. thus achieving higher answer completeness and relevance."

## Discussion


## Related Claims
- [Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations](artifact-indexing-improves-analytical-retrieval.md) — related
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
