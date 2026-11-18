---
type: design
id: smartwatch-privacy-game-wear-os
title: Smartwatch privacy game for Wear OS with dynamically customised challenges
description: A maze-narrative game for Android Wear OS watches in which players traverse four levels, collect coins and encounter villager NPCs asking functionality questions and thieves triggering timed settings-configuration cha...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: meredydd-williams-2019
    resource: "https://arxiv.org/abs/1905.05222"
    title: "Meredydd Williams, Jason R C Nurse, Sadie Creese. (2019). Smartwatch Games: Encouraging Privacy-Protective Behaviour in a Longitudinal Study. https://arxiv.org/abs/1905.05222"
    author: Meredydd Williams, Jason R C Nurse, Sadie Creese
---

# Smartwatch privacy game for Wear OS with dynamically customised challenges

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A maze-narrative game for Android Wear OS watches in which players traverse four levels, collect coins and encounter villager NPCs asking functionality questions and thieves triggering timed settings-configuration challenges. "The privacy game focused on the three protective approaches: restricting permissions, disabling GPS and enabling a screen lock", divided into 14 challenges. Challenges were "dynamically customised around user behaviour" by reading recent monitoring-app log files, providing an educational feedback loop. The design implements learning-science techniques including reflection, story-based agents and the conceptual-procedural principle, plus a simulated settings interface for safe practice.

## Design Implications

### Context
#### Requirements
- A monitoring app logging settings every five minutes supplies the recent behaviour data needed for dynamic customisation of challenges
#### Constraints
- The control version contained identical gameplay but concerned general smartwatch use such as adjusting screen brightness, to minimise confounding variables and reduce Hawthorne Effect bias

### Target Learners
- adult smartwatch users new to Wear OS devices
- university students

### Learning Goals
- configuring app permissions, GPS and screen locks on smartwatches
- privacy-protective behaviour change

### Claims
- [Smartwatch Privacy Game Screen Lock Increase](../claims/smartwatch-privacy-game-screen-lock-increase.md) [+M]
- [Smartwatch Posttest Treatment Understanding Self Efficacy](../claims/smartwatch-posttest-treatment-understanding-self-efficacy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Meredydd Williams, Jason R C Nurse, Sadie Creese. (2019). Smartwatch Games: Encouraging Privacy-Protective Behaviour in a Longitudinal Study. https://arxiv.org/abs/1905.05222
