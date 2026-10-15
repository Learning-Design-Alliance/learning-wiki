---
type: theory
title: Mathematical framework of edit-based hint policies
description: "The article provides \"precise definitions of key concepts in the field of edit-based hint policies and integrate them into a mathematical framework\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: benjamin-paaßen-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158"
    title: "Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158"
    author: Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart
---

# Mathematical framework of edit-based hint policies

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
The article provides "precise definitions of key concepts in the field of edit-based hint policies and integrate them into a mathematical framework". It defines the edit set (functions on a state space, ideally symmetric so every edit is reversible), the hint policy as a function from states to edits, the legal move graph whose edges are edits, and the edit distance as the shortest-path distance in that graph under an edit cost function. This framework contextualizes existing approaches and forms the basis for the CHF.

## Design Implications

### Context
#### Requirements
- A symmetric edit set and a symmetric edit cost function so that any student action can be reversed and distances are well-defined
#### Constraints
- Edit distances on unordered trees are NP-hard, making some distances infeasible in practice

### Target Learners
- students solving multi-step tasks such as programming problems

### Target Learning Objectives
- next-step guidance toward correct and complete task solutions

### Claims


## Related Theories

- [Edit distance space: Euclidean embedding of states under a symmetric edit distance](edit-distance-space-embedding-theorem.md)

## Examples

- [Continuous Hint Factory (CHF)](../elements/continuous-hint-factory-chf.md)
- [Select hint-training data from successful students using a goal-directedness criterion](../strategies/successful-goal-directed-trace-selection.md)

## Key Sources
- Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158
