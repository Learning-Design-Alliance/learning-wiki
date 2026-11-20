---
type: design
id: scaffolded-chain-of-thought-prompting
title: "Scaffolded chain of thought: a prompt structure forcing rubric-grounded reasoning before grading"
description: Scaffolded COT is a prompt-engineering structure the authors name and develop for LLM grading.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics"
    author: Zhongzhou Chen and Tong Wan
---

# Scaffolded chain of thought: a prompt structure forcing rubric-grounded reasoning before grading

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Scaffolded COT is a prompt-engineering structure the authors name and develop for LLM grading. It is "a stronger form of COT that integrates some of the features of generated knowledge prompting": the prompt has five components (context, general grading instructions, problem statement, detailed rubric with per-item explanations, and specific grading requirements), and the grading requirement "forces the LLM to first select the most relevant portion of the student answer, and then explicitly compare it to the rubric explanation before generating a grade", using a fixed scaffold of quoted rubric text, quoted student text, similarity statements, and a concluding binary score.

## Design Implications

### Context
#### Requirements
- A detailed rubric accompanied by per-item explanation text, such as requiring that the student's explanation must explicitly contain 'frictionless' or 'smooth' or a similar phrase
- A grading-requirement scaffold that mandates quoting the rubric item and the most relevant part of the student explanation before stating the binary grade
#### Constraints
- The article's version was developed and refined iteratively using five student explanations
- The detailed rubric explanation was authored by a rater who had also graded student responses, which the authors state could have biased prompt design

### Target Learners
- calculus-based introductory mechanics students at a large public research university

### Learning Goals
- accurate partial-credit grading of student written explanations of physics reasoning against a rubric

### Claims
- [Scaffolded Cot Human Level Agreement Gpt35 Grading](../claims/scaffolded-cot-human-level-agreement-gpt35-grading.md) [+M]
- [Scaffolded Cot Significance By Rater](../claims/scaffolded-cot-significance-by-rater.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. https://www.semanticscholar.org/search?q=Scaffolded%20Chain%20of%20Thought%20GPT-3.5%20partial%20credit%20grading%20physics
