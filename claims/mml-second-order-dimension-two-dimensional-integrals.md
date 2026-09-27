---
type: claim
title: Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals
description: Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals
id: mml-second-order-dimension-two-dimensional-integrals
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
    kind: theoretical
    rigour: 3
---

# Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` For a multidimensional IRT model in which all dependencies between first-order dimensions are explained by a second-order dimension, the efficient EM algorithm's E-step involves a sequence of two-dimensional integrals over (zk, zg). [→ Rijmen 2009](#rijmen-2009)

## Evidence

### Rijmen 2009

Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html

`q2 · i?` · `theoretical · r3`

Analytical demonstration in the section on a multidimensional model with a second-order dimension, derived from the junction tree for a four-dimensional model (Figures 5 and 6). The article notes the second-order model "is a bi-factor model with the additional restriction that the conditional item response probabilities do not directly depend on the general dimension".

> "It turns out that full information maximum likelihood estimation for such a model also requires the evaluation of two-dimensional integrals only."

## Discussion


## Related Claims
- [Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker](mml-bifactor-two-dimensional-integrals-general-conditions.md) — related
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — a broader claim this one bears on
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](bifactor-within-occasion-tractable-cliques.md) — related
