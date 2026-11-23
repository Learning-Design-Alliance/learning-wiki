---
type: strategy
id: google-sheets-euler-iteration-lab
title: Guided Google Sheets laboratory exercise in which first-year physics students iteratively implement the Euler-method approximation
description: A 1-3 hour classroom laboratory exercise in which students build a Google Sheets spreadsheet with a Time column incremented by 0.5 s and a Position column implementing the discretized equation of motion, fill the colu...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: scott-c-scharlach-2025
    resource: "https://arxiv.org/abs/2505.03099"
    title: "Scott C. Scharlach. (2025). Pedagogical Implications for the Falling Astronaut Problem. https://arxiv.org/abs/2505.03099"
    author: Scott C. Scharlach
---

# Guided Google Sheets laboratory exercise in which first-year physics students iteratively implement the Euler-method approximation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 4 studies (3 design, 1 theoretical), `q1`–`q2` · 0 of 4 report an effect size · 4 claims rest on one study

## Description
A 1-3 hour classroom laboratory exercise in which students build a Google Sheets spreadsheet with a Time column incremented by 0.5 s and a Position column implementing the discretized equation of motion, fill the columns down thousands of rows, trim rows below the planet radius, and plot a position-versus-time chart. The exercise is "intended for first-year undergraduate physics students with high-school level experience in forces, gravity, and kinematics" and follows one class introducing the problem and technique. A homework assignment applies the same technique in a new context to prevent mechanical copying.

## Design Implications

### Context
#### Requirements
- Students should first have one class on the Falling Astronaut Problem covering the problem statement and an overview of the numerical technique
- Access to Google Sheets or comparable spreadsheet software
#### Constraints
- Intended to take 1-3 hours including software familiarization
- Assumes students are new to numerical approximation and will engage in productive struggle

### Target Learners
- first-year undergraduate physics students

### Target Learning Goals
- understanding numerical approximations of differential equations
- discretized time and iterative computation
- modeling motion under non-constant gravity

## Claims

- [The numerical approximation requires only high-school calculus as prerequisite, with the main barrier being conceptual (discretized time and iteration) rather than mathematical](../claims/numerical-approximation-accessible-prerequisite-conceptual-barrier.md) [+W]
- [Comparing analytic with Euler and Euler-Cromer numerical solutions led students to quantify iteration error, which affected position but not velocity](../claims/analytic-versus-numerical-solution-error-activity.md) [+W]
- [Students successfully performed quantitative data analysis in spreadsheets, though this unit was the most challenging](../claims/spreadsheet-data-analysis-unit-outcomes.md) [+W]
- [The spring exercise lets students demonstrate interactively that the half-cycle time of harmonic motion does not depend on amplitude, even under Euler-Cromer integration](../claims/spring-exercise-period-amplitude-independence.md) [+W]

## Related Strategies

- [Spreadsheet homework sequence: reproduce small-system tables, then scale up and add entropy columns](spreadsheet-homework-sequence-einstein-solids.md)
- [Guided enquiry-based programming tasks that signpost the physics and leave the programming method to the student](signposted-physics-open-programming-enquiry-task.md)
- [Use simple spreadsheet-based numerical simulation of orbital systems as an engaging team-based learning activity](spreadsheet-numerical-simulation-team-learning-strategy.md)
- [Embed computational skills into an existing lab course by replacing a preset analysis tool with Python while retaining original lab goals](embed-python-without-altering-course-structure.md)
- [Streamline data processing with browser-based analysis so class time focuses on physical interpretation](browser-based-analysis-streamlining-strategy.md)
- [Have students implement the Euler method in a spreadsheet to numerically solve a nonlinear equation of motion](euler-method-spreadsheet-strategy-nonlinear-oscillator.md)

## Examples
-

## Key Sources
- Scott C. Scharlach. (2025). Pedagogical Implications for the Falling Astronaut Problem. https://arxiv.org/abs/2505.03099
