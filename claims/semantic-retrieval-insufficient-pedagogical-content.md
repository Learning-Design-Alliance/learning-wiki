---
type: claim
title: "Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)"
description: "Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)"
id: semantic-retrieval-insufficient-pedagogical-content
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: laurent-brisson-2026
    resource: "https://doi.org/10.48550/arxiv.2607.22598"
    title: "Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598 [doi:10.48550/arxiv.2607.22598](https://doi.org/10.48550/arxiv.2607.22598)"
    author: Laurent Brisson, Maria Teresa Segarra and Gregory Smits
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A standalone semantic retrieval system found the required chunk in only 62.6% of real-corpus queries overall, and only 14.3% for COMPARE, showing the failure is structural rather than parametric. [→ Laurent Brisson 2026](#laurent-brisson-2026)

## Evidence

### Laurent Brisson 2026

Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598 [doi:10.48550/arxiv.2607.22598](https://doi.org/10.48550/arxiv.2607.22598)

`q2 · i?` · `design · r2`

Retrieval evaluation (RQ1) on the real corpus of student questions: a semantic-only pipeline (nomic-embed-text-v1.5, cosine similarity, top-15) was tested for whether the required chunk type appears in top-15. DEFINE reached 89.1% retrieval, EXPLAIN 58.2%, and COMPARE only 14.3%, described as "structural rather than parametric".

> "C OMPARE fails most severely: only 14.3% of comparison chunks are retrieved. This failure is struc- tural rather than parametric: a comparison chunk en- codes a relationship between two speciﬁc concepts, a constraint that embedding similarity cannot capture from a single query vector."

## Discussion


## Related Claims
- [Manual error analysis finds incomplete retrieval is the most frequent failure category, ahead of code-semantics limits, bilingual retrieval gaps, and over-conservative refusals](eduguard-failure-analysis-incomplete-retrieval.md) — related
- [Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient](evidence-tracing-114-claims-retrieval-limit.md) — related
- [Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication](fabrication-despite-successful-retrieval.md) — related
- [General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance](embedding-model-tradeoff-retrieval-vs-completeness.md) — related
