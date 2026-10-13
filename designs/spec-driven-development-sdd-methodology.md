---
type: design
id: spec-driven-development-sdd-methodology
title: "Spec-Driven Development (SDD): a development methodology in which AI agents generate code from structured specification documents that developers must verify"
description: SDD is a software development methodology proposed for use with AI agents, positioned as an alternative to Vibe Coding.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: hidetake-tanaka-2026
    resource: "https://arxiv.org/abs/2608.30572"
    title: "Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572"
    author: Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu
---

# Spec-Driven Development (SDD): a development methodology in which AI agents generate code from structured specification documents that developers must verify

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
SDD is a software development methodology proposed for use with AI agents, positioned as an alternative to Vibe Coding. "This approach involves deﬁning detailed speciﬁcations cl early at the early stages of development and having AI agents gener ate code based on those speciﬁcations." Its distinguishing feature is that agents proceed from structured specification documents rather than ambiguous natural-language instructions, with specifications describing architectural patterns, coding conventions, security requirements, and testing strategies that agents treat as constraints. Because developers must understand and verify the generated documents and code, the authors judge SDD more suitable than Vibe Coding for project-based courses where students take responsibility for AI outputs.

## Design Implications

### Context
#### Requirements
- Developers must understand and verify AI-generated specifications and documents at each step to maintain code quality and consistency
#### Constraints
- SDD demands greater expertise compared to Vibe Coding, per the authors

### Target Learners
- third-year undergraduate information systems students

### Learning Goals
- application development skills
- understanding and verifying AI-generated specifications and code

### Claims
- [Ai Usage Varies By Team And Phase Sdpbl Sdd](../claims/ai-usage-varies-by-team-and-phase-sdpbl-sdd.md) [+M]

## Related Designs

- [Purpose-built no-code vibe-coding research platform for controlled experimentation](no-code-vibe-coding-research-platform.md)

## Examples
-

## Key Sources
- Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572
