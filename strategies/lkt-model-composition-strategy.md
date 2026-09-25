---
type: strategy
id: lkt-model-composition-strategy
title: Compose LKT models by starting with a student-ability feature, adding KC/item difficulty intercepts, then adding and splitting dynamic learning features
description: The article recommends a stepwise procedure for building a learner model from scratch in LKT.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: philip-i-pavlik-2021
    resource: "https://doi.org/10.1109/TLT.2021.3128569"
    title: "Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569"
    author: Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams
---

# Compose LKT models by starting with a student-ability feature, adding KC/item difficulty intercepts, then adding and splitting dynamic learning features

> **Strategy** · [All strategies](index.md)

## Description
The article recommends a stepwise procedure for building a learner model from scratch in LKT. Models meant to generalize to unseen students should begin with the propdec or logitdec features to capture student variability; initial KC or item difficulty is accounted for with fixed or random intercepts; then learning features such as lineafm are added, and dynamic features that work well can be split (e.g., lineafm into linesuc and linefail) to capture richer effects, with cross-validation confirming generalizability.

## Design Implications

### Context
#### Requirements
- A dataset with a sequence of learner events including subject and correctness columns
- Cross-validation and model visualizations to confirm found models are generalizable
#### Constraints
- Fixed effects may be inadequate if items are truly sampled from a distribution or if data are sparse

### Target Learners
- students in adaptive learning technology systems

### Target Learning Goals
- accurate prediction of student correctness to guide pedagogical decisions

### Affordances
- [Lkt Logistic Knowledge Tracing Framework](../theories/lkt-logistic-knowledge-tracing-framework.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569
