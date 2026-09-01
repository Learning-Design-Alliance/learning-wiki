---
type: pattern
id: computational-essay-writing
title: Computational Essay Writing
description: Students investigate a disciplinary question by extending a provided code simulation and writing a computational essay — a document mixing prose, executable code, and visualization — to explain their question, method, and findings to peers.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
author: Odden & Zwicki
grain_size: unit
sources:
  - id: odden-zwicki-2025
    resource: "https://doi.org/10.1080/10508406.2025.2494791"
    title: "Odden, T. O. B., & Zwicki, B. (2025). How physics students build computational literacy by creating computational literature. Journal of the Learning Sciences, 34(5), 700-742."
    author: "Odden, T. O. B., & Zwicki, B."
---

# Computational Essay Writing

> **Pattern** · [All patterns](index.md)

## Description
Students are given example "computational literature" — documents that mix executable code with prose, visualization, and explanation to convey a disciplinary idea — plus a working code "seed" (e.g., a provided simulation) and its extension questions. Working in pairs, they formulate their own investigation question, extend or modify the provided code to explore it, and write a computational essay (e.g., a Jupyter notebook) documenting their question, method, results, and interpretation, which they then present orally to peers. The pattern treats code as a thinking and communication tool, not only a technical skill to master, and mirrors how professional computational scientists work: reading existing computational literature before proposing a novel direction.

## Implications

### Context
#### Requirements
- Example computational essays that model the genre (mixing code, prose, and visualization)
- A working code "seed" (a runnable simulation) with built-in extension questions, so students are extending rather than starting from a blank editor
- An audience and format for presenting the finished essay (e.g., a mock research-group meeting)
#### Constraints
- Students with limited coding background may make only minor code modifications, yet the source study found this did not prevent them from developing disciplinary sensemaking — [Creating computational literature develops computational literacy even when code modification is minor](../claims/creating-computational-literature-develops-computational-literacy.md) [~W]
- Grain Size: unit

### Target Goals
- Building computational literacy along three interdependent pillars: material (technical fluency with code), cognitive (using computation to reason about a disciplinary problem), and social (communicating computational work to others)

### Target Learners
- Studied with undergraduate physics students, including those initially reluctant toward programming

### Theory
#### Supporting
- [Cognitive Apprenticeship](../theories/cognitive-apprenticeship.md) — students are positioned as apprentice computational scientists, working from modeled expert artifacts (example essays) toward independent investigation, with articulation (writing, presenting) built into the task
#### Contradicting / Qualifying
- None identified in the source study

### Claims
- [Creating computational literature develops computational literacy even when code modification is minor](../claims/creating-computational-literature-develops-computational-literacy.md) [+W]

## Design

### Sequence
1. Students review example computational essays and a provided code seed (a runnable simulation) with built-in extension questions.
2. Students formulate an investigation question, often inspired by the seed's extension questions.
3. Students comprehend and extend or modify the provided code to investigate their question.
4. Students run their code, interpret results, and debug both code and conceptual understanding.
5. Students write a computational essay explaining their question, method, results, and interpretation.
6. Students present their essay orally to peers (e.g., in a mock research-group meeting) and receive feedback.

### Affordances
- [Problem-Based Learning (PBL)](problem-based-learning-pbl.md) — the open-ended investigation question and defended final artifact mirror PBL's structure, with a computational essay in place of a proposal or case response

## Related Patterns
- [Problem-Based Learning (PBL)](problem-based-learning-pbl.md)

## Examples
- Two physics students, initially reluctant toward coding, extended a biophysics simulation of ion motion in nerve cells to investigate intermolecular forces, producing an essay rich in physical interpretation despite making only minor code changes.
- Two other students who enjoyed coding produced a more code- and visualization-heavy essay on a different topic, showing different pairs can develop different pillars of computational literacy from the same task structure.

## Key Sources
- Odden, T. O. B., & Zwicki, B. (2025). How physics students build computational literacy by creating computational literature. *Journal of the Learning Sciences, 34*(5), 700-742. [https://doi.org/10.1080/10508406.2025.2494791](https://doi.org/10.1080/10508406.2025.2494791)
