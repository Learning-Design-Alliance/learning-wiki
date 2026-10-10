---
type: design
id: educasim-agent-persona-memory-architecture
title: Behavior-based persona and course-grounded memory architecture for simulated students
description: "EducaSim's student-agent architecture synthesizes generative agents with personas and memories, domain-contextualized memories aligned with actual course material, and a classroom dynamic tree using LLM as a judge."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: cameron-mohne-2026
    resource: "https://arxiv.org/abs/2603.11444"
    title: "Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech. (2026). EducaSim: Interactive Simulacra for CS1 Instructional Practice. https://arxiv.org/abs/2603.11444"
    author: Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech
---

# Behavior-based persona and course-grounded memory architecture for simulated students

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
EducaSim's student-agent architecture synthesizes generative agents with personas and memories, domain-contextualized memories aligned with actual course material, and a classroom dynamic tree using LLM as a judge. Personas are defined by pedagogically relevant behaviors rather than demographic identity traits, including "(1) name, (2) engagement style, and (3) speech style". Course texts are chunked chronologically, tagged with low/medium/high engagement levels, and prepended with strings describing what the student does and does not know; retrieval scores memories by recency, importance, and cosine-similarity, returning the top-k.

## Design Implications

### Context
#### Requirements
- Course materials must be ordered chronologically based on when a student would encounter them so teachers can refer to past material
#### Constraints
- Agents are an approximation, not a perfect representation, of student behavior and cannot fully represent the diversity of human understandings or confusions

### Target Learners
- Teachers-in-training practicing instruction

### Learning Goals
- Realistic simulated student interactions grounded in actual course content

### Claims
- 

## Related Designs
- Educasim Simulated Section Teacher Practice Tool

## Examples
-

## Key Sources
- Cameron Mohne, Nicholas Vo, Dora Demszky, Chris Piech. (2026). EducaSim: Interactive Simulacra for CS1 Instructional Practice. https://arxiv.org/abs/2603.11444
