---
type: claim
title: The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake
description: The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake
id: workflow-finds-mistakes-unexplained-by-prior-hand-picked
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lilian-killich-2026
    resource: "https://arxiv.org/abs/2609.17111"
    title: "Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111"
    author: Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The workflow discovers new mistake candidates not explained by prior hand-picked mistakes, such as an exclusive-or-instead-of-negated-conjunction mistake

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The transformation representing using an exclusive or, expressed as a disjunction of conjunctions, instead of a negated conjunction explains 114 pairs (6.57% of pairs unexplained by hand-picked mistakes); a related hand-picked mistake covered only the bi-implication case. [→ Lilian Killich 2026](#lilian-killich-2026)

## Evidence

### Lilian Killich 2026

Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111

`q2 · i?` · `design · r2`

Analysis of pairs exclusively explained by workflow-found transformations on the full propositional dataset; the xor-nand transformation "explains 114 pairs (6.57% of the pairs unexplained by the hand-picked mistakes)". A second transformation explained 28 pairs (1.61%).

> "The transformation𝜌xor-nand represents the common mistake of using an exclusive or, expressed using a disjunction of conjunctions, instead of a negated conjunction which explains 114 pairs (6.57% of the pairs unexplained by the hand-picked mistakes)."

## Discussion


## Related Claims
- [Educator inspection found most large clusters' main transformations suitable for feedback, though many required sub-transformations for targeted feedback](cluster-main-transformations-suitable-for-feedback-with-limits.md) — related
- [On the full propositional logic dataset, LLM-found bug fixing transformations explain 84.44% of pairs versus 71.57% for hand-picked mistakes](llm-transformations-explain-more-propositional-pairs-than-hand-picked.md) — a broader claim this one bears on
- [Across linguistic-operator subdatasets, workflow-found transformations explain at least as many pairs as hand-picked mistakes in most cases](workflow-matches-hand-analysis-on-linguistic-operator-subsets.md) — related
- [The workflow generalizes beyond propositional logic, explaining 79.39% of modal logic pairs and 35.89% of CTL pairs](workflow-generalizes-to-modal-logic-and-ctl.md) — related
