---
type: design
id: llm-practice-platform-offloading-classifier
title: Custom LLM practice platform with validated offloading classifier for extent-of-support labeling
description: The article built a custom web platform (React frontend, Python backend, PostgreSQL) giving full experimental control and logging of a fraction-arithmetic learning session with an LLM assistant built on GPT-OSS-120B a...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: sebastian-maier-2026
    resource: "https://arxiv.org/abs/2609.20143"
    title: "Sebastian Maier, Kai Schwabe, Manuel Schneider, and Stefan Feuerriegel. (2026). Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants. arXiv. https://arxiv.org/abs/2609.20143"
    author: Sebastian Maier, Kai Schwabe, Manuel Schneider, and Stefan Feuerriegel
---

# Custom LLM practice platform with validated offloading classifier for extent-of-support labeling

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article built a custom web platform (React frontend, Python backend, PostgreSQL) giving full experimental control and logging of a fraction-arithmetic learning session with an LLM assistant built on GPT-OSS-120B accessed via Amazon Bedrock at temperature 0. A custom LLM-based offloading classifier, combined with a rule-based numerical check, labeled the highest level of support requested per item across four levels: no AI use, guided help, intermediate result, and complete answer. Validation showed that on a held-out set of 198 dialogues "the classifier agreed with the intended labels in every case, yielding no confirmed classification error."

## Design Implications

### Context
#### Requirements
- The system prompt was iteratively validated against a fixed evaluation set of 55 synthetic participant messages until no unrequested solution was given, no requested answer was withheld, and every stated number was correct; the configuration was frozen before data collection.
#### Constraints
- The classifier was developed on 198 synthetic tutoring dialogues and frozen before launch; evaluation is reported only on a separate held-out set of 198 dialogues.

### Target Learners
- Adult online participants practicing fraction arithmetic

### Learning Goals
- Measuring and incentivizing the extent of LLM assistance requested during practice

### Claims
- 

## Related Designs

- [Purpose-built no-code vibe-coding research platform for controlled experimentation](no-code-vibe-coding-research-platform.md)
- [Custom GenAI writing platform with 30-word prompt limit and copy-paste disabled](deepseek-abstract-writing-platform-constrained-prompts.md)

## Examples
-

## Key Sources
- Sebastian Maier, Kai Schwabe, Manuel Schneider, and Stefan Feuerriegel. (2026). Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants. arXiv. https://arxiv.org/abs/2609.20143
