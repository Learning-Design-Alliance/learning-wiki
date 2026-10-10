---
type: strategy
id: zero-shot-prompt-codebook-translation-strategy
title: Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding
description: The article describes a pipeline in which human codebook rubrics are converted into zero-shot prompts built on the PARTS framework (Persona, Aim, Recipients, Theme, Structure) and CLEAR criteria, with each variation i...
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

# Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article describes a pipeline in which human codebook rubrics are converted into zero-shot prompts built on the PARTS framework (Persona, Aim, Recipients, Theme, Structure) and CLEAR criteria, with each variation incrementally adding guidance to a baseline zero-shot prompt. The authors write that "we translate deductive essay coding rubrics into zero -shot prompts with various levels of information", ending every prompt with an instruction to return 1 or 0 and no additional text. This design lets models be compared directly without exemplar-selection bias.

## Design Implications

### Context
#### Requirements
- Prompts must align with the human codebook and be clear, structured, precise, tailored, and restricted; the article used meta-prompting with ChatGPT-4o to refine them
#### Constraints
- Few-shot and chain-of-thought prompting were beyond the study's scope; zero-shot prompting may not always produce scores matching human ratings

### Target Learners
- higher education instructors assessing student writing
- qualitative researchers coding student essays

### Target Learning Goals
- accurate automated coding of theory-based concepts in student essays
- reduced instructor grading workload

## Related Strategies

- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)
- [Use AI chatbots as one-shot generators of candidate cooperative learning techniques, then select via a researcher-built rubric](ai-chatbot-technique-generation-rubric-selection.md)

## Examples
-

## Key Sources
- Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries
