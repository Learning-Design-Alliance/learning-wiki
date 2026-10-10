---
type: design
id: greedy-dynamic-skill-weighting-assignment-algorithm
title: Greedy student-to-project assignment algorithm with dynamic skill weighting and tunable preference weight
description: "The matching system iteratively computes a match score for every student-project pair, combining a student's preference score weighted by an instructor-tunable parameter α with skill self-ratings weighted by a dynamic..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: brandon-pardi-2026
    resource: "https://arxiv.org/abs/2606.15572"
    title: "Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572"
    author: Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar
---

# Greedy student-to-project assignment algorithm with dynamic skill weighting and tunable preference weight

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The matching system iteratively computes a match score for every student-project pair, combining a student's preference score weighted by an instructor-tunable parameter α with skill self-ratings weighted by a dynamic skill weight β. As the article explains, "as the algorithm progresses, and more students are assigned to the project, the value ofβp(k)for unfulfilled skills will increase leading to a higher match score for students that satisfy those skills." A skill counts as unfulfilled when no assigned student self-rated proficiency of 3 or higher on the survey's 1–5 scale. The greedy process selects the highest match score each round, with ties broken by preference then randomly, and projects with higher average preference receive more capacity up to a fixed team-size limit of five.

## Design Implications

### Context
#### Requirements
- Instructor-defined preference weight α
- Student skill and preference survey data
- A predetermined skill list shared by surveys and LLM extraction
#### Constraints
- The current method can favor projects with many required skills at the expense of those with rare but critical skills
- All skills are currently treated equally, with fulfillment based on a single student's intermediate-level rating

### Target Learners
- senior-level computer science capstone students

### Learning Goals
- balanced teams with skill coverage and preference alignment

### Claims
- [Dynamic Skill Matching Higher Skill Coverage](../claims/dynamic-skill-matching-higher-skill-coverage.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572
