---
type: strategy
id: refined-marking-scheme-llm-grading-strategy
title: Use detailed, refined marking schemes within LLM grading prompts to obtain more consistent and precise grading
description: "The article's refined marking scheme function generates or refines scoring guidelines from the assignment questions, which the authors say is particularly beneficial for introductory courses where assignments depend o..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: calvin-yeung-2025
    resource: "https://arxiv.org/abs/2501.14305"
    title: "Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. https://arxiv.org/abs/2501.14305"
    author: Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii
---

# Use detailed, refined marking schemes within LLM grading prompts to obtain more consistent and precise grading

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 6 studies (3 design, 2 causal, 1 review), `q2` · 2 of 6 report an effect size · 6 claims rest on one study

## Description
The article's refined marking scheme function generates or refines scoring guidelines from the assignment questions, which the authors say is particularly beneficial for introductory courses where assignments depend on timely topics. Their comparison showed that with a detailed scheme "both human and AAG scores for Question 1 were more diverse, while scores for Question 2 were more concentrated," leading them to state the function "ensures more consistent and precise grading." Instructors should supply or refine detailed mark-awarding guidelines when deploying LLM grading.

## Design Implications

### Context
#### Requirements
- Instructors provide assignment questions and, ideally, detailed marking guidelines; the system can generate or refine scoring guidelines from the questions themselves
#### Constraints
- The article notes implementing adaptive marking scheme generation would still require human validation

### Target Learners
- instructors of introductory higher-education courses with changing assignment content

### Target Learning Goals
- consistent and precise automated grading of open-ended student responses

## Claims

- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](../claims/mark-scheme-improves-llm-grading.md) [+M]
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](../claims/prompt-rubric-quality-drives-llm-grading.md) [+M]
- [Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results](../claims/rubric-examples-prompt-variant-balances-grading-bias.md) [+M]
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](../claims/explicit-rubric-conditions-reduce-ai-disagreement.md) [+M]
- [Adding explanation text to rubric items targeting observed machine-grading errors cut cases where GPT-4o differed from both human graders from 21.7% to 9.6% on Question 2](../claims/rubric-explanation-targeting-machine-errors.md) [+M]
- [AAG system scores align closely with human TA scores on open-ended statistics questions, with Pearson correlations of 0.75 and 0.82](../claims/aag-ta-score-correlation-open-ended.md) [+M]

## Related Strategies

- [Use role-prompted VLMs with the DAST-C rubric to automatically score drawn images and provide scoring rationales for classroom use](vlm-role-prompting-dast-auto-scoring-strategy.md)

## Examples
-

## Key Sources
- Calvin Yeung, Jeff Yu, King Chau Cheung, Tat Wing Wong, Chun Man Chan, Kin Chi Wong, and Keisuke Fujii. (2025). A Zero-Shot LLM Framework for Automatic Assignment Grading in Higher Education. arXiv preprint. https://arxiv.org/abs/2501.14305
