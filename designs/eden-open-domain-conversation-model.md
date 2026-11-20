---
type: design
id: eden-open-domain-conversation-model
title: Open-domain chit-chat conversation model for EDEN
description: "EDEN's conversation model is a fine-tuned Llama-2 model \"capable of discussing various topics to accommodate user interest\", built to engage interest-oriented learners in social chit-chat and reduce language anxiety."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: li-siyan-2024
    resource: "https://arxiv.org/abs/2406.17982"
    title: "Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg. (2024). EDEN: Empathetic Dialogues for English learning. arXiv:2406.17982v2 [cs.CL]. https://arxiv.org/abs/2406.17982"
    author: Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg
---

# Open-domain chit-chat conversation model for EDEN

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
EDEN's conversation model is a fine-tuned Llama-2 model "capable of discussing various topics to accommodate user interest", built to engage interest-oriented learners in social chit-chat and reduce language anxiety. Training data were synthesized by adapting a persona-based pipeline: ChatGPT generated 10 two-party conversations per topic across 243 topics in seven broad areas; after filtering, 1,227 conversations remain with an average length of 8.35 turns.

## Design Implications

### Context
#### Requirements
- Training data synthesized via persona-based ChatGPT prompting with one generic persona and one persona whose first language is not English
#### Constraints
- GPT-4o was rejected as the conversation engine because it can be too slow for chit-chat and is not widely accessible in China
- A Chinese college student persona produced problematically low generation diversity and was replaced

### Target Learners
- Native Mandarin speakers learning English out of interest

### Learning Goals
- Open-domain spoken English conversation practice
- Reduced language anxiety

### Claims
- 

## Related Designs
- Eden Empathetic English Chatbot

## Examples
-

## Key Sources
- Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg. (2024). EDEN: Empathetic Dialogues for English learning. arXiv:2406.17982v2 [cs.CL]. https://arxiv.org/abs/2406.17982
