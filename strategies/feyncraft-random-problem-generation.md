---
type: strategy
id: feyncraft-random-problem-generation
title: Endless randomly generated diagram problems with configurable options and sample solutions for self-paced practice
description: The Sandbox generates problems at random, configurable by number of state particles, fundamental-force toggles, and hadron frequency (never/allowed/always).
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: gaunt-2025
    resource: "https://arxiv.org/abs/2510.14082"
    title: "Gaunt, J. R. and Owen, A. (2025). FeynCraft: A Game of Feynman Diagrams. https://arxiv.org/abs/2510.14082"
    author: Gaunt, J. R. and Owen, A
---

# Endless randomly generated diagram problems with configurable options and sample solutions for self-paced practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The Sandbox generates problems at random, configurable by number of state particles, fundamental-force toggles, and hadron frequency (never/allowed/always). "The game only generates processes for which valid Feynman diagrams exist, and is able to show sample solutions if the user is stuck." A daily problem feature stores a streak of consecutive days solved, resetting on failure, and submissions are accepted only if states match, validation passes, and the diagram is not a duplicate of a previous submission.

## Design Implications

### Context
#### Requirements
- Problem options must be set before generation; force toggles grey out disallowed particles
- The lowest-order solution count is capped: if more than 4 diagrams exist at lowest order, only 4 are requested; hadron and degree ≥ 5 problems ask for one solution
#### Constraints
- Hadron problems request only one illustrative diagram, since such diagrams in undergraduate courses are illustrative rather than used for calculations

### Target Learners
- advanced undergraduate students
- school pupils

### Target Learning Goals
- practising drawing all lowest-order Feynman diagrams for a process

## Related Strategies

- [Lecturers convert example-sheet Feynman diagram problems into shareable, importable FeynCraft problem sets](feyncraft-lecturer-problem-sets.md)
- [Visual overlays (QCD colour flow, electroweak flow, coupling-strength visualisation) as scaffolds for judging diagram importance](feyncraft-vision-overlays.md)
- [Automatically reconfigure the physical learning task via AR rendering to generate targeted practice opportunities on unmastered skills](ar-automatic-task-reconfiguration-strategy.md)

## Examples
-

## Key Sources
- Gaunt, J. R. and Owen, A. (2025). FeynCraft: A Game of Feynman Diagrams. https://arxiv.org/abs/2510.14082
