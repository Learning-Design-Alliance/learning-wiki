---
type: design
id: guided-parsons-problems-logic-tutor
title: Guided Parsons problems (GPPs) in an intelligent logic tutor
description: GPPs are a problem type in a propositional logic tutor that augment subgoal-oriented Parsons problems with step-specific hints.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: sutapa-dey-tithi-2025
    resource: "https://arxiv.org/abs/2505.04712"
    title: "Sutapa Dey Tithi, Xiaoyi Tian, Min Chi and Tiffany Barnes. (2025). Investigating the Impact and Student Perceptions of Guided Parsons Problems for Learning Logic with Subgoals. CSEDM'25 Workshop. https://arxiv.org/abs/2505.04712"
    author: Sutapa Dey Tithi, Xiaoyi Tian, Min Chi and Tiffany Barnes
---

# Guided Parsons problems (GPPs) in an intelligent logic tutor

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
GPPs are a problem type in a propositional logic tutor that augment subgoal-oriented Parsons problems with step-specific hints. Proofs are divided into chunks or subgoals that are data-driven groupings of logic statements, and students complete a partially solved proof by justifying nodes with rules and parent nodes. Hints clarify rule application, e.g. "Apply Simplification here to isolate ¬P." Subgoals were extracted via a clustering algorithm on prior interaction log data and verified by an expert instructor.

## Design Implications

### Context
#### Requirements
- A partially solved proof with all statement nodes provided, with students adding justifications to connect nodes
- Subgoal chunks extracted from prior student log data and verified by an expert instructor
#### Constraints
- The study was conducted in only one ITS platform, limiting generalizability

### Target Learners
- undergraduate CS majors in a Discrete Mathematics course

### Learning Goals
- constructing propositional logic proofs
- applying logic rules accurately
- problem decomposition skills

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Sutapa Dey Tithi, Xiaoyi Tian, Min Chi and Tiffany Barnes. (2025). Investigating the Impact and Student Perceptions of Guided Parsons Problems for Learning Logic with Subgoals. CSEDM'25 Workshop. https://arxiv.org/abs/2505.04712
