---
type: strategy
id: fill-gaps-in-example-input-files
title: Include deliberate gaps (__FILL__) in example input files to force engagement with documentation
description: Tutorial authors insert gaps marked with the keyword __FILL__ into example PLUMED input files.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: tribello-2024
    resource: "https://arxiv.org/abs/2412.03595"
    title: "Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595"
    author: Tribello, G. A., et al
---

# Include deliberate gaps (__FILL__) in example input files to force engagement with documentation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Tutorial authors insert gaps marked with the keyword __FILL__ into example PLUMED input files. "Gaps in input files are useful as they force students to look at the PLUMED documentation before running their calculations." The intent is to "encourage students to think about the steps involved in a particular calculation rather than simply uncritically performing the tutorial instructions." Contributors can secretly link a complete solution via a #SOLUTIONFILE comment that is not shown in the rendered page.

## Design Implications

### Context
#### Requirements
- a parser able to render input files containing __FILL__ gaps and a hidden solution file for badge validation
#### Constraints
- the solution file location is hidden from students, so badge colors reflect the complete solution rather than the visible incomplete input

### Target Learners
- novice PLUMED users working through tutorials independently

### Target Learning Goals
- consulting software documentation deliberately
- understanding the steps of a simulation calculation rather than copying instructions

## Related Strategies

- [Engineer pauses, multimodal anchors, and improved prosody into AI-generated audio revision tools](engineer-pauses-anchors-prosody-ai-audio.md)

## Examples
-

## Key Sources
- Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595. [doi:10.48550/arxiv.2412.03595](https://doi.org/10.48550/arxiv.2412.03595)
