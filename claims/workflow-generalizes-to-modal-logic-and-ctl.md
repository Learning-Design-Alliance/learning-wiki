---
type: claim
title: "The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs"
description: "The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs"
id: workflow-generalizes-to-modal-logic-and-ctl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lilian-killich-2026
    resource: "https://doi.org/10.48550/arxiv.2609.17111"
    title: "Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)"
    author: Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: lilian-killich-2026-2
    resource: "https://arxiv.org/abs/2609.17111"
    title: "Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111"
    author: Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` On the modal logic dataset (12482 pairs) the workflow's transformations explain 79.39% of pairs, comparable to the propositional case. [→ Lilian Killich 2026](#lilian-killich-2026)
`q2 i?` On the CTL dataset (7210 pairs) the workflow's transformations explain 35.89% of pairs, with the two largest transformations explaining 2.98% and 2.48%. [→ Lilian Killich 2026 (2)](#lilian-killich-2026-2)

## Evidence

### Lilian Killich 2026

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)

`q2 · i?` · `design · r2`

Second experiment set applying the workflow to a modal logic dataset of 12482 pairs (3951 distinct) from prior work; the article reports coverage of "79.39% of the pairs in the data set". No effect size printed.

> "For modal logic, the transformations found by our workflow explain 79.39% of the pairs in the data set, which is comparable to the propositional logic case."

### Lilian Killich 2026 (2)

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111

`q2 · i?` · `design · r2`

Application to a CTL dataset of 7210 pairs (2695 distinct) collected by the authors with an interactive learning tool in two iterations of an introductory logic course; coverage is "35.89% of the pairs", lower than the other formalisms.

> "For CTL, the transformations found by our workflow explain 35.89% of the pairs with the two transformations that explain the largest fractions of the data set being"

## Discussion


## Related Claims
- [Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback](cluster-main-transformations-suitable-for-feedback-with-limits.md) — related
- [On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes](llm-transformations-explain-more-propositional-pairs-than-hand-picked.md) — related
- [The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake](workflow-finds-mistakes-unexplained-by-prior-hand-picked.md) — related
- [Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases](workflow-matches-hand-analysis-on-linguistic-operator-subsets.md) — related
