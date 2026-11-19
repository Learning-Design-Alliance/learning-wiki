---
type: design
id: quantum-debugging-assignments-three-error-types
title: Debugging assignments built around the three error types of quantum programs
description: Debugging assignments deepen proficiency with course programming tools and introduce the debugging step of the quantum software development cycle.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: mariia-mykhailova-2022
    resource: "https://arxiv.org/abs/2211.16347"
    title: "Mariia Mykhailova. (2022). Developing Programming Assignments for Teaching Quantum Computing and Quantum Programming. arXiv. https://arxiv.org/abs/2211.16347"
    author: Mariia Mykhailova
---

# Debugging assignments built around the three error types of quantum programs

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Debugging assignments deepen proficiency with course programming tools and introduce the debugging step of the quantum software development cycle. The article groups quantum program errors into three types: syntax errors that prevent compilation, runtime errors that fail during execution, and logical errors that "do not manifest as failures during either compile-time or runtime, but rather produce incorrect results." Tasks present code containing one error of each type for students to find and fix, and are recommended after the first few weeks of the course once students move on to simple algorithms.

## Design Implications

### Context
#### Requirements
- Students must have moved past basic quantum computing concepts to simple algorithms for such assignments to be useful
#### Constraints
- For probabilistic algorithms or errors that show up only sometimes, identifying the errors can involve rather sophisticated statistical analysis

### Target Learners
- undergraduate and graduate computer science students in an introductory quantum computing course

### Learning Goals
- debugging quantum programs
- understanding quantum algorithms and their practical application

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Mariia Mykhailova. (2022). Developing Programming Assignments for Teaching Quantum Computing and Quantum Programming. arXiv. https://arxiv.org/abs/2211.16347
