---
type: claim
title: Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions
description: Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions
id: junction-tree-em-linear-complexity-occasions
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
    rigour: 3
---

# Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` For the leading unidimensional model with a first-order Markov structure, the efficient EM algorithm's E-step complexity is of order 2 × T × S² rather than exponential in T. [→ Rijmen 2010](#rijmen-2010)

## Evidence

### Rijmen 2010

Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

`q2 · i?` · `theoretical · r3`

Analytical derivation for the leading example model (unidimensional within occasions, first-order Markov across occasions). The article derives that the E-step of the efficient EM-algorithm requires computations "of order 2 × T × S2" versus S^T for a traditional EM-algorithm, so complexity becomes "linear in the number of measurement occasions."

> "So, a complexity that is exponential in the number of measurement occasions is reduced to a complexity that is linear in the number of measurement occasions."

## Discussion


## Related Claims
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](bifactor-within-occasion-tractable-cliques.md) — related
- [Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions](markov-all-dimensions-poor-scaling.md) — related
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — a broader claim this one bears on
- [Multidimensional IRT scores that account for latent variable covariances over time produce better recovery of growth parameters in longitudinal growth models than sum scores and other IRT approaches](multidimensional-irt-covariance-scores-better-growth-recovery.md) — related
