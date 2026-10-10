---
type: design
id: cc-self-train-adaptive-learning-system
title: "cc-self-train adaptive learning system: a three-layer hook-based engagement observation and scaffolding adjustment mechanism"
description: The adaptive learning system observes learner engagement quality through keyword-heuristic classification of each learner message into six engagement categories with quality scores from 1 to 5, accumulated in a local...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: zain-naboulsi-2026
    resource: "https://arxiv.org/abs/2604.17460"
    title: "Zain Naboulsi. (2026). Agentic Education: Using Claude Code to Teach Claude Code. arXiv. https://arxiv.org/abs/2604.17460"
    author: Zain Naboulsi
---

# cc-self-train adaptive learning system: a three-layer hook-based engagement observation and scaffolding adjustment mechanism

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The adaptive learning system observes learner engagement quality through keyword-heuristic classification of each learner message into six engagement categories with quality scores from 1 to 5, accumulated in a local learner profile. Layer 1 is a silent Stop hook that fires after every Claude response and computes streak booleans; Layer 2 injects a teaching note into Claude's context at session start based on the productive/unproductive ratio; Layer 3 adjusts the learner's Effective Level at module boundaries. The article describes "a two-timescale system" in which a slow clock adjusts the persona schedule at module boundaries using aggregate statistics while a fast clock triggers scaffolding changes mid-module using sequential patterns, governed by an asymmetric response principle that is quicker to increase scaffolding than to withdraw it.

## Design Implications

### Context
#### Requirements
- Operates entirely through Claude Code's hook system with no external dependencies, no API calls for observation, and no web backend
#### Constraints
- Observation uses keyword heuristics rather than LLM-based classification, so individual classifications are noisy; Effective Level changes occur only at module boundaries; level changes are silent to the student

### Target Learners
- developers learning an agentic AI coding tool through the cc-self-train curriculum

### Learning Goals
- sustained productive engagement and appropriately paced scaffolding during tool-mastery learning

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zain Naboulsi. (2026). Agentic Education: Using Claude Code to Teach Claude Code. arXiv. https://arxiv.org/abs/2604.17460
