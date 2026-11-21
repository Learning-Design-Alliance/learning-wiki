---
type: strategy
id: injected-concept-aligned-drift-strategy
title: Inject concept-aligned objective drift with predefined failure signatures to train diagnosis and recovery
description: In selected labs the curriculum deliberately injects objective drift targeting specific learning objectives, creating structured opportunities for diagnosis and recovery from specification violations.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: mark-dranias-and-adam-whitley-2025
    resource: "https://arxiv.org/abs/2604.00281"
    title: "Mark Dranias and Adam Whitley. (2025). Human-in-the-Loop Control of Objective Drift in LLM-Assisted Computer Science Education. https://arxiv.org/abs/2604.00281"
    author: Mark Dranias and Adam Whitley
---

# Inject concept-aligned objective drift with predefined failure signatures to train diagnosis and recovery

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 qualitative), `q2`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
In selected labs the curriculum deliberately injects objective drift targeting specific learning objectives, creating structured opportunities for diagnosis and recovery from specification violations. Each injected-drift event is specified in advance by "a curricular concept, a workflow landmark for injection, a fixed message appended to the AI context without student knowledge, and an expected failure signature observable in outputs". Students are told drift will occur and are expected to detect and correct it using their planning documents; injections are limited in number, aligned with explicit learning objectives, and do not affect grades.

## Design Implications

### Context
#### Requirements
- Each drift injection must be pre-specified with a curricular concept, workflow landmark, hidden context message, and expected failure signature; students must be informed that errors will occur
#### Constraints
- Drift injections are limited in number, aligned with explicit learning objectives, and do not affect student grades

### Target Learners
- undergraduate computer science students

### Target Learning Goals
- diagnosis and recovery from specification violations; learning of targeted CS concepts such as indexing conventions

## Claims

- [Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies](../claims/prompting-strategies-differ-by-bug-source.md) [+W]
- [Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck](../claims/correct-solution-in-prompt-bottleneck.md) [+W]

## Related Strategies

- [Error-injection exercises: diagnosing subtly wrong simulations as graded practice](error-injection-diagnosis-exercises.md)

## Examples
-

## Key Sources
- Mark Dranias and Adam Whitley. (2025). Human-in-the-Loop Control of Objective Drift in LLM-Assisted Computer Science Education. https://arxiv.org/abs/2604.00281
