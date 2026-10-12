---
type: research-method
id: llm-scoring-generated-feedback-and-essay-feature-analysis-framework
title: LLM scoring, generated-feedback, and essay-feature analysis framework
description: "The article proposes an analysis framework in which \"Essays are first evaluated by LLMs to produce both predicted scores and textual feedback.\" Essay-level features (length, Flesch Reading Ease readability, and LanguageTool error counts) and feedback-derived signals (trait-specific praise and critic"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# LLM scoring, generated-feedback, and essay-feature analysis framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes an analysis framework in which "Essays are first evaluated by LLMs to produce both predicted scores and textual feedback." Essay-level features (length, Flesch Reading Ease readability, and LanguageTool error counts) and feedback-derived signals (trait-specific praise and criticism via aspect-based sentiment analysis with a DeBERTa-v3 ABSA model, confidence above 0.9) are then extracted and related to the scores. The framework was applied to GPT-3.5, GPT-4.1, GPT-5-mini, and Llama 2, 3, and 4 models on the ASAP and DREsS datasets to compare LLM scores with human ratings and examine how feedback sentiment and essay characteristics relate to assigned scores.

## Accounts
<!-- How each source describes or uses the method -->
- **Framework combining LLM scoring, generated feedback, and essay-feature analysis**: The article proposes an analysis framework in which "Essays are first evaluated by LLMs to produce both predicted scores and textual feedback." Essay-level features (length, Flesch Reading Ease readability, and LanguageTool error counts) and feedback-derived signals (trait-specific praise and criticism via aspect-based sentiment analysis with a DeBERTa-v3 ABSA model, confidence above 0.9) are then extracted and related to the scores. The framework was applied to GPT-3.5, GPT-4.1, GPT-5-mini, and Llama 2, 3, and 4 models on the ASAP and DREsS datasets to compare LLM scores with human ratings and examine how feedback sentiment and essay characteristics relate to assigned scores. (Jerin George Mathew et al. (2026))

### Claims
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](../claims/llm-feedback-sentiment-tracks-scores.md) [+M]
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](../claims/llm-essay-scoring-weak-human-agreement.md) [+M]

## Related Research Methods
-

## Key Sources
- Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714
