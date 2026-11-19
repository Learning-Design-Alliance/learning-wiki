---
type: design
id: programming-exercise-gamification-modes
title: Gamification modes for grading programming exercises
description: "The paper defines six gamification modes that grade solutions on factors beyond correctness: Slender/Golf (fewest characters, instructions or lines), Sprinter (execution time below a teacher-set threshold), Economic (..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: alberto-simões-and-ricardo-queirós-2020
    resource: "https://arxiv.org/abs/2006.14476"
    title: "Alberto Simões and Ricardo Queirós. (2020). On the Nature of Programming Exercises. OpenAccess Series in Informatics, ICPEC 2020. https://arxiv.org/abs/2006.14476"
    author: Alberto Simões and Ricardo Queirós
---

# Gamification modes for grading programming exercises

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The paper defines six gamification modes that grade solutions on factors beyond correctness: Slender/Golf (fewest characters, instructions or lines), Sprinter (execution time below a teacher-set threshold), Economic (memory used), Sedulous (rewarding persistent honest attempts), Scout (bonus for passing all tests on first submission), and Meticulous (bonus for using specified keywords or methods). The authors argue that "Gamification can be used to challenge students to solve a solution in a specific way, and therefore, being not just useful for motivation, but also for learning".

## Design Implications

### Context
#### Requirements
- Grading systems must detect honest attempts versus repeated wrong submissions for the Sedulous mode
- Keyword-based modes need instrumentation or wrappers to verify actual use, since pattern matching can be cheated with comments or void contexts
#### Constraints
- The Slender/Golf mode is counterproductive as a main goal because shorter solutions are usually ugly, difficult to maintain, and explore obscure language details
- Meticulous mode risks cheating if students learn which keyword is checked

### Target Learners
- novice programming students
- students with learning difficulties who demotivate easily
- more advanced students needing new challenges

### Learning Goals
- algorithm and data structure efficiency understanding
- memory management awareness
- code reading and comprehension

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Alberto Simões and Ricardo Queirós. (2020). On the Nature of Programming Exercises. OpenAccess Series in Informatics, ICPEC 2020. https://arxiv.org/abs/2006.14476
