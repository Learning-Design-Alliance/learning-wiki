---
type: claim
title: Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases
description: Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases
id: workflow-matches-hand-analysis-on-linguistic-operator-subsets
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
---

# Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` For more than 64% of the linguistic operator subdatasets the workflow finds transformations explaining more pairs than the hand-picked mistakes, and for more than 14% it explains exactly as many. [→ Lilian Killich 2026](#lilian-killich-2026)

## Evidence

### Lilian Killich 2026

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)

`q2 · i?` · `design · r2`

Comparison experiment on the propositional dataset partitioned into 34 subdatasets by linguistic operator (median size 65.5), testing whether the workflow reproduces the by-hand approach; the workflow "explain[s] more data points than the mistakes identified in [13]" for over 64% of subdatasets.

> "For > 64% of the lingustic operator data sets, our workflow finds bug fixing transformations transformations that explain more data points than the mistakes identified in [13]. For > 14%of the subdata sets, the transformations explain exactly as many pairs as the hand-picked mistakes."

## Discussion


## Related Claims
- [Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback](cluster-main-transformations-suitable-for-feedback-with-limits.md) — related
- [On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes](llm-transformations-explain-more-propositional-pairs-than-hand-picked.md) — related
- [The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake](workflow-finds-mistakes-unexplained-by-prior-hand-picked.md) — related
- [The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs](workflow-generalizes-to-modal-logic-and-ctl.md) — related
