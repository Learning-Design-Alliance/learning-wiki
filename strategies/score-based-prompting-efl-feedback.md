---
type: strategy
id: score-based-prompting-efl-feedback
title: "Score-based prompting: inform the LLM of rubric-based essay scores to elicit more constructive feedback"
description: Score-based prompting addresses the positivity limitation of RLHF-aligned models by supplying predicted rubric scores and rubric explanations in the prompt so the LLM can self-refine its feedback.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: jieun-han-2023
    resource: "https://arxiv.org/abs/2310.05191"
    title: "Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2023). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. https://arxiv.org/abs/2310.05191"
    author: Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh
---

# Score-based prompting: inform the LLM of rubric-based essay scores to elicit more constructive feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (2 causal, 1 review), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
Score-based prompting addresses the positivity limitation of RLHF-aligned models by supplying predicted rubric scores and rubric explanations in the prompt so the LLM can self-refine its feedback. Student essays are scored on three rubrics (content, organization, and language) by an automated essay scoring model, and the article states it "leverage[s] rubric-based scores for LLM self-refinement of feedback generation". The method assumes scoring information guides the model toward feedback aligned with students' needs.

## Design Implications

### Context
#### Requirements
- An automated essay scoring model that produces rubric-based scores (content, organization, language) for student essays
- A scoring rubric with explanations to include in the prompt
#### Constraints
- Evaluated with gpt-3.5-turbo, a black-box model lacking transparency in why feedback was generated

### Target Learners
- EFL (English as a Foreign Language) writing learners, undergraduate

### Target Learning Goals
- Argumentative essay writing improvement across content, organization, and language rubrics

## Claims

- [gpt-3.5-turbo with standard prompting generates overly positive, indirect, and unhelpful essay feedback for EFL writing](../claims/gpt35-standard-prompting-overly-positive-feedback.md) [+W]
- [Score-based prompting generates more negative, straightforward, direct, and extensive feedback, and experts prefer it](../claims/score-based-prompting-feedback-characteristics-preference.md) [+W]
- [Score-based prompting outperforms standard prompting on feedback accuracy, relevance, and helpfulness across all rubrics](../claims/score-based-prompting-outperforms-standard-quality.md) [+W]
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](../claims/prompting-limited-uneven-proficiency-control-writing-simulation.md) [~W]
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](../claims/prompt-rubric-quality-drives-llm-grading.md) [+W]

## Related Strategies

- [Include an explicit rubric in GenAI feedback prompts, even in Zero-shot conditions](include-explicit-rubric-in-genai-feedback-prompts.md)
- [Implement AI-peer integrated feedback as a standardized two-phase revision cycle with rubric-aligned prompting and instructor monitoring](ai-peer-integrated-feedback-cycle-strategy.md)

## Examples
-

## Key Sources
- Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2023). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. https://arxiv.org/abs/2310.05191
