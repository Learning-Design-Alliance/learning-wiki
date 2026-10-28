---
type: strategy
id: simulated-students-pre-deployment-testing
title: Use simulated students to test and compare adaptive-system strategies before engaging human students
description: "The article recommends testing and validating new student-modelling approaches through simulation first, because experiments with real students demand \"substantial amounts of financial, human resources and time.\" Simu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: fabiano-dorça-2015
    resource: "https://doi.org/10.1007/s40593-015-0037-0"
    title: "Fabiano Dorça. (2015). Implementation and use of Simulated Students for Test and Validation of new Adaptive Educational Systems: a Practical Insight. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0037-0"
    author: Fabiano Dorça
---

# Use simulated students to test and compare adaptive-system strategies before engaging human students

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends testing and validating new student-modelling approaches through simulation first, because experiments with real students demand "substantial amounts of financial, human resources and time." Simulation allows immediate evaluations, comparisons, adjustments and corrections from the very beginning of development, and human students should enter the process only when an approach's quality is attested. In this work the simulation rapidly identified the best of three strategies and enabled parameter adjustment at low cost.

## Design Implications

### Context
#### Requirements
- A stochastic model of how learning styles affect performance, derived from published studies, must be available to drive the simulated student
#### Constraints
- Simulation results are only a pre-deployment filter; the article does not report validation with real students

### Target Learners
- researchers and developers of adaptive educational systems

### Target Learning Goals
- efficient discovery of students' learning styles

### Affordances
- Probabilistic Learning Styles Model Lsp

## Related Strategies

- [Use LLM persona simulation only for preliminary experimentation, stress testing, and hypothesis generation, with separate validation for consequential applications](persona-simulation-preliminary-use-only.md)
- [Evaluate LLM-based tutors with human-inspired methods such as simulated students and behavior analysis before classroom deployment](human-inspired-evaluation-of-llm-tutors.md)
- [Simulation-based pre-validation of adaptive coaching systems before classroom deployment](simulation-prevalidation-before-classroom-deployment.md)
- [Develop complex simulations incrementally, testing each stage before adding the next feature](incremental-llm-simulation-development.md)
- [Initialize BKT parameters from simulated student data when no human data is available](initialize-bkt-parameters-from-simulated-data.md)

## Examples
-

## Key Sources
- Fabiano Dorça. (2015). Implementation and use of Simulated Students for Test and Validation of new Adaptive Educational Systems: a Practical Insight. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0037-0
