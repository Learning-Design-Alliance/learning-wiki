---
type: design
id: scripted-dpp-framework
title: "Scripted distributed pair programming: structuring DPP with collaboration scripts to balance participation"
description: "The article's framework combines distributed pair programming with collaboration scripts: a script defines participants, groups, activities, roles, and policies for group formation and task distribution."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-03
sources:
  - id: despina-tsompanoudi-2015
    resource: "https://doi.org/10.15388/infedu.2015.17"
    title: "Despina TSOMPANOUDI, Maya SATRATZEMI, Stelios XINOGALOS. (2015). Distributed Pair Programming Using Collaboration Scripts: An Educational System and Initial Results. Informatics in Education. https://doi.org/10.15388/infedu.2015.17"
    author: Despina TSOMPANOUDI, Maya SATRATZEMI, Stelios XINOGALOS
---

# Scripted distributed pair programming: structuring DPP with collaboration scripts to balance participation

> **Design** · [All designs](index.md)
> **Evidence** · 5 claims (2 for, 3 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article's framework combines distributed pair programming with collaboration scripts: a script defines participants, groups, activities, roles, and policies for group formation and task distribution. Programming assignments are decomposed into smaller problem-solving tasks categorized by learning goals, and task-role distribution policies ("rotating role switching" and "balanced knowledge") guide pairs through problem solving. The approach "aims to address the most important drawback of PP, namely unbalanced student participation".

## Design Implications

### Context
#### Requirements
- A teacher defines script components and mechanisms via the authoring tool; assignments must be decomposable into tasks with learning goals
#### Constraints
- Role assignment is not mandatory; students may request individual role switches at any time

### Target Learners
- novice programmers in higher education

### Learning Goals
- balanced participation in pair programming
- symmetric skill acquisition across learning goals

### Claims

- [The balanced knowledge acquisition policy achieved more even task distribution across learning goals than free collaboration](../claims/balanced-knowledge-policy-task-distribution.md) [+W]
- [System-initiated role switching produced more role switches than free collaboration in DPP](../claims/structured-dpp-more-role-switches.md) [+W]
- [Structured collaboration did not significantly improve balance of student code contributions compared to free collaboration](../claims/structured-dpp-no-contribution-balance-gain.md) [~W]
- [Both conditions improved Java knowledge from pre- to post-test, with no difference in learning outcomes between structured and free collaboration](../claims/dpp-pre-post-knowledge-gains.md) [~W]
- [Structured collaboration did not influence assignment completion time compared to free collaboration](../claims/structured-dpp-no-completion-time-effect.md) [~W]

## Related Designs
- 

## Examples
-

## Key Sources
- Despina TSOMPANOUDI, Maya SATRATZEMI, Stelios XINOGALOS. (2015). Distributed Pair Programming Using Collaboration Scripts: An Educational System and Initial Results. Informatics in Education. https://doi.org/10.15388/infedu.2015.17
