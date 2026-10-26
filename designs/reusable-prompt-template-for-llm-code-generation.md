---
type: design
id: reusable-prompt-template-for-llm-code-generation
title: Reusable structured prompt template built up across lesson sections
description: The lesson taught students a reusable template for constructing prompts, built up throughout the lesson sections, to help them remember to address each learning objective.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: keith-tran-2026
    resource: "https://arxiv.org/abs/2606.30547"
    title: "Keith Tran, Samiha Marwan, and Thomas Price. (2026). Teaching Prompt-Based Programming with LLMs: A 45-Minute Lesson with Guided Practice for End-User Programmers. https://arxiv.org/abs/2606.30547"
    author: Keith Tran, Samiha Marwan, and Thomas Price
---

# Reusable structured prompt template built up across lesson sections

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The lesson taught students a reusable template for constructing prompts, built up throughout the lesson sections, to help them remember to address each learning objective. The template prompts learners to "Write me a Python function that takes as input [describe the input, including its type] and it should output [describe the output, including its type], that [explain how the function transforms the input into the output]" plus an example input and expected output. It operationalizes the Gulf of Envisioning dimensions of describing the problem, phrasing prompts, and assessing output.

## Design Implications

### Context
#### Requirements
- Instruction across the five learning objectives so students can fill each template slot (input, output, transformation, example)
#### Constraints
- Taught in the context of Promptly-style tasks requiring natural-language specification of computational intent rather than code writing

### Target Learners
- end-user programmers
- novice LLM users

### Learning Goals
- articulating inputs, outputs, and transformations to an LLM
- reducing vague or underspecified prompts

### Claims
- [Prompting Lesson Raises Self Efficacy](../claims/prompting-lesson-raises-self-efficacy.md) [+M]

## Related Designs

- [Structured prompt-template and keyword-card interaction design for human-LLM co-creation](structured-prompt-template-keyword-interaction-design.md)

## Examples
-

## Key Sources
- Keith Tran, Samiha Marwan, and Thomas Price. (2026). Teaching Prompt-Based Programming with LLMs: A 45-Minute Lesson with Guided Practice for End-User Programmers. https://arxiv.org/abs/2606.30547
