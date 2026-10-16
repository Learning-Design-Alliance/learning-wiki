---
type: design
id: sdd-template-project-copilot-instructions
title: SDD template project with copilot-instructions.md custom instructions and docs/ artifact directories for AI-agent workflow in SDPBL
description: A template project directory for Visual Studio Code distributed to each team to operationalize SDD in the course.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: hidetake-tanaka-2026
    resource: "https://arxiv.org/abs/2608.30572"
    title: "Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572"
    author: Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu
---

# SDD template project with copilot-instructions.md custom instructions and docs/ artifact directories for AI-agent workflow in SDPBL

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A template project directory for Visual Studio Code distributed to each team to operationalize SDD in the course. "copilot-instructions.md contains the workﬂow and project-speciﬁc rules as custom in structions." AI-generated artifacts are stored in the docs/ directory, with done/, investigate/, and review/ subdirectories holding the corresponding reports, alongside specs.md and tasks.md and a NewSpringBootProject directory registered as a GitHub repository. Based on their observations, the authors report these templates appeared to help students smoothly initiate development tasks using AI agents, and that a 30-minute lecture and one-hour demonstration accompanied distribution.

## Design Implications

### Context
#### Requirements
- Pre-configured AI instructions (copilot-instructions.md), specification templates, and development rules such as coding conventions
#### Constraints
- The study context is a specific Java/Spring Boot course with only four teams in 2025, limiting generalization per the authors

### Target Learners
- third-year undergraduate information systems students working in teams of three to four

### Learning Goals
- team-based web application development with Spring Boot
- structuring instructions and specifications for AI agents

### Claims
- 

## Related Designs

- [Clover: an instrumented AI code completion tool with attention checks](clover-instrumented-code-completion-tool.md)

## Examples
-

## Key Sources
- Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572
