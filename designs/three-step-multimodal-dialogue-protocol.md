---
type: design
id: three-step-multimodal-dialogue-protocol
title: Three-step structured multimodal dialogue intervention protocol (describe, correct, solve)
description: "A prompting protocol for correcting LLM multimodal errors, described as follows: \"The intervention followed a three-step dialogue: (i) 'Describe what you observe in the figure/graph,' (ii) researcher correction of any..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: akshay-syal-2026
    title: Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education.
    author: Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar
---

# Three-step structured multimodal dialogue intervention protocol (describe, correct, solve)

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A prompting protocol for correcting LLM multimodal errors, described as follows: "The intervention followed a three-step dialogue: (i) 'Describe what you observe in the figure/graph,' (ii) researcher correction of any misidentified visual elements, and (iii) 'Solve the problem'." Step (ii) corrections were limited to observable visual properties, such as clarifying a force vector direction or a graph intercept value, without physics hints. It was applied to all incorrect baseline responses and corrected 82% of errors without model retraining.

## Design Implications

### Context
#### Requirements
- Access to the model via web interface or programmatic API workflow with chat history maintained per question.
#### Constraints
- No inter-rater verification was performed to confirm researcher corrections stayed free of domain-relevant information; the article recommends blind auditing of correction content.

### Target Learners
- undergraduate physics students
- educators integrating AI tutoring

### Learning Goals
- correcting LLM errors on image-dependent physics problems

### Claims
- [Structured Dialogue Corrects 82 Percent Llm Errors](../claims/structured-dialogue-corrects-82-percent-llm-errors.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education.
