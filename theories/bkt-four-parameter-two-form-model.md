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
> **Evidence** · 7 claims (5 for, 1 mixed, 1 against) · 3 studies, `q1`–`q2` · 1 of 3 report an effect size · 7 claims rest on one study

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

- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](../claims/bkt-hmm-exponential-form-questions-fitting-practice.md) [-W]
- [The HMM form of BKT, solved analytically, is a three-parameter exponential in opportunity number](../claims/bkt-hmm-form-is-three-parameter-exponential.md) [+W]
- [The identifiability problem of the BKT HMM arises because combinations of P(G) and P(L0) with the same product A give identical functional forms](../claims/bkt-identifiability-explained-by-parameter-a.md) [+W]
- [Fixed point analysis of the Knowledge Tracing Algorithm yields parameter constraints P(G)+P(S)<1 and 0<P(T)<(1−P(S))/(1−P(G)) for sensible behavior](../claims/kt-algorithm-fixed-point-parameter-constraints.md) [+W]
- [The Knowledge Tracing Algorithm does not suffer the identifiability problem: all four parameters affect its behavior separately](../claims/kt-algorithm-no-identifiability-problem.md) [+W]
- [Under standard BKT with non-degenerate parameters, the mastery probability stays above the learn rate even after unboundedly many incorrect responses](../claims/bkt-mastery-floor-above-learn-rate.md) [+W]
- [BKT-BF suffers high computational cost and does not resolve BKT's identifiability problem, while EM is cheaper but suffers local minima](../claims/bkt-bf-cost-identifiability-em-local-minima.md) [~W]

## Related Theories

- [Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories](bkt-two-state-hmm-student-model.md)
- [Bayesian Knowledge Tracing (Two-State Hidden Markov Model)](bayesian-knowledge-tracing-two-state-model.md)

## Examples

- [Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM](../strategies/fit-a-fix-one-parameter-alternative-to-dirichlet-priors.md)

## Key Sources
- Brett Van de Sande. (2013). Properties of the Bayesian Knowledge Tracing Model. Journal of Educational Data Mining, Volume 5, No 2. https://jedm.educationaldatamining.org
