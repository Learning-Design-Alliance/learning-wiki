---
type: claim
title: Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions
description: Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions
id: markov-all-dimensions-poor-scaling
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
---

# Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` For the within-occasion bifactor model with first-order Markov structures over time for all dimensions, the maximal number of latent variables in a clique increases with T (four when D = 3 and T = 3; six when T = 6 under the heuristic triangulation used). [→ Rijmen 2010](#rijmen-2010)

## Evidence

### Rijmen 2010

Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html

`q2 · i?`

Graphical analysis of the model requiring triangulation edges. The article reports the maximal clique held four latent variables when both D = 3 and T = 3, and that "For T = 6, the largest number of latent variables in a clique was six" using the same heuristic triangulation algorithm.

> "In contrast to all previously presented models, the model with a bifactor within-measurement occasion structure and a first-order Markov structure over time for all dimensions does not scale well with the number of measurement occasions."

## Discussion


## Related Claims
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](bifactor-within-occasion-tractable-cliques.md) — related
- [Meaningful longitudinal linking depends on the construct not changing across measurement occasions](construct-stability-assumption-longitudinal-linking.md) — related
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](junction-tree-em-linear-complexity-occasions.md) — related
- [Multidimensional latent variable models rarely support more than about four to six latent variables, limiting fine-grained SKIVE modeling](latent-variable-models-limit-grain-size.md) — related
- [Computational complexity of the graph-based MML procedure scales with the number of latent variables within a conditionally independent subset, and brute-force integration scales exponentially with dimensionality](mml-complexity-scales-with-clique-state-spaces.md) — related
