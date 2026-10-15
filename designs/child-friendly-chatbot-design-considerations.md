---
type: design
id: child-friendly-chatbot-design-considerations
title: "Three design considerations for a child-friendly educational chatbot: topic focus, age-appropriate context management, and a simple fun interface"
description: "The authors enumerate three design considerations for AMA: \"(1) to encourage engagement by focusing conversation on specific topics; (2) to respond to children in an age-appropriate and on-topic manner (context manage..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: saniya-vahedian-movahed-and-fred-martin-2025
    resource: "https://arxiv.org/abs/2502.14217"
    title: "Saniya Vahedian Movahed and Fred Martin. (2025). Ask Me Anything: Exploring children's attitudes toward an age-tailored AI-powered chatbot. arXiv. https://arxiv.org/abs/2502.14217"
    author: Saniya Vahedian Movahed and Fred Martin
---

# Three design considerations for a child-friendly educational chatbot: topic focus, age-appropriate context management, and a simple fun interface

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors enumerate three design considerations for AMA: "(1) to encourage engagement by focusing conversation on specific topics; (2) to respond to children in an age-appropriate and on-topic manner (context management); and (3) to provide a simple and fun user interface." Topic focus drives targeted questioning and engagement; context management uses age and topic variables in the API prompt; the single-screen interface uses playful images, clear font, and simple layout.

## Design Implications

### Context
#### Requirements
- A prompt template carrying topic and age variables
- Selection of a language model that reliably stays on-topic
#### Constraints
- Prompt instructions alone did not keep gpt-3.5-turbo on-topic; engine choice mattered

### Target Learners
- Elementary and middle school students

### Learning Goals
- Safe, engaging, age-appropriate interaction with conversational AI

### Claims
- [Gpt35 Turbo Off Topic Prompting Insufficient](../claims/gpt35-turbo-off-topic-prompting-insufficient.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Saniya Vahedian Movahed and Fred Martin. (2025). Ask Me Anything: Exploring children's attitudes toward an age-tailored AI-powered chatbot. arXiv. https://arxiv.org/abs/2502.14217
