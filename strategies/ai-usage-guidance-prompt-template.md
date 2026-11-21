---
type: strategy
id: ai-usage-guidance-prompt-template
title: Provide an optional AI-usage prompt template that requests step-by-step method guidance instead of finished code
description: "The materials include an optional AI-usage prompt template telling the model \"Please do not give me finished source code\" and instead asking step-by-step method questions about requirements, inputs and outputs, data s..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: christina-maria-mayr-2026
    resource: "https://arxiv.org/abs/2604.06331"
    title: "Christina Maria Mayr. (2026). Knowledge Markers: An AI-Agnostic Concept for the Design of Programming Courses. https://arxiv.org/abs/2604.06331"
    author: Christina Maria Mayr
---

# Provide an optional AI-usage prompt template that requests step-by-step method guidance instead of finished code

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The materials include an optional AI-usage prompt template telling the model "Please do not give me finished source code" and instead asking step-by-step method questions about requirements, inputs and outputs, data structures, libraries, and testing. The intended stance is AI as a learning coach: "students decide whether and how to use AI", while the guidance encourages explanation and systematic verification rather than solution outsourcing.

## Design Implications

### Context
#### Requirements
- Guidance must preserve student agency: students decide whether and how to use AI.
#### Constraints
- Students may use general-purpose LLM tools with or without explicit allowance, so the guidance is optional rather than enforced.

### Target Learners
- first-semester programming students in a non-computer-science programme

### Target Learning Goals
- explanation and systematic verification of AI outputs rather than solution outsourcing

### Affordances
- [Asp Knowledge Marker Framework](../designs/asp-knowledge-marker-framework.md)

## Related Strategies

- [Replace complete AI-generated solutions with active-learning scaffolding when students request help during programming practice](active-scaffolding-instead-of-llm-complete-solutions.md)
- [Provide sample keywords and prompt guidance so students ask short, simple questions to the AI tool](sample-keywords-short-simple-prompts-strategy.md)
- [Query each LLM once per question in a new conversation thread with a standardized prompt template](standardized-single-query-llm-evaluation-protocol.md)

## Examples
-

## Key Sources
- Christina Maria Mayr. (2026). Knowledge Markers: An AI-Agnostic Concept for the Design of Programming Courses. https://arxiv.org/abs/2604.06331
