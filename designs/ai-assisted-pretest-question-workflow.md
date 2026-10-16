---
type: design
id: ai-assisted-pretest-question-workflow
title: AI-assisted pretest question generation workflow with generator, evaluator, and controller components
description: "The article presents an AI-assisted workflow for pretest question development with three iterative components: automated generation grounded in instructional materials, rubric-based evaluation of question quality, and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: pei-yu-tseng-2026
    resource: "https://arxiv.org/abs/2606.23629"
    title: "Pei-Yu Tseng, Mahir Akgun, and Peng Liu. (2026). Why Machines Misread Pedagogical Quality: Human–Machine Alignment in LLM-Based Pretest Question Evaluation. arXiv preprint. https://arxiv.org/abs/2606.23629"
    author: Pei-Yu Tseng, Mahir Akgun, and Peng Liu
---

# AI-assisted pretest question generation workflow with generator, evaluator, and controller components

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article presents an AI-assisted workflow for pretest question development with three iterative components: automated generation grounded in instructional materials, rubric-based evaluation of question quality, and iterative selection of high-quality questions. The Generator produces candidate questions each round; the Evaluator scores questions on rubric dimensions and removes those below level 3 on relevance or clarity, then runs blind pairwise comparison flagging contradictions; the Controller analyzes gaps in quality and topic coverage and feeds back to the Generator. Both generator and evaluator use GPT-5.1.

## Design Implications

### Context
#### Requirements
- Requires four inputs: course material, a scenario, key concepts, and a rubric defining the quality dimensions of openness, cognitive depth, relevance, and clarity
#### Constraints
- The study is situated in an intermediate-level statistics course in the Cybersecurity major, focusing on multiple regression for undergraduate learners

### Target Learners
- undergraduate Cybersecurity students in an intermediate-level statistics course

### Learning Goals
- pretest questions aligned with learning objectives on multiple regression, spanning openness and cognitive depth dimensions

### Claims
- [Rubric Revision Improves Machine Alignment](../claims/rubric-revision-improves-machine-alignment.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Pei-Yu Tseng, Mahir Akgun, and Peng Liu. (2026). Why Machines Misread Pedagogical Quality: Human–Machine Alignment in LLM-Based Pretest Question Evaluation. arXiv preprint. https://arxiv.org/abs/2606.23629
