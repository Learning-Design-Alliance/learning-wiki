---
type: strategy
id: frame-llm-as-instructor-predicting-student-response
title: "Frame the LLM as an instructor predicting a student's response rather than as the learner itself"
description: "This prompting strategy instructs the LLM to take the teacher's perspective and predict how a student would respond, instead of role-playing the learner directly."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: luis-marquez-carpintero-2025
    resource: "https://arxiv.org/abs/2511.06078"
    title: "Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078"
    author: Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla
---

# Frame the LLM as an instructor predicting a student's response rather than as the learner itself

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
This prompting strategy instructs the LLM to take the teacher's perspective and predict how a student would respond, instead of role-playing the learner directly. The review reports that "A widely adopted approach frames the LLM not as the learner but as an instructor that predicts a student's response" and that this stance yields predictions aligning more closely with actual student profiles. Prompts embed illustrative examples of both mastered and misunderstood rules, with correct answers for mastered rules and incorrect answers for confused rules to simulate misconceptions. The framing helps constrain the model's knowledge to the Simulated Student's profile and avoid leakage of expert knowledge.

## Design Implications

### Context
#### Requirements
- A structured prompt template with a task description, a detailed student profile listing known, confused, and unknown rules, and the question to be answered
#### Constraints
- The review notes that simulation fidelity depends on well-crafted prompts that guide the model to use its pre-trained knowledge and supplied context

### Target Learners
- virtual simulated students in intelligent tutoring system evaluation and question quality assessment

### Target Learning Goals
- generating realistic simulated student responses at varied proficiency levels for evaluating questions and tutoring strategies

## Related Strategies

- [Perspective Taking Prompts](perspective-taking-prompts.md)

## Examples
-

## Key Sources
- Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078
