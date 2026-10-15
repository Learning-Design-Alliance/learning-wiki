---
type: claim
title: "Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication"
description: "Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication"
id: fabrication-despite-successful-retrieval
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: brian-wright-2026
    resource: "https://doi.org/10.48550/arxiv.2609.25303"
    title: "Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)"
    author: Brian Wright
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: brian-wright-2026-2
    resource: "https://arxiv.org/abs/2609.25303"
    title: "Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303"
    author: Brian Wright
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` Retrieval itself was largely successful: 43 of 45 topic-page questions (96%) retrieved a chunk from the question's actual source page in the top 5. [→ Brian Wright 2026](#brian-wright-2026)
`q2 i?` Only 2 of the 11 ungrounded Arm A answers were retrieval misses; the other 9 retrieved the correct page or relevant chunks and were still marked ungrounded, with the answerer adding unsupported detail. [→ Brian Wright 2026 (2)](#brian-wright-2026-2)

## Evidence

### Brian Wright 2026

Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)

`q2 · i?` · `causal · r2`

Retrieval-tracing analysis of Arm A (vector RAG) in the head-to-head evaluation. The article reports "43 of 45 topic page questions(96%)" retrieved from the correct source page; the two misses pulled in short navigational pages and scored low (3 and 4) while marked ungrounded.

> "Retrieval itself was largely successful: 43 of 45 topic page questions(96%)retrievedachunkfromthequestion'sactual source page in the top 5."

### Brian Wright 2026 (2)

Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303

`q2 · i?` · `causal · r2`

Ungrounded-answer analysis of Arm A in the same evaluation. The article reports "retrieval failure explains only 2 of the11ungroundedArmAanswers" and that the answerer added unsupported detail even with the right excerpts in context, suggesting chunked context invites fabrication.

> "More striking is that retrieval failure explains only 2 of the11ungroundedArmAanswers.Theother9retrievedthe correct page (or, for cross page questions, relevant chunks frommorethanonepage)andwerestillmarkedungrounded."

## Discussion


## Related Claims
- [The topic-page groundedness gap between wiki and vector RAG was the study's only comparison not reaching significance at the 95% level](topic-page-groundedness-gap-not-significant.md) — related
- [Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)](semantic-retrieval-insufficient-pedagogical-content.md) — related
- [In a ten-request live textbook audit, citation integrity coexisted with substantive error: every citation resolved to its source, yet answers included retrieval misses and contradictions](citation-integrity-coexists-with-error.md) — related
- [The wiki's advantage over vector RAG is roughly three times larger on cross-page questions than on topic-page questions, in both score and groundedness](wiki-advantage-triples-cross-page-questions.md) — related
- [NLI analysis reveals reference-based grading is limited: many semantically correct responses contradict reference answers](nli-reference-based-grading-limitation.md) — related
