---
type: strategy
id: atb-design-recommendations-interactive-agent-authoring
title: Design recommendations for tutor-authoring systems using interactive AI agents
description: "From the study's findings the authors identify four design recommendations for systems like ATB: expected features matching established interface-builder norms, tutorials and always-available guidance, flexible design..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: glen-smith-2024
    resource: "https://arxiv.org/abs/2404.07883"
    title: "Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. https://arxiv.org/abs/2404.07883"
    author: Glen Smith, Adit Gupta, and Chris MacLellan
---

# Design recommendations for tutor-authoring systems using interactive AI agents

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
From the study's findings the authors identify four design recommendations for systems like ATB: expected features matching established interface-builder norms, tutorials and always-available guidance, flexible design offering multiple interaction options, and real-time testing for model correctness. They state, "We must therefore provide a way to test the learned expert models in real-time for users," because knowing when a model has achieved full correctness is difficult and some users terminated training without confidence in the agent's knowledge.

## Design Implications

### Context
#### Requirements
- Systems should provide a video tutorial or real-time quick-reference guidance for each component
- Systems should offer users a set of ways to interact with the AI agent and leave the choice to them
#### Constraints
- The authors caution that flexible interaction options require considering how the presence or absence of interactions affects the agent's ability to learn, framing this as an optimization problem of maximizing user satisfaction while mitigating risk

### Target Learners
- teachers and other non-technical users authoring tutors

### Target Learning Goals
- creating robust expert models in the shortest time with the fewest examples

## Claims

- [In a user study, all 14 instructor participants recreated both tutor interfaces with the builder and 13 of 14 authored expert models that could solve both tasks.](../claims/atb-14-instructors-built-tutors-13-authored-models.md) [+W]
- [Average authoring time was higher for the Fraction Arithmetic task (11.85 min) than the Square 25 task (7.12 min), with programming experience moderating interface-building and agent-training times in opposite directions across tasks.](../claims/atb-authoring-time-task-and-experience-differences.md) [+W]
- [The Low programming-experience group had a higher incidence of delete actions during interface building (Avg: 7.1 vs 3.4), explaining their longer S25 interface authoring time.](../claims/atb-delete-actions-explain-interface-time-gap.md) [+W]
- [All High-experience participants authored expert models with 100% correctness on both tasks, while one Low-experience participant's model dropped to 20% on fraction multiplication.](../claims/atb-model-correctness-by-experience-group.md) [+W]
- [Teachers in the study saw value in ATB, citing time savings and quick agent training, and expressed willingness to integrate it into their classrooms.](../claims/atb-teachers-see-value-willing-to-adopt.md) [+W]
- [Validation-problem counts moved in opposite directions for the two experience groups: the Low group's average rose from 0.33 to 1.0 across tasks while the High group's fell from 2.25 to 0.15.](../claims/atb-validation-problems-group-trends.md) [+W]

## Related Strategies

- [Extend AI-driven interface design to in-session analytics pages and iterate on further AI-expressive designs](future-in-session-ai-analytics-page-strategy.md)

## Examples
-

## Key Sources
- Glen Smith, Adit Gupta, and Chris MacLellan. (2024). Apprentice Tutor Builder: A Platform For Users to Create and Personalize Intelligent Tutors. https://arxiv.org/abs/2404.07883
