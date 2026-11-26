---
type: strategy
id: cross-validation-conjunctivity-evaluation-strategy
title: Evaluate cognitive models for skill conjunctivity by comparing additive and conjunctive IRT fits via cross-validation and parameter interpretability
description: "The article's method for answering whether skills in student log data are conjunctive is to fit both an additive and a conjunctive IRT model and compare them."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
sources:
  - id: hao-cen-2008
    resource: "https://doi.org/10.1007/978-3-540-69132-7_111"
    title: "Hao Cen, Kenneth Koedinger, and Brian Junker. (2008). Comparing Two IRT Models for Conjunctive Skills. ITS 2008, LNCS 5091, pp. 796–798. https://doi.org/10.1007/978-3-540-69132-7_111"
    author: Hao Cen, Kenneth Koedinger, and Brian Junker
---

# Evaluate cognitive models for skill conjunctivity by comparing additive and conjunctive IRT fits via cross-validation and parameter interpretability

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's method for answering whether skills in student log data are conjunctive is to fit both an additive and a conjunctive IRT model and compare them. Cross validation errors and the interpretability of the actual parameter fits are used to evaluate the models, with simulated conjunctive data used to establish which model wins when the data is known to be conjunctive, and real assessment data used to test whether the data is conjunctive in character.

## Design Implications

### Context
#### Requirements
- Simulated data drawn from the conjunctive model to calibrate expectations, plus a real assessment dataset with a Q-matrix skill coding
#### Constraints
- When students were not exposed to repetitive learning opportunities, the learning term was removed from both models

### Target Learners
- students in intelligent tutoring systems

### Target Learning Goals
- evaluating and improving the quality of cognitive models used by tutors

## Claims

- [On the real EAPS algebra dataset, CFM-P was not clearly better than AFM-P, and AFM-P essentially performed as a conjunctive model through negative skill estimates](../claims/afm-acts-conjunctive-eaps-real-data.md) [+W]
- [On simulated conjunctive data, CFM-PMLE was as good as or better than AFM-PMLE in mean cross-validation error, with the largest gap when all skill probabilities were high (.9, .9, .9)](../claims/cfm-beats-afm-simulated-conjunctive-data.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Hao Cen, Kenneth Koedinger, and Brian Junker. (2008). Comparing Two IRT Models for Conjunctive Skills. ITS 2008, LNCS 5091, pp. 796–798. https://doi.org/10.1007/978-3-540-69132-7_111
