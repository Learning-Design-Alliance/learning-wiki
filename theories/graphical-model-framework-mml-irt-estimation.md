---
type: theory
title: Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models
description: The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: rijmen-2009
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Graphical model framework for deriving efficient MML estimation schemes for multidimensional IRT models

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (5 for, 1 against) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article presents a framework in which a multidimensional IRT model is represented as a directed acyclic graph whose nodes are random variables and whose edges encode conditional (in)dependence relations. The DAG is moralized, triangulated, and transformed into a junction tree, and the E-step of the EM algorithm is carried out via local computations on the tree. A stated advantage is that "these subsets of variables can be derived in a fully automatic way by applying algorithms to the graphical representation of the model", making the approach generally applicable and rendering hand derivations obsolete.

## Design Implications

### Context
#### Requirements
- The statistical model must be representable as a directed acyclic graph, with latent variables approximated by discrete latent variables when continuous parents would have discrete children
- Conditional independence relations must be imposed by the model structure for the efficiency gains to materialize
#### Constraints
- A thorough account of the graph theory behind the general procedure is stated to be outside the scope of the paper, with main results given without proof
- Finding an optimal triangulation is NP-hard, though well performing heuristic algorithms are available

### Target Learners
- Educational measurement researchers and psychometricians estimating multidimensional IRT models

### Target Learning Objectives
- Efficient, feasible estimation of parameters of structured multidimensional item response theory models

### Claims

- [Mml Bifactor Two Dimensional Integrals General Conditions](../claims/mml-bifactor-two-dimensional-integrals-general-conditions.md) [+S]
- [Mml Complexity Scales With Clique State Spaces](../claims/mml-complexity-scales-with-clique-state-spaces.md) [+S]
- [Full information MML estimation of a multidimensional IRT model with a second-order dimension also requires only two-dimensional integrals](../claims/mml-second-order-dimension-two-dimensional-integrals.md) [+W]
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](../claims/bifactor-within-occasion-tractable-cliques.md) [+M]
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](../claims/junction-tree-em-linear-complexity-occasions.md) [+W]
- [Adding Markov structures for both general and specific dimensions over time yields a model that does not scale well with the number of measurement occasions](../claims/markov-all-dimensions-poor-scaling.md) [-W]

## Related Theories

- [Graphical model framework for exploiting conditional independence to make multidimensional IRT estimation tractable](graphical-model-framework-multidimensional-irt-complexity.md)

## Examples

- [Bayes Net Toolbox for Matlab used to carry out graph transformations algorithmically](../elements/bayes-net-toolbox-graph-transformations.md)
- [BNL (Bayesian networks with logistic regression nodes)](../elements/bnl-bayesian-networks-logistic-regression-nodes.md)
- [Explore candidate models with limited-information estimation first, then estimate the structured model with the efficient EM algorithm](../strategies/limited-information-then-efficient-em-sequential-procedure.md)

## Key Sources
- Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html
