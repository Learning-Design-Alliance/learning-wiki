---
type: strategy
id: refine-feedback-training-dataset-strategy
title: Refine fine-tuning datasets by selecting teachers who write personalized feedback and supplementing with GPT-generated feedback
description: "The authors propose improving future fine-tuned feedback models by curating higher-quality training data: \"training only teachers who spend more time writing personalized feedback and supplementing our dataset with fe..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: sami-baral-2024
    resource: "https://arxiv.org/abs/2411.08910"
    title: "Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. https://arxiv.org/abs/2411.08910"
    author: Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan
---

# Refine fine-tuning datasets by selecting teachers who write personalized feedback and supplementing with GPT-generated feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors propose improving future fine-tuned feedback models by curating higher-quality training data: "training only teachers who spend more time writing personalized feedback and supplementing our dataset with feedback from GPT". They also recommend fine-tuning across many problems regardless of examples per problem, to make the model generally better at math and feedback rather than overfitting to a few questions.

## Design Implications

### Context
#### Requirements
- Access to teacher training data with detailed, personalized feedback messages
#### Constraints
- The current dataset suffered from vague, short, and sometimes irrelevant teacher feedback messages

### Target Learners
- middle-school math students

### Target Learning Goals
- improved automated feedback quality on open-ended math responses

## Claims

- [GOAT's feedback quality is limited by low-quality teacher feedback in its training data](../claims/goat-feedback-limited-by-training-data-quality.md) [+W]
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](../claims/sft-less-effective-than-prompting-for-feedback-generation.md) [-W]

## Related Strategies

- [Future directions: fine-tuning on human-refined frameworks and hybrid human–LLM or multi-agent annotation systems](future-hybrid-human-llm-annotation-systems.md)

## Examples
-

## Key Sources
- Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. https://arxiv.org/abs/2411.08910
