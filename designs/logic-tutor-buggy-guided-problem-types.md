---
type: design
id: logic-tutor-buggy-guided-problem-types
title: Three-panel intelligent logic tutor with Buggy, Guided, WE, and PS problem types
description: "An intelligent tutoring system for propositional logic used in an undergraduate Discrete Mathematics course, with a three-panel interface: student workspace (left), domain rules (center), and contextual information/in..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: sutapa-dey-tithi-2026
    resource: "https://arxiv.org/abs/2602.16806"
    title: "Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). https://arxiv.org/abs/2602.16806"
    author: Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes
---

# Three-panel intelligent logic tutor with Buggy, Guided, WE, and PS problem types

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
An intelligent tutoring system for propositional logic used in an undergraduate Discrete Mathematics course, with a three-panel interface: student workspace (left), domain rules (center), and contextual information/instructions (right). Proofs are built as graphical nodes connected by edges showing logical dependencies. The tutor includes introduction, pretest, training (five levels of four problems), and posttest (six problems) sections, records all clickstream interactions, and scores problems 0-100 based on completion time, solution length, and rule application accuracy.

## Design Implications

### Context
#### Requirements
- Students complete a two-problem pretest used to measure incoming proficiency and assign intervention groups through stratified sampling
- During pretest and posttest the tutor provides no next-step hints, only immediate error messages
#### Constraints
- Comparison analyses include only students who completed all 7 levels in the tutor (52 Control, 52 Buggy, 51 Guided)

### Target Learners
- Undergraduate Computer Science majors in a mandatory Discrete Mathematics course

### Learning Goals
- Multi-step propositional logic proof solving
- Correct application of logical inference rules

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). https://arxiv.org/abs/2602.16806
