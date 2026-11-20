---
type: design
id: instructor-tuned-gpt35-sql-chatbot
title: Instructor-tuned GPT-3.5 chatbot with course context and guardrails for SQL query writing
description: "A chatbot built on GPT-3.5 configured with a system prompt \"to be particularly helpful for writing the SQL queries and provided the context of the questions used in the study.\" It included guardrails such as being tol..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: kumar-2024
    resource: "https://arxiv.org/abs/2408.08401"
    title: "Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M. (2024). Understanding Help-Seeking Behavior of Students Using LLMs vs. Web Search for Writing SQL Queries. Preprint. https://arxiv.org/abs/2408.08401"
    author: "Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M"
---

# Instructor-tuned GPT-3.5 chatbot with course context and guardrails for SQL query writing

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A chatbot built on GPT-3.5 configured with a system prompt "to be particularly helpful for writing the SQL queries and provided the context of the questions used in the study." It included guardrails such as being told not to give out direct answers and course context describing learning goals and content. It served as a proxy for instructor-provided LLM chatbots in classrooms, analogous to tools like KhanMigo and the CS50 bot.

## Design Implications

### Context
#### Requirements
- System prompt configuration with course context and anti-cheating guardrails
#### Constraints
- Built on GPT-3.5, which was the frontier model at the time of the study

### Target Learners
- third-year undergraduate computing students

### Learning Goals
- writing SQL queries

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M. (2024). Understanding Help-Seeking Behavior of Students Using LLMs vs. Web Search for Writing SQL Queries. Preprint. https://arxiv.org/abs/2408.08401
