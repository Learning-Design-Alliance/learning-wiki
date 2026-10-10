---
type: design
id: genai-slide-tools-five-tool-evaluation
title: Five-tool GenAI slide generation evaluation (NotebookLM, M365 Copilot, Claude, Cursor, Claude Code)
description: "The article evaluates five accessible GenAI tools for transforming online textbook chapters into lecture slides for a 5 ECTS Web Software Development course: NotebookLM, M365 Copilot, Claude (Sonnet 4.5), Cursor, and..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: juho-leinonen-lisa-zhang-and
    resource: "https://arxiv.org/abs/2605.13532"
    title: "Juho Leinonen, Lisa Zhang, and Arto Hellas. 2026. AI-Generated Slides: Are They Good? Can Students Tell?. In Proceedings of Western Canada Conference on Computing Education 2026 (WCCCE 2026). ACM, New York, NY, USA. https://arxiv.org/abs/2605.13532"
---

# Five-tool GenAI slide generation evaluation (NotebookLM, M365 Copilot, Claude, Cursor, Claude Code)

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article evaluates five accessible GenAI tools for transforming online textbook chapters into lecture slides for a 5 ECTS Web Software Development course: NotebookLM, M365 Copilot, Claude (Sonnet 4.5), Cursor, and Claude Code. The tools "represent different points on the spectrum from automated to instructor-in-the-loop workflows". Each was prompted with the same textbook-derived prompt requesting a 15-minute lecture segment with peer-instruction exercises, and assessed for factual accuracy, completeness, and pedagogical soundness.

## Design Implications

### Context
#### Requirements
- Accessible tools (free, under USD$30 per month, or institutionally licensed) and instructor-authored source materials
#### Constraints
- NotebookLM had no out-of-the-box slide generation at the time; styling rules in the initial prompt degraded content quality, so styling was separated as post-processing

### Target Learners
- upper-year undergraduate web programming students

### Learning Goals
- lecture slides covering HTML, Svelte, shared state, CRUD, and the Fetch API

### Claims
- [Coding Assistants Best Slide Generation](../claims/coding-assistants-best-slide-generation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Juho Leinonen, Lisa Zhang, and Arto Hellas. 2026. AI-Generated Slides: Are They Good? Can Students Tell?. In Proceedings of Western Canada Conference on Computing Education 2026 (WCCCE 2026). ACM, New York, NY, USA. https://arxiv.org/abs/2605.13532
