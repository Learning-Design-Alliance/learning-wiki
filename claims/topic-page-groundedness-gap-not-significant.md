---
type: claim
title: "The topic-page groundedness gap between wiki and vector RAG was the study's only comparison not reaching significance at the 95% level"
description: "The topic-page groundedness gap between wiki and vector RAG was the study's only comparison not reaching significance at the 95% level"
id: topic-page-groundedness-gap-not-significant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: brian-wright-2026
    resource: "https://doi.org/10.48550/arxiv.2609.25303"
    title: "Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)"
    author: Brian Wright
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The topic-page groundedness gap between wiki and vector RAG was the study's only comparison not reaching significance at the 95% level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On topic-page questions, the 11-point grounded-rate gap between RAG (87%) and wiki (98%) had a 95% CI of [0, 22] that just touches zero at n=45, so RAG's shortfall there was directionally consistent but not statistically established. [→ Brian Wright 2026](#brian-wright-2026)

## Evidence

### Brian Wright 2026

Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)

`q2 · i?` · `causal · r2`

Bootstrap analysis of the groundedness endpoint on the 45 topic-page questions in the head-to-head evaluation. The article reports an 11-point gap with "95% CI [0, 22]" touching zero, and no effect size is printed for this comparison.

> "the topic page grounded rate gap (11 points, 95% CI [0, 22]) just touches zero atn= 45, the one comparison in this study that does not reach significance at the 95% level"

## Discussion


## Related Claims
- [Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication](fabrication-despite-successful-retrieval.md) — related
- [The wiki's advantage over vector RAG is roughly three times larger on cross-page questions than on topic-page questions, in both score and groundedness](wiki-advantage-triples-cross-page-questions.md) — related
