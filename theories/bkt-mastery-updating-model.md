---
type: theory
title: Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment
description: "BKT models students' changing knowledge states during practice by updating, after each response, the probability that a skill is mastered."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: ying-cui-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    title: "Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    author: Ying Cui, Man-Wai Chu, Fu Chen
---

# Bayesian Knowledge Tracing as a model of changing skill mastery during game-based assessment

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
BKT models students' changing knowledge states during practice by updating, after each response, the probability that a skill is mastered. It parameterizes initial mastery, transition to mastery after an opportunity, slipping, and guessing, and updates mastery conditional on each correct or incorrect response. The article applies it to Raging Skies by treating each storm-feature measurement as a subskill updated per opportunity, and storm-type identification as evidence for the general interpreting skill. The authors note it "typically models the first attempts of solving a problem".

## Design Implications

### Context
#### Requirements
- Tasks must be scoreable as correct or incorrect per step, with retry actions removed so first attempts are modeled
#### Constraints
- Assumes model parameters do not vary with time, a simplification relative to DBN

### Target Learners
- Grade 5 science students

### Target Learning Objectives
- Weather observation and interpretation skills from the Weather Watch unit

### Claims
- [Bkt Fits Raging Skies Process Data](../claims/bkt-fits-raging-skies-process-data.md) [+M]
- [Bkt Mastery Profile Weather Skills](../claims/bkt-mastery-profile-weather-skills.md) [+M]

## Related Theories

- [Bayesian Knowledge Tracing (Two-State Hidden Markov Model)](bayesian-knowledge-tracing-two-state-model.md)
- [Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)](bkt-four-parameter-two-form-model.md)
- [Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories](bkt-two-state-hmm-student-model.md)
- [BKT+IRT: Bayesian Knowledge Tracing augmented with multidimensional generalizable student abilities and problem effects](bkt-irt-multidimensional-generalizable-model.md)
- [MS-BKT: a multistate knowledge tracing model with data-driven recency weights replacing the learning rate](ms-bkt-multistate-recency-weight-model.md)
- [Spectral BKT: a BKT variant combining feature compensation (3-gram observations) with model compensation (four latent states)](spectral-bkt-model.md)

## Examples
-

## Key Sources
- Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397
