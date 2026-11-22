---
type: claim
title: "CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message"
description: "CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message"
id: cares-answer-relevance-100
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

# CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three LLM judges, CARES responses were classified as relevant in essentially all eligible turns, with an overall majority-vote answer relevance score of 1.00. [→ Yang 2026](#yang-2026)

## Evidence

### Yang 2026

Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)

`q2 · i?` · `design · r2`

Pooled LLM-as-a-judge evaluation of the same 15 sessions: each response was classified relevant or not by three judges. The article reports judge scores of 0.99, 0.99, and 1.00 and an "overall majority -vote score of 1.00"; no effect size is printed.

> "Answer Relevance showed the strongest and most consistent performance. GPT -4o-mini and Gemini 2.5 Flash each produced a score of 0.99, while Claude 3 Haiku produced a score of 1.00, resulting in an overall majority -vote score of 1.00."

## Discussion


## Related Claims
- [CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context](cares-faithfulness-074.md) — related
- [In an 18-participant user study, the system received a 4.00/5 overall recommendation, with hallucination resistance rated 4.44/5 and highest ratings for ease of starting a conversation (4.39/5) and response relevance and accuracy (4.06/5)](user-study-18-participants-recommendation-4-of-5.md) — related
- [The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set](rag-assistant-high-recall-relevance.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related
- [Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17](cares-retrieval-precision-proxy-017.md) — related
