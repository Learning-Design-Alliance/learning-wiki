---
type: design
id: rubric-examples-llm-grading-prompt-workflow
title: Rubric-and-examples LLM grading prompt workflow with structured JSON output
description: A grading workflow in which each student text answer is evaluated with a single LLM query combining a generic system prompt and an exercise-specific user prompt.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://arxiv.org/abs/2501.14499"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. https://arxiv.org/abs/2501.14499"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
---

# Rubric-and-examples LLM grading prompt workflow with structured JSON output

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A grading workflow in which each student text answer is evaluated with a single LLM query combining a generic system prompt and an exercise-specific user prompt. The prompt's 'two key components' are 'the grading rubric,' which provides structured grading criteria and point allotments, and 'the grading examples of several TA-corrected student submissions'; the model returns a JSON structured text with the score, satisfied criteria, and written feedback.

## Design Implications

### Context
#### Requirements
- Except for the student submission, all prompt entries (question, correct answer, grading rubric, graded examples) must be provided by the TA in advance
- Grading examples should be grouped by uniquely satisfied criteria and uniformly sampled to obtain a diverse range of graded examples
#### Constraints
- Grading criteria in this study were only additive; subtractive point schemes were not tested
- Requiring LLMs to explicitly list satisfied grading criteria was found to improve results

### Target Learners
- university students submitting text-based answers in a bioinformatics course

### Learning Goals
- numeric scoring and constructive written feedback on essay-style exercise answers

### Claims
- [Rubric Examples Prompt Variant Balances Grading Bias](../claims/rubric-examples-prompt-variant-balances-grading-bias.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. https://arxiv.org/abs/2501.14499
