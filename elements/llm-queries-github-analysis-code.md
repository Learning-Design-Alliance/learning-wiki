---
type: element
id: llm-queries-github-analysis-code
title: LLM-queries GitHub repository for LLM essay-coding analysis pipeline
description: The authors released the code for their LLM prompting and analysis pipeline, which processed anonymized student paper PDFs into text files, applied each prompt to each LLM via OpenRouter.ai with unified API-level cont...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: keith-2026
    resource: "https://github.com/imrryr/LLM-queries"
    title: "Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries"
    author: Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean
---

# LLM-queries GitHub repository for LLM essay-coding analysis pipeline

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The authors released the code for their LLM prompting and analysis pipeline, which processed anonymized student paper PDFs into text files, applied each prompt to each LLM via OpenRouter.ai with unified API-level control and temperature 0, merged LLM ratings with human ratings, and computed correlation, absolute error, and normalized signed bias measures. The article states: "The code is available at https://github.com/imrryr/LLM-queries". It supports replication of the 60,060-prompt study design.

## Design Implications

### Context
#### Requirements
- Access to the tested closed-source LLMs via an API gateway such as OpenRouter.ai
#### Constraints
- Small response variability may be introduced by sources other than temperature, as the authors note in their limitations

### Target Learners
- education researchers
- learning analytics practitioners

### Target Learning Goals
- replicating or extending human-AI coding comparison studies

## Claims

- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](../claims/coding-dimension-listing-easier-than-correct-defining.md) [+M]
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](../claims/llm-choice-affects-human-ai-coding-correspondence.md) [+M]
- [Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing](../claims/prompt-dimension-interaction-error-rates.md) [+W]
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](../claims/prompt-type-minimal-impact-llm-coding.md) [+W]
- [LLMs align better with human coding on concise theories with discrete concepts than on more complex ones](../claims/theory-complexity-affects-llm-coding-agreement.md) [+M]

## Related Elements

- [OSF repository of prompts, codebooks, and code for LLM-assisted codebook development](osf-gpt-codebook-replication-artifact.md)

## Examples
-

## Key Sources
- Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries
