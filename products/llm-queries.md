---
type: product
id: llm-queries
title: LLM-queries
description: A GitHub repository released by Keith et al.
product_kind: software
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: keith-2026
    resource: "https://github.com/imrryr/LLM-queries"
    title: "Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries"
    author: Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean
---

# LLM-queries

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A GitHub repository released by Keith et al. containing the code for prompting multiple large language models, processing student essay text, merging model and human ratings, and computing agreement and bias measures.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **LLM-queries GitHub repository for LLM essay-coding analysis pipeline**: The authors released the code for their LLM prompting and analysis pipeline, which processed anonymized student paper PDFs into text files, applied each prompt to each LLM via OpenRouter.ai with unified API-level control and temperature 0, merged LLM ratings with human ratings, and computed correlation, absolute error, and normalized signed bias measures. The article states: "The code is available at https://github.com/imrryr/LLM-queries". It supports replication of the 60,060-prompt study design. (Keith et al. (2026))

### Claims

- [Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2](../claims/claude-erratic-few-shot-performance-across-items.md) [~W]

## Related Products and Programmes

- [GenAICanHarmLearning anonymized dataset and code repository](genaicanharmlearning-anonymized-dataset-and-code-repository.md)
- [LT_NLP_SET_pub](lt-nlp-set-pub.md)

## Key Sources
- Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries

<!-- merged 2026-10-10 from elements/llm-queries-github-analysis-code ("LLM-queries GitHub repository for LLM essay-coding analysis pipeline"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Elements

- [OSF repository of prompts, codebooks, and code for LLM-assisted codebook development](osf-repository.md)

## Examples
-

## Key Sources
- Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries
-->
