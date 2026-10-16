---
type: element
id: continuous-hint-factory-chf
title: Continuous Hint Factory (CHF)
description: "The CHF is a hint-generation method extending the Hint Factory to \"vast and sparsely populated state spaces\"."
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

# Continuous Hint Factory (CHF)

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The CHF is a hint-generation method extending the Hint Factory to "vast and sparsely populated state spaces". It works in three steps: embed past student data in the edit distance space; infer a hint policy there via Gaussian process prediction for structured data, producing a weighted average of reference states chosen in a probabilistically optimal sense; and transform this mixture back into a human-readable edit via pre-image identification. By averaging multiple reference solutions it avoids emulating individual stylistic particularities without relying on frequency information.

## Design Implications

### Context
#### Requirements
- An edit distance and some, possibly few, data samples of past successful students
#### Constraints
- Requires trace data of successful students; the article recommends restricting data to successful students and goal-directed intermediate solutions

### Target Learners
- students in intelligent tutoring systems for multi-step tasks such as programming

### Target Learning Goals
- personalized next-step hints that reflect generic solution steps

### Affordances
- [Edit Distance Space Embedding Theorem](../theories/edit-distance-space-embedding-theorem.md)

## Claims


## Related Elements
- 

## Examples

- [Select hint-training data from successful students using a goal-directedness criterion](../strategies/successful-goal-directed-trace-selection.md)

## Key Sources
- Benjamin Paaßen, Barbara Hammer, Thomas W. Price, Tiffany Barnes, Sebastian Gross, Niels Pinkwart. (2018). The Continuous Hint Factory - Providing Hints in Vast and Sparsely Populated Edit Distance Spaces. Journal of Educational Data Mining, Volume 10, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/158
