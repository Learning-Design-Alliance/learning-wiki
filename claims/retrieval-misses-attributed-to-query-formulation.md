---
type: claim
title: Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor
description: Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor
id: retrieval-misses-attributed-to-query-formulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: sidney-shapiro-and-joshua-lindemann-2026
    resource: "https://doi.org/10.48550/arxiv.2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sidney-shapiro-and-joshua-lindemann-2026-2
    resource: "https://arxiv.org/abs/2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2`–`r3` · `q2`

## Subclaims
`q2 i?` The five-course run still contained 93 no-match turns, of which twelve were intentional locked-module refusals and fifteen were quiz follow-ups whose wording did not retrieve a qualifying passage. [→ Sidney Shapiro and Joshua Lindemann 2026](#sidney-shapiro-and-joshua-lindemann-2026)
`q2 i?` A bounded expansion using only words in the student question recovered eleven of the original 24 queries without lowering the relevance floor. [→ Sidney Shapiro and Joshua Lindemann 2026 (2)](#sidney-shapiro-and-joshua-lindemann-2026-2)

## Evidence

### Sidney Shapiro and Joshua Lindemann 2026

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)

`q2 · i?` · `design · r2`

Diagnostic analysis of the five-course conversation replay: the section reports "93 no match turns", decomposed into intentional refusals, quiz follow-ups without qualifying passages, and 66 other requests spanning 24 topics.

> "The five-course run still contained 93 no match turns. Twelve were intentional locked-module refusals, fifteen were quiz follow-ups whose wording did not retrieve a qualifying passage, and 66 involved other requests spanning 24 topics."

### Sidney Shapiro and Joshua Lindemann 2026 (2)

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510

`q2 · i?` · `design · r3`

Retrieval diagnostic on the affected topics: the section reports that "a bounded expansion using only words in the student question recovered eleven of the original queries", indicating many misses arose from query formulation rather than missing material.

> "A bounded expansion using only words in the student question recovered eleven of the original queries without lowering the relevance floor."

## Discussion


## Related Claims

- [In a ten-request live textbook audit, citation integrity coexisted with substantive error: every citation resolved to its source, yet answers included retrieval misses and contradictions](citation-integrity-coexists-with-error.md)
- [DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)](query-robustness-paraphrase-keyword-perturbation.md)
- [Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline](retrieval-augmentation-essential-local-llm-below-tfidf.md)
