---
type: theory
title: "Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories"
description: "Bayesian Knowledge Tracing (BKT) is a student model used to infer a student's knowledge from their history of responses to skill-tagged problems and to predict future performance."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: martori-2015
    resource: "https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    title: "Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf"
    author: "Martori, F., Cuadros, J., & González-Sabaté, L"
---

# Bayesian Knowledge Tracing: a two-state Hidden Markov Model inferring skill mastery from response histories

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies, `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Bayesian Knowledge Tracing (BKT) is a student model used to infer a student's knowledge from their history of responses to skill-tagged problems and to predict future performance. It is "a two state Hidden Markov Model", with states for knowing and not knowing a skill, and an absorbent knowledge state implying no forgetting. It requires four probabilities: L0 (prior knowledge), T (transition/learning probability per practice opportunity), G (guess rate), and S (slip rate). Knowledge affects performance mediated by guess and slip rates, and knowledge at one time step affects knowledge at the next. Usually a separate BKT model is fit per skill using only first attempts.

## Design Implications

### Context
#### Requirements
- Response data tagged with the skills the instructor wants students to learn
- A history of student responses to problems (typically first attempts only)
- Values for the four probabilities L0, T, G, and S
#### Constraints
- The knowledge state is absorbent: the model assumes the student will not forget the skill once learned
- Usually a separate BKT model is fit for each skill

### Target Learners
- students in online/cognitive-tutor courses (e.g., MOOC students)

### Target Learning Objectives
- inferring mastery of instructor-tagged skills
- predicting future student performance

### Claims

- [MS-BKT mastery estimates fluctuate less than classic BKT and avoid over-high estimates after long incorrect runs, in fictitious-student comparisons](../claims/ms-bkt-estimates-fluctuate-less-than-bkt.md) [+W]
- [The exponential functional form of the BKT HMM calls into question the popular practice of fitting that model form to student data](../claims/bkt-hmm-exponential-form-questions-fitting-practice.md) [-W]

## Related Theories

- [Bayesian Knowledge Tracing: a four-parameter student-learning model in two forms (HMM and Knowledge Tracing Algorithm)](bkt-four-parameter-two-form-model.md)
- [Bayesian Knowledge Tracing (Two-State Hidden Markov Model)](bayesian-knowledge-tracing-two-state-model.md)
- [BKT Brute Force (BKT-BF): grid-search parameter estimation minimizing Residual Sum of Squares](bkt-brute-force-grid-search-estimation.md)
- [Spectral BKT: a BKT variant combining feature compensation (3-gram observations) with model compensation (four latent states)](spectral-bkt-model.md)
- [BKTransformer: transformer-based generation of temporally-evolving BKT parameters](bktransformer-temporal-bkt-parameters.md)

## Examples

- [Fit the combined parameter A and fix P(G) or P(L0) externally as an alternative to Dirichlet priors when fitting the BKT HMM](../strategies/fit-a-fix-one-parameter-alternative-to-dirichlet-priors.md)

## Key Sources
- Martori, F., Cuadros, J., & González-Sabaté, L. (2015). Direct estimation of the minimum RSS value for training Bayesian Knowledge Tracing parameters. Proceedings of the 8th International Conference on Educational Data Mining. https://www.educationaldatamining.org/EDM2015/proceedings/short364-367.pdf
