---
type: element
id: synthetic-within-study-comparison-rd
title: Synthetic within-study comparison design for assessing RD performance
description: "A methodological artifact in which the authors \"generate synthetic RD data sets from experimental data sets\" from two recent evaluations of educational interventions—the Educational Technology Study and the Teach for..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: philip-gleason-2018
    resource: "https://www.mathematica.org/publications/rd-or-not-rd-using-experimental-studies-to-assess-the-performance-of-the-regression-discontinuity"
    title: "Philip Gleason, Alexandra Resch, Jillian Berk. (2018). RD or Not RD: Using Experimental Studies to Assess the Performance of the Regression Discontinuity Approach. Evaluation Review, vol. 42. https://www.mathematica.org/publications/rd-or-not-rd-using-experimental-studies-to-assess-the-performance-of-the-regression-discontinuity"
    author: Philip Gleason, Alexandra Resch, Jillian Berk
---

# Synthetic within-study comparison design for assessing RD performance

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (2 causal, 1 quant-synthesis), `q2`–`q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
A methodological artifact in which the authors "generate synthetic RD data sets from experimental data sets" from two recent evaluations of educational interventions—the Educational Technology Study and the Teach for America Study—and "compare the RD impact estimates to the experimental estimates of the same intervention." This lets RD performance be benchmarked against randomized estimates for the same interventions. The article uses it both to test well-implemented RD and to study manipulation bias.

## Design Implications

### Context
#### Requirements
- Requires original experimental data sets from evaluations of the same interventions so RD estimates can be compared with experimental benchmarks.
#### Constraints
- Findings are based on synthetic RD data generated from two specific educational intervention evaluations, not on RD designs fielded directly.

### Target Learners
- students in the evaluated educational interventions

### Target Learning Goals
- estimating program impacts of educational interventions

## Claims

- [When well implemented, RD and experimental estimators produce impact estimates that are not significantly different and similar in magnitude on average](../claims/rd-well-implemented-matches-experimental-estimates.md) [+W]
- [Regression discontinuity impact estimates for two education interventions were not significantly different from experimental impact estimates, though point-estimate differences were sometimes nontrivial](../claims/rd-replication-matches-experimental-estimates-two-interventions.md) [+W]
- [Regression discontinuity estimates show high internal validity, with average bias below 0.01 standard deviations relative to RCT estimates at the same cutoff](../claims/rd-average-bias-below-0-01-sd-high-internal-validity.md) [+W]

## Related Elements

- [Empirical design-effect estimates based on four previously published education studies](four-published-education-studies-rd-power-basis.md)

## Examples

- [Simulate RD analysis files by selectively dropping observations from experimental data files](../strategies/simulate-rd-files-by-dropping-observations.md)

## Key Sources
- Philip Gleason, Alexandra Resch, Jillian Berk. (2018). RD or Not RD: Using Experimental Studies to Assess the Performance of the Regression Discontinuity Approach. Evaluation Review, vol. 42. https://www.mathematica.org/publications/rd-or-not-rd-using-experimental-studies-to-assess-the-performance-of-the-regression-discontinuity
