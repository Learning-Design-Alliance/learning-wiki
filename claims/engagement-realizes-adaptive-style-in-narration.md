---
type: claim
title: Engagement removal lowers the adaptive score, indicating the engagement generator realizes persona-conditioned style choices in narration
description: Engagement removal lowers the adaptive score, indicating the engagement generator realizes persona-conditioned style choices in narration
id: engagement-realizes-adaptive-style-in-narration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: md-zabirul-islam-2026
    resource: "https://arxiv.org/abs/2606.20608"
    title: "Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608"
    author: Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Engagement removal lowers the adaptive score, indicating the engagement generator realizes persona-conditioned style choices in narration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When engagement is disabled, the adaptive judge score drops from 4.80 to 3.40, which the authors interpret as the adaptive style controller alone being insufficient to realize persona-conditioned choices in narration. [→ Md Zabirul Islam 2026](#md-zabirul-islam-2026)

## Evidence

### Md Zabirul Islam 2026

Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608

`q2 · i?` · `design · r2`

Same five-topic ablation (n=5 topics); the adaptive-dimension judge median falls from 4.80 to 3.40 when the engagement module is disabled. The quoted interpretation is the authors' own; no effect size is printed.

> "The adaptive score drops from 4.80 to 3.40 when engagement is disabled. This indicates that the adaptive style controller alone is not sufficient: it specifies persona-conditioned depth, vocabulary, abstraction, and example density, but the engagement generator is the module that realizes those choices in the narration"

## Discussion


## Related Claims
- [Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation](engagement-contract-ablation-reduces-pck-scores.md) — related
