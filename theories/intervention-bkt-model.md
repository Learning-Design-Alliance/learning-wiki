---
type: theory
title: "Intervention-BKT: a BKT extension that models the effect of instructional interventions on student knowledge states"
description: Intervention-BKT (IBKT) extends Bayesian Knowledge Tracing by adding input nodes representing instructional interventions such as elicit and tell.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: ye-mao-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
---

# Intervention-BKT: a BKT extension that models the effect of instructional interventions on student knowledge states

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Intervention-BKT (IBKT) extends Bayesian Knowledge Tracing by adding input nodes representing instructional interventions such as elicit and tell. The article describes it as "an extension of BKT, which incorporates the effect of multiple types of instructional interventions on student modeling": a student's knowledge state depends on the previous state and the current intervention, and performance depends on both the knowledge state and the intervention. It is a special case of an Input Output Hidden Markov Model using 1+4×K parameters, with per-intervention Learning Rate, Forget, Guess and Slip parameters.

## Design Implications

### Context
#### Requirements
- Requires logged sequences of instructional interventions paired with student performance observations, unlike conventional BKT which trains on performance alone
#### Constraints
- Observations on tell interventions are noisy because the exact duration a student spent reading a tell step is unknown; the authors used "fast and no performance observed" for all tells

### Target Learners
- college students in introductory physics or probability intelligent tutoring systems

### Target Learning Objectives
- domain knowledge in physics and probability as measured by post-test scores and learning gains

### Claims
- [Bkt Best Post Test Prediction Intervention Tutors](../claims/bkt-best-post-test-prediction-intervention-tutors.md) [~M]

## Related Theories

- [Four-Phase Taxonomy of Knowledge Tracing Variants](knowledge-tracing-variants-learning-phases.md)
- [Bayesian Knowledge Tracing (Two-State Hidden Markov Model)](bayesian-knowledge-tracing-two-state-model.md)
- [Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories](bkt-two-state-hmm-student-model.md)

## Examples
-

## Key Sources
- Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318
