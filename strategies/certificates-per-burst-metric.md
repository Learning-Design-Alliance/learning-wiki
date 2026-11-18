---
type: strategy
id: certificates-per-burst-metric
title: Use certificates-per-burst rather than raw certificate rate to track expected user success
description: "Because many burst registrations may never receive serious user effort, the authors propose that \"we propose certificates-per-burst as a simple metric for the expected overall success of each user upon each approach t..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: wintermute-2019
    resource: "https://arxiv.org/abs/1905.04201"
    title: "Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. https://arxiv.org/abs/1905.04201"
    author: "Wintermute, E. H., Cisel, M., & Lindner, A. B"
---

# Use certificates-per-burst rather than raw certificate rate to track expected user success

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Because many burst registrations may never receive serious user effort, the authors propose that "we propose certificates-per-burst as a simple metric for the expected overall success of each user upon each approach to the platform." The per-burst certificate rate for FUN was 12.2%, 1.5-fold higher than the raw certificate rate, making it a fairer summary of a typical user's experience.

## Design Implications

### Context
#### Requirements
- Registration data must be clusterable into burst events so per-burst certificate counts can be computed
#### Constraints
- The metric is proposed for platforms where bursting registration behavior occurs, which the authors say is likely common given activity bursts are a general feature of internet user behavior

### Target Learners
- MOOC platform users and analysts tracking learner progress

### Target Learning Goals
- Monitoring user progress and success across course registrations

## Claims

- [The βEND model outperforms logistic regression in predicting certificate-rate patterns in the FUN dataset](../claims/bend-outperforms-logistic-regression-mooc.md) [+M]
- [Per-course certificate rate drops in inverse proportion to registration burst size](../claims/certificate-rate-drops-with-burst-size.md) [+M]
- [Co-registration changes certificate rates for roughly a third of courses in each direction, with effects governed by course engagement level](../claims/co-registration-effects-governed-by-engagement.md) [+M]
- [Returning users show no significant certificate-rate change but significantly increasing difficulty and engagement of selected courses](../claims/returning-users-engagement-difficulty-increase.md) [+M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. https://arxiv.org/abs/1905.04201. [doi:10.48550/arxiv.1905.04201](https://doi.org/10.48550/arxiv.1905.04201)
