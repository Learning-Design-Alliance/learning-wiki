---
type: design
id: four-design-goals-process-visualization-teachers
title: "Four design goals for teacher-facing programming-process visualization: visibility, workflow support, formative feedback, and non-automated integrity clarification"
description: "The article organizes the tool's design around four stated goals: DG1 making students' programming processes visible to teachers through interpretable views; DG2 supporting teacher decision-making through workflows fo..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: heidi-taveter-and-marina-lepp-2026
    resource: "https://arxiv.org/abs/2607.24757"
    title: "Heidi Taveter and Marina Lepp. (2026). From Idea to Classroom in Days: Using “Vibe Coding” to Create a Programming Process Visualizer from IDE Activity Logs. https://arxiv.org/abs/2607.24757"
    author: Heidi Taveter and Marina Lepp
---

# Four design goals for teacher-facing programming-process visualization: visibility, workflow support, formative feedback, and non-automated integrity clarification

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article organizes the tool's design around four stated goals: DG1 making students' programming processes visible to teachers through interpretable views; DG2 supporting teacher decision-making through workflows for both quick individual inspection and efficient review of larger log sets; DG3 supporting process-informed formative feedback; and DG4 supporting clarification of academic-integrity concerns without automating judgment. For DG3, the tool should help teachers "identify situations in which students may need support, such as repeated run-error cycles with limited progress, a late start of the program execution, or unusually long periods of inactivity." The framework translates prior programming-process research into teacher-facing views.

## Design Implications

### Context
#### Requirements
- Underlying IDE activity logs must be available, since the views summarize signals such as runs, errors, debugs, pauses, and copy-paste behavior captured in Thonny logs
#### Constraints
- Integrity-related indicators are intended as warning signals rather than automated determinations, with interpretation left to teachers

### Target Learners
- teachers of large introductory programming courses

### Learning Goals
- teacher triage and case prioritization
- timely formative feedback
- academic-integrity case clarification

### Claims
- 

## Related Designs

- [Three design tensions from expert feedback: authenticity versus cognitive load, integration versus visible progress, and team construction versus individual accountability](three-design-tensions-robotics-curriculum.md)
- [Four-step formative assessment cycle: create assignments, assist students through immediate feedback, assess class performance, analyze answers together](four-step-formative-assessment-cycle-assistments.md)

## Examples
-

## Key Sources
- Heidi Taveter and Marina Lepp. (2026). From Idea to Classroom in Days: Using “Vibe Coding” to Create a Programming Process Visualizer from IDE Activity Logs. https://arxiv.org/abs/2607.24757
