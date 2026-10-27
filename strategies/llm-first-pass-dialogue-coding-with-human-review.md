---
type: strategy
id: llm-first-pass-dialogue-coding-with-human-review
title: Use customised LLM coding as a scalable first-pass for classroom dialogue analysis, with human review of low-reliability codes
description: "The article supports using a customised GPT-4 system to streamline qualitative dialogue coding where manual coding is labour-intensive, noting \"significant time savings and high coding consistency between the model an..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: long-2024
    resource: "https://doi.org/10.1038/s41539-024-00273-3"
    title: "Long, Y., Luo, H. & Zhang, Y. (2024). Evaluating large language models in analysing classroom dialogue. npj Science of Learning 9:60. https://doi.org/10.1038/s41539-024-00273-3"
    author: "Long, Y., Luo, H. & Zhang, Y"
---

# Use customised LLM coding as a scalable first-pass for classroom dialogue analysis, with human review of low-reliability codes

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article supports using a customised GPT-4 system to streamline qualitative dialogue coding where manual coding is labour-intensive, noting "significant time savings and high coding consistency between the model and human coders, with minor discrepancies". Because Kappa was weak for co-ordination-related codes, deployment should pair automated coding with human checking of the codes where AI diverges, and refinement of AI coding algorithms for alignment.

## Design Implications

### Context
#### Requirements
- A pre-defined, expert-validated coding scheme supplied to the model via retrieval-augmented generation
#### Constraints
- Generalisability is limited: the article states the "sample size and scope remain limited" and broader validation across disciplines, age groups and collaborative environments is necessary

### Target Learners
- middle school students in mathematics and Chinese classes

### Target Learning Goals
- efficient, large-scale teaching diagnosis and assessment from classroom dialogue

## Claims

- [GPT-4's coding consistency differed between math and Chinese lessons for codes such as CI, SC, RW and SU](../claims/gpt4-coding-consistency-subject-differences.md) [~W]
- [ChatGPT-based coding of classroom dialogue is about 30 times faster than experienced human manual coding](../claims/gpt4-dialogue-coding-thirtyfold-time-saving.md) [+W]
- [A customised GPT-4 agreed with a human coder on over 90% of coded dialogue turns in both math and Chinese lessons](../claims/gpt4-human-coder-agreement-over-90-percent.md) [+W]
- [Human–GPT coding agreement varied sharply by code, with near-chance or negative Kappa for co-ordination codes despite near-perfect agreement on others](../claims/gpt4-kappa-varies-by-dialogue-code.md) [~W]
- [A GPT-4-based coding scheme achieved over 90% inter-coder agreement, surpassing results reported for specialised pre-2017 AI (~80%)](../claims/gpt4-surpasses-specialised-intelligence-agreement.md) [+W]

## Related Strategies

- [Incorporate an expert human in the loop to support LLM coding of difficult adjacent coding categories](expert-human-in-loop-for-llm-pck-coding.md)
- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)

## Examples
-

## Key Sources
- Long, Y., Luo, H. & Zhang, Y. (2024). Evaluating large language models in analysing classroom dialogue. npj Science of Learning 9:60. https://doi.org/10.1038/s41539-024-00273-3
