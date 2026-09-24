---
type: theory
title: Dialogue Knowledge Tracing (dialogueKT) Framework
description: "DialogueKT is the task the article proposes, which \"analyzes student discourse within the knowledge tracing (KT) framework\"."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# Dialogue Knowledge Tracing (dialogueKT) Framework

> **Theory** · [All theories](index.md)

## Description
DialogueKT is the task the article proposes, which "analyzes student discourse within the knowledge tracing (KT) framework". It treats tutor turns as posing tasks tied to knowledge components (KCs) and student turns as correct or incorrect responses, so that "A pair of tutor-student dialogue turns corresponds to a time step in KT". The framework has three stages: identify the KCs in each turn, classify student correctness, then apply KT methods. Because most turns involve several KCs, it adopts "a compensatory model rather than a conjunctive model", predicting correctness as average KC mastery.

## Design Implications

### Context
#### Requirements
- Each student turn must be annotated with a correctness label and a list of KCs; the article uses Common Core math standards as KCs.
- Correctness of a turn is modeled as the average mastery of all KCs involved in the turn (a compensatory model).
#### Constraints
- A time step corresponds to a single student turn; an entire dialogue cannot be a time step since no existing open-source large-scale tutoring dialogue dataset links students across dialogues.
- The work is restricted to math, and it remains to be seen whether Common Core standard tagging generalizes to other subjects.
- Annotating a full dialogue with a single prompt makes real-time KT impossible, because information from future turns is available when annotating a given turn.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Objectives
- Estimating student knowledge of math knowledge components (Common Core standards) and predicting student response correctness across dialogue turns

### Claims
- [Llmkt Outperforms Existing Kt Methods On Tutoring Dialogues](../claims/llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) [~M]
- [Dialogue Kt Performance Is Relatively Low Compared To Standard Kt](../claims/dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) [~W]

## Related Theories
- Formative Assessment
- Mastery Learning

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
