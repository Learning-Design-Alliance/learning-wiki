---
type: design
id: genai-subject-content-design-finetuning-prompting
title: GenAI-assisted subject content design combining custom-data fine-tuning with staged role- and task-based prompting
description: The article describes a two-approach method for adapting general-purpose LLMs to educational content generation.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: aakanksha-sharma-2025
    title: Aakanksha Sharma, Samar Shailendra, and Rajan Kadel. (2025). Experiences with Content Development and Assessment Design in the Era of GenAI. Pre-print version of the paper accepted in CSEE 2025.
    author: Aakanksha Sharma, Samar Shailendra, and Rajan Kadel
---

# GenAI-assisted subject content design combining custom-data fine-tuning with staged role- and task-based prompting

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a two-approach method for adapting general-purpose LLMs to educational content generation. Custom Data Fine-Tuning ensures responses draw on the educator's own reference material, while Prompt-based Fine-Tuning first has the model assume a role and then follow task instructions. The authors state: "In this paper, we have used a combination of these strategies to fine-tune our model for the particular task."

## Design Implications

### Context
#### Requirements
- Access to custom reference material for the course and APIs provided by the LLM provider for fine-tuning
- Two prompting stages: role-assumption prompts followed by instructional task prompts
#### Constraints
- General-purpose pre-trained LLMs "lose the rigour for special purpose scenarios and only achieve limited precision"

### Target Learners
- Higher education students

### Learning Goals
- Subject content development (lectures, labs, assessments) aligned with unit learning outcomes

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Aakanksha Sharma, Samar Shailendra, and Rajan Kadel. (2025). Experiences with Content Development and Assessment Design in the Era of GenAI. Pre-print version of the paper accepted in CSEE 2025.
