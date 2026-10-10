---
type: claim
title: Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions
description: Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions
id: assertion-cross-model-agreement-moderate-median-0401
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: julian-bernado-2026
    resource: "https://arxiv.org/abs/2609.27043"
    title: "Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043"
    author: Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 221 assertions annotated by five LLMs, cross-model agreement is moderate with a median Krippendorff's alpha of 0.401, and construct-derived assertions agree more than corpus-derived ones; filtering at alpha ≥ 0.5 leaves 33 of 74 corpus-derived and 11 of 48 construct-derived assertions. [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043

`q2 · i?` · `design · r2`

Annotation analysis of 221 assertions (74 corpus-derived, 48 construct-derived, 100 word-based) by a panel of five language models, with per-assertion Krippendorff's alpha shown in Figure 1. The article reports agreement is "moderate (median = 0.401" and higher for construct-derived assertions.

> "Overall, cross-model agreement is moderate (median = 0.401 and higher among the construct-derived assertions than the data-derived assertions."

## Discussion


## Related Claims
- [All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy](all-assertion-sources-contribute-predictive-accuracy.md) — related
- [Adding a cross-model agreement filter improves performance for the top three LLM annotators](cross-model-agreement-filter-improves-top-annotators.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement](construct-clarity-predicts-coding-agreement.md) — related
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](human-human-agreement-lower-than-llm-llm.md) — related
