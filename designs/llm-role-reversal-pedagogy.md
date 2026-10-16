---
type: design
id: llm-role-reversal-pedagogy
title: "Role-reversal pedagogy: positioning the student as instructor of an LLM to convert passive consumption into active knowledge construction"
description: "The article's organizing framework inverts the dominant LLM-as-tutor paradigm: \"we propose to use LLMs in a reversed role, i.e., let a student teach an LLM to solve a question,\" so that \"a student will be pushed to un..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: xinming-yang-2025
    resource: "https://arxiv.org/abs/2508.05979"
    title: "Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979"
    author: Xinming Yang, Haasil Pujara, Jun Li
---

# Role-reversal pedagogy: positioning the student as instructor of an LLM to convert passive consumption into active knowledge construction

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's organizing framework inverts the dominant LLM-as-tutor paradigm: "we propose to use LLMs in a reversed role, i.e., let a student teach an LLM to solve a question," so that "a student will be pushed to understand the materials behind the given question." It is grounded in the protégé effect, where the act of teaching deepens the instructor's own understanding, and in constructivist learning theory, with novel underspecified scenarios requiring students to define the rules of a new system. The framework targets over-reliance risks the authors identify in tutor-mode LLM use.

## Design Implications

### Context
#### Requirements
- Questions must be designed so the LLM cannot solve them independently, creating a knowledge gap only the student can bridge
#### Constraints
- The authors state the study does not isolate the specific cognitive effects of re-encoding versus other factors
- Designing questions robust against all forms of sophisticated gaming, such as remapping the novel problem onto a known equivalent, remains an open challenge

### Target Learners
- undergraduate computer science students

### Learning Goals
- active knowledge construction and mastery of core course competencies instead of passive information consumption

### Claims
- [Learning By Teaching Llm Improves Assignments Projects](../claims/learning-by-teaching-llm-improves-assignments-projects.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979
