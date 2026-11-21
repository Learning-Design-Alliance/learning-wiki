---
type: design
id: llm-partial-credit-grading-confidence-workflow
title: LLM-assisted partial-credit grading and feedback workflow with grading confidence index
description: A grading pipeline in which GPT-4o grades student written explanations against a multi-item binary rubric using a prompt template with replaceable components (problem body, rubric, requirements, student response), run...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://www.ucf.edu"
    title: "Zhongzhou Chen and Tong Wan. (2024). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. https://www.ucf.edu"
    author: Zhongzhou Chen and Tong Wan
---

# LLM-assisted partial-credit grading and feedback workflow with grading confidence index

> **Design** · [All designs](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
A grading pipeline in which GPT-4o grades student written explanations against a multi-item binary rubric using a prompt template with replaceable components (problem body, rubric, requirements, student response), runs self-consistency grading five times, computes normalized Shannon entropy across runs as a grading confidence index for human review, and generates student-facing feedback explaining the grading outcome. The article reports "The entire grading and feedback generating process cost roughly $5 per 100 student answers."

## Design Implications

### Context
#### Requirements
- Azure OpenAI deployment of gpt-4o (temperature 0.8)
- A multi-item binary rubric per problem
- Two independent human graders to establish the agreement baseline and flag potentially incorrect machine gradings
#### Constraints
- Grading focused on reasoning processes rather than calculational fluency; math-expression evaluation was left to tools like python or Mathematica
- Responses using alternative correct solution paths (10 students on Question 3) were removed from the research data set

### Target Learners
- university students in introductory Newtonian mechanics courses

### Learning Goals
- partial-credit assessment of written problem-solving explanations
- timely, transparent feedback on grading outcomes

### Claims

- [Entropy Grading Confidence Index](../claims/entropy-grading-confidence-index.md) [+M]
- [Llm Generated Student Facing Feedback Quality](../claims/llm-generated-student-facing-feedback-quality.md) [+M]
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](../claims/rubric-explanation-targeting-machine-errors.md) [+W]
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](../claims/gpt4o-self-consistency-human-level-grading-agreement.md) [+W]
- [GPT-4o significantly outperformed GPT-3.5 on every grading measure under all prompt versions for Question 1, and outperformed it across all conditions for Questions 2 and 3](../claims/gpt4o-outperforms-gpt35-grading.md) [+W]
- [Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT](../claims/gpt4o-chat-mode-detailed-rubric-reliability.md) [~W]

## Related Designs

- [GPT-3.5 Turbo AI grading pipeline with three prompt versions (Naive, Detailed-rubric, Scaffolded COT)](gpt35-turbo-partial-credit-grading-pipeline.md)
- [Scaffolded chain of thought: a prompt structure forcing rubric-grounded reasoning before grading](scaffolded-chain-of-thought-prompting.md)
- [Four-workflow AI-assisted grading pipeline for handwritten exams](four-workflow-ai-grading-pipeline.md)

## Examples
-

## Key Sources
- Zhongzhou Chen and Tong Wan. (2024). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. https://www.ucf.edu
