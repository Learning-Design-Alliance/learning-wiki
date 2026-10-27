---
type: strategy
id: reserve-llm-grading-for-structured-rubric-tasks
title: Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines
description: "The review identifies the conditions under which agreement with human grades was strongest: \"when tasks were short, tightly structured, and written in English; when models received detailed rubrics or exemplar answers..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: marcin-jukiewicz-and-michał-wyrwa-2026
    resource: "https://doi.org/10.3390/app16020680"
    title: "Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680"
    author: Marcin Jukiewicz and Michał Wyrwa
---

# Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The review identifies the conditions under which agreement with human grades was strongest: "when tasks were short, tightly structured, and written in English; when models received detailed rubrics or exemplar answers; and when newer versions such as GPT-4 were used through stable API workflows." As tasks became longer, more open-ended, or non-English, accuracy and consistency often declined unless prompts contained rich, explicit criteria and a human remained in the loop. Educators are advised to develop prompt-engineering skill, since the principle "garbage in, garbage out" applies.

## Design Implications

### Context
#### Requirements
- Detailed scoring rubrics or sample correct answers supplied in prompts; prompts tested beforehand for precision.
#### Constraints
- Effectiveness declines for less-represented languages and for tasks requiring contextual understanding or subjective judgment.

### Target Learners
- students in higher education and K-12 settings where routine grading is delegated to LLMs

### Target Learning Goals
- reliable automated scoring of short-answer and structured student work

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)
- [Include an explicit rubric in GenAI feedback prompts, even in Zero-shot conditions](include-explicit-rubric-in-genai-feedback-prompts.md)
- [Engineer LLM grading prompts with detailed, domain-specific evaluation criteria and band descriptors](prompt-llm-grading-with-detailed-band-descriptors.md)
- [Use LLM grading with an instructor's model answer and rubric for formative assessment of writing in large science classes](llm-formative-grading-model-answer-rubric.md)

## Examples
-

## Key Sources
- Marcin Jukiewicz and Michał Wyrwa. (2026). Can ChatGPT Replace the Teacher in Assessment? A Review of Research on the Use of Large Language Models in Grading and Providing Feedback. Appl. Sci. 2026, 16, 680. https://doi.org/10.3390/app16020680
