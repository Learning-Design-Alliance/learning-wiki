---
type: design
id: edusim-llm-four-module-architecture
title: Four-module architecture for language-driven robot control in educational simulation
description: The article describes a hierarchical instruction processing pipeline in which natural language is translated into executable robot behavior.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: shenqi-lu-and-liangwei-zhang-2026
    resource: "https://arxiv.org/abs/2601.01196"
    title: "Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196"
    author: Shenqi Lu and Liangwei Zhang
---

# Four-module architecture for language-driven robot control in educational simulation

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article describes a hierarchical instruction processing pipeline in which natural language is translated into executable robot behavior. The architecture "consist of four modules: (1) Natural language interface, (2) LLM-based instruction planner, (3) Simulation control backend, and (4) User interaction frontend." User instructions are sent to an LLM via structured prompts, and the LLM output is converted into Python control code executed in CoppeliaSim through action primitives such as moveForward, moveToXY, and closeGripper. The backend also implements 7-stage progressive deceleration with overshoot detection and maintains trajectory history for navigation.

## Design Implications

### Context
#### Requirements
- A structured prompt template and a pre-constructed control function library are needed so the LLM planner can translate directives into robot-compatible action primitives
#### Constraints
- The LLM planner depends on the language-model backend chosen; the backend was evaluated with Groq's llama-3.3-70b-versatile

### Target Learners
- beginner robotics learners
- non-expert robot users

### Learning Goals
- intuitive natural-language control of robotic systems
- understanding language-to-action translation in robotics

### Claims

- [A single natural-language command can be decomposed by an LLM into coordinated sequential action sequences for multiple robots](../claims/llm-decomposes-command-into-multi-robot-action-sequences.md) [+W]
- [Natural language control requires less human operation time than manual control for all five complex tasks tested](../claims/natural-language-control-faster-than-manual-complex-tasks.md) [+W]
- [LLM-generated robot control code succeeds on 100%, 94.4%, and 88.9% of simple, composite, and complex instructions respectively](../claims/llm-code-success-rate-declines-with-instruction-difficulty.md) [+W]

## Related Designs
- Edusim Llm Platform

## Examples
-

## Key Sources
- Shenqi Lu and Liangwei Zhang. (2026). EduSim-LLM: An Educational Platform Integrating Large Language Models and Robotic Simulation for Beginners. https://arxiv.org/abs/2601.01196
