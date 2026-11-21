---
type: strategy
id: genai-lab-design-execution-validation-strategy
title: "Lab design strategy: fine-tune on the same lecture reference material, prompt with the lecture topic, and validate solutions by execution"
description: A strategy for generating lab tasks that augment lecture topics, shown in Figure 2.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: aakanksha-sharma-2025
    resource: "https://arxiv.org/abs/2503.00081"
    title: "Aakanksha Sharma, Samar Shailendra, and Rajan Kadel. (2025). Experiences with Content Development and Assessment Design in the Era of GenAI. Pre-print version of the paper accepted in CSEE 2025. https://arxiv.org/abs/2503.00081"
    author: Aakanksha Sharma, Samar Shailendra, and Rajan Kadel
---

# Lab design strategy: fine-tune on the same lecture reference material, prompt with the lecture topic, and validate solutions by execution

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
A strategy for generating lab tasks that augment lecture topics, shown in Figure 2. The same reference material used for lecture content trains the model to maximise lecture-lab correlation, and the model is prompted with the corresponding lecture topic to generate a lab problem and its solution. The article states: "The expert should validate that the solution generated is getting executed correctly on the real system as well."

## Design Implications

### Context
#### Requirements
- Reference material shared with lecture design
- Lecture topic supplied in the prompt to align lab with lecture
- Execution-based validation of the generated solution on the real system
#### Constraints
- 

### Target Learners
- Higher education students in lab-based subjects

### Target Learning Goals
- Lab tasks and solutions aligned with lecture topics and learning objectives

## Claims

- [GenAI content generation requires iterative refinement, accurate training material, and pre-processing of image-heavy reference data](../claims/genai-content-generation-iterative-refinement-accuracy.md) [+W]
- [In the authors' experience, content generated with good prompts is more detailed and topic-aligned than content generated with bad prompts](../claims/good-prompts-yield-detailed-aligned-genai-content.md) [+W]
- [Fine-tuning an LLM on expert (task, solution) data significantly improves its student synthesis performance, including capturing the student's behavior](../claims/finetuning-improves-llm-ss-student-synthesis.md) [+M]

## Related Strategies

- [Assignment design strategy using ULOs, qualification level and Bloom's Taxonomy action verbs, with expert examination and refinement rather than regeneration](genai-assignment-design-blooms-refinement-strategy.md)

## Examples
-

## Key Sources
- Aakanksha Sharma, Samar Shailendra, and Rajan Kadel. (2025). Experiences with Content Development and Assessment Design in the Era of GenAI. Pre-print version of the paper accepted in CSEE 2025. https://arxiv.org/abs/2503.00081
