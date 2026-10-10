---
type: claim
title: Manual error analysis finds incomplete retrieval is the most frequent failure category, ahead of code-semantics limits, bilingual retrieval gaps, and over-conservative refusals
description: Manual error analysis finds incomplete retrieval is the most frequent failure category, ahead of code-semantics limits, bilingual retrieval gaps, and over-conservative refusals
id: eduguard-failure-analysis-incomplete-retrieval
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: s-m-asif-hossain-2026
    resource: "https://arxiv.org/abs/2607.15738"
    title: "S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738"
    author: S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin
    q: 2
    i: "?"
    kind: qualitative
    rigour: 1
---

# Manual error analysis finds incomplete retrieval is the most frequent failure category, ahead of code-semantics limits, bilingual retrieval gaps, and over-conservative refusals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r1` · `q2`

## Subclaims
`q2 i?` In manual analysis of sampled errors, the most frequent failure was incomplete retrieval, where course chunks lacked detail to support a specific error message or assignment context. [→ S M Asif Hossain 2026](#s-m-asif-hossain-2026)

## Evidence

### S M Asif Hossain 2026

S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha, and Jungpil Shin. (2026). EduGuard: A Safe RAG-Based LLM Tutor for Programming Education. arXiv preprint arXiv:2607.15738. https://arxiv.org/abs/2607.15738

`q2 · i?` · `qualitative · r1`

Qualitative failure analysis of 80 randomly sampled BILearn-CS errors and 30 CS50-Forum errors (Table 8), where incomplete retrieval accounts for a 31% share, followed by code-semantics error at 24% and bilingual retrieval gap at 18%.

> "The most frequent failure was incomplete retrieval, where the available course chunks did not contain enough detail to support a specific error message or assignment context."

## Discussion


## Related Claims
- [Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)](semantic-retrieval-insufficient-pedagogical-content.md) — related
