---
type: strategy
id: two-question-llm-tutor-evaluation
title: "Evaluate LLM tutoring systems in two steps: first whether an intervention changes the assistance students receive, then whether that change improves learning"
description: "The article proposes that evaluations of LLM tutoring systems should distinguish a behavioral question from an educational question: \"does a pedagogical intervention change the assistance students receive?\" versus \"do..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: suhyeon-lee-2026
    resource: "https://arxiv.org/abs/2608.22993"
    title: "Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993"
    author: Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin
---

# Evaluate LLM tutoring systems in two steps: first whether an intervention changes the assistance students receive, then whether that change improves learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes that evaluations of LLM tutoring systems should distinguish a behavioral question from an educational question: "does a pedagogical intervention change the assistance students receive?" versus "does that change improve learning?" The scaffolding scale addresses the first question directly — a tutoring prompt, policy, or model intended to encourage greater student reasoning should produce a measurable shift in scaffolding relative to the general-purpose baseline — while whether such a shift improves learning remains a separate empirical question.

## Design Implications

### Context
#### Requirements
- A baseline scaffolding distribution for the general-purpose assistant and a validated scaffolding measure applied to interaction logs before and after the intervention
#### Constraints
- The article's baseline comes from one introductory AI course and one model configuration, so the reference distribution characterizes that setting rather than general-purpose LLMs universally

### Target Learners
- students using LLM tutors for coursework and problem solving

### Target Learning Goals
- evaluating whether pedagogically designed LLM tutors change the assistance students actually receive and whether such changes improve learning

### Affordances
- [Five Level Llm Scaffolding Scale](../research-methods/five-level-scaffolding-scale-for-measuring-the-directness-of-assistance-in-llm-tutoring-re.md)

## Claims

- [Commercially optimized study-oriented modes achieve higher learner-side scores than baseline, and CURIOBOT shifts general-purpose LLM behavior toward those patterns via prompting alone](../claims/study-oriented-modes-upper-bound-reference.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993
