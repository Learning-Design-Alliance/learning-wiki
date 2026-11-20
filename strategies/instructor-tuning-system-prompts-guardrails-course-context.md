---
type: strategy
id: instructor-tuning-system-prompts-guardrails-course-context
title: Low-cost instructor tuning of LLM chatbots via system prompts with guardrails and course context
description: "The article describes configuring an off-the-shelf LLM (GPT-3.5) with a system prompt providing course context and guardrails, such as \"being told not to give out direct answers\" and \"a description of the learning goa..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: kumar-2024
    resource: "https://arxiv.org/abs/2408.08401"
    title: "Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M. (2024). Understanding Help-Seeking Behavior of Students Using LLMs vs. Web Search for Writing SQL Queries. Preprint. https://arxiv.org/abs/2408.08401"
    author: "Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M"
---

# Low-cost instructor tuning of LLM chatbots via system prompts with guardrails and course context

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article describes configuring an off-the-shelf LLM (GPT-3.5) with a system prompt providing course context and guardrails, such as "being told not to give out direct answers" and "a description of the learning goals and content covered by the course." This low-cost tuning method can be employed by instructors to enhance student engagement without degrading task performance or increasing mental demand. The tuned chatbot acts as a proxy for instructor-provided LLM chatbots used in classrooms.

## Design Implications

### Context
#### Requirements
- Access to an off-the-shelf LLM chatbot configurable via system prompts
#### Constraints
- Effectiveness depends on model accuracy and students' ability to ask the right questions through prompts

### Target Learners
- undergraduate computing students

### Target Learning Goals
- writing SQL queries
- self-regulated learning in programming education

## Claims

- [Increased engagement with instructor-tuned LLM did not increase reported mental demand or reduce query quality](../claims/increased-engagement-without-increased-mental-demand.md) [+W]
- [Students interacted significantly more with an instructor-tuned LLM than with ChatGPT or web search when writing SQL queries](../claims/instructor-tuned-llm-more-interactions-than-chatgpt-web-search.md) [+W]
- [No significant differences in the number of edits made to the final SQL query across conditions](../claims/no-significant-edit-count-difference-across-conditions.md) [+W]
- [Self-reported mental demand did not differ significantly across conditions, with suggestive evidence of lower demand for the instructor-tuned LLM](../claims/no-significant-mental-demand-difference-suggestive-lower-tuned-llm.md) [+W]
- [No significant differences in final SQL query quality across web search, ChatGPT, and instructor-tuned LLM conditions](../claims/no-significant-query-quality-difference-llm-conditions.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Kumar, H., Reza, M., Mitchell, J., Musabirov, I., Zhang, L., & Liut, M. (2024). Understanding Help-Seeking Behavior of Students Using LLMs vs. Web Search for Writing SQL Queries. Preprint. https://arxiv.org/abs/2408.08401
