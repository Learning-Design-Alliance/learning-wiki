---
type: strategy
id: ar-automatic-task-reconfiguration-strategy
title: Automatically reconfigure the physical learning task via AR rendering to generate targeted practice opportunities on unmastered skills
description: "Use AR rendering over a marker-equipped physical object to digitally reconfigure the task state instead of requiring learners to manually reset it, then generate problems targeting each learner's unmastered knowledge..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: haocheng-ren-2025
    resource: "https://doi.org/10.1145/3715336.3735788"
    title: "Haocheng Ren, Muzhe Wu, Gregory Croisdale, Anhong Guo, and Xu Wang. (2025). Rubikon: Intelligent Tutoring for Rubik's Cube Learning Through AR-enabled Physical Task Reconfiguration. Designing Interactive Systems Conference (DIS '25). https://doi.org/10.1145/3715336.3735788"
    author: Haocheng Ren, Muzhe Wu, Gregory Croisdale, Anhong Guo, and Xu Wang
---

# Automatically reconfigure the physical learning task via AR rendering to generate targeted practice opportunities on unmastered skills

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
Use AR rendering over a marker-equipped physical object to digitally reconfigure the task state instead of requiring learners to manually reset it, then generate problems targeting each learner's unmastered knowledge components. Rubikon's configurations "are randomly sampled from a set of cube states associated with each knowledge component, with the specific color arrangements also randomized at runtime, ensuring task variety", while learners keep handling the physical object.

## Design Implications

### Context
#### Requirements
- A method to track the physical object's state (e.g., ArUco markers) and render it digitally
- A task model defining knowledge components and their associated target states
#### Constraints
- The authors note Rubikon is a Rubik's Cube-specific solution and the setup may not generalize beyond that task

### Target Learners
- novices learning 3D physical tasks

### Target Learning Goals
- deliberate practice on specific unmastered skill components of a physical task

### Affordances
- [Rubikon Ar Task Reconfiguration Tutor](../products/rubikon.md)

## Claims

- [The AR-rendered-cube setup did not add to learners' reported cognitive load compared to a regular cube with video tutorials](../claims/ar-setup-no-extra-cognitive-load.md) [+W]
- [Rubikon learners distributed practice more evenly across knowledge components, while baseline learners skewed toward easier components](../claims/rubikon-balanced-coverage-practice.md) [+W]
- [Rubikon learners scored 25% higher on the post-test than learners using video tutorials with a regular or AR-rendered cube, with pre-test and completion time controlled](../claims/rubikon-higher-posttest-gains.md) [+W]
- [Rubikon learners had significantly lower preparation cost — the ratio of preparation time to exercise time — than both baselines](../claims/rubikon-lower-preparation-cost.md) [+W]
- [Rubikon learners exercised significantly more knowledge components during practice than both baselines](../claims/rubikon-more-knowledge-components-exercised.md) [+W]

## Related Strategies

- [Build a dynamic function-generation system so teachers can draw arbitrary 2D or 3D graphs without printing new markers](dynamic-function-generation-teacher-authored-vr-graphs.md)
- [Endless randomly generated diagram problems with configurable options and sample solutions for self-paced practice](feyncraft-random-problem-generation.md)

## Examples
-

## Key Sources
- Haocheng Ren, Muzhe Wu, Gregory Croisdale, Anhong Guo, and Xu Wang. (2025). Rubikon: Intelligent Tutoring for Rubik's Cube Learning Through AR-enabled Physical Task Reconfiguration. Designing Interactive Systems Conference (DIS '25). https://doi.org/10.1145/3715336.3735788
