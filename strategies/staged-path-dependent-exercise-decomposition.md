---
type: strategy
id: staged-path-dependent-exercise-decomposition
title: Decompose complex open statistics exercises into path-dependent stages with fallback stages and accepted input corridors
description: To digitalize open-ended statistics exercises without revealing the solution strategy, the authors decompose an exercise into several stages, each a stand-alone exercise sharing the same context.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: nils-schwinning-2018
    resource: "https://arxiv.org/abs/1811.02391"
    title: "Nils Schwinning, Michael Striewe, Till Massing, Christoph Hanck, Michael Goedicke. (2018). Towards digitalisation of summative and formative assessments in academic teaching of statistics. arXiv preprint. https://arxiv.org/abs/1811.02391"
    author: Nils Schwinning, Michael Striewe, Till Massing, Christoph Hanck, Michael Goedicke
---

# Decompose complex open statistics exercises into path-dependent stages with fallback stages and accepted input corridors

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To digitalize open-ended statistics exercises without revealing the solution strategy, the authors decompose an exercise into several stages, each a stand-alone exercise sharing the same context. "The decomposition into several stages enables us to provide detailed feedback messages for each single task" and to react differently to possible flaws. Stages can be path dependent (later stages depend on earlier answers), non-numeric or skipped submissions route to a defined fallback stage, and numeric answers accept a corridor of input around the correct solution whose size can be adjusted per stage.

## Design Implications

### Context
#### Requirements
- Fallback stages must be defined for non-numeric or skipped submissions, since otherwise computations with user input are impossible
- Exercise authors must spend time predicting possible erroneous submissions that are still worth some points, especially for electronic exams
#### Constraints
- In summative assessments, repetitions of stages should not be allowed because this could reveal information about the correctness of the submission
- Using student input from previous stages in later calculations needs care because submissions may not be of the expected type

### Target Learners
- university students in higher statistics courses

### Target Learning Goals
- multi-step statistical problem solving such as hypothesis testing, including choosing test strategy, distribution, degrees of freedom, and computed results

## Related Strategies

- [Structured/Segmented Instruction](structured-segmented-instruction.md)
- [IDEAL Problem-Solving Model](ideal-problem-solving-model.md)

## Examples
-

## Key Sources
- Nils Schwinning, Michael Striewe, Till Massing, Christoph Hanck, Michael Goedicke. (2018). Towards digitalisation of summative and formative assessments in academic teaching of statistics. arXiv preprint. https://arxiv.org/abs/1811.02391
