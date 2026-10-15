---
type: strategy
id: engineered-knowledge-gap-question-design
title: Design questions with engineered knowledge gaps LLMs cannot bridge alone, via non-existing scenarios and guided mathematical reasoning
description: "The article develops two question-design strategies so that questions \"cannot be solved by an LLM, but can be solved with appropriately designed prompts.\" Strategy 1 \"embeds known concepts within a completely novel co..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: xinming-yang-2025
    resource: "https://arxiv.org/abs/2508.05979"
    title: "Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979"
    author: Xinming Yang, Haasil Pujara, Jun Li
---

# Design questions with engineered knowledge gaps LLMs cannot bridge alone, via non-existing scenarios and guided mathematical reasoning

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article develops two question-design strategies so that questions "cannot be solved by an LLM, but can be solved with appropriately designed prompts." Strategy 1 "embeds known concepts within a completely novel context defined by arbitrary, multi-part rules that an LLM cannot infer from its training data," such as a signed number system with case-based sign convention or a hypothetical SWAPADD instruction. Strategy 2 uses "complex, multi-step procedures where LLMs are known to struggle without explicit step-by-step guidance," with students guiding the full logical process rather than giving final answers.

## Design Implications

### Context
#### Requirements
- Questions must prevent solution retrieval from training data and force a guided reasoning process, creating a genuine knowledge dependency the student must fill
#### Constraints
- More advanced models may solve problems previously considered LLM-hard; the authors mitigate this by selecting less-capable models, assuming a controlled environment, and appending hidden prompts with constraints or personas

### Target Learners
- undergraduate computer science students

### Target Learning Goals
- mastering procedures and first principles rather than final answers, e.g., number-system conversion, Boolean algebra transformation, assembly operations

## Related Strategies

- [Adapt the two question-design strategies across disciplines: novel scenarios for logic puzzles, guided reasoning for proofs and critical analyses](cross-disciplinary-adaptation-of-question-strategies.md)

## Examples
-

## Key Sources
- Xinming Yang, Haasil Pujara, Jun Li. (2025). Learning by Teaching: Engaging Students as Instructors of Large Language Models in Computer Science Education. Published as a conference paper at COLM 2025. https://arxiv.org/abs/2508.05979
