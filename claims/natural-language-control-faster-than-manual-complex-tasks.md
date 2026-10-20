---
type: claim
title: Natural language control requires less human operation time than manual control for all five complex tasks tested
description: Natural language control requires less human operation time than manual control for all five complex tasks tested
id: natural-language-control-faster-than-manual-complex-tasks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: shenqi-lu-and-liangwei-zhang-2026
    resource: "https://doi.org/10.48550/arxiv.2601.01196"
    title: "Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196 [doi:10.48550/arxiv.2601.01196](https://doi.org/10.48550/arxiv.2601.01196)"
    author: Shenqi Lu and Liangwei Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Natural language control requires less human operation time than manual control for all five complex tasks tested

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` For five complex tasks executed once under each condition, human operation time under manual control exceeded 29 s for all tasks while natural language control stayed under 21 s for all tasks. [→ Shenqi Lu and Liangwei Zhang 2026](#shenqi-lu-and-liangwei-zhang-2026)

## Evidence

### Shenqi Lu and Liangwei Zhang 2026

Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196 [doi:10.48550/arxiv.2601.01196](https://doi.org/10.48550/arxiv.2601.01196)

`q2 · i?` · `design · r2`

Comparative simulation experiment in which five complex tasks were each executed once under manual keyboard-and-mouse control and once under natural language control. Timing ran from the start of command entry until the command was sent to the simulator, so it measures human operation time, not robot execution time; natural language control took less operation time in all five tasks (Fig. 6 (A)).

> "For these five complex tasks, the human operation time under the manual control condition exceeds 29 s for all tasks, while the human operation time under the natural language control condition is less than 21 s for all tasks"

## Discussion


## Learner Variables
- [Time and Continuity](../learner-variables/time-and-continuity.md) — outcome: instruction changes it

## Related Claims
- [A single natural-language command can be decomposed by an LLM into coordinated sequential action sequences for multiple robots](llm-decomposes-command-into-multi-robot-action-sequences.md) — related
- [Manual adaptation is slightly superior to automatic adaptation in adaptive training of manual control](manual-adaptation-slightly-superior-automatic-adaptive-training.md) — related
