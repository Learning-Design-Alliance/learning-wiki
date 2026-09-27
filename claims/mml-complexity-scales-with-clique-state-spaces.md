---
type: claim
title: Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality
description: Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality
id: mml-complexity-scales-with-clique-state-spaces
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: weak
sources:
  - id: rijmen-2009
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html"
    author: Rijmen, F.
    q: 2
    i: "?"
  - id: rijmen-2009-2
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html"
    author: Rijmen, F.
    q: 2
    i: "?"
---

# Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` The computational complexity of a full information MML procedure exploiting the model's conditional independence relations scales with the number of latent variables within a subset, which may be substantially lower than the total number of latent variables. [→ Rijmen 2009](#rijmen-2009)
`q2 i?` Without imposed conditional independence structure, full information MML estimation remains infeasible as dimensionality grows. [→ Rijmen 2009 (2)](#rijmen-2009-2)

## Evidence

### Rijmen 2009

Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html

`q2 · i?`

Analytical statement from the introduction, elaborated in the junction tree algorithm section where the E-step's complexity is stated to scale with "the sum of the clique state spaces", so smaller clique state spaces yield greater efficiency gains over the standard EM algorithm.

> "The level of computational complexity of a full information MML procedure that exploits the conditional independence relation implied by the model scales with the number of latent variables within a subset, which may be substantially lower than the total number of latent variables."

### Rijmen 2009 (2)

Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html

`q2 · i?`

Boundary-condition statement from the Discussion, grounding the earlier observation that with Gaussian quadrature "the number of calculations involved increases exponentially with the number of dimensions". Such unstructured models are mostly considered at an exploratory stage, where MML results are not crucial.

> "When one is not willing to impose any conditional independence relations, full information MML estimation still becomes infeasible with an increasing number of dimensions."

## Discussion


## Related Claims
- [Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker](mml-bifactor-two-dimensional-integrals-general-conditions.md) — a narrower finding that bears on this claim
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](junction-tree-em-linear-complexity-occasions.md) — a narrower finding that bears on this claim
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](bifactor-within-occasion-tractable-cliques.md) — a narrower finding that bears on this claim
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](mml-second-order-dimension-two-dimensional-integrals.md) — a narrower finding that bears on this claim
- [Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions](markov-all-dimensions-poor-scaling.md) — related
