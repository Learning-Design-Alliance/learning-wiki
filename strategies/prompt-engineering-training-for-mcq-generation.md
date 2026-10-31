---
type: strategy
id: prompt-engineering-training-for-mcq-generation
title: Train medical educators in prompt engineering, using specific, contextualized prompts to improve LLM-generated MCQ quality
description: "The review recommends that educators craft prompts carefully when generating MCQs with LLMs, since it observed \"a wide range of approaches to writing the prompts\" across studies, with some requiring modifications to i..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
sources:
  - id: artsi-yaara-2024
    resource: "https://doi.org/10.1186/s12909-024-05239-y"
    title: "Artsi Yaara, Sorin Vera, Konen Eli, Glicksberg Benjamin S., Nadkarni Girish, Klang Eyal. (2024). Large language models for generating medical examinations: systematic review. BMC Medical Education. https://doi.org/10.1186/s12909-024-05239-y"
    author: Artsi Yaara, Sorin Vera, Konen Eli, Glicksberg Benjamin S., Nadkarni Girish, Klang Eyal
---

# Train medical educators in prompt engineering, using specific, contextualized prompts to improve LLM-generated MCQ quality

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 5 studies (4 causal, 1 review), `q2`–`q3` · 0 of 5 report an effect size · 5 claims rest on one study

## Description
The review recommends that educators craft prompts carefully when generating MCQs with LLMs, since it observed "a wide range of approaches to writing the prompts" across studies, with some requiring modifications to improve validity. It suggests general guidelines: "trying to be as specific as possible, provide appropriate setting and context when phrasing the prompt, ask open ended questions, and request examples". It calls for training educators and students in AI literacy and prompt engineering.

## Design Implications

### Context
#### Requirements
- Prompt crafting must be a requisite consideration for AI-generated MCQ application in medical education, per the review
#### Constraints
- Prompt-engineering may require specific training so that MCQ quality is not impaired

### Target Learners
- medical educators
- medical students

### Target Learning Goals
- AI literacy and prompt engineering for generating valid medical MCQs

## Claims

- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](../claims/prompt-design-affects-mcq-accuracy-asymmetrically.md) [+W]
- [On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants](../claims/prompt-privilege-monotonic-accuracy-gap-medqa.md) [+W]
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](../claims/reasoning-prompting-improves-llm-distractor-match.md) [+W]
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](../claims/hint-prompts-raise-llm-scoring-agreement.md) [+W]
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](../claims/prompt-rubric-quality-drives-llm-grading.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Artsi Yaara, Sorin Vera, Konen Eli, Glicksberg Benjamin S., Nadkarni Girish, Klang Eyal. (2024). Large language models for generating medical examinations: systematic review. BMC Medical Education. https://doi.org/10.1186/s12909-024-05239-y
