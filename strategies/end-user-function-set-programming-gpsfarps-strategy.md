---
type: strategy
id: end-user-function-set-programming-gpsfarps-strategy
title: Deduce candidate functions from the failure-rate graph and program them into GPSFARPS via end-user programming
description: "The authors recommend that school administrators with knowledge of the failure-rate shape discover it \"using simple graph operations on test data\", deduce candidate functions, and program them into GPSFARPS using end-..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: jo-orove-2013
    resource: "https://www.osegi.com"
    title: "J.O. Orove, N.E. Osegi, B.O. Eke. (2013). A Multi-Gene Genetic Programming Application for Predicting Students Failure at School. https://www.osegi.com"
    author: J.O. Orove, N.E. Osegi, B.O. Eke
---

# Deduce candidate functions from the failure-rate graph and program them into GPSFARPS via end-user programming

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors recommend that school administrators with knowledge of the failure-rate shape discover it "using simple graph operations on test data", deduce candidate functions, and program them into GPSFARPS using end-user programming callback functions. In this way, they state, "novel solutions to the fa ilure rate problem may be discovered by the end -users themselves". A future design with an interactive-agile function data set to facilitate end-user programming is proposed.

## Design Implications

### Context
#### Requirements
- The school administrator needs first-hand knowledge of the shape of the failure rate, obtainable via simple graph operations on test data
- A function-set specification mechanism (callback functions) must be available in the application
#### Constraints
- The flexible function-set specification is discussed as a desirable capability; the proposed interactive-agile function data set is future work, not part of the reported system

### Target Learners
- school students whose failure rates administrators model

### Target Learning Goals
- predicting student failure rate with function sets matched to the observed failure-rate shape

## Claims

- [For the present case the GP algorithm should not be run for fewer than 10 generations](../claims/gp-minimum-ten-generations-boundary.md) [+W]
- [GPSFARPS simulations show fast convergence of the multi-gene GP run at about 30 generations from a specified maximum of 500](../claims/gpsfarps-fast-convergence-30-generations.md) [+W]
- [The multi-gene GP system minimized the evolved model to 4 of 6 predictor variables while predicting student failure rate](../claims/gpsfarps-minimal-model-four-predictors.md) [+W]
- [Evolved multi-gene GP solutions exhibit an accuracy-complexity trade-off with a non-dominated Pareto front](../claims/mggp-pareto-accuracy-complexity-tradeoff.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- J.O. Orove, N.E. Osegi, B.O. Eke. (2013). A Multi-Gene Genetic Programming Application for Predicting Students Failure at School. https://www.osegi.com
