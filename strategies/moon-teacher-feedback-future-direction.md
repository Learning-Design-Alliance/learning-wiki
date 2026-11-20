---
type: strategy
id: moon-teacher-feedback-future-direction
title: Leverage scenario traces and scripts to give teachers feedback on notebook pain points
description: "As future work, the authors propose turning MOON's recorded execution traces and scripts into feedback for teachers."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: christophe-casseau-2023
    resource: "https://arxiv.org/abs/2309.16201"
    title: "Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. https://arxiv.org/abs/2309.16201"
    author: Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc
---

# Leverage scenario traces and scripts to give teachers feedback on notebook pain points

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
As future work, the authors propose turning MOON's recorded execution traces and scripts into feedback for teachers. They suggest analyzing traces and scripts "to pinpoint pain points in a scenario and provide improvement suggestions", and gathering data from MOON instances in real time to assist teachers during a session by identifying students struggling with or lagging behind the scenario. They also plan to improve script writing, which currently must be done manually.

## Design Implications

### Context
#### Requirements
- MOON instances must record user traces and the scenario scripts must be available for analysis
#### Constraints
- This is stated as future work; the article reports no evaluation of teacher feedback

### Target Learners
- teachers running notebook-based practical sessions

### Target Learning Goals
- improving notebook scenario design and detecting struggling students during sessions

## Claims

- [MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario](../claims/moon-increases-notebook-scenario-compliance.md) [+W]
- [MOON does not hinder students' progression through the notebook (no significant completeness difference)](../claims/moon-no-completeness-hindrance.md) [+W]
- [Most surveyed students perceived MOON as useful and reported it helped them follow the execution order](../claims/moon-user-study-perceived-usefulness.md) [+W]

## Related Strategies

- Moon Jupyterlab Scenario Plugin
- [Provide real-time in-notebook visual guidance instead of relying on written instructions alone](in-notebook-real-time-execution-guidance.md)

## Examples
-

## Key Sources
- Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. https://arxiv.org/abs/2309.16201
