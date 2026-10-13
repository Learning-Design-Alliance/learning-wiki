---
type: strategy
id: demographic-psychometric-response-profiles
title: Vary LLM response profiles via demographic and psychometric prompting to increase response variability
description: "To counter the tendency of LLMs to give similar answers to the same item, CPIG prompts item-response generators with a baseline, a demographic profile (e.g., \"You are a Hispanic woman who works in real estate\"), or a..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://arxiv.org/abs/2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
---

# Vary LLM response profiles via demographic and psychometric prompting to increase response variability

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
To counter the tendency of LLMs to give similar answers to the same item, CPIG prompts item-response generators with a baseline, a demographic profile (e.g., "You are a Hispanic woman who works in real estate"), or a psychometric profile drawn from validated scales such as creative self-efficacy, creativity anxiety, creative mindset, openness to experience, tolerance for ambiguity, cynicism, and the RIASEC interest types. Participant profiles were sampled at random for each response, with names drawn from census data. This strategy is implementable whenever synthetic respondent variability is needed.

## Design Implications

### Context
#### Requirements
- A pool of participant creativity profiles based on responses to prior creativity studies, including differing occupations and psychometric assessment responses
#### Constraints
- The article reports that even with these strategies, the prompted distributions still have lower variance than humans and much higher peaks in originality scores

### Target Learners
- LLM test takers simulating human respondents

### Target Learning Goals
- eliciting varied, human-like creative responses to test items

### Affordances
- [Cpig Framework](../research-methods/cpig-the-creative-psychometric-item-generator-framework.md)

## Claims

- [Demographic and psychometric response prompting produces higher-variance, heavier-tailed originality distributions than a no-context baseline, though still less variable than humans](../claims/response-prompting-styles-increase-variance.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202
