---
type: strategy
id: llms-supportive-tools-medical-education-feedback
title: Use high-performance LLMs as supportive tools in medical education for feedback and learning-process optimization, pending image-based validation
description: The article recommends deploying high-accuracy LLMs as supportive tools in medical education rather than as autonomous clinical agents.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: atlanoğlu-ş-2026
    resource: "https://doi.org/10.1097/MD.0000000000049517"
    title: "Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517"
    author: Atlanoğlu Ş, Gedik MA
---

# Use high-performance LLMs as supportive tools in medical education for feedback and learning-process optimization, pending image-based validation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends deploying high-accuracy LLMs as supportive tools in medical education rather than as autonomous clinical agents. It reports that "Large-language models demonstrated high-accuracy performance on fundamental radiology questions, indicating their potential as supportive tools in medical education for providing feedback and optimizing learning processes." The recommendation is tied to the observed 84–90% accuracy on non-visual questions and benchmarking against residents.

## Design Implications

### Context
#### Requirements
- Models must achieve high accuracy on fundamental theoretical questions, as demonstrated in the study's question-set benchmarking against residents
#### Constraints
- The article states current text-based models alone are insufficient for direct clinical use because radiology practice fundamentally relies on visual data analysis
- The study used only non-visual, multiple-choice questions from a restricted pool of 100 items derived from 2 textbooks

### Target Learners
- radiology residents (years 1–3)

### Target Learning Goals
- radiology theoretical knowledge assessment and feedback

## Claims

- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](../claims/claude-sonnet-superior-temporal-reliability-radiology-questions.md) [+M]
- [Gemini 2.5 Pro achieved the highest accuracy (90%) on 100 radiology multiple-choice questions, and all LLMs and 3rd-year residents significantly outperformed 1st- and 2nd-year residents](../claims/llms-gemini-highest-radiology-mcq-accuracy-outperform-junior-residents.md) [+M]
- [Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions](../claims/no-accuracy-difference-across-llm-versions-radiology.md) [+M]
- [No statistically significant performance gap existed between Turkish and English administration of the same radiology questions to ChatGPT-5 and Gemini 2.5 Pro](../claims/no-language-gap-turkish-english-llm-radiology-accuracy.md) [+M]
- [Subspecialty performance varied: Gemini 2.5 Pro and Claude Sonnet led in abdominal and musculoskeletal radiology, and 3rd-year residents significantly outperformed 1st-year residents in musculoskeletal radiology](../claims/subspecialty-variation-llm-radiology-performance.md) [+M]

## Related Strategies

- [Deploy healthcare LLMs as augmentative tools under human oversight rather than autonomous decision-makers](llm-augmentative-tools-human-oversight.md)
- [Use ChatGPT-4o as a supplementary educational tool rather than an autonomous clinical decision-support system in non-English contexts](chatgpt-4o-as-supplementary-tool-non-english.md)
- [Use LLMs cautiously as supplementary learning tools in dental education, with output verification and professional supervision](cautious-llm-supplementary-tools-dental-education.md)
- [Use LLMs in medical education as support tools requiring human review, not as independent decision-makers or authoritative instructors](llms-as-support-tools-medical-education.md)
- [Use LLMs cautiously in ophthalmology resident training, particularly for complex clinical decision-making cases](cautious-llm-use-in-resident-training-complex-cases.md)
- [Guide medical students to use ChatGPT cautiously with cross-checking, disclosure, and teacher oversight](cautious-chatgpt-use-teacher-oversight-strategy.md)
- [Use multimodal AI chatbots such as ChatGPT-4o as diagnostic support tools in dental education, particularly endodontics](multimodal-ai-chatbot-diagnostic-support-dental-education.md)

## Examples
-

## Key Sources
- Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517
