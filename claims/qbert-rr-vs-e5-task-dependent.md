---
type: claim
title: QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval
description: QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval
id: qbert-rr-vs-e5-task-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: mixed
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: zhaozhen-xu-2024
    resource: "https://doi.org/10.1007/s40593-023-00377-8"
    title: "Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8"
    author: Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhaozhen-xu-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00377-8"
    title: "Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8"
    author: Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` QBERT-RR outperforms E5 on QT and QE tasks, but E5 achieves leading performance in answer retrieval. [→ Zhaozhen Xu 2024](#zhaozhen-xu-2024)
`q2 i?` In QA retrieval from a 26k-sentence WikiQA corpus, QBERT beats SBERT and the single-task model, yet E5 leads. [→ Zhaozhen Xu 2024 (2)](#zhaozhen-xu-2024-2)

## Evidence

### Zhaozhen Xu 2024

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Benchmark comparison on the YT and QQP test sets (Table 4) between QBERT-RR and E5, a state-of-the-art general-purpose embedding model. The article reports E5 obtains similar QA performance while "QBERT-RR outperforms E5 on QT and QE tasks".

> "The results show that E5 obtains similar performance on QA. On the other hand, QBERT-RR outperforms E5 on QT and QE tasks."

### Zhaozhen Xu 2024 (2)

Zhaozhen Xu, Amelia Howarth, Nicole Briggs, Nello Cristianini. (2024). Understanding Visitors' Curiosity in a Science Centre with Deep Question Processing Network. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00377-8

`q2 · i?` · `design · r2`

Accuracy@K retrieval evaluation on WikiQA shown in Fig. 4, with a 26k-sentence candidate answer corpus. QBERT beats SBERT and the single-task model, but "E5 achieves a leading performance in answer retrieval".

> "The results show that QBERT has a better performance in retrieving answers from a given corpus compared to SBERT and the single-task model. However, E5 achieves a leading performance in answer retrieval."

## Discussion


## Related Claims
- [The multi-task QBERT-RR generalist achieves comparable or better accuracy than single-task SBERT models on question topic, equivalence, and answering tasks](qbert-rr-comparable-or-better-than-single-task.md) — related
- [General-purpose embedding yields better retrieval while domain-specific embedding yields higher answer completeness and relevance](embedding-model-tradeoff-retrieval-vs-completeness.md) — related
- [QBERT-RR finds high-confidence one-sentence Wikipedia answers for 463 WTC questions](wtc-463-questions-answered-wikipedia.md) — related
- [Graph community detection over QBERT-RR embeddings yields 5,930 question communities, with 5,337 questions having no similar group](wtc-5930-question-communities.md) — a narrower finding that bears on this claim
