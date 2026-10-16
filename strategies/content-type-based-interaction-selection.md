---
type: strategy
id: content-type-based-interaction-selection
title: Select interaction types based on content type rather than random variation to preserve format-meaning coherence
description: "To resolve the tension between retrieval-format diversity and extraneous cognitive load, Memdora routes content by type: \"vocabulary items to Language cards, quotable passages to By Heart cards, factual content to Exa..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: ruiyang-zhang-2027
    resource: "https://arxiv.org/abs/2607.25096"
    title: "Ruiyang Zhang. (2027). Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition. Proceedings of ACM International Conference on Intelligent User Interfaces (IUI '27). https://arxiv.org/abs/2607.25096"
    author: Ruiyang Zhang
---

# Select interaction types based on content type rather than random variation to preserve format-meaning coherence

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To resolve the tension between retrieval-format diversity and extraneous cognitive load, Memdora routes content by type: "vocabulary items to Language cards, quotable passages to By Heart cards, factual content to Exam cards". The paper argues variation prevents format-specific learning strategies, but "excessive novelty may increase extraneous cognitive load", so content-type-based selection preserves format-meaning coherence while delivering retrieval format diversity.

## Design Implications

### Context
#### Requirements
- A content-type classification step in the generation pipeline that routes extracted knowledge items to appropriate interaction types
#### Constraints
- Whether interaction diversity improves or impairs learning is stated by the authors as an open design question

### Target Learners
- learners studying mixed content across vocabulary, memorization, and exam domains

### Target Learning Goals
- matching retrieval format to learning goal

## Related Strategies
- 

## Examples
-

## Key Sources
- Ruiyang Zhang. (2027). Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition. Proceedings of ACM International Conference on Intelligent User Interfaces (IUI '27). https://arxiv.org/abs/2607.25096
