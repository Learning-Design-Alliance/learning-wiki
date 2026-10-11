---
type: design
id: cpig-multi-stage-prompting-quality-filters
title: Multi-stage prompting with rule-based quality filters for LLM item generation
description: "CPIG's item generation follows a multi-stage prompting pattern: a first LLM produces word lists (three names, a place, and an action) that item-generator LLMs must incorporate, which the authors say helps \"maximize di..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://arxiv.org/abs/2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
---

# Multi-stage prompting with rule-based quality filters for LLM item generation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CPIG's item generation follows a multi-stage prompting pattern: a first LLM produces word lists (three names, a place, and an action) that item-generator LLMs must incorporate, which the authors say helps "maximize diversity in scenario content by using different word lists to ensure no two item generation prompts are the same." Generated scenarios then pass rule-based validity filters: a Flesch reading-ease floor of 45 with a 140-token minimum, a string blacklist targeting priming (e.g., scenarios containing "on the one hand" or "is torn between"), and a required termination string. The pattern is meant to reduce, not replace, human expert review of items.

## Design Implications

### Context
#### Requirements
- Human experts make the final decision on which items to include in a creativity assessment; the filters only eliminate items unlikely to be valid
#### Constraints
- The authors do not claim the priming string list is comprehensive, stating only that it eliminated most priming in generated scenarios

### Target Learners
- human test takers of creativity assessments

### Learning Goals
- generating valid, diverse creative problem-solving test items

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202
