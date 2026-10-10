---
type: strategy
id: gale-shapley-lab-project-partitioning
title: Partition projects across course lab sections using the Gale-Shapley algorithm before student-to-project assignment
description: "To support courses with labs, the article describes a supplementary algorithm run before the main assignment: it computes teams needed per lab from an instructor-defined base team size, then treats lab-to-project allo..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: brandon-pardi-2026
    resource: "https://arxiv.org/abs/2606.15572"
    title: "Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572"
    author: Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar
---

# Partition projects across course lab sections using the Gale-Shapley algorithm before student-to-project assignment

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To support courses with labs, the article describes a supplementary algorithm run before the main assignment: it computes teams needed per lab from an instructor-defined base team size, then treats lab-to-project allocation as "a version of the college admissions problem, solvable via the Gale-Shapley algorithm," seeking a stable matching without blocking pairs. Labs rank projects by average student preference; projects rank labs by average lab skill frequency of their required skills. This ensures all students on a project share a lab, facilitating consistent collaboration, after which the main skill-weighted algorithm runs within each lab.

## Design Implications

### Context
#### Requirements
- Instructor-defined base team size
- Student skill and preference survey data to build both preference lists
#### Constraints
- Gale-Shapley ensures stability but does not account for skill diversity within teams, so skill-based matching proceeds separately within each lab

### Target Learners
- capstone students enrolled in lecture-plus-lab courses

### Target Learning Goals
- overlapping team availability during lab hours for consistent collaboration

### Affordances
- [Three Stage Llm Team Formation Methodology](../designs/three-stage-llm-team-formation-methodology.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572
