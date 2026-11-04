---
type: strategy
id: standardized-single-query-llm-evaluation-protocol
title: Query each LLM once per question in a new conversation thread with a standardized prompt template
description: "The article used a standardized protocol in which \"A new conversation thread was initiated for each query to prevent cross-contamination of responses\" and a fixed prompt template asking models to \"Please identify all..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: stefan-andrei-2026
    resource: "https://doi.org/10.2196/95859"
    title: "Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859"
    author: Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie
---

# Query each LLM once per question in a new conversation thread with a standardized prompt template

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article used a standardized protocol in which "A new conversation thread was initiated for each query to prevent cross-contamination of responses" and a fixed prompt template asking models to "Please identify all correct answers and explain your reasoning." This single-query design was chosen to reflect typical real-world use patterns where students query an LLM once per question. The approach ensures comparability across models but the authors note it may not reflect optimal performance achievable through advanced prompting techniques.

## Design Implications

### Context
#### Requirements
- A new conversation thread for each query to prevent cross-contamination
- A consistent prompt format maintained across all queries
#### Constraints
- Standardized prompting may not reflect optimal performance achievable through chain-of-thought prompting, few-shot learning, or retrieval-augmented generation
- No test-retest reliability assessment was performed to evaluate response consistency

### Target Learners
- medical education researchers
- anesthesiology educators

### Target Learning Goals
- comparative evaluation of LLM performance on examination questions
- reproducible assessment of AI-generated responses

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)

## Examples
-

## Key Sources
- Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859
