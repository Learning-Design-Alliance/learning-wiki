---
type: theory
title: "BKTransformer: transformer-based generation of temporally-evolving BKT parameters"
description: "BKTransformer extends OptimNN by generating BKT parameters that vary over time within a student's problem sequence."
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

# BKTransformer: transformer-based generation of temporally-evolving BKT parameters

> **Theory** · [All theories](index.md)

## Description
BKTransformer extends OptimNN by generating BKT parameters that vary over time within a student's problem sequence. A base parameter network f generates per-skill parameters, and a transformer decoder g (GPT-2-style, resembling SAKT) additively adjusts them conditioned on the student's sequence; the key architectural difference from SAKT is that the final layer "outputs BKT parameters as opposed to the correctness prediction". Predicting BKT parameters rather than correctness directly lets correctness predictions be "probabilistically justified by the produced slip, guess, forget, and learn parameters", retaining a layer of interpretability over deep KT methods while allowing non-Markovian learning and parameter sharing across skills.

## Design Implications

### Context
#### Requirements
- Penalty terms on adjustment magnitude and consecutive-timestep adjustment differences (coefficients lambda5, lambda6) to keep parameters from varying arbitrarily over time
#### Constraints
- The paper states it is unable to fully interpret the components of BKTransformer that precede the BKT layer, preventing understanding of how and why parameters evolve as they do

### Target Learners
- students in intelligent tutoring systems and computerized tutoring contexts

### Target Learning Objectives
- student response correctness prediction and mastery probability estimation in knowledge tracing

### Claims
- [Bktransformer Rivals Deep Kt Auc](../claims/bktransformer-rivals-deep-kt-auc.md) [+M]
- [Bkt Parameter Evolution Interpretability](../claims/bkt-parameter-evolution-interpretability.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Badrinath, A. and Pardos, Z. (2023). Optimizing Bayesian Knowledge Tracing with Neural Network Parameter Generation. https://github.com/abadrinath947/OptimNN
