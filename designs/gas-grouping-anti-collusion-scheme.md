---
type: design
id: gas-grouping-anti-collusion-scheme
title: "Grouping-based anti-collusion scheme (GAS): grouping students by competence, optimizing inter-group question overlap, and augmenting the question pool to control collusion gain below any desired level"
description: "The GAS is the article's core anti-collusion design for distanced online testing."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
sources:
  - id: mengzhou-li-2021
    resource: "https://doi.org/10.1038/s41539-020-00083-3"
    title: "Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3"
    author: Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang
---

# Grouping-based anti-collusion scheme (GAS): grouping students by competence, optimizing inter-group question overlap, and augmenting the question pool to control collusion gain below any desired level

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The GAS is the article's core anti-collusion design for distanced online testing. It consists of three elements the article enumerates: "Grouping: Students with similar competences are grouped together to receive the same sequence of questions in an exam"; Optimization, which aggressively reduces the number of questions that can be copied between groups, even to zero; and Augmentation, enlarging the pool beyond M1 questions. It works because cyclic sequences can reduce maximum question leakage to zero when M2 - M1 + 1 >= C, grouping reduces the equivalent number of students, and similar-competence students gain little from intra-group collusion. Competences can be estimated from GPA, earlier quizzes, or a first portion of the exam via dynamic programming.

## Design Implications

### Context
#### Requirements
- Prior knowledge of students' competences, estimated from GPA, earlier quizzes, or a first portion of the exam
#### Constraints
- The analysis is a first-order approximation of an idealized DOT scenario; intra-group collusion is facilitated because group members share the same sequence

### Target Learners
- undergraduate students in math or fact-based courses

### Learning Goals
- valid measurement of learning outcomes in remote online exams

### Claims
- [Theorem1 Collusion Gain Upper Bound](../claims/theorem1-collusion-gain-upper-bound.md) [+M]
- [Dot Final Exam Collusion Gain Three Orders Reduction](../claims/dot-final-exam-collusion-gain-three-orders-reduction.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Mengzhou Li, Lei Luo, Sujoy Sikdar, Navid Ibtehaj Nizam, Shan Gao, Hongming Shan, Melanie Kruger, Uwe Kruger, Hisham Mohamed, Lirong Xia and Ge Wang. (2021). Optimized collusion prevention for online exams during social distancing. npj Science of Learning 6:5. https://doi.org/10.1038/s41539-020-00083-3
