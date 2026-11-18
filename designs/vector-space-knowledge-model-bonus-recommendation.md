---
type: design
id: vector-space-knowledge-model-bonus-recommendation
title: "Knowledge model: a vector-space student profile for content-based bonus-exercise recommendation"
description: "The article presents a content-based recommender built on a vector-space knowledge model that \"reﬂects how well a student understood the topics taught in the course with a value between 0 (not understood) to 1 (fully..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: ralf-teusner-2018
    resource: "https://doi.org/10.1145/3231644.3231650"
    title: "Ralf Teusner, Thomas Hille, Thomas Staubitz. (2018). Effects of Automated Interventions in Programming Assignments: Evidence from a Field Experiment. L@S 2018. https://doi.org/10.1145/3231644.3231650"
    author: Ralf Teusner, Thomas Hille, Thomas Staubitz
---

# Knowledge model: a vector-space student profile for content-based bonus-exercise recommendation

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article presents a content-based recommender built on a vector-space knowledge model that "reﬂects how well a student understood the topics taught in the course with a value between 0 (not understood) to 1 (fully understood)". Unlike prior adaptive frameworks, "we do not rely on self evaluation, but leverage our data on automated grading and testing". Exercises are manually annotated with topics, weights and difficulty; a knowledge score function combines scoring, topic share, difficulty and a diminishing function ranking recent exercises higher. The algorithm filters out too-difficult or not-yet-encountered exercises and ranks candidates by potential benefit to topic scores.

## Design Implications

### Context
#### Requirements
- Course instructors must provide the topics taught and annotate each exercise with topics, weights and a difficulty level, and domain models must be created per course independently
#### Constraints
- The authors left topic-relationship annotations for future research to keep teaching-team effort small

### Target Learners
- MOOC students in an introductory Java programming course, including students who never programmed before

### Learning Goals
- Addressing individual topic weaknesses through tailored practice exercises

### Claims

- [Bonus Exercise Tailoring No Perception Difference](../claims/bonus-exercise-tailoring-no-perception-difference.md) [~M]
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](../claims/clustering-recovers-expert-bundles.md) [+W]

## Related Designs

- [Interactive research-oriented teaching package for \"Atomistic Materials Modeling\": group worksheets, computer exercises and a voluntary research-proposal sketch with bonus points](element-interactive-research-oriented-package-atomistic-modeling.md)

## Examples
-

## Key Sources
- Ralf Teusner, Thomas Hille, Thomas Staubitz. (2018). Effects of Automated Interventions in Programming Assignments: Evidence from a Field Experiment. L@S 2018. https://doi.org/10.1145/3231644.3231650
