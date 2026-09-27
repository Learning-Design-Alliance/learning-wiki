---
type: element
id: bayes-net-toolbox-graph-transformations
title: Bayes Net Toolbox for Matlab used to carry out graph transformations algorithmically
description: "The article reports that all directed-acyclic-graph to moral-graph, triangulated-graph, and junction-tree transformations were done algorithmically with software rather than by hand: \"All graph transformations in this..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: rijmen-2010
    resource: "https://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Bayes Net Toolbox for Matlab used to carry out graph transformations algorithmically

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The article reports that all directed-acyclic-graph to moral-graph, triangulated-graph, and junction-tree transformations were done algorithmically with software rather than by hand: "All graph transformations in this paper were carried out using the Bayes Net Toolbox for Matlab (Murphy, 2001, 2007)." Directed acyclic graphs are represented as adjacency matrices, from which the moral graph, a triangulated graph, its cliques, and the junction tree can be readily obtained.

## Design Implications

### Context
#### Requirements
- The directed acyclic graph must be specified in matrix form, whose (i, j)th element equals 1 if there is an edge from node i to node j
#### Constraints
- 

### Target Learners
- Psychometricians and researchers estimating multidimensional IRT models for longitudinal data

### Target Learning Goals
- Automated determination of conditionally independent latent variable subsets for efficient model estimation

## Related Elements

- [BNL (Bayesian networks with logistic regression nodes)](bnl-bayesian-networks-logistic-regression-nodes.md)

## Examples
-

## Key Sources
- Rijmen, F. (2010). Measuring Multidimensional Latent Growth. ETS Research Report RR-10-24. https://www.ets.org/research/contact.html
