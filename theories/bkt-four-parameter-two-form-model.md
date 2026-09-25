---
type: theory
title: "Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)"
description: "Bayesian Knowledge Tracing models student learning of a skill with four parameters: P(L0) the initial probability the student knows the skill, P(G) the guessing probability, P(S) the slipping probability, and P(T) the..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: brett-van-de-sande-2013
    resource: "https://jedm.educationaldatamining.org"
    title: "Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org"
    author: Brett Van de Sande
---

# Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)

> **Theory** · [All theories](index.md)

## Description
Bayesian Knowledge Tracing models student learning of a skill with four parameters: P(L0) the initial probability the student knows the skill, P(G) the guessing probability, P(S) the slipping probability, and P(T) the per-opportunity learning probability, with P(T) assumed constant over time. The article treats two forms: the hidden Markov model form that predicts the probability of correct application as a function of prior opportunities, and the Knowledge Tracing Algorithm form that updates the conditional probability of knowing in real time from each correct or incorrect response. The article states the model 'has four parameters which must be supplied externally' for the algorithm form.

## Design Implications

### Context
#### Requirements
- The four parameters P(L0), P(G), P(S), and P(T) must be supplied externally for the Knowledge Tracing Algorithm form
#### Constraints
- P(T) is assumed to be constant over time

### Target Learners
- students practicing skills in tutor systems

### Target Learning Objectives
- estimating whether a student has learned a skill from correctness of practice opportunities

### Claims
- 

## Related Theories
- 

## Examples
-

## Key Sources
- Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org
