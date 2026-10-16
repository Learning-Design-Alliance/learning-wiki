---
type: strategy
id: leap-three-segment-prompt-design
title: "Three-segment prompt design: Condition, Consequence, and Refinement"
description: The article describes a systematic way to write prompts for LLM-based feedback by splitting each prompt into three segments.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
sources:
  - id: steinert-2024
    resource: "https://doi.org/10.1186/s40561-024-00354-1"
    title: "Steinert, S., Avila, K. E., Ruzika, S., Kuhn, J., & Küchemann, S. (2024). Harnessing large language models to develop research-based learning assistants for formative feedback. Smart Learning Environments. https://doi.org/10.1186/s40561-024-00354-1"
    author: "Steinert, S., Avila, K. E., Ruzika, S., Kuhn, J., & Küchemann, S"
---

# Three-segment prompt design: Condition, Consequence, and Refinement

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article describes a systematic way to write prompts for LLM-based feedback by splitting each prompt into three segments. The Condition specifies when support should be given (e.g., "If the students' answer is incomplete or incorrect"), the Consequence requests a specific output adaptable by the teacher and adaptive to the student's answer, and the Refinement includes a restriction such as "without giving the correct answer". This structure is intended to allow systematic manipulation and empirical investigation of adaptive and adaptable prompt segments.

## Design Implications

### Context
#### Requirements
- The teacher or researcher must specify the condition, the desired output type, and a refinement restriction for each prompt
#### Constraints
- The refinement restriction is included because prior research cited by the authors indicates that elaborated feedback combined with the correct answer has low efficiency and may lead to superficial learning

### Target Learners
- teachers and researchers designing LLM-based feedback tasks

### Target Learning Goals
- formative feedback design
- self-regulated learning

## Related Strategies
- Leap Llm Formative Feedback Platform

## Examples
-

## Key Sources
- Steinert, S., Avila, K. E., Ruzika, S., Kuhn, J., & Küchemann, S. (2024). Harnessing large language models to develop research-based learning assistants for formative feedback. Smart Learning Environments. https://doi.org/10.1186/s40561-024-00354-1
