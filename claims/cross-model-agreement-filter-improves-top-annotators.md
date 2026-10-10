---
type: claim
title: Adding a cross-model agreement filter improves performance for the top three LLM annotators
description: Adding a cross-model agreement filter improves performance for the top three LLM annotators
id: cross-model-agreement-filter-improves-top-annotators
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

# Adding a cross-model agreement filter improves performance for the top three LLM annotators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The top three annotators perform better when classification includes only assertions with Krippendorff's alpha of at least 0.5, indicating the agreement filter helps select more faithful assertions. [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043

`q2 · i?` · `design · r2`

Within the same TalkMoves classification experiment, four covariate-set conditions per annotator isolated the effect of filtering assertions to those with Krippendorff's α ≥ 0.5. The article reports that "our top three anno- tators perform better with the cross-model agreement filter."

> "Furthermore, our top three anno- tators perform better with the cross-model agreement filter."

## Discussion


## Related Claims
- [Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions](assertion-cross-model-agreement-moderate-median-0401.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
