---
type: claim
title: "On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes"
description: "On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes"
id: llm-transformations-explain-more-propositional-pairs-than-hand-picked
status: draft
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

# On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the full propositional dataset of 6106 pairs, workflow-found transformations explain 5156 pairs (84.44%) while hand-picked mistakes explain 4370 pairs (71.57%), with 918 pairs (15.03%) explained exclusively by the transformations. [→ Lilian Killich 2026](#lilian-killich-2026)

## Evidence

### Lilian Killich 2026

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111 [doi:10.48550/arxiv.2609.17111](https://doi.org/10.48550/arxiv.2609.17111)

`q2 · i?` · `design · r2`

Evaluation on the propositional logic dataset from prior work (6106 pairs, 1572 distinct), comparing coverage of workflow-found transformations against hand-picked mistakes; the transformations "explain 5156 of the pairs (84.44%)" versus 71.57% for hand-picked mistakes. No effect size is printed.

> "Across the whole data set, the bug fixing transformations found by our workflow explain 5156 of the pairs (84.44%), whereas the hand-picked mistakes only explain 4370 of the pairs (71.57%). 918 pairs (15.03%) are exclusively explained by the transformations"

## Discussion


## Related Claims
- [Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback](cluster-main-transformations-suitable-for-feedback-with-limits.md) — related
- [Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases](workflow-matches-hand-analysis-on-linguistic-operator-subsets.md) — related
- [The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake](workflow-finds-mistakes-unexplained-by-prior-hand-picked.md) — a narrower finding that bears on this claim
- [The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs](workflow-generalizes-to-modal-logic-and-ctl.md) — related
