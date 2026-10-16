---
type: design
id: three-dimensional-scaffolding-design-paratutor
title: Three-dimensional scaffolding design coordinating user roles, tutoring phases, and guidance strategies
description: "ParaTutor organizes its support as a design that \"coordinates user roles, tutoring phases, and guidance strategies during parent-child math tutoring.\" The role dimension differentiates support between parents (guidanc..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: luo-lan-2024
    resource: "https://arxiv.org/abs/2606.18030"
    title: "LUO Lan, WANG Anqi, ZHOU Muzhi, ZHU Junhua, CAI Jie, YU Ao, and PAN Hui. (2024). ParaTutor: Coordinating Parent-Child Math Tutoring through Role-Separated LLM Scaffolding. https://arxiv.org/abs/2606.18030"
    author: LUO Lan, WANG Anqi, ZHOU Muzhi, ZHU Junhua, CAI Jie, YU Ao, and PAN Hui
---

# Three-dimensional scaffolding design coordinating user roles, tutoring phases, and guidance strategies

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
ParaTutor organizes its support as a design that "coordinates user roles, tutoring phases, and guidance strategies during parent-child math tutoring." The role dimension differentiates support between parents (guidance for conducting tutoring) and children (visual grounding for interpreting problems). The phase dimension structures how support changes across understanding, calculation, and summarization. The strategy dimension translates tutoring goals into concrete parent-facing guidance including suggested actions, example language, and ways of using the child-facing visualization. Together these dimensions define ParaTutor as a scaffold for parent-led tutoring.

## Design Implications

### Context
#### Requirements
- A shared internal state maintained by a Main Agent that stores the current problem, active phase, interaction history, selected mode, child progress, and visualization state
- Phase transitions controlled by explicit rule-based conditions rather than LLM decisions
- Two synchronized panels separating parent-facing and child-facing interfaces
#### Constraints
- Designed for parent-child dyads in home math word problem tutoring, not single-user learning
- Visual grounding withholds procedural solution steps reserved for parent-facing scaffolding

### Target Learners
- Parent-child dyads with children aged 10-12 in grades 4-6

### Learning Goals
- Mathematical word problem solving with shared understanding and active reasoning

### Claims
- [Visual Grounding Increases Child Reasoning Turns](../claims/visual-grounding-increases-child-reasoning-turns.md) [+M]
- [Role Separated Scaffolding Distributed Support](../claims/role-separated-scaffolding-distributed-support.md) [+M]
- [Parent Facing Guidance Reduces Breakdowns](../claims/parent-facing-guidance-reduces-breakdowns.md) [+M]

## Related Designs
- Paratutor Multi Agent Llm Scaffolding System

## Examples
-

## Key Sources
- LUO Lan, WANG Anqi, ZHOU Muzhi, ZHU Junhua, CAI Jie, YU Ao, and PAN Hui. (2024). ParaTutor: Coordinating Parent-Child Math Tutoring through Role-Separated LLM Scaffolding. https://arxiv.org/abs/2606.18030
