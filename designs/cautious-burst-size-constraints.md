---
type: design
id: cautious-burst-size-constraints
title: Constraining burst registration sizes could raise certificate rates, but users may not be well served by it
description: "The article reports that a significant drop in average certificate rate is linked to bursting registration behaviors and suggests \"certificate rates could be increased by constraining burst sizes, for example by limit..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: wintermute-2019
    resource: "https://www.fun-mooc.fr"
    title: "Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. https://www.fun-mooc.fr"
    author: "Wintermute, E. H., Cisel, M., & Lindner, A. B"
---

# Constraining burst registration sizes could raise certificate rates, but users may not be well served by it

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article reports that a significant drop in average certificate rate is linked to bursting registration behaviors and suggests "certificate rates could be increased by constraining burst sizes, for example by limiting users to one new registration per day." However, it immediately cautions that it is not clear users would be well served, since bursts may be a course-shopping strategy through which users optimize their course selections.

## Design Implications

### Context
#### Requirements
- A platform that records registration time stamps so burst events can be detected and limited
#### Constraints
- The article states it is not clear that users would be well served by such constraints, and users in larger bursts earn more total certificates

### Target Learners
- MOOC platform users registering for multiple courses

### Learning Goals
- Improving certificate completion rates

### Claims
- [Certificate Rate Drops With Burst Size](../claims/certificate-rate-drops-with-burst-size.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Wintermute, E. H., Cisel, M., & Lindner, A. B. (2019). A survival model for course-course interactions in a Massive Open Online Course platform. arXiv. https://www.fun-mooc.fr. [doi:10.48550/arxiv.1905.04201](https://doi.org/10.48550/arxiv.1905.04201)
