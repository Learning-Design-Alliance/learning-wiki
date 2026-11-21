---
type: strategy
id: filter-then-evaluate-llm-tutor-assessment-strategy
title: Use a two-stage filter-then-evaluate prompting pipeline with self-consistency voting to assess tutor moves at scale
description: "The article's implementable recipe: first ask the LLM a filter question (does the tutoring situation apply, e.g., did the tutor praise the student or did the student make a math error), then, if applicable, an evaluat..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: danielle-r-thomas-2025
    resource: "https://arxiv.org/abs/2506.17410"
    title: "Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. https://arxiv.org/abs/2506.17410"
    author: Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger
---

# Use a two-stage filter-then-evaluate prompting pipeline with self-consistency voting to assess tutor moves at scale

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article's implementable recipe: first ask the LLM a filter question (does the tutoring situation apply, e.g., did the tutor praise the student or did the student make a math error), then, if applicable, an evaluation question about adherence to best practices. The authors report that "Prompt chaining [12] and self-consistency [9] allowed us to modularize the evaluation process and stabilize predictions, with majority voting proving effective for binary decisions in filter and evaluation stages." This modular design also enables cost savings, since the evaluation prompt is skipped when the filter is negative.

## Design Implications

### Context
#### Requirements
- Access to LLMs (GPT-4 family, Gemini 1.5 Pro, LearnLM were used)
- Few-shot examples covering both ideal and suboptimal tutor responses
- A scoring rubric distinguishing effective from ineffective tutor moves
#### Constraints
- The authors tested this on lightly processed audio transcripts of 1:1 remote math tutoring; speaker identification was challenging and video, screenshots, and chat messages were absent

### Target Learners
- middle school students in remote mathematics tutoring

### Target Learning Goals
- scalable assessment of tutor moves
- identifying tutors' application of praise and error-response best practices

## Claims

- [LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection](../claims/llms-detect-student-math-errors-82-88.md) [+W]
- [LLMs reliably detect tutor praise in real-life math tutoring transcripts, with 94-98% accuracy across five models](../claims/llms-detect-tutor-praise-high-accuracy.md) [+W]
- [LLMs evaluate tutor responses to student math errors at 73-77% accuracy, the weakest performance](../claims/llms-evaluate-error-responses-73-77.md) [+W]
- [LLMs evaluate tutor praise quality in line with human judgments at 83-89% accuracy](../claims/llms-evaluate-praise-quality-83-89.md) [+W]
- [No single LLM significantly outperformed the others on these tutor-move tasks](../claims/no-llm-significantly-outperformed-others-tutor-moves.md) [+W]
- [Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition](../claims/prompting-techniques-task-dependent-tutor-moves.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. https://arxiv.org/abs/2506.17410
