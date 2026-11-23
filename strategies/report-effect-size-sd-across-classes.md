---
type: strategy
id: report-effect-size-sd-across-classes
title: Report the standard deviation of effect sizes across classes whenever conducting multilevel modeling, to quantify differential effectiveness
description: "The article's concluding recommendation is that analysts go beyond a single average effect size: whenever conducting multilevel modeling, one should report the standard deviations of the estimates across the multileve..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: yannis-bähni-2025
    resource: "https://arxiv.org/abs/2507.14848"
    title: "Yannis Bähni. (2025). A Bayesian Approach to Estimating Effect Sizes in Educational Research. arXiv. https://arxiv.org/abs/2507.14848"
    author: Yannis Bähni
---

# Report the standard deviation of effect sizes across classes whenever conducting multilevel modeling, to quantify differential effectiveness

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's concluding recommendation is that analysts go beyond a single average effect size: whenever conducting multilevel modeling, one should report the standard deviations of the estimates across the multilevel structure. Even when the mean effect size has a positive credible interval, its standard deviation across classes can still be large, and this differential perspective should prevent overestimation of effect sizes and make interpretation more nuanced.

## Design Implications

### Context
#### Requirements
- A multilevel model with the clustering structure (e.g., students nested within classes) must be fitted so that class-wise effect sizes and their standard deviation can be computed.
#### Constraints
- Including the multilevel structure can make model estimation slow and result in convergence issues, especially with random slopes and intercepts for residual standard deviations.
- Multilevel modeling remains a variable-centered method that does not qualitatively or quantitatively capture heterogeneity between individuals, unlike person-centered methods such as latent profile analysis.

### Target Learners
- Educational researchers evaluating interventions in clustered classroom settings

### Target Learning Goals
- Quantifying the differential effectiveness of educational interventions across classes

## Claims

- [Effect sizes varied across classes, revealing the intervention's differential effectiveness: SD of d_s was 0.09 at pretest and 0.18 at posttest, with some classes showing control outperforming intervention](../claims/differential-effectiveness-across-classes.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yannis Bähni. (2025). A Bayesian Approach to Estimating Effect Sizes in Educational Research. arXiv. https://arxiv.org/abs/2507.14848
