---
type: strategy
id: unified-physics-benchmarks-for-llm-evaluation
title: Develop unified physics benchmarks and language-specific evaluations for LLMs
description: "The article's forward-looking recommendation for the physics education community: create a unified benchmark, analogous to GLUE and MMLU, for evaluating LLMs on physics tasks, and evaluate whether LLM physics skill de..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: pranav-gupta-2023
    resource: "https://arxiv.org/abs/2312.04613"
    title: "Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. https://arxiv.org/abs/2312.04613"
    author: Pranav Gupta
---

# Develop unified physics benchmarks and language-specific evaluations for LLMs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 design, 1 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article's forward-looking recommendation for the physics education community: create a unified benchmark, analogous to GLUE and MMLU, for evaluating LLMs on physics tasks, and evaluate whether LLM physics skill depends on language. The article states "There is a need in the physics education community to come up with a unified benchmarks such as GLUE (Wang et al., 2018) and MMLU (Hendrycks et al., 2021) for evaluating the capacility of LLMs in solving physics tasks." It also suggests specialized physics-specific metrics rather than n-gram metrics such as BLEU.

## Design Implications

### Context
#### Requirements
- Benchmarks comparable in role to GLUE and MMLU but targeted at physics tasks
#### Constraints
- Many students study physics in languages other than English, implying a need for language-specific evaluations or machine-translation-based evaluations

### Target Learners
- grade school and university physics students
- physics graduate school applicants

### Target Learning Goals
- reliable LLM reasoning about physics concepts
- physics problem solving across languages

## Claims

- [Bard answered 26 of 98 Physics GRE questions correctly, earning a raw score of 8 out of 100 and placing in the bottom 2% of test-takers](../claims/bard-bottom-2-percent-physics-gre.md) [+W]
- [Among questions Bard answered correctly, some correct options were chosen by chance with fabricated explanations, and Bard hallucinated numerical values for variables](../claims/bard-hallucinated-explanations-physics-gre.md) [+W]
- [Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions](../claims/bard-image-upload-failures-two-of-100.md) [+W]
- [Modern SLMs around 3B parameters match or exceed earlier-generation LLMs on the MMLU benchmark, including STEM subjects](../claims/slms-match-legacy-llms-mmlu.md) [+W]

## Related Strategies

- [Future research should use broader question formats, non-English training data, and LLMs beyond ChatGPT](future-research-broader-questions-non-english-llms.md)
- [Three future research directions: education-focused benchmarks, a taxonomy of educational LLM harms, and multi-turn human feedback](three-recommendations-llm-education-research.md)
- [Select AI models for physics tasks by empirical evaluation on the specific domain, not by general benchmarks or price](empirical-domain-evaluation-for-model-selection.md)

## Examples
-

## Key Sources
- Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. https://arxiv.org/abs/2312.04613
