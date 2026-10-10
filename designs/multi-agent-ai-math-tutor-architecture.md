---
type: design
id: multi-agent-ai-math-tutor-architecture
title: Multi-agent AI tutoring architecture with an orchestrating Tutor Agent and specialist agents
description: The article proposes a multi-agent architecture implemented on LangGraph in which a central Tutor Agent (GPT-4o) interprets student input and orchestrates other components via a ReAct-style framework.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: jarosław-a-chudziak-and-adam-kostka-2025
    resource: "https://arxiv.org/abs/2507.12484"
    title: "Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484"
    author: Jarosław A. Chudziak and Adam Kostka
---

# Multi-agent AI tutoring architecture with an orchestrating Tutor Agent and specialist agents

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a multi-agent architecture implemented on LangGraph in which a central Tutor Agent (GPT-4o) interprets student input and orchestrates other components via a ReAct-style framework. A Memory Dispatcher oversees conversations and controls memory modules, while a pipeline of agents (Research, Planning, Step Handling, Coding) builds courses, and auxiliary tools include a Symbolic Solver, Function Plotter, and Course Graph Drawer. The design prioritizes "deep understanding and independent problem-solving over direct answers" through guided, tool-assisted learning.

## Design Implications

### Context
#### Requirements
- Underlying LLM capabilities: the article states system performance remains fundamentally dependent on underlying LLM capabilities and possible biases
#### Constraints
- Personalization currently operates on a basic set of attributes
- Pedagogical effectiveness of generated courses is yet to be evaluated empirically

### Target Learners
- students learning mathematics, including exam-preparation students

### Learning Goals
- deep conceptual understanding of mathematics topics
- independent problem-solving
- exam revision and targeted practice

### Claims
- [Tutor Prompt Outperforms Base Prompt Mathdial](../claims/tutor-prompt-outperforms-base-prompt-mathdial.md) [+M]
- [O3 Mini Highest Mathdial Accuracy](../claims/o3-mini-highest-mathdial-accuracy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484
