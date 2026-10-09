---
type: theory
title: Mathematical framework of edit-based hint policies
description: "The article provides \"precise definitions of key concepts in the field of edit-based hint policies and integrate them into a mathematical framework\"."
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

# Mathematical framework of edit-based hint policies

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

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

- [Programming State Sparsity States Visited Once](../claims/programming-state-sparsity-states-visited-once.md) [+M]
- [The Continuous Hint Factory predicts capable students' next edits more accurately than existing prediction schemes on two learning tasks, especially an open-ended programming task](../claims/chf-predicts-capable-student-edits-more-accurately.md) [+M]
- [Frequency-based hint policies fail in sparsely populated state spaces because almost no state is visited more than once](../claims/frequency-hint-policies-fail-sparse-spaces.md) [+M]

## Related Theories

- [Edit distance space: Euclidean embedding of states under a symmetric edit distance](edit-distance-space-embedding-theorem.md)

## Examples

- [Continuous Hint Factory (CHF)](../elements/continuous-hint-factory-chf.md)

## Key Sources
- Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158
