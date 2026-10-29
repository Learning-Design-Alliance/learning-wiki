---
type: design
id: bespoke-dsa-automarker-tool
title: Bespoke automarker for C++ DSA coursework with test-case marking, resubmission, tolerance intervals and infinite-loop timer
description: A purpose-built client–server automated assessment tool for C++ programming exercises in a second-year DSA course, written in PHP with MySQL storage under Apache/Linux, separate from the institutional LMS.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-29
sources:
  - id: andre-l-c-barczak-2023
    resource: "https://doi.org/10.1007/s11423-023-10277-2"
    title: "Andre L. C. Barczak, Anuradha Mathrani, Binglan Han, Napoleon H. Reyes. (2023). Automated assessment system for programming courses: a case study for teaching data structures and algorithms. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10277-2"
    author: Andre L. C. Barczak, Anuradha Mathrani, Binglan Han, Napoleon H. Reyes
---

# Bespoke automarker for C++ DSA coursework with test-case marking, resubmission, tolerance intervals and infinite-loop timer

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A purpose-built client–server automated assessment tool for C++ programming exercises in a second-year DSA course, written in PHP with MySQL storage under Apache/Linux, separate from the institutional LMS. Students upload code from a template; the server compiles with GCC and "executes the code over 10 test cases, while referencing a model solution supplied by the teacher", marking 0–10 with endless resubmission until the deadline. A parser tolerates text variation, tolerance intervals handle approximate answers, and a timer flags possible infinite loops.

## Design Implications

### Context
#### Requirements
- Students access the stand-alone server via the institutional network or the institution's VPN
- A well-defined code template is crucial since assignments are directly handled by the machine
#### Constraints
- The tool cannot analyse code directly to give a specific clue why code fails
- It is not possible to know if a program is truly in an infinite loop due to the undecidability of the halting problem

### Target Learners
- second-year undergraduate computer science students

### Learning Goals
- programming and algorithmic reasoning skills in data structures and algorithms

### Claims
- [Automarker Survey Favourable Formative Perceptions](../claims/automarker-survey-favourable-formative-perceptions.md) [+M]
- [Automarker Clues Extremely Helpful 30 Responses](../claims/automarker-clues-extremely-helpful-30-responses.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Andre L. C. Barczak, Anuradha Mathrani, Binglan Han, Napoleon H. Reyes. (2023). Automated assessment system for programming courses: a case study for teaching data structures and algorithms. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10277-2
