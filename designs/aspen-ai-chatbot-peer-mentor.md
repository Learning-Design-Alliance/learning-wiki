---
type: design
id: aspen-ai-chatbot-peer-mentor
title: "Aspen: a prompt-engineered AI chatbot peer mentor for inquiry revision"
description: Aspen is a custom AI chatbot built as a prompt-engineered pedagogical agent on a general-purpose GPT model, not a fine-tuned model, with behavior shaped through system-level instructions, response-format constraints,...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: kilinc-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100683"
    title: "Kilinc, S., Aldemir, T., Misiejuk, K., Kaliisa, R., Sabanwar, V., Bicer, A., Song, D., & Yalvac, B. (2026). A mixed-methods analysis of AI scaffolding patterns and student inquiry profiles in a middle-school agriculture-STEM classroom. Computers and Education: Artificial Intelligence, 11, 100683. https://doi.org/10.1016/j.caeai.2026.100683"
    author: "Kilinc, S., Aldemir, T., Misiejuk, K., Kaliisa, R., Sabanwar, V., Bicer, A., Song, D., & Yalvac, B"
---

# Aspen: a prompt-engineered AI chatbot peer mentor for inquiry revision

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Aspen is a custom AI chatbot built as a prompt-engineered pedagogical agent on a general-purpose GPT model, not a fine-tuned model, with behavior shaped through system-level instructions, response-format constraints, task-specific scaffolds, and iterative testing. It was positioned as "a peer mentor for middle school agricultural research teams," using brief, friendly, task-relevant language and prioritizing questions, hints, feedback, and explanations over unrestricted answer provision. The web-based interface (Flutter Web) included a text chat window and animated 3-D avatar, with interactions logged in Firebase Realtime Database.

## Design Implications

### Context
#### Requirements
- Task-specific grounding, iterative testing, and prompt constraints to reduce risks of hallucinated or instructionally misaligned content and answer-oriented interaction
#### Constraints
- Because Aspen relied on a general-purpose model, its responses remained subject to variability, occasional hallucination, and imperfect alignment with domain-specific instructional goals; safeguards are design measures, not independent verification of response quality

### Target Learners
- eighth-grade students in a rural agriculture-STEM classroom

### Learning Goals
- revising research questions and hypotheses against inquiry criteria

### Claims
- 

## Related Designs

- [Jordan Chatbot: a unit-specific GPT-4o pedagogical support agent grounded in constructivist and socio-cultural learning theory](jordan-chatbot-unit-specific-gpt4o-agent.md)
- [Seven unit-specific custom GPT chatbots for pharmaceutical science units](seven-co-created-cgpt-chatbots-pharmaceutical-science.md)

## Examples
-

## Key Sources
- Kilinc, S., Aldemir, T., Misiejuk, K., Kaliisa, R., Sabanwar, V., Bicer, A., Song, D., & Yalvac, B. (2026). A mixed-methods analysis of AI scaffolding patterns and student inquiry profiles in a middle-school agriculture-STEM classroom. Computers and Education: Artificial Intelligence, 11, 100683. https://doi.org/10.1016/j.caeai.2026.100683
