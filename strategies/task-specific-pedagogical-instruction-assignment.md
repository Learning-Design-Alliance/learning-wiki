---
type: strategy
id: task-specific-pedagogical-instruction-assignment
title: Attach task-specific pedagogical system instructions to each training example
description: Following the idea of pedagogical instruction following, each selected training example is associated with a task-specific system instruction that explicitly describes the desired response behavior, determined by the...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: hao-liang-2026
    resource: "https://arxiv.org/abs/2609.23088"
    title: "Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088"
    author: Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang
---

# Attach task-specific pedagogical system instructions to each training example

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Following the idea of pedagogical instruction following, each selected training example is associated with a task-specific system instruction that explicitly describes the desired response behavior, determined by the example's predefined task bucket. The pipeline uses 20 system-instruction templates covering behaviors such as reasoned problem solving, reading comprehension, diagnosis and correction, Socratic questioning, and tutoring dialogue. This design allows the same model to learn multiple pedagogical behaviors while making the desired behavior explicit in the input, separating example content from the response behavior it is intended to teach.

## Design Implications

### Context
#### Requirements
- Examples must first be partitioned into fine-grained task buckets so that each example receives exactly one system instruction matched to its task.
#### Constraints
- A single generic system instruction would conflate distinct, and sometimes conflicting, behaviors, such as providing a justified final answer versus deliberately withholding it to scaffold reasoning.

### Target Learners
- K-12 learners

### Target Learning Goals
- Scaffolded tutoring dialogue
- Problem solving with justification
- Diagnosis and correction of errors

## Related Strategies
- 

## Examples
-

## Key Sources
- Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088
