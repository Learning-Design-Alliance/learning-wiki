---
type: design
id: hrcf-mechanism-element
title: High-Resolution Course Feedback (HRCF) mechanism
description: "HRCF is a formative course feedback mechanism in which, instead of surveying all students at fixed points, \"HRCF makes a fixed number of feedback requests to every student but in randomly selected weeks of the course\"..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: yunsung-kim-2026
    resource: "https://doi.org/10.1145/3774398.3811622"
    title: "Yunsung Kim, Hansol Lee, Candace Thille, and Chris Piech. 2026. A Large-Scale Observational Study on Obtaining Lightweight, Randomized Weekly Student Feedback: Associations with End-of-Term Course Evaluations. In Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811622"
    author: Yunsung Kim, Hansol Lee, Candace Thille, and Chris Piech
---

# High-Resolution Course Feedback (HRCF) mechanism

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
HRCF is a formative course feedback mechanism in which, instead of surveying all students at fixed points, "HRCF makes a fixed number of feedback requests to every student but in randomly selected weeks of the course" (typically S=2 weeks, spaced at least two weeks apart). It follows a 3-phase weekly cycle: Monday invitations to an anonymous survey with four default questions (weekly sentiment Likert item plus three free-text items), Thursday reminders, and a Sunday digest email to instructors with response rates, visual summaries, and a class-mood graph. In this study it was used across 42 courses and 103 offerings with 24,216 enrollments and a 39.8% overall response rate.

## Design Implications

### Context
#### Requirements
- Instructors review weekly digest emails and act on the feedback to adjust instruction
#### Constraints
- Baseline setup surveys each student in only S=2 randomly chosen weeks per term

### Target Learners
- university students in computer science courses

### Learning Goals
- formative instructional improvement during the term
- surfacing course-level student pain points

### Claims
- [First Time Hrcf Use No Rating Change](../claims/first-time-hrcf-use-no-rating-change.md) [+M]
- [Repeat Hrcf Use Learning Ratings Small Courses](../claims/repeat-hrcf-use-learning-ratings-small-courses.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yunsung Kim, Hansol Lee, Candace Thille, and Chris Piech. 2026. A Large-Scale Observational Study on Obtaining Lightweight, Randomized Weekly Student Feedback: Associations with End-of-Term Course Evaluations. In Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811622
