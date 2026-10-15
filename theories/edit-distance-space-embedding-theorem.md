---
type: theory
title: "Edit distance space: Euclidean embedding of states under a symmetric edit distance"
description: "The article introduces \"the notion of an edit distance space, a continuous space in which each state corresponds to one vector and the Euclidean distance between vectors corresponds to the edit distance between two st..."
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

# Edit distance space: Euclidean embedding of states under a symmetric edit distance

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
The article introduces "the notion of an edit distance space, a continuous space in which each state corresponds to one vector and the Euclidean distance between vectors corresponds to the edit distance between two states". Theorem 2 proves that for any symmetric edit set and symmetric edit cost function, an eigenvalue-corrected Euclidean embedding exists in which pairwise distances match the edit distance, and Theorem 3 shows the edit distance in this space is equivalent to the original, up to eigenvalue correction.

## Design Implications

### Context
#### Requirements
- A symmetric edit distance and eigenvalue correction of the squared distance matrix
#### Constraints
- Eigenvalue correction is an approximation and distorts distances to the extent negative entries are present

### Target Learners
- students working on multi-step learning tasks with edit-based tutoring support

### Target Learning Objectives
- automatic generation of next-step edit hints

### Claims


## Related Theories

- [Mathematical framework of edit-based hint policies](edit-based-hint-policy-framework.md)

## Examples

- [Continuous Hint Factory (CHF)](../elements/continuous-hint-factory-chf.md)
- [Select hint-training data from successful students using a goal-directedness criterion](../strategies/successful-goal-directed-trace-selection.md)

## Key Sources
- Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158
