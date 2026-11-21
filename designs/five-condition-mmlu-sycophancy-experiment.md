---
type: design
id: five-condition-mmlu-sycophancy-experiment
title: Five-condition MMLU prompt experiment measuring LLM sycophancy in a simulated educational context
description: A benchmark evaluation setup that runs five OpenAI models (GPT-4o-mini, GPT-4o, GPT-4.1-nano, GPT-4.1-mini, GPT-4.1) over all 14,042 MMLU questions under one control and four prompt variations, totaling 350,000 distin...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: chuck-arvin-2025
    resource: "https://arxiv.org/abs/2506.10297"
    title: "Chuck Arvin. (2025). \"Check My Work?\" Measuring Sycophancy in a Simulated Educational Context. KDD EAI 2025. https://arxiv.org/abs/2506.10297"
    author: Chuck Arvin
---

# Five-condition MMLU prompt experiment measuring LLM sycophancy in a simulated educational context

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A benchmark evaluation setup that runs five OpenAI models (GPT-4o-mini, GPT-4o, GPT-4.1-nano, GPT-4.1-mini, GPT-4.1) over all 14,042 MMLU questions under one control and four prompt variations, totaling 350,000 distinct Q&A results. Conditions include "Correct Suggestion: “Is it Correct?”" and an incorrect-suggestion analogue, with options presented in alphabetical order to avoid ordering effects. Answers are parsed programmatically by extracting the first letter from the set [A-D].

## Design Implications

### Context
#### Requirements
- A labeled question-answer dataset allowing programmatic accuracy measurement, here MMLU with its correct answer assumed correct
- A regular expression to extract the first answer letter from the set [A-D] for programmatic parsing
#### Constraints
- The article notes it cannot perfectly replicate the full ChatGPT experience because OpenAI does not offer the model for batch inference at scale and the system prompts behind ChatGPT are not available
- The article acknowledges MMLU ground truth labels are incorrect in about 6.5% of cases per cited work and models may have been trained on the questions

### Target Learners
- students interacting with LLM tools in educational settings

### Learning Goals
- accurate answers to educational multiple-choice questions across MMLU subjects

### Claims
- [Llm Accuracy Shifts When Students Mention Answers](../claims/llm-accuracy-shifts-when-students-mention-answers.md) [+M]
- [Llm Flip To User Suggested Options](../claims/llm-flip-to-user-suggested-options.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Chuck Arvin. (2025). "Check My Work?" Measuring Sycophancy in a Simulated Educational Context. KDD EAI 2025. https://arxiv.org/abs/2506.10297
