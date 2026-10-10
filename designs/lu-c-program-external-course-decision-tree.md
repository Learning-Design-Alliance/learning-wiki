---
type: design
id: lu-c-program-external-course-decision-tree
title: Decision tree used by a curriculum administrator to assess external courses for the Lund C program
description: Based on correspondence with the former program director, the authors constructed a decision tree (Fig.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: arthur-nijdam-2026
    resource: "https://arxiv.org/abs/2608.05910"
    title: "Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910"
    author: Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian
---

# Decision tree used by a curriculum administrator to assess external courses for the Lund C program

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Based on correspondence with the former program director, the authors constructed a decision tree (Fig. 1) capturing how external courses are assessed for the Lund University Information and Communication Engineering (C) program. "Firstly, the program director decides whether a course is within the scope of the C program, or counted as external." External courses are capped at 15 ECTS; in-scope courses are matched to LU equivalents, assigned a level (G1/G2/A), and possibly counted toward one of five specialization tracks. Partial overlap is credited proportionally: "overlap below 20% (less than 1.5 ECTS) is disregarded; overlap between 20% and 66.7% warrants 2–5 ECTS; and overlap exceeding 66.7% (more than 5 ECTS) is treated as full equivalence." CourseGraph targets the content-overlap decisions in this tree.

## Design Implications

### Context
#### Requirements
- A curriculum administrator's decision process and program metadata (levels, specialization tracks) to ground the assessment rules
#### Constraints
- Automatic assignment of course level falls outside the scope of this paper

### Target Learners
- exchange students in the Lund University C program

### Learning Goals
- crediting external courses appropriately toward degree requirements

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910
