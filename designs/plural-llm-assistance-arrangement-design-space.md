---
type: design
id: plural-llm-assistance-arrangement-design-space
title: Plural LLM assistance as a configurable arrangement of support around the user
description: This framework treats LLM assistance as a design space defined by arrangement rather than only by model capability or response quality.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: harsh-kumar-2026
    resource: "https://arxiv.org/abs/2604.02677"
    title: "Harsh Kumar, Zi Kang (Jace) Mu, Jonathan Vincentius, Ashton Anderson. (2026). Human Thinking under Plural LLM Assistance: Mathematical Problem Solving and Open-Ended Writing. Working Paper, July 2026, Toronto, Canada. https://arxiv.org/abs/2604.02677"
    author: Harsh Kumar, Zi Kang (Jace) Mu, Jonathan Vincentius, Ashton Anderson
---

# Plural LLM assistance as a configurable arrangement of support around the user

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This framework treats LLM assistance as a design space defined by arrangement rather than only by model capability or response quality. As the article puts it, "LLM assistance can vary not only in model capability or response quality, but also in how support is arranged, e.g., one voice or many, one model or several, generalist or specialist roles". The framework holds that roles and personas are interfaces and prompting choices rather than human-like social actors, and that arrangement affects performance, confidence, and diversity of thought. The two experiments instantiate this space with tutor/peer arrangements in math and single-versus-role-specialized-duo arrangements in writing.

## Design Implications

### Context
#### Requirements
- LLM agents instantiated with distinct system prompts defining roles, with learners introduced to each agent's strengths and tendencies so they can calibrate trust
#### Constraints
- The explored design space is deliberately narrow: agent count, error types, role specializations, and interaction structure were held largely constant, and the experiments are a first step rather than a definitive map

### Target Learners
- adult crowdworkers solving math problems or writing essays

### Learning Goals
- mathematical problem solving and retention
- open-ended argumentative and creative writing quality and idea diversity

### Claims
- [Tutor Plus Peers Strongest Unassisted Math Accuracy](../claims/tutor-plus-peers-strongest-unassisted-math-accuracy.md) [+M]
- [Role Specialized Duo Preserves Idea Diversity](../claims/role-specialized-duo-preserves-idea-diversity.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Harsh Kumar, Zi Kang (Jace) Mu, Jonathan Vincentius, Ashton Anderson. (2026). Human Thinking under Plural LLM Assistance: Mathematical Problem Solving and Open-Ended Writing. Working Paper, July 2026, Toronto, Canada. https://arxiv.org/abs/2604.02677
