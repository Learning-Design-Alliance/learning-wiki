---
type: strategy
id: specialized-tcm-llm-training-and-chain-of-thought-strategy
title: Improve LLM performance on TCM examinations by incorporating TCM texts into training, developing specialized TCM LLMs, and using chain-of-thought prompting
description: "The authors propose concrete avenues for making AI usable in TCM education: incorporating \"textbooks on TCM in Chinese and ancient TCM texts\" into training data, standardizing TCM terminology, developing \"specialized..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: tseng-liang-wei-2025
    resource: "https://doi.org/10.2196/58897"
    title: "Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897"
    author: Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu
---

# Improve LLM performance on TCM examinations by incorporating TCM texts into training, developing specialized TCM LLMs, and using chain-of-thought prompting

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 3 studies (1 causal, 1 associational, 1 design), `q2`–`q3` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
The authors propose concrete avenues for making AI usable in TCM education: incorporating "textbooks on TCM in Chinese and ancient TCM texts" into training data, standardizing TCM terminology, developing "specialized ChatGPT models or custom LLMs" narrowed to TCM schools, and adopting chain-of-thought prompting, which "can also improve the performance of ChatGPT in medical examinations." They also note open-ended or repeated questioning may outperform single-choice formats.

## Design Implications

### Context
#### Requirements
- Access to comprehensive, standardized TCM training data, including ancient texts in Chinese
#### Constraints
- The article reports these as proposed future directions, not tested interventions in this study; generalizability is limited to the Taiwanese TCM examination context

### Target Learners
- TCM students preparing for licensing examinations

### Target Learning Goals
- TCM domain knowledge and examination readiness

## Claims

- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](../claims/reasoning-prompting-improves-llm-distractor-match.md) [+M]
- [GPT-4's chain-of-thought reasoning, captured via structured output, was consistently reliable and appeared to provide logical, context-grounded justification usable for prompt tuning and end-user insight](../claims/gpt4-cot-reasoning-reliable-transparent.md) [+W]
- [Most GPT-4 errors on TCM examination questions stemmed from misunderstanding of TCM concepts (55.3%), not misreading questions](../claims/gpt4-tcm-errors-concept-misunderstanding-55-3.md) [+W]
- [GPT-4 achieved 43.9% accuracy on the 2022 Taiwanese TCM licensing examination, below two human TCM resident doctors (70% and 78.4%) and below the 60% pass threshold](../claims/gpt4-43-9-accuracy-tcm-licensing-below-humans.md) [+W]
- [Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches](../claims/gpt4-answer-explanation-consistency-low-kappa.md) [-W]

## Related Strategies

- [Use Chain-of-Thought and Tree-of-Thought prompting to mitigate hallucination and weak complex reasoning in LLMs used for learning](cot-tot-prompting-mitigate-llm-hallucination.md)
- [Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM](simulated-multiagent-prompting-for-osce-generation.md)
- [Use few-shot prompting with chain-of-thought and annotated rubric examples for LLM-based scoring of learner-generated clinical text](few-shot-cot-annotated-rubric-prompting-strategy.md)
- [Apply effective zero-shot prompting practices — CoT, label definitions, survey-question context, function calling, and persona — when using LLMs for survey analysis](zero-shot-llm-prompting-practices-for-survey-analysis.md)

## Examples
-

## Key Sources
- Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897
