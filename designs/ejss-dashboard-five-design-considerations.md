---
type: design
id: ejss-dashboard-five-design-considerations
title: "Five-facet framework for designing simulation teacher dashboards: thought process, behaviour, engagement, choice, feedback"
description: The paper proposes five key considerations for designing the EJSS teacher dashboard, relating Student Thought Process, Student Behaviour, Student Engagement, Student Choice, and Teacher Feedback.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: wee-2021
    resource: "https://iwant2study.org/moodle402/"
    title: "Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F. (2021). Easy JavaScript Simulation (EJSS) Data Analytics for Singapore. https://iwant2study.org/moodle402/"
    author: "Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F"
---

# Five-facet framework for designing simulation teacher dashboards: thought process, behaviour, engagement, choice, feedback

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The paper proposes five key considerations for designing the EJSS teacher dashboard, relating Student Thought Process, Student Behaviour, Student Engagement, Student Choice, and Teacher Feedback. The authors state these "five facets provide a framework for aligning our design efforts with the needs of students and teachers, also drawing upon research in data analytics for education". Each facet maps to a concrete dashboard feature: chronological interaction sequences, active/inactive attempt counts, a gamified re-attempt marking scheme, free navigation among questions, and a visual percentage bar of incorrect answers.

## Design Implications

### Context
#### Requirements
- Dashboard features must log per-question interaction history (via assessment.json) and attempt counts so that each facet's indicator can be computed
#### Constraints
- The framework is derived from the authors' own simulation design work linked to learning analytics literature; no external evaluation of the framework is reported

### Target Learners
- School students using EJSS simulations in SLS

### Learning Goals
- Supporting teachers' diagnosis of student thinking, effort, motivation and class-wide feedback during simulation-based learning

### Claims
- [Ejss Dashboard Reveals Vector Angle Misconception](../claims/ejss-dashboard-reveals-vector-angle-misconception.md) [+M]
- [Ejss Data Reveals Trial And Error Strategy](../claims/ejss-data-reveals-trial-and-error-strategy.md) [+M]
- [Ejss Attempt Data Localise Direction Difficulties](../claims/ejss-attempt-data-localise-direction-difficulties.md) [+M]

## Related Designs
- Ejss Data Analytics Teacher Dashboard

## Examples
-

## Key Sources
- Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F. (2021). Easy JavaScript Simulation (EJSS) Data Analytics for Singapore. https://iwant2study.org/moodle402/
