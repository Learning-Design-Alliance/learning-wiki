---
type: strategy
id: duration-distribution-comparison-strategy
title: Use duration-distribution comparison and learner-type fractions to profile learners, weigh course attraction, and evaluate teaching methods
description: "The article recommends exploiting the fitted duration distributions analytically: profiling learners into lognormal-learners, segment-learners with durations of at least one minute, and the rest; weighting each type w..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: zheng-xie-2019
    resource: "https://arxiv.org/abs/1809.07170"
    title: "Zheng Xie. (2019). Modelling the Dropout Patterns of MOOC Learners. arXiv preprint. https://arxiv.org/abs/1809.07170"
    author: Zheng Xie
---

# Use duration-distribution comparison and learner-type fractions to profile learners, weigh course attraction, and evaluate teaching methods

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The article recommends exploiting the fitted duration distributions analytically: profiling learners into lognormal-learners, segment-learners with durations of at least one minute, and the rest; weighting each type with a different value to measure course attraction fairly; and comparing duration distributions before and after adopting a teaching method. The author notes the comparison "removes the heterogeneity of the number of learners, and hence is a fair way for the courses with high quality but having few learners".

## Design Implications

### Context
#### Requirements
- Log data yielding per-learner viewing durations and viewed-video counts, and the categorization algorithm to identify learner types
#### Constraints
- A KS test showing identical lognormal-learner duration distributions cannot establish that an adopted method significantly improved learning durations

### Target Learners
- MOOC learners across subject domains on the iCourse platform

### Target Learning Goals
- Assessing course attraction and the effect of teaching methods on learning persistence

## Claims

- [Viewing durations of learners who have viewed no fewer than a course-specific number of videos follow a lognormal distribution](../claims/lognormal-learners-duration-distribution.md) [+W]
- [Segment-learner viewing durations follow a power law with exponential cutoff, with durations of at least one minute approximately exponential (constant dropout rate)](../claims/segment-learner-exponential-cutoff.md) [+W]
- [A non-parametric KS-test algorithm categorizes learners into lognormal-rounder and other-learner types, with all-rounders very few per course](../claims/ks-test-lognormal-learner-categorization.md) [+W]
- [A random differential equation with duration-dependent change rate expresses memory in lognormal-learners' viewing behavior](../claims/lognormal-learner-memory-equation.md) [+W]
- [MOOC viewing-duration hazard functions simultaneously exhibit a bathtub curve and a Lindy-effect decreasing tail](../claims/mooc-viewing-hazard-bathtub-lindy.md) [+W]
- [An equation with duration change rate inversely proportional to time, plus a uniformly random start time, accounts for segment-learner exponential cutoffs and early decreasing dropouts](../claims/segment-learner-inverse-time-equation.md) [+W]
- [Shannon evenness and 2^H/n indexes measure the balance of a course's attraction over videos, with low balance indicating less-viewed videos need content improvement](../claims/attraction-balance-shannon-evenness-index.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zheng Xie. (2019). Modelling the Dropout Patterns of MOOC Learners. arXiv preprint. https://arxiv.org/abs/1809.07170
