---
type: strategy
id: llm-mcq-generation-prompt-template
title: Use an iteratively crafted system prompt requiring one correct answer, three plausible distractors, no giveaway clues, parallel options, and mixed cognitive levels
description: "An iteratively crafted system prompt casts the LLM as 'an expert college course instructor teaching data science programing and cloud computing' tasked to 'create high-quality, pedagogically sound multiple choice ques..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: an-2025
    resource: "https://arxiv.org/abs/2507.05629"
    title: "An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. https://arxiv.org/abs/2507.05629"
    author: An, Y., Liu, J., Acharya, N., and Hashmi, R
---

# Use an iteratively crafted system prompt requiring one correct answer, three plausible distractors, no giveaway clues, parallel options, and mixed cognitive levels

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (1 causal, 1 review, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
An iteratively crafted system prompt casts the LLM as 'an expert college course instructor teaching data science programing and cloud computing' tasked to 'create high-quality, pedagogically sound multiple choice questions (MCQs) based on the course content provided below'. It mandates one correct answer with three plausible distractors, no giveaway clues in the stem, grammatically parallel options, mixed cognitive levels, and at least 15 MCQs per generation.

## Design Implications

### Context
#### Requirements
- Course content converted to markdown text with relevant sections injected into the AI prompts
#### Constraints
- Generated MCQs still undergo human quality-assurance checks before release

### Target Learners
- college data science instructors

### Target Learning Goals
- generating pedagogically sound retrieval practice MCQs

## Claims

- [About two-thirds of LLM-generated MCQs did not meet the authors' quality objectives, so at least 15 had to be generated to select 5 usable questions](../claims/two-thirds-llm-mcqs-fail-quality-checks.md) [~W]
- [Most LLM-generated MCQs from video transcripts met established quality criteria, with 84.05% rated clear, 86.38% containing plausible distractors, and 93.39% directly answerable](../claims/llm-mcq-video-quality-ratings-majority-clear.md) [+W]
- [Distractor similarity to the correct answer increases MCQ complexity](../claims/distractor-similarity-increases-complexity.md) [+W]

## Related Strategies

- [Craft educational LLM prompts using iterative refinement, role-playing, and constraints with suitable context](three-pillar-educational-prompting-strategy.md)
- [Use detailed, structured prompts specifying question type, case details, distractors, explanation, source, and difficulty level](structured-nine-component-mcq-prompt.md)
- [Subject AI-generated items to trained human expert review, including a technical review and difficulty refinement](human-expert-review-of-ai-mcqs.md)

## Examples
-

## Key Sources
- An, Y., Liu, J., Acharya, N., and Hashmi, R. (2025). Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses. arXiv:2507.05629v2 [cs.AI]. https://arxiv.org/abs/2507.05629
