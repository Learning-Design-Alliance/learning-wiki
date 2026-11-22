---
type: claim
title: "Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17"
description: "Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17"
id: cares-retrieval-precision-proxy-017
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yang-2026
    resource: "https://doi.org/10.48550/arXiv.2609.19429"
    title: "Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)"
    author: Yang, F.; Wu, J.; Tian, Y.; and Zhang, J.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Relevant regulatory information was not consistently concentrated in the first four fused retrieval positions, with a pooled Retrieval Precision Proxy@4 of 0.17. [→ Yang 2026](#yang-2026)

## Evidence

### Yang 2026

Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)

`q2 · i?` · `design · r2`

Automated retrieval evaluation across the 15 sessions, using reciprocal rank fusion of dense and BM25 retrieval with model-generated relevance labels. The article reports the proxy "was 0.17"; no effect size is printed.

> "The pooled Retrieval Precision Proxy@4 was 0.17, indicating that relevant regulatory information was not consistently concentrated within the first four positions of the fused retrieval ranking."

## Discussion


## Related Claims
- [CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context](cares-faithfulness-074.md) — related
- [First-time resident users retrieved relevant answers to a higher proportion of clinical questions with UpToDate (76%) than with PubMed Clinical Queries (43%)](uptodate-higher-answer-retrieval-than-pubmed-clinical-queries.md) — related
- [Retrieval context has a sweet spot at Top-K = 10: raising it to 15 did not improve recall but significantly worsened context precision via the distraction issue](rag-top-k-10-sweet-spot-context-precision.md) — related
- [CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message](cares-answer-relevance-100.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related
