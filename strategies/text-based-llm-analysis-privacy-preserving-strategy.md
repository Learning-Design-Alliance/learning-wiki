---
type: strategy
id: text-based-llm-analysis-privacy-preserving-strategy
title: Use text-based LLM analysis instead of visual or physiological data collection to preserve privacy and scale emotion analysis
description: This strategy replaces intrusive webcam- and sensor-based monitoring of students with analysis of text the students already produce, using LLMs with tailored prompts.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: kaito-tanaka-2024
    resource: "https://arxiv.org/abs/2408.06874"
    title: "Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. https://arxiv.org/abs/2408.06874"
    author: Kaito Tanaka, Benjamin Tan, Brian Wong
---

# Use text-based LLM analysis instead of visual or physiological data collection to preserve privacy and scale emotion analysis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
This strategy replaces intrusive webcam- and sensor-based monitoring of students with analysis of text the students already produce, using LLMs with tailored prompts. The article argues that "Our method's reliance on textual data, as opposed to visual or physiological data, enhances its scalability and practicality", since text is easier to collect, raises fewer privacy concerns, and requires no specialized hardware. It is intended for educational settings seeking scalable, non-intrusive monitoring of emotion and engagement.

## Design Implications

### Context
#### Requirements
- Students must generate analyzable text such as written responses, discussion posts, or chat messages
- Access to an LLM capable of the classification prompts
#### Constraints
- The article notes traditional visual methods can be effective; the text-based approach is positioned as an alternative where intrusiveness and privacy are concerns

### Target Learners
- students in online learning platforms

### Target Learning Goals
- monitoring emotional states
- monitoring engagement for personalized support

## Claims

- [On GPT-4, the prompt-based method reaches 88.3% accuracy versus 71.0% for the base model and 77.2% for chain-of-thought prompting](../claims/gpt4-prompt-method-88-3-accuracy.md) [+W]
- [The prompt-based method achieves contextual relevance scores of 0.89 to 0.92 across the four LLMs on the GPT-4 based scoring metric](../claims/llm-contextual-scores-089-092.md) [+W]
- [Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis](../claims/prompt-engineering-outperforms-baselines-llm-emotion-analysis.md) [+W]
- [The prompt-based method correctly identified subtle mixed-emotion and nuanced-feedback cues that the base model and CoT method missed](../claims/prompt-method-captures-subtle-emotion-cues.md) [+W]
- [The prompt-based method maintains high accuracy and contextual understanding across diverse educational contexts and interaction types](../claims/prompt-method-robust-across-contexts.md) [+W]

## Related Strategies

- [Use open-source, preference-optimized LLMs as a cheaper, privacy-preserving alternative to proprietary models for Socratic question generation](open-source-dpo-socratic-question-generation-strategy.md)
- [Privacy-preserving deployment measures for an ITS under GDPR and EU AI Act](gdpr-compliant-its-deployment-measures.md)

## Examples
-

## Key Sources
- Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. https://arxiv.org/abs/2408.06874
