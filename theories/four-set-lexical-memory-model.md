---
type: theory
title: Four-set student lexical memory model with staged progression from introduction to long-term retention
description: "The adaptive tutoring algorithm formalizes each student's lexical memory as four non-intersecting sets: \"N – units assigned to the student and pending introduction; P – units in the process of active acquisition; S –..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: evgeny-chukharev-hudilainen-and-tatiana-a-klepikova-2016
    resource: "https://doi.org/10.1558/cj.v33i3.26055"
    title: "Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova. (2016). The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction: a double-blind study. calico journal vol 33.3. https://doi.org/10.1558/cj.v33i3.26055"
    author: Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova
---

# Four-set student lexical memory model with staged progression from introduction to long-term retention

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study, `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The adaptive tutoring algorithm formalizes each student's lexical memory as four non-intersecting sets: "N – units assigned to the student and pending introduction; P – units in the process of active acquisition; S – units in the student's short-term memory; L – learned units (in the long-term memory)." Units move forward from N to P to S to L, with the only backward movement from S to P on recall failure. A unit enters short-term memory after at least four successful recalls in activities of increasing difficulty, and is deemed fully learned after remaining in short-term memory for at least seven days and still being recalled. The model is rooted in the Linguistic Automaton framework and the cybernetic approach to instruction as regulation.

## Design Implications

### Context
#### Requirements
- Each lexical unit carries a numerical parameter vector describing anticipated complexity and degree of learning; session quotas allocate time across the three active sets.
#### Constraints
- The stage thresholds (four recalls; seven days) were selected arbitrarily with the intention to refine them through further experimentation; the relationship between these operational terms and psycholinguistic reality, including tacit versus explicit knowledge, is not investigated in the study.

### Target Learners
- EFL students using the tutoring system

### Target Learning Objectives
- Long-term retention of target vocabulary items

### Claims

- [Tutoring Stage Thresholds Validated By Posttest](../claims/tutoring-stage-thresholds-validated-by-posttest.md) [+M]
- [Lexical units brought to the 'fully learned' stage by the tutor scored significantly lower on the posttest than units students already knew before introduction](../claims/learned-units-below-previously-known-units.md) [-W]

## Related Theories
- 

## Examples

- [Automated generation of seven vocabulary activity types with distractor collision prevention](../patterns/generated-activity-types-collision-prevention.md)

## Key Sources
- Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova. (2016). The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction: a double-blind study. calico journal vol 33.3. https://doi.org/10.1558/cj.v33i3.26055
