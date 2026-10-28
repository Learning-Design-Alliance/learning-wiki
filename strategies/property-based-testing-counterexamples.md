---
type: strategy
id: property-based-testing-counterexamples
title: Use property-based testing to give counterexamples when student programs deviate from model solutions
description: When a student program cannot be matched with a model solution, Ask-Elle uses QuickCheck property-based testing to search for a counterexample demonstrating the program is incorrect.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: gerdes-2016
    resource: "https://doi.org/10.1007/s40593-015-0080-x"
    title: "Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x"
    author: "Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T"
---

# Use property-based testing to give counterexamples when student programs deviate from model solutions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
When a student program cannot be matched with a model solution, Ask-Elle uses QuickCheck property-based testing to search for a counterexample demonstrating the program is incorrect. This addresses the observation that some students believed their unrecognized solutions were correct when in fact they were not. Properties are specified in the exercise configuration file and tested with randomly generated inputs; when a counterexample is found, a specialised message explains to the student why her program is incorrect.

## Design Implications

### Context
#### Requirements
- A configuration file with QuickCheck properties must be defined for the exercise
#### Constraints
- Test cases that run into holes are discarded, which may influence the distribution of random values considered for partial programs

### Target Learners
- students learning functional programming in Haskell

### Target Learning Goals
- recognising and correcting incorrect program behaviour

## Claims

- [Strategy-based assessment recognised 62 of 72 correct student programs (86%) from four model solutions with no false positives](../claims/ask-elle-assessment-recognises-62-of-72-programs.md) [+W]
- [In log analysis of 3466 interactions, 56.1% of interactions and 46.3% of attempts were recognised as correct model solutions](../claims/ask-elle-log-analysis-recognition-rates.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x
