---
type: strategy
id: zero-shot-llm-prompting-practices-for-survey-analysis
title: Apply effective zero-shot prompting practices — CoT, label definitions, survey-question context, function calling, and persona — when using LLMs for survey analysis
description: "The article enumerates prompting techniques used to improve LLM results without any labeled training data: zero-shot chain-of-thought prompting, prompt tuning via inspection of CoT reasoning, adding descriptive contex..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: michael-j-parker-2024
    resource: "https://doi.org/10.1007/s40593-024-00414-0"
    title: "Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0"
    author: Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh
---

# Apply effective zero-shot prompting practices — CoT, label definitions, survey-question context, function calling, and persona — when using LLMs for survey analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 4 studies (4 causal), `q2` · 0 of 4 report an effect size · 4 claims rest on one study

## Description
The article enumerates prompting techniques used to improve LLM results without any labeled training data: zero-shot chain-of-thought prompting, prompt tuning via inspection of CoT reasoning, adding descriptive context for labels, injecting the survey question into the prompt, using function calling for reliable structured JSON output, and the memetic proxy or persona pattern. By applying these practices the authors report achieving human-level performance with GPT-4 on multiple tasks, enabling survey-analysis workflows in education settings where labeled data is scarce.

## Design Implications

### Context
#### Requirements
- Access to LLMs via API with function-calling capability; label definitions must be written into prompts since there is no fine-tuning to teach the model label meanings.
#### Constraints
- Techniques were tested on biomedical science course feedback with GPT-3.5 and GPT-4; the article notes prompt sensitivity and the need to validate against human annotation per cited prior work.

### Target Learners
- educators, course teams, and education administrators analyzing student feedback

### Target Learning Goals
- reliable automated qualitative analysis of open-ended survey responses

### Affordances
- [Llm Nlp Task Workflows For Survey Analysis](../research-methods/composable-llm-workflow-for-educational-survey-analysis.md)

## Claims

- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](../claims/curricular-cot-improves-accuracy-larger-models.md) [+M]
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](../claims/prompt-design-affects-mcq-accuracy-asymmetrically.md) [+M]
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](../claims/in-context-examples-improve-bloom-classification.md) [~M]
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](../claims/icl-no-better-than-zero-shot-engagement-coding.md) [~M]

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)

## Examples
-

## Key Sources
- Michael J. Parker, Caitlin Anderson, Claire Stone, YeaRim Oh. (2024). A Large Language Model Approach to Educational Survey Feedback Analysis. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00414-0
