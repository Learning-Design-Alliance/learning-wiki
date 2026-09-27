---
type: claim
title: Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable
description: Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable
id: bifactor-within-occasion-tractable-cliques
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: moderate
sources:
  - id: rijmen-2010
    resource: "https://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html"
    author: Rijmen, F.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
  - id: rijmen-2010-2
    resource: "https://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html"
    author: Rijmen, F.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r2`–`r3` · `q2`

## Subclaims
`q2 i?` For within-occasion bifactor and second-order models with a first-order Markov structure on the general dimension, no clique contains more than two latent variables, making the models computationally tractable. [→ Rijmen 2010](#rijmen-2010)
`q2 i?` Adding an overarching general dimension to the within-occasion bifactor model yields cliques with at most three latent variables, the same complexity order as the unidimensional within-occasion model with combined bifactor and Markov structure. [→ Rijmen 2010 (2)](#rijmen-2010-2)

## Evidence

### Rijmen 2010

Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

`q2 · i?` · `theoretical · r2`

Graphical analysis of within-occasion bifactor (D = 3 + 1) and second-order models with a first-order Markov structure on the general dimension over T = 3 occasions. The article reports that "no clique contains more than two latent variables," so both models are tractable.

> "Again, the graphs are already triangulated. For both models, no clique contains more than two latent variables, and hence both models are computationally tractable."

### Rijmen 2010 (2)

Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

`q2 · i?` · `theoretical · r3`

Graphical derivation for the tri-factor model (D specific dimensions per occasion, T general dimensions over time, one overarching dimension). The article finds the complexity "of the same order" as the unidimensional within-occasion model, with at most three latent variables per clique.

> "It is remarkable that the computational complexity of this model is of the same order as the computational complexity of the unidimensional within-measurement occasion model with a combined bifactor and first-order Markov structure across measurement occasions."

## Discussion


## Related Claims
- [Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions](markov-all-dimensions-poor-scaling.md) — related
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](junction-tree-em-linear-complexity-occasions.md) — related
- [Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker](mml-bifactor-two-dimensional-integrals-general-conditions.md) — related
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — a broader claim this one bears on
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](mml-second-order-dimension-two-dimensional-integrals.md) — related
