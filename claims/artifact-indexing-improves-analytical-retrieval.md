---
type: claim
title: Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations
description: Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations
id: artifact-indexing-improves-analytical-retrieval
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: dawei-xie-2026
    resource: "https://arxiv.org/abs/2605.17259"
    title: "Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259"
    author: Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dawei-xie-2026-2
    resource: "https://arxiv.org/abs/2605.17259"
    title: "Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259"
    author: Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On 20 analytical queries whose evaluative vocabulary does not appear in student speech, transcript-only retrieval achieved Recall@5 = .371, while combining all artifact types yielded the strongest performance (Recall@5 = .739, Recall@10 = .804, MRR@5 = .942). [→ Dawei Xie 2026](#dawei-xie-2026)
`q2 i?` On 10 direct queries with terms appearing in transcript text, all four artifact configurations performed comparably (Recall@5 .867–.933; MRR@5 1.000). [→ Dawei Xie 2026 (2)](#dawei-xie-2026-2)

## Evidence

### Dawei Xie 2026

Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259

`q2 · i?` · `design · r2`

Retrieval evaluation of four artifact configurations (transcript-only, +concept maps, +7C assessments, all artifacts) over 30 curated queries with manually identified ground truth, using reciprocal rank fusion. Transcript-only Recall@5 was .371 on analytical queries; adding concept maps gave .534 and 7C assessments .563.

> "Combiningallartifacttypesyieldedthestrongestperformance (Recall@5=.739, Recall@10=.804, MRR@5=.942)."

### Dawei Xie 2026 (2)

Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259

`q2 · i?` · `design · r2`

For the 10 direct queries whose terms appear in transcripts, retrieval found relevant sessions regardless of which collections were available, so the artifact advantage was specific to analytical queries framed in evaluative vocabulary.

> "On direct queries, all configurations performed comparably(Recall@5: .867–.933; Recall@10: .933–.967; MRR@5: 1.000 across conditions)."

## Discussion


## Related Claims
- [Artifact-grounded agent responses are rated significantly higher than transcript-only responses on groundedness, analytical depth, helpfulness, relevance, and overall quality](artifact-grounded-responses-rated-higher.md) — related
- [A hybrid human-AI workflow using GPT-4o with retrieval-augmented generation supported efficient inductive thematic analysis while preserving researcher judgment](hybrid-gpt4o-human-inductive-thematic-analysis-workflow.md) — related
- [General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance](embedding-model-tradeoff-retrieval-vs-completeness.md) — related
