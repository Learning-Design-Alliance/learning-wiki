---
type: product
id: moodlequizr
title: moodlequizR
description: moodlequizR is an R package by Wolfgang Rolke that generates highly randomized quizzes and exams in Moodle-compatible XML format, with support for graphs and transfer of data to R.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# moodlequizR

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
moodlequizR is an R package by Wolfgang Rolke that generates highly randomized quizzes and exams in Moodle-compatible XML format, with support for graphs and transfer of data to R.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Fifteen included example quizzes as templates for Statistics and pre-calculus/calculus**: moodlequizR ships 15 example quizzes, callable in the shiny app, that serve "both as illustrations on what can be done and as starting points for more complicated quizzes and exams". They cover means, five-number summaries, categorical variables, confidence intervals, hypothesis testing, sample size, correlation and regression, internet-downloaded data, R output display, solving linear systems, and derivatives and integrals. (Wolfgang Rolke (2024))
- **paste.data and paste.moodle routines for transferring quiz data into R**: moodlequizR includes routines that let students move quiz data into R by copy-paste: the student highlights the data in the quiz, copies it, and runs moodledata = paste.data() in R. The article states the routine "correctly reads vectors, both numeric and character. Also tables with a mix of character and numeric columns", and works on Windows, MacOS and Linux. moodle.table displays data in the quiz as a table. (Wolfgang Rolke (2024))

### Claims

- [Moodle's built-in randomization is insufficient for Statistics courses, while moodlequizR provides far greater randomization](../claims/moodlequizr-randomization-exceeds-moodle-builtin.md) [+W]

## Related Products and Programmes

- [shinymoodlequizR](shinymoodlequizr.md)

## Key Sources
- Wolfgang Rolke. (2024). R Package moodlequizR: Fully Randomized Moodle Tests. https://arxiv.org/abs/2411.08032
