---
type: element
id: ml-early-warning-risk-score-algorithm
title: Machine learning early warning algorithm using in- and out-of-school data to estimate per-student, per-problem, per-quarter risk scores
description: "The report describes an algorithm that uses \"a range of in- and out-of-school data to estimate the specific risk of each academic problem for each student in each quarter.\" Unlike simple prior-performance flags, it pr..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: lindsay-cattell-2021
    resource: "https://ies.ed.gov/ncee/edlabs"
    title: "Lindsay Cattell, Julie Bruch. (2021). Identifying Students At Risk Using Prior Performance Versus a Machine Learning Algorithm. Regional Educational Laboratory Mid-Atlantic, U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov/ncee/edlabs"
    author: Lindsay Cattell, Julie Bruch
---

# Machine learning early warning algorithm using in- and out-of-school data to estimate per-student, per-problem, per-quarter risk scores

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The report describes an algorithm that uses "a range of in- and out-of-school data to estimate the specific risk of each academic problem for each student in each quarter." Unlike simple prior-performance flags, it produces risk scores that allow districts to create low- and high-risk groups using one or more cutoffs, enabling differentiation of risk levels among students for intervention targeting.

## Design Implications

### Context
#### Requirements
- Access to a range of in- and out-of-school data for each student in each quarter.
#### Constraints
- Less accurate when predicting outcomes for students who are Black, as stated in the report's findings.

### Target Learners
- K-12 students monitored by district early warning systems

### Target Learning Goals
- Early identification of students at risk of chronic absenteeism, low GPA, course failure, or suspension

## Claims

- [A machine learning algorithm with 10-percent risk-score cutoffs better targets students most likely to experience academic problems and has the advantage in predicting suspensions](../claims/algorithm-ten-percent-cutoffs-targets-highest-risk.md) [+W]
- [Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black](../claims/ews-and-algorithm-less-accurate-black-students.md) [~W]
- [A prior performance early warning system and a machine learning algorithm with same-percentage risk-score cutoffs are similarly accurate at identifying students who experience academic problems](../claims/prior-performance-ews-similarly-accurate-same-percentage-cutoffs.md) [~W]

## Related Elements

- [Predictive model of near-term academic risk combining school and child welfare data](near-term-academic-risk-predictive-model.md)
- [Linked school and human services data approach for predicting near-term academic risk](linked-data-early-warning-approach-element.md)

## Examples

- [Use linked school and child welfare data to flag students at academic risk in the coming quarter or semester](../strategies/linked-school-child-welfare-data-early-warning-strategy.md)
- [Use an early warning system based on linked school and human services data to target resources and lessen risks before they become more serious](../strategies/early-warning-system-target-resources-near-term-risks.md)

## Key Sources
- Lindsay Cattell, Julie Bruch. (2021). Identifying Students At Risk Using Prior Performance Versus a Machine Learning Algorithm. Regional Educational Laboratory Mid-Atlantic, U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov/ncee/edlabs
