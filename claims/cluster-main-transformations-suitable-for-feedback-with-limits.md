---
type: claim
title: "Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback"
description: "Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback"
id: cluster-main-transformations-suitable-for-feedback-with-limits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: lilian-killich-2026
    resource: "https://doi.org/10.48550/arxiv.2609.17111"
    title: "Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)"
    author: Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` A CS educator inspected all clusters explaining at least 0.5% of pairs in each dataset; in propositional logic 19 clusters had main transformations suitable for feedback, with at least 4 requiring sub-transformations, and in modal logic 18 were suitable with at least 7 requiring sub-transformations. [→ Lilian Killich 2026](#lilian-killich-2026)

## Evidence

### Lilian Killich 2026

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)

`q1 · i?` · `design · r2`

Qualitative usefulness inspection by one CS educator of clusters explaining at least 0.5% of pairs across the three datasets, judging whether main transformations suffice for targeted feedback; "19 clusters had main transformations suitable for feedback" in propositional logic. Single-rater judgment, no effect size.

> "In propositional logic, 19 clusters had main transformations suitable for feedback, though at least 4 required sub-transformations for more targeted feedback. In CTL, all 17 clusters had useful main transformations, with at least 6 requiring sub-transformations for sufficiently specific feedback."

## Discussion


## Related Claims
- [Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases](workflow-matches-hand-analysis-on-linguistic-operator-subsets.md) — related
- [On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes](llm-transformations-explain-more-propositional-pairs-than-hand-picked.md) — related
- [The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs](workflow-generalizes-to-modal-logic-and-ctl.md) — related
- [The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake](workflow-finds-mistakes-unexplained-by-prior-hand-picked.md) — related
