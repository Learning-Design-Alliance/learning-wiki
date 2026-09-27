---
type: claim
title: Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker
description: Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker
id: mml-bifactor-two-dimensional-integrals-general-conditions
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
---

# Full information MML estimation of the bi-factor model requires only two-dimensional integrations under more general conditions than the probit-link, multivariate-normal derivation of Gibbons and Hedeker

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` The junction-tree derivation reduces the bi-factor model's E-step to two-dimensional integrations over (theta_g, theta_k) for any link function, without assuming multivariate normality, requiring only conditional independence of the specific latent variables given general ability. [→ Rijmen 2009](#rijmen-2009)

## Evidence

### Rijmen 2009

Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html

`q2 · i?`

Analytical derivation in the paper, using the graphical model framework applied to the bi-factor model. It generalizes the earlier result that full information estimation "only requires the integration over two-dimensional integrals" beyond the probit link, normal distribution, and fully independent latent variables assumed by Gibbons and Hedeker.

> "It follows that an efficient full information MML estimation method, involving a sequence of two-dimensional integrations over the sets ( ),g kθ θ , can be derived under much more general conditions than the ones stated by Gibbons and Hedeker (1992)."

## Discussion


## Related Claims
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](mml-second-order-dimension-two-dimensional-integrals.md) — related
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — a broader claim this one bears on
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](bifactor-within-occasion-tractable-cliques.md) — related
