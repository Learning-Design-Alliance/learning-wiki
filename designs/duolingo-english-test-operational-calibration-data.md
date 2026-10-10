---
type: design
id: duolingo-english-test-operational-calibration-data
title: Duolingo English Test operational calibration data used for the empirical evaluation
description: "The evaluation applied consensus calibration to operational response data from the Duolingo English Test, described as \"a high-volume, continuously evolving language assessment\" measuring two latent dimensions with it..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: paul-a-jewsbury-and-steven-w-nydick-and-manqian-liao-and-siyuan-marco-chen-2026
    resource: "https://arxiv.org/abs/2609.13590v1"
    title: "Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen. (2026). Bayesian Consensus Calibration of Continuously Evolving IRT Item Banks. https://arxiv.org/abs/2609.13590v1"
    author: Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen
---

# Duolingo English Test operational calibration data used for the empirical evaluation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The evaluation applied consensus calibration to operational response data from the Duolingo English Test, described as "a high-volume, continuously evolving language assessment" measuring two latent dimensions with items in several response formats (selected-response, partial-credit, and continuous). Each period was calibrated by a scalable Bayesian explanatory IRT engine with period-specific item posteriors thinned to approximately 1,000 draws. The run comprised four consecutive quarterly calibration periods spanning approximately one year with the third period defining the reference metric.

## Design Implications

### Context
#### Requirements
- A scalable Bayesian explanatory IRT calibration engine per period
- Consecutive calibration periods with a designated reference period
#### Constraints
- Each period included on the order of tens of thousands of items and hundreds of thousands of examinees
- The benchmark was fit with a separate ability distribution per period (a multiple-group model) to match the ability structure of the per-period calibrations

### Target Learners
- Duolingo English Test examinees

### Learning Goals
- language-proficiency scoring and adaptive item selection in a high-stakes assessment

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen. (2026). Bayesian Consensus Calibration of Continuously Evolving IRT Item Banks. https://arxiv.org/abs/2609.13590v1
