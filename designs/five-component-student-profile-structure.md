---
type: design
id: five-component-student-profile-structure
title: Five-component structured student profile capturing knowledge and dialogue behavior
description: "Each generated profile has a fixed structure with five sections: Knowledge State (estimated KC mastery as correct over total attempts), Knowledge Acquisition (how mastery changes over time), Misconception (recurring m..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: zhangqi-duan-2026
    resource: "https://arxiv.org/abs/2605.30051"
    title: "Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051"
    author: Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan
---

# Five-component structured student profile capturing knowledge and dialogue behavior

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Each generated profile has a fixed structure with five sections: Knowledge State (estimated KC mastery as correct over total attempts), Knowledge Acquisition (how mastery changes over time), Misconception (recurring mathematical errors), Dialogue Behavior (tendencies and common dialogue acts), and Linguistic Style (verbosity, terminology use, fragment versus full explanations). "Each generated profile has a fixed structure with five components, which align with important aspects of student knowledge and behavior identified in (Scarlatos et al., 2026)." Profiles are initialized by prompting a proprietary reasoning LLM, then distilled into a trainable open-source generator.

## Design Implications

### Context
#### Requirements
- A recent window of question-answering and dialogue interactions as input for profile generation
#### Constraints
- The profile is a compact summary of a truncated history window, not the student's entire learning history

### Target Learners
- Students with longitudinal histories on a math learning platform

### Learning Goals
- Representing student knowledge state, misconceptions, and dialogue behavior for turn-level simulation

### Claims
- [Knowledge Behavior Profile Complementary Signals](../claims/knowledge-behavior-profile-complementary-signals.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051
