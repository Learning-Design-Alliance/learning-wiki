---
type: strategy
id: llm-data-leakage-restriction-strategy
title: Restrict corpus use with LLMs to locally-stored or non-retaining commercial models to prevent data leakage
description: The authors ask corpus users to consider data leakage, whereby NLP/SLP datasets enter LLM training data via commercial APIs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: kate-knill-2024
    resource: "https://arxiv.org/abs/2412.11986"
    title: "Kate Knill, Diane Nicholls, Mark J.F. Gales, Mengjie Qian, Pawel Stroinski. (2024). Speak & Improve Corpus 2025: an L2 English Speech Corpus for Language Assessment and Feedback. https://arxiv.org/abs/2412.11986"
    author: Kate Knill, Diane Nicholls, Mark J.F. Gales, Mengjie Qian, Pawel Stroinski
---

# Restrict corpus use with LLMs to locally-stored or non-retaining commercial models to prevent data leakage

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors ask corpus users to consider data leakage, whereby NLP/SLP datasets enter LLM training data via commercial APIs. They "ask that the Corpus is only passed to locally-stored LLMs" such as models from the Hugging Face Transformers library, or to commercial LLMs in a way that the data is not retained for training. This is an implementable data-governance recipe for releasing educational language datasets.

## Design Implications

### Context
#### Requirements
- Users must either use locally-stored LLMs or ensure commercial LLM providers do not retain the data for model training
#### Constraints
- 

### Target Learners
- Researchers using the corpus for language assessment and feedback research

### Target Learning Goals
- Preserving corpus integrity for evaluation in language learning technology research

## Claims

- [Data contamination and single-dataset limitations restrict generalizability of LLM benchmarking results on dental specialization exams](../claims/llm-dental-benchmark-data-contamination-limitation.md) [+W]
- [Privacy protection in the framework is partial: three residual leakage channels remain open](../claims/partial-privacy-three-residual-leakage-channels.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Kate Knill, Diane Nicholls, Mark J.F. Gales, Mengjie Qian, Pawel Stroinski. (2024). Speak & Improve Corpus 2025: an L2 English Speech Corpus for Language Assessment and Feedback. https://arxiv.org/abs/2412.11986
