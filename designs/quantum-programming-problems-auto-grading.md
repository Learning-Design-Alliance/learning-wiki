---
type: design
id: quantum-programming-problems-auto-grading
title: Programming-problem assignments with automatic grading as the core quantum programming assignment type
description: "The article's most broadly used assignment type asks students to apply learned quantum concepts by implementing Q# operations that solve concrete problems, replacing a placeholder comment in a provided operation signa..."
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

# Programming-problem assignments with automatic grading as the core quantum programming assignment type

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's most broadly used assignment type asks students to apply learned quantum concepts by implementing Q# operations that solve concrete problems, replacing a placeholder comment in a provided operation signature. Solutions are graded automatically by a predefined testing harness that runs them on a set of tests, and "The solutions are evaluated based on whether their effects match the tasks' requirements, rather than on the exact paths they take to accomplish the tasks." The Quantum Katas open-source project provides a large collection of such problems and was used in both courses described.

## Design Implications

### Context
#### Requirements
- Assignments are implemented in a way that supports automatic grading, using a Q# testing harness that validates results against expected ones
#### Constraints
- Due to the probabilistic nature of many quantum algorithms, creating automated testing harnesses for some kinds of tasks can be challenging

### Target Learners
- undergraduate and graduate computer science students with previous exposure to linear algebra and programming

### Learning Goals
- applying quantum computing concepts and algorithms to practical programming problems
- quantum software development skills

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Mariia Mykhailova. (2022). Developing Programming Assignments for Teaching Quantum Computing and Quantum Programming. arXiv. https://arxiv.org/abs/2211.16347
