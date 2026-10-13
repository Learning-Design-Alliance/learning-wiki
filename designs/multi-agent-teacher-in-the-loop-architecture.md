---
type: design
id: multi-agent-teacher-in-the-loop-architecture
title: Multi-agent teacher-in-the-loop architecture for context personalization
description: The article introduces a multi-agent, teacher-in-the-loop architecture for context personalization in which a teacher enters a base problem and desired topic, an LLM generates the problem, and then four AI agents eval...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: walkington-2025
    title: Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A. (2025). Mathematics Teachers’ Interactions with a Multi-Agent System for Personalized Problem Generation.
    author: Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A
---

# Multi-agent teacher-in-the-loop architecture for context personalization

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article introduces a multi-agent, teacher-in-the-loop architecture for context personalization in which a teacher enters a base problem and desired topic, an LLM generates the problem, and then four AI agents evaluate it using criteria each specializes in: mathematical accuracy, authenticity, readability, and realism. Each agent has a specified role and prompt and returns a binary pass/fail decision. Failed cases trigger a refinement agent that revises the problem, iterating until all evaluations pass or a maximum of five refinement steps is reached. After refinement, teachers can further author the problem before submitting it.

## Design Implications

### Context
#### Requirements
- A teacher provides a base problem and a topic, and can choose whether to retain or modify the original numerical values
#### Constraints
- The process iterates until all agent evaluations pass or a maximum number of refinement steps is reached (five in this study)

### Target Learners
- Middle school mathematics students (7th grade)

### Learning Goals
- Personalized mathematics word problems aligned to student interests

### Claims
- 

## Related Designs

- [Four specialized evaluation agents for LLM-generated problems](four-specialized-evaluation-agents-llm-problems.md)
- [Multi-agent generate–validate–revise framework with four specialized validator agents for math problem personalization](multi-agent-generate-validate-revise-personalization-framework.md)
- [MAIC: an LLM-driven multi-agent online course framework balancing scalability and adaptivity](maic-multi-agent-course-framework.md)

## Examples
-

## Key Sources
- Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A. (2025). Mathematics Teachers’ Interactions with a Multi-Agent System for Personalized Problem Generation.
