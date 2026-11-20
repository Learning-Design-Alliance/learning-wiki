---
type: research-method
id: prompt-engineering-techniques-for-llm-based-classroom-discourse-analysis
title: Prompt engineering techniques for LLM-based classroom discourse analysis
description: The article describes a framework of prompting techniques — Vanilla, Chain of Thought, and Self-Ask — applied with zero-shot and few-shot strategies to detect teacher questions from ASR outputs.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Prompt engineering techniques for LLM-based classroom discourse analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article describes a framework of prompting techniques — Vanilla, Chain of Thought, and Self-Ask — applied with zero-shot and few-shot strategies to detect teacher questions from ASR outputs. "Recent advancements have introduced techniques to enhance response quality, such as Chain of Thought (CoT) ([Lee et al., 2024](https://doi.org/10.1186/s41239-024-00447-4)) and Self-Ask (SA) (Press et al., 2023)." Self-Ask "explicitly introduces intermediate sub-questions that guide the model through each reasoning step." The framework frames prompt engineering as "designing effective prompts to elicit desired responses from LLMs, crucial for instructing models in specific tasks."

## Accounts
<!-- How each source describes or uses the method -->
- **Prompt engineering techniques for LLM-based classroom discourse analysis**: The article describes a framework of prompting techniques — Vanilla, Chain of Thought, and Self-Ask — applied with zero-shot and few-shot strategies to detect teacher questions from ASR outputs. "Recent advancements have introduced techniques to enhance response quality, such as Chain of Thought (CoT) ([Lee et al., 2024](https://doi.org/10.1186/s41239-024-00447-4)) and Self-Ask (SA) (Press et al., 2023)." Self-Ask "explicitly introduces intermediate sub-questions that guide the model through each reasoning step." The framework frames prompt engineering as "designing effective prompts to elicit desired responses from LLMs, crucial for instructing models in specific tasks." (Lehesvuori et al. (2026))
- **Multi-round tailored prompt design framework for LLM-based emotion and behavior analysis**: The article proposes a method combining large language models with prompt engineering to infer emotional and engagement states from student text. It organizes prompts into three types: "Emotion Detection Prompts", "Engagement Assessment Prompts", and "Behavioral Indicators Prompts", each with a template directing the LLM to classify emotional tone, assess engagement, or identify confusion and frustration. A multi-round design iteratively refines the model's understanding, with outputs aggregated into a holistic view of each student's state. (Kaito Tanaka et al. (2024))

### Claims
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](../claims/cot-outperforms-self-ask-zero-shot.md) [+M]
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](../claims/few-shot-cot-outperforms-zero-shot-question-detection.md) [+M]
- [Tailored prompt engineering consistently outperforms base models and chain-of-thought prompting across four LLMs for educational emotion and behavior analysis](../claims/prompt-engineering-outperforms-baselines-llm-emotion-analysis.md) [+M]

## Related Research Methods

- [Automated analysis of argumentative discourse for diagnostic learning analytics](automated-analysis-of-argumentative-discourse-for-diagnostic-learning-analytics.md)

## Key Sources
- Lehesvuori, S., Urrutia, F., Heilala, V., Araya, R., & Hämäläinen, R. (2026). Discovering technology-aided possibilities for automatic analysis of science teacher questions. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10545-3
- Kaito Tanaka, Benjamin Tan, Brian Wong. (2024). Leveraging Language Models for Emotion and Behavior Analysis in Education. https://arxiv.org/abs/2408.06874
