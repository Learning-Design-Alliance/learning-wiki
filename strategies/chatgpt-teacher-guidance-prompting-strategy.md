---
type: strategy
id: chatgpt-teacher-guidance-prompting-strategy
title: Configure ChatGPT prompts to act as a teacher who guides students toward correct answers without revealing them
description: "In this study, feedback prompts instructed ChatGPT to compare the student's answer with the correct answer and, for incorrect or incomplete responses, guide students toward the correct answer without providing informa..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: atakan-coban-2024
    resource: "https://arxiv.org/abs/2411.00849"
    title: "Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer. (2024). AI Support Meets AR Visualization for Alice and Bob: Personalized Learning Based on Individual ChatGPT Feedback in an AR Quantum Cryptography Experiment for Physics Lab Courses. https://arxiv.org/abs/2411.00849"
    author: "Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer"
---

# Configure ChatGPT prompts to act as a teacher who guides students toward correct answers without revealing them

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 3 claims rest on one study

## Description
In this study, feedback prompts instructed ChatGPT to compare the student's answer with the correct answer and, for incorrect or incomplete responses, guide students toward the correct answer without providing information about it, telling students to proceed once their answer was considered correct. The article stresses that "ChatGPT was not used to provide information but rather as a tool to guide students towards discovering information", positioning the model as a virtual group partner that fosters discussion of missing points.

## Design Implications

### Context
#### Requirements
- the correct answer must be embedded in the prompt for comparison
- speech-to-text and text-to-speech channels for verbal interaction
#### Constraints
- the article notes prompts whose answer content was not clearly structured led ChatGPT to accept incomplete answers

### Target Learners
- university students in physics laboratory courses

### Target Learning Goals
- improving accuracy of answers to conceptual and procedural comprehension questions during experimentation

## Claims

- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](../claims/gpt4-feedback-66-percent-targeted-35-percent-flawed.md) [~W]
- [ChatGPT feedback significantly improved university students' answer scores in an AR quantum cryptography lab experiment, with a large effect](../claims/chatgpt-feedback-improves-ar-quantum-crypto-lab-scores.md) [+W]
- [Score improvements with ChatGPT feedback varied by question, reaching significance on Q2, Q3 and Q4 but not Q1](../claims/feedback-score-gains-vary-by-question.md) [+W]

## Related Strategies

- [Questioning Techniques to Address Errors](questioning_techniques_to_address_errors.md)
- [Structure chatbot teacher-training activities as find a right and a wrong answer, guide improvement with questions, then reflect](chatgpt-socratic-activity-three-task-structure.md)

## Examples
-

## Key Sources
- Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer. (2024). AI Support Meets AR Visualization for Alice and Bob: Personalized Learning Based on Individual ChatGPT Feedback in an AR Quantum Cryptography Experiment for Physics Lab Courses. https://arxiv.org/abs/2411.00849
