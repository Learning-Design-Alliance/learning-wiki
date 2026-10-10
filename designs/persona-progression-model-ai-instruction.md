---
type: design
id: persona-progression-model-ai-instruction
title: "Persona progression model: a four-stage AI-instructor persona (Guide→Collaborator→Peer→Launcher) operationalizing the Gradual Release of Responsibility framework for AI-mediated instruction"
description: "The persona progression model ties the AI instructor's tone and scaffolding depth to the learner's position in the module sequence across four stages: Guide (patient teacher, explains every concept), Collaborator (wor..."
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

# Persona progression model: a four-stage AI-instructor persona (Guide→Collaborator→Peer→Launcher) operationalizing the Gradual Release of Responsibility framework for AI-mediated instruction

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
The persona progression model ties the AI instructor's tone and scaffolding depth to the learner's position in the module sequence across four stages: Guide (patient teacher, explains every concept), Collaborator (working partner, asks before telling), Peer (senior colleague, terse and direct), and Launcher (states the goal and steps back). The article states that "The curriculum defines four personas, each specified as a prompt engineering directive in every module file", mapping 1:1 to GRR's four phases, with "I do it" reinterpreted so the learner is always hands-on. Persona boundaries are set at onboarding from three experience-level schedules (4/3/2/1, 3/3/3/1, 1/3/5/1) and can shift at module boundaries via the adaptive system. Implementation uses descriptive prompt directives alone, without fine-tuning, RLHF, or RAG.

## Design Implications

### Context
#### Requirements
- Each module file must contain an explicit persona directive metadata line consumed by Claude Code when reading the module
#### Constraints
- The article notes a static tone either underwhelms beginners or patronizes experts, motivating stage-dependent personas; the adaptation is validated only for structural consistency, not instructional effectiveness

### Target Learners
- professional software engineers learning an agentic AI coding tool, at beginner, intermediate, or advanced experience levels

### Learning Goals
- compositional mastery of an agentic AI coding tool's features, from setup through multi-agent orchestration

### Claims
- [Cc Self Train Pilot Self Efficacy Gains](../claims/cc-self-train-pilot-self-efficacy-gains.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zain Naboulsi. (2026). Agentic Education: Using Claude Code to Teach Claude Code. arXiv. https://arxiv.org/abs/2604.17460
