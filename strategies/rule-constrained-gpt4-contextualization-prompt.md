---
type: strategy
id: rule-constrained-gpt4-contextualization-prompt
title: Rule-constrained GPT-4 prompt for interest-based problem contextualization
description: "The authors used a few-shot prompt presenting input-output example pairs (e.g., a line-queue problem contextualized for 'Video Games' and 'basketball', a bulb-inspection problem for 'World of Warcraft') followed by ex..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: gautam-yadav-2023
    resource: "https://arxiv.org/abs/2306.00190"
    title: "Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni. (2023). Contextualizing Problems to Student Interests at Scale in Intelligent Tutoring System Using Large Language Models. CEUR Workshop Proceedings. https://arxiv.org/abs/2306.00190"
    author: Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni
---

# Rule-constrained GPT-4 prompt for interest-based problem contextualization

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors used a few-shot prompt presenting input-output example pairs (e.g., a line-queue problem contextualized for 'Video Games' and 'basketball', a bulb-inspection problem for 'World of Warcraft') followed by explicit rules: "don't change values", deeper rather than surface contextualization, and that the "output question should ask same thing as input question" without adding unnecessary details. Rules were gradually refined and added based on testing until outputs accommodated novel interests such as TikTok and NBA.

## Design Implications

### Context
#### Requirements
- A few-shot prompt with worked input-output examples across a range of contexts and interests, plus explicit preservation rules, refined iteratively based on testing
#### Constraints
- Rules were tuned over four problem sets in TutorShop; the article notes the approach needs help with geometric problems involving graphs, tables, or diagrammatic components

### Target Learners
- algebra students using intelligent tutoring systems

### Target Learning Goals
- maintain problem difficulty and original intent while personalizing context to student interests

## Claims

- [The GPT-4 contextualization system fails on geometry problems involving graphs, tables, or diagrammatic components](../claims/gpt4-contextualization-geometry-visual-limitation.md) [-W]
- [Iterative prompt engineering of GPT-4 achieved meaningful contextualization of algebra problems that preserved difficulty and original intent](../claims/gpt4-prompt-engineering-contextualization-preserves-intent.md) [+W]
- [Prior research found context personalization to student interests associated with improved engagement, performance, and learning outcomes in algebra](../claims/walkington-interest-contextualization-engagement-performance.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gautam Yadav, Ying-Jui Tseng and Xiaolin Ni. (2023). Contextualizing Problems to Student Interests at Scale in Intelligent Tutoring System Using Large Language Models. CEUR Workshop Proceedings. https://arxiv.org/abs/2306.00190
