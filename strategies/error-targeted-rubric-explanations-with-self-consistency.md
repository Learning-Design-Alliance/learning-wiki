---
type: strategy
id: error-targeted-rubric-explanations-with-self-consistency
title: Improve LLM partial-credit grading by adding error-targeting explanations to rubric items and taking the mode of five grading runs
description: "The article identifies two methods as essential for reaching human-level machine grading accuracy: \"Adding explanation language to each rubric item that targets the errors of initial machine grading\" and \"Running the..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://arxiv.org/abs/2412.06910"
    title: "Zhongzhou Chen and Tong Wan. (2024). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. https://arxiv.org/abs/2412.06910"
    author: Zhongzhou Chen and Tong Wan
---

# Improve LLM partial-credit grading by adding error-targeting explanations to rubric items and taking the mode of five grading runs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article identifies two methods as essential for reaching human-level machine grading accuracy: "Adding explanation language to each rubric item that targets the errors of initial machine grading" and "Running the grading process five times and taking the most frequent outcome." Instructors first inspect initial machine gradings, expand rubric items to cover the observed error patterns, then repeat grading and use the modal binary vector as the outcome.

## Design Implications

### Context
#### Requirements
- A multi-item rubric with binary (1/0) scoring for each item
- An initial grading pass whose errors can be examined to write the rubric explanations
- Capacity to run the same grading prompt five times
#### Constraints
- Few-shot examples and standard reference answers were deliberately omitted; the article cites prior work suggesting reference answers can harm grading of complex multi-step problems

### Target Learners
- university students in introductory physics courses

### Target Learning Goals
- assessing students' written reasoning of multi-step problem-solving processes

## Claims

- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](../claims/rubric-explanation-targeting-machine-errors.md) [+W]
- [Self-consistency mode scores outperform individual grading runs for all three problems](../claims/self-consistency-mode-beats-individual-runs.md) [+W]
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](../claims/gpt4o-self-consistency-human-level-grading-agreement.md) [+W]
- [Normalized Shannon entropy across five grading runs serves as a confidence index: a 0.4 threshold flags ~40% of potentially incorrect gradings via review of 10-15% of responses](../claims/entropy-grading-confidence-index.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zhongzhou Chen and Tong Wan. (2024). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. https://arxiv.org/abs/2412.06910
