---
type: design
id: three-agent-learner-teacher-evaluator-architecture
title: "Three-agent division of labor: learner simulation, didactical adaptation, and automated evaluation as coordinated roles"
description: "The framework's organizing architecture assigns personalization to three specialized, transparent agent modules with typed interfaces."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: jana-gonnermann-müller-2025
    resource: "https://arxiv.org/abs/2508.11401"
    title: "Jana Gonnermann-Müller, Jennifer Haase, Konstantin Fackeldey, Sebastian Pokutta. (2025). FACET: Teacher-Centred LLM-Based Multi-Agent Systems—Towards Personalized Educational Worksheets. https://arxiv.org/abs/2508.11401"
    author: Jana Gonnermann-Müller, Jennifer Haase, Konstantin Fackeldey, Sebastian Pokutta
---

# Three-agent division of labor: learner simulation, didactical adaptation, and automated evaluation as coordinated roles

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The framework's organizing architecture assigns personalization to three specialized, transparent agent modules with typed interfaces. The learner agent emits a transcript capturing attempted solution steps, misconceptions, and affective cues; the teacher agent consumes this transcript and produces a one-page worksheet with tasks annotated by Bloom level, scaffolds, hints, and motivational comments; the evaluator returns rubric-aligned scores and diagnostics. The article argues this agent-based design "increases the robustness of the learner personas compared to single-LLM setups and reduces prompting effort" by letting teachers define personas once and instantiate variants. Modularization preserves interpretability of intermediate decisions and supports stable behavior.

## Design Implications

### Context
#### Requirements
- Structured inter-agent communication with typed interfaces
- Hard constraints encoded in prompts (e.g., task count, length budget)
#### Constraints
- Tested with GPT-4.1 and GPT-4o; additional iterative refinement iterations did not improve results

### Target Learners
- K-12 students in heterogeneous classrooms

### Learning Goals
- personalized instructional materials addressing both cognitive and motivational learner dimensions

### Claims
- [Facet Single Iteration Sufficient](../claims/facet-single-iteration-sufficient.md) [+M]

## Related Designs
- Facet Multi Agent Framework

## Examples
-

## Key Sources
- Jana Gonnermann-Müller, Jennifer Haase, Konstantin Fackeldey, Sebastian Pokutta. (2025). FACET: Teacher-Centred LLM-Based Multi-Agent Systems—Towards Personalized Educational Worksheets. https://arxiv.org/abs/2508.11401
