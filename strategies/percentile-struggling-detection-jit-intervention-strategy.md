---
type: strategy
id: percentile-struggling-detection-jit-intervention-strategy
title: Identify struggling students via the 75th percentile of working time and issue just-in-time RFC or break interventions
description: "The article describes an implementable detection-and-intervention strategy for programming MOOCs: compute each student's working time on an exercise (summing gaps between run, assess and submit events, discarding gaps..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: ralf-teusner-2018
    resource: "https://doi.org/10.1145/3231644.3231650"
    title: "Ralf Teusner, Thomas Hille, Thomas Staubitz. (2018). Effects of Automated Interventions in Programming Assignments: Evidence from a Field Experiment. L@S 2018. https://doi.org/10.1145/3231644.3231650"
    author: Ralf Teusner, Thomas Hille, Thomas Staubitz
---

# Identify struggling students via the 75th percentile of working time and issue just-in-time RFC or break interventions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 1 mixed, 1 against) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article describes an implementable detection-and-intervention strategy for programming MOOCs: compute each student's working time on an exercise (summing gaps between run, assess and submit events, discarding gaps over five minutes) and, when a student exceeds "the 75th percentile of students to be regarded as considerable slower than their peers", show a closable dialog encouraging either a Request for Comments or a study break. Limits of three interventions per day and two per exercise keep annoyance low, and a 10-minute minimum protects against false positives on short exercises.

## Design Implications

### Context
#### Requirements
- A coding platform that logs code run, unit-test and submit events so working time can be computed, plus at least 10 minutes of exercise time before any intervention triggers
#### Constraints
- The percentile approach "can not separate actually struggling students from ones just taking it slow", and 53% of surveyed students perceived interventions as too early

### Target Learners
- MOOC students working on programming exercises, particularly less skilled students

### Target Learning Goals
- Encouraging help-seeking (peer feedback requests) and restudy or breaks when students struggle

## Claims

- [Just-in-time interventions cause students to take earlier action and longer breaks, but many students perceived them as unhelpful or poorly timed](../claims/jit-intervention-timing-and-perception.md) [~W]
- [Just-in-time interventions had no significant effects on course dropout rates or scores](../claims/jit-interventions-no-effect-scores-dropout.md) [-W]
- [RFC just-in-time interventions significantly increase the rate of Requests for Comments by students in a programming MOOC](../claims/rfc-intervention-increases-help-requests-mooc.md) [+W]

## Related Strategies

- [Identify struggling students early from in-unit assignment interactions and provide timely personalized support](early-identification-of-struggling-students-from-in-unit-interactions.md)

## Examples
-

## Key Sources
- Ralf Teusner, Thomas Hille, Thomas Staubitz. (2018). Effects of Automated Interventions in Programming Assignments: Evidence from a Field Experiment. L@S 2018. https://doi.org/10.1145/3231644.3231650
