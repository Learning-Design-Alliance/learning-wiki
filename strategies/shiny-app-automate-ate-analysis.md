---
type: strategy
id: shiny-app-automate-ate-analysis
title: Automate E-TRIALS data cleaning and ATE modeling through a Shiny application with predefined outcome variables
description: The authors propose building a Shiny application so researchers can evaluate E-TRIALS experiments without manually running the analysis pipeline.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: siedahmed-2025
    resource: "https://arxiv.org/abs/2502.10545"
    title: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. https://arxiv.org/abs/2502.10545"
    author: "Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A"
---

# Automate E-TRIALS data cleaning and ATE modeling through a Shiny application with predefined outcome variables

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors propose building a Shiny application so researchers can evaluate E-TRIALS experiments without manually running the analysis pipeline. The article states the plan is "to build a Shiny application to fully automate the data cleaning and modeling process," letting users "upload their CSV files and select from a predefined list of outcome variables." This would reduce the time and effort required to evaluate experiments using the paper's estimator code.

## Design Implications

### Context
#### Requirements
- Users upload their E-TRIALS CSV data files to the application
- Outcome variables must be selected from a predefined list
#### Constraints
- The method and code discussed in the paper are designed for support comparison studies; a generalized framework for problem-varied studies is not feasible due to researchers' design autonomy

### Target Learners
- education researchers conducting experiments in computer-based learning platforms

### Target Learning Goals
- estimating average treatment effects of instructional interventions

## Claims

- [The LOOP estimator provides an unbiased ATE estimate with greater precision than the Student's t-test when covariate imputation improves on mean imputation](../claims/loop-estimator-unbiased-precise.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Siedahmed, A., Pei, Y., Sales, A., Heffernan, N. T., Gagnon-Bartsch, J. A., Zhang, D., Schuetze, B. A., & Zengilowski, A. (2025). E-TRIALS: Empowering Data-Driven Decisions to Enhance Computer-Based Learning Platforms. arXiv. https://arxiv.org/abs/2502.10545
