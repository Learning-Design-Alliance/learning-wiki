---
type: strategy
id: combine-statistical-and-physical-uncertainty-metrics
title: Use statistical standard deviations alongside physical uncertainties to interrogate data sets for outliers
description: "Rather than treating LINEST-style statistical metrics as a replacement or a rival, the article recommends deploying both: the physical uncertainty analysis as the primary consistent treatment, and the statistical stan..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: kevin-l-haglin-2023
    resource: "https://arxiv.org/abs/2303.13413"
    title: "Kevin L. Haglin. (2023). Uncertainty Principles for Teaching Laboratories. arXiv. https://arxiv.org/abs/2303.13413"
    author: Kevin L. Haglin
---

# Use statistical standard deviations alongside physical uncertainties to interrogate data sets for outliers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Rather than treating LINEST-style statistical metrics as a replacement or a rival, the article recommends deploying both: the physical uncertainty analysis as the primary consistent treatment, and the statistical standard deviations as a comparison tool. The author states that "the statistical metrics are often very useful to be used in conjunction with the measurement uncertainty techniques to interrogate data sets" and that both strategies are encouraged.

## Design Implications

### Context
#### Requirements
- Access to the LINEST function or the printed formulas (Eqs. 11 and 12) for the statistical standard deviations of slope and intercept
#### Constraints
- If a full uncertainty analysis is not feasible, the standard deviations are suitable alternatives, but they cannot express measurement uncertainties

### Target Learners
- introductory physics laboratory students
- educators designing laboratory activities

### Target Learning Goals
- uncertainty analysis
- identifying outliers in laboratory data sets

## Claims

- [The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes](../claims/minmax-uncertainty-outlier-susceptible.md) [+W]
- [The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures](../claims/mad-converges-negative-point-23.md) [+W]
- [In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity](../claims/uncertainty-quality-increases-with-complexity.md) [+W]

## Related Strategies

- [Sequence uncertainty measures by increasing complexity: start with min-max, then exclude extremes, middle 50%, MAD, and finally standard deviation](strategy-sequence-uncertainty-measures-by-complexity.md)

## Examples
-

## Key Sources
- Kevin L. Haglin. (2023). Uncertainty Principles for Teaching Laboratories. arXiv. https://arxiv.org/abs/2303.13413
