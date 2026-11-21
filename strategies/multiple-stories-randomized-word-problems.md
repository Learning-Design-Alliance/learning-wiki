---
type: strategy
id: multiple-stories-randomized-word-problems
title: Vary the cover story as well as the numbers in randomized word problems
description: "For statistics word problems, the article shows defining several stories (survey preference, voting, vacation planning) within one R script, each matched to plausible parameter ranges: the Coca-Cola vs Pepsi story use..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: wolfgang-rolke-2024
    resource: "https://arxiv.org/abs/2411.08032"
    title: "Wolfgang Rolke. (2024). R Package moodlequizR: Fully Randomized Moodle Tests. https://arxiv.org/abs/2411.08032"
    author: Wolfgang Rolke
---

# Vary the cover story as well as the numbers in randomized word problems

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 review, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
For statistics word problems, the article shows defining several stories (survey preference, voting, vacation planning) within one R script, each matched to plausible parameter ranges: the Coca-Cola vs Pepsi story uses sample sizes between 200 and 500 while the voting story uses 1000 to 1200. By default about equally many of the stories are generated, and make.xml can force a single story.

## Design Implications

### Context
#### Requirements
- An R script with per-story parameter ranges matched to the story context
#### Constraints
- The article recommends doing multiple stories via the R script rather than the shiny app

### Target Learners
- university students in Statistics courses

### Target Learning Goals
- practicing percentage and survey-based inference problems

## Claims

- [Structure-emphasizing example sets, using varied cover stories across problem types, lead students to categorize problems by structure rather than surface features](../claims/structure-emphasizing-cover-stories-categorization.md) [+W]
- [Moodle's built-in randomization is insufficient for Statistics courses, while moodlequizR provides far greater randomization](../claims/moodlequizr-randomization-exceeds-moodle-builtin.md) [+W]

## Related Strategies

- [Replace few long homework assignments with many short auto-graded randomized quizzes](many-short-autograded-randomized-quizzes.md)

## Examples
-

## Key Sources
- Wolfgang Rolke. (2024). R Package moodlequizR: Fully Randomized Moodle Tests. https://arxiv.org/abs/2411.08032
