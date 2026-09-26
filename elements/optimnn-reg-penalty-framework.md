---
type: element
id: optimnn-reg-penalty-framework
title: "OptimNN-Reg: penalty-based regularization framework for non-degenerate BKT parameters"
description: OptimNN-Reg extends OptimNN by adding regularizing penalty terms to the binary cross-entropy loss with chosen coefficients, enforcing allowable-parameter rules (slip below 0.5, guess below 0.5, learn below (1-slip)/gu...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: badrinath-2023
    resource: "https://github.com/abadrinath947/OptimNN"
    title: "Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN"
    author: Badrinath, A. and Pardos, Z
---

# OptimNN-Reg: penalty-based regularization framework for non-degenerate BKT parameters

> **Element** · [All elements](index.md)

## Description
OptimNN-Reg extends OptimNN by adding regularizing penalty terms to the binary cross-entropy loss with chosen coefficients, enforcing allowable-parameter rules (slip below 0.5, guess below 0.5, learn below (1-slip)/guess) and supporting priors over BKT parameters via any differentiable distribution, demonstrated with a Dirichlet prior on guess rates. The paper argues the penalty approach "not only effectively generalizes to simple bound-based rules, but it could be used in more complex distribution-based rules". Generated guess-rate histograms roughly matched the chosen Dirichlet distribution on AST09.

## Design Implications

### Context
#### Requirements
- Choice of penalty coefficients, where higher values encourage the rule more aggressively; selection of an appropriate Dirichlet prior via domain knowledge or automatic approaches
#### Constraints
- Constraints are not hard and can be violated in favour of maximizing correctness prediction; no guarantees exist that given rules are followed, and challenging rules may require hyperparameter tuning of penalty weights

### Target Learners
- students in intelligent tutoring systems and computerized tutoring contexts

### Target Learning Goals
- fitting interpretable, non-degenerate knowledge tracing parameters for skill mastery estimation

### Affordances
- [Optimnn Hypernetwork Parameter Generation](../theories/optimnn-hypernetwork-parameter-generation.md)

## Related Elements
- 

## Examples
-

## Key Sources
- Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN
