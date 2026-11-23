---
type: strategy
id: polished-few-shot-decomposed-coding-strategy
title: Decomposed coding with a GPT-polished few-shot prompt for reliable LLM text classification
description: "An implementable prompting recipe: give the LLM a role prompt, theme criteria with human-labeled example quotes, and one text segment to label at a time as a binary classification per theme."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: nikhil-sanjay-borse-2025
    resource: "https://arxiv.org/abs/2508.14764"
    title: "Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. https://arxiv.org/abs/2508.14764"
    author: Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello
---

# Decomposed coding with a GPT-polished few-shot prompt for reliable LLM text classification

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 3 studies (2 design, 1 causal), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
An implementable prompting recipe: give the LLM a role prompt, theme criteria with human-labeled example quotes, and one text segment to label at a time as a binary classification per theme. The article reports that GPT-4o was used to polish the prompt: "We then asked GPT-4o to polish the few-shot prompt, which simplified and improved its clarity, and generated prototypical examples that were unambiguous to process for the LLM". Testing on three of the 14 transcripts showed the few-shot prompt generally yielded better classification than zero-shot, and polishing increased reliability for all themes at low computational cost.

## Design Implications

### Context
#### Requirements
- Theme criteria with human-labeled example quotes (few-shot examples)
- Dividing the prompt using triple quotes due to task complexity
- Batch processing via the OpenAI API
#### Constraints
- The few-shot advantage was established through preliminary testing on three of the 14 transcripts, not a full controlled comparison

### Target Learners
- qualitative researchers in physics education using LLM raters

### Target Learning Goals
- reliable LLM classification of student discussion transcripts against a human coding rubric

### Affordances
- [Stem Ways Of Thinking Four Theme Framework](../products/stem-ways-of-thinking-framework.md)

## Claims

- [Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes](../claims/llm-optimization-increases-inter-rater-reliability.md) [+W]
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](../claims/icl-no-better-than-zero-shot-engagement-coding.md) [-W]
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](../claims/regex-rules-improve-fewshot-llm-labeling-accuracy.md) [+W]

## Related Strategies

- [Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context](few-shot-prompt-with-preconceptions-for-feedback-generation.md)
- [Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts](iterative-prompt-engineering-mirroring-human-coder-refinement.md)
- [Craft educational LLM prompts using iterative refinement, role-playing, and constraints with suitable context](three-pillar-educational-prompting-strategy.md)
- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)
- [Apply effective zero-shot prompting practices — CoT, label definitions, survey-question context, function calling, and persona — when using LLMs for survey analysis](zero-shot-llm-prompting-practices-for-survey-analysis.md)
- [Development strategies targeting AI virtual patient limitations: expert-reviewed content, iterative prompt engineering, behavioral rules, few-shot prompting, and conversational memory](ai-virtual-patient-mitigation-strategies.md)

## Examples
-

## Key Sources
- Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. https://arxiv.org/abs/2508.14764
