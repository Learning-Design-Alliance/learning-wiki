---
type: strategy
id: in-notebook-real-time-execution-guidance
title: Provide real-time in-notebook visual guidance instead of relying on written instructions alone
description: The article recommends operationalizing teacher instructions directly inside the notebook rather than relying only on written text, citing evidence that reading efficiency on digital media is lower than on paper and t...
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

# Provide real-time in-notebook visual guidance instead of relying on written instructions alone

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends operationalizing teacher instructions directly inside the notebook rather than relying only on written text, citing evidence that reading efficiency on digital media is lower than on paper and that students may inadvertently corrupt notebook state. MOON materializes the scenario as color and emoji indicators updated at every step, plus buttons to jump to the next possible cells, so students see which cells to execute without re-reading instructions, while backtracking keeps exploration possible.

## Design Implications

### Context
#### Requirements
- A formalized scenario script must exist so the tool can compute which cells are permitted at each step
#### Constraints
- The article states the approach was evaluated in only one context, so results could vary with student level or the notebook used

### Target Learners
- students working through scenario-based educational notebooks in practical sessions

### Target Learning Goals
- complying with the intended execution order while retaining exploratory programming

### Affordances
- [Moon Scenario Scripting Language](../products/moon.md)

## Claims

- [Notebook grades (correctness) do not differ significantly between MOON and control groups, though descriptively higher with MOON](../claims/moon-correctness-no-significant-difference.md) [~M]
- [MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario](../claims/moon-increases-notebook-scenario-compliance.md) [+M]
- [MOON does not hinder students' progression through the notebook (no significant completeness difference)](../claims/moon-no-completeness-hindrance.md) [~M]
- [Most surveyed students perceived MOON as useful and reported it helped them follow the execution order](../claims/moon-user-study-perceived-usefulness.md) [+M]

## Related Strategies

- Moon Jupyterlab Scenario Plugin
- [Leverage scenario traces and scripts to give teachers feedback on notebook pain points](moon-teacher-feedback-future-direction.md)
- [Embed factor-aware guidance directly within analytics tools at the point of interpretation](embed-factor-aware-guidance-in-analytics-tools.md)

## Examples
-

## Key Sources
- Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. https://arxiv.org/abs/2309.16201
