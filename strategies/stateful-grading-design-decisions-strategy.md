---
type: strategy
id: stateful-grading-design-decisions-strategy
title: "Grading Stateful exercises: author decisions on parallel paths, review loops, penalties, and gameability, with encouraging continuous feedback"
description: "The article recommends that Stateful authors take explicit positions on five design questions: equal point values for parallel parts, point value of review loops relative to the direct route, rewarding activity versus..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: matti-harjula-2024
    resource: "https://arxiv.org/abs/2403.04424"
    title: "Matti Harjula, Ville Havu, Inkeri Kontro, Kimmo Kulmala, Jarmo Malinen, and Petri Salo. (2024). Student behaviour and engagement with adaptive exercises on a thermodynamics course. A PREPRINT. https://arxiv.org/abs/2403.04424"
    author: Matti Harjula, Ville Havu, Inkeri Kontro, Kimmo Kulmala, Jarmo Malinen, and Petri Salo
---

# Grading Stateful exercises: author decisions on parallel paths, review loops, penalties, and gameability, with encouraging continuous feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that Stateful authors take explicit positions on five design questions: equal point values for parallel parts, point value of review loops relative to the direct route, rewarding activity versus success, penalising wrong attempts, and preventing undesirable gameability. It concludes that "the students' need for steady motivation to carry on and complete the task is common to all Stateful exercises" and that "the student should get encouraging continuous feedback, at least, by getting indication about the level of completion and the points already accrued". Graphical scene graphs help detect accidents in grading logic.

## Design Implications

### Context
#### Requirements
- Explicit definition of how many times the same points can be collected (first time only, or best attempt)
- Alternative branching paths designed in a reasonably balanced way, or difficulty and maximum points disclosed before students choose
#### Constraints
- Maximum score cannot plainly be the sum of score values over all PRTs; penalising shortcuts extra instruction is described as unmotivating because more work then yields fewer points

### Target Learners
- university students completing adaptive e-learning exercises

### Target Learning Goals
- sustained motivation and completion of multi-scene adaptive exercises

## Related Strategies

- Stateful Diesel Exercise Sde
- [Push students to attempt exercises up to the ~90-exercise threshold via reminders or push notifications](push-students-toward-90-exercise-threshold.md)

## Examples
-

## Key Sources
- Matti Harjula, Ville Havu, Inkeri Kontro, Kimmo Kulmala, Jarmo Malinen, and Petri Salo. (2024). Student behaviour and engagement with adaptive exercises on a thermodynamics course. A PREPRINT. https://arxiv.org/abs/2403.04424
