---
type: strategy
id: successful-goal-directed-trace-selection
title: Select hint-training data from successful students using a goal-directedness criterion
description: "When constructing the edit distance space and hint policy, the article recommends two data-selection heuristics: \"we should limit ourselves to data of successful students\" who reached a correct solution, and apply the..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: benjamin-paaßen-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158"
    title: "Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158"
    author: Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart
---

# Select hint-training data from successful students using a goal-directedness criterion

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When constructing the edit distance space and hint policy, the article recommends two data-selection heuristics: "we should limit ourselves to data of successful students" who reached a correct solution, and apply the goal-directedness criterion of Rivers and Koedinger (2014), incorporating "only those intermediate solutions which get closer to the correct solution the student ended up in". This filters trace data so hints reflect generic progress toward solutions.

## Design Implications

### Context
#### Requirements
- Trace data with recorded intermediate states and known final outcomes
#### Constraints
- Requires being able to determine which intermediate states move closer to the final correct solution

### Target Learners
- students whose solution traces populate the hint system's database

### Target Learning Goals
- hints that emulate capable students' generic next steps

## Related Strategies
- 

## Examples
-

## Key Sources
- Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158
