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
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

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

## Claims

- [Systematic human coding added five codes the LLM-assisted phases had not surfaced, extending the codebook from 67 to 72 items and 18 to 19 categories](../claims/human-coding-added-five-codes-llm-missed.md) [~W]

## Related Strategies

- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)
- [Use AI chatbots as one-shot generators of candidate cooperative learning techniques, then select via a researcher-built rubric](ai-chatbot-technique-generation-rubric-selection.md)
- [Guide student instruction with chain-of-thought decomposition, few-shot worked examples, and self-consistency over multiple LLM queries](cot-fewshot-selfconsistency-student-guidance.md)
- [Reserve LLM grading for short, well-structured tasks with explicit rubrics or exemplar answers, newer models, and stable API pipelines](reserve-llm-grading-for-structured-rubric-tasks.md)
- [Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)](rubric-enhanced-llm-grading-prompt.md)

## Examples
-

## Key Sources
- Keith, Shelley; Pavlik, Philip I., Jr.; Stives, Kristen L.; Kerr, Laura Jean. (2026). Comparing Zero-Shot Large Language Model Prompting with Human Coding of Theory Concepts in Student Essays. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/imrryr/LLM-queries
