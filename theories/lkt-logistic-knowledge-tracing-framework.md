---
type: theory
title: "Logistic knowledge tracing (LKT): a symbolic notation framework for specifying logistic regression learner models"
description: LKT is a theoretically motivated framework for systematic specification and evaluation of student models for adaptive instructional environments, built on logistic regression.
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

# Logistic knowledge tracing (LKT): a symbolic notation framework for specifying logistic regression learner models

> **Theory** · [All theories](index.md)

## Description
LKT is a theoretically motivated framework for systematic specification and evaluation of student models for adaptive instructional environments, built on logistic regression. Its strength is a symbolic notation system in which models are composed of terms, each with a feature applied at a component level (student, item, KC), including intercept, linear, and nonlinear features such as recency, decay, and spacing. The framework subsumes extant models like AFM, PFA, and R-PFA as special cases and facilitates comparing their strengths and weaknesses.

## Design Implications

### Context
#### Requirements
- A sequence of learner event data with subject and correctness columns, minimally in DataShop format
#### Constraints
- The article intentionally limits scope to logistic regression models and does not compare against BKT or deep knowledge tracing

### Target Learners
- students using adaptive learning technology systems

### Target Learning Objectives
- predicting correctness of subsequent practice items to guide pedagogical decisions

### Claims
- [No Single Learner Model Best Across Datasets](../claims/no-single-learner-model-best-across-datasets.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569
