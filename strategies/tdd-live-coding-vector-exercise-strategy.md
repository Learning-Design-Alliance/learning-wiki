---
type: strategy
id: tdd-live-coding-vector-exercise-strategy
title: Teach test-driven development via live coding on a vector class exercise
description: The APC introduces TDD by demonstrating the workflow live while implementing a simple vector class in C++ or python, choosing the language by audience preference, using a xUnit-style framework (Boost.Test).
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: s-kluth-2015
    resource: "https://arxiv.org/abs/1505.04604"
    title: "S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach. (2015). How do particle physicists learn the programming concepts they need? https://arxiv.org/abs/1505.04604"
    author: S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach
---

# Teach test-driven development via live coding on a vector class exercise

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The APC introduces TDD by demonstrating the workflow live while implementing a simple vector class in C++ or python, choosing the language by audience preference, using a xUnit-style framework (Boost.Test). Students "are then asked to practice TDD on their own by extending the vector to oﬀer a magnitude member function", including policies such as Minkowski or Euclidean metric, and are encouraged to code along on their own laptops during the live demonstration.

## Design Implications

### Context
#### Requirements
- A unit test framework such as Boost.Test and laptops for participants to code along
#### Constraints
- The article notes students are not expected to pick up TDD as their style of programming; the lecture is an entrance to contemplating programming from a higher level

### Target Learners
- PhD students and post-docs in code-centric physics environments

### Target Learning Goals
- test-driven development and thinking about independent feature sets of classes

## Related Strategies

- [Real-time lecture demonstrations deriving theoretical predictions and testing them numerically with modifiable code](real-time-lecture-simulation-demonstrations.md)

## Examples
-

## Key Sources
- S Kluth, M G Pia, T Schoerner-Sadenius, P Steinbach. (2015). How do particle physicists learn the programming concepts they need? https://arxiv.org/abs/1505.04604
