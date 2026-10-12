---
type: design
id: no-code-vibe-coding-research-platform
title: Purpose-built no-code vibe-coding research platform for controlled experimentation
description: A custom web platform built for controlled study of LLM-native software creation.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: sverrir-thorgeirsson-theo-b-weidmann
    resource: "https://doi.org/10.1145/3772318.3791666"
    title: "Sverrir Thorgeirsson, Theo B. Weidmann, and Zhendong Su. 2026. Computer Science Achievement and Writing Skills Predict Vibe Coding Proficiency. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3791666"
---

# Purpose-built no-code vibe-coding research platform for controlled experimentation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A custom web platform built for controlled study of LLM-native software creation. Unlike commercial tools, "our own platform deliberately conceals the code entirely, consistent with the original definition of vibe coding", retaining a chat window on the left and app preview on the right, with rollback, a blurred live stream of model output, task descriptions, and a timer. It was informed by a survey of Replit, Cursor, Lovable, and Bolt, runs on Claude Sonnet 4 with a diff-based update mechanism, and logs feature exploration of sample applications to support reproducible, privacy-compliant evaluation.

## Design Implications

### Context
#### Requirements
- The integrated AI model must not retain participant inputs or train on participants' prompts, per the ethics committee's data-protection requirements.
#### Constraints
- Exposing source code is intentionally avoided, as it would introduce an additional interaction mode and risk confounding the pure vibe-coding construct.

### Target Learners
- tertiary-level students in controlled laboratory studies

### Learning Goals
- measuring proficiency in iterative, behavior-guided natural-language programming

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Sverrir Thorgeirsson, Theo B. Weidmann, and Zhendong Su. 2026. Computer Science Achievement and Writing Skills Predict Vibe Coding Proficiency. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3791666
