---
type: research-method
id: llm-extracted-pedagogical-feature-based-item-difficulty-prediction-method
title: LLM-extracted pedagogical feature-based item difficulty prediction method
description: "A set of features extracted from question text using Google's Gemini models, intended to capture pedagogical signals typically assessed by human experts."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# LLM-extracted pedagogical feature-based item difficulty prediction method

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A set of features extracted from question text using Google's Gemini models, intended to capture pedagogical signals typically assessed by human experts. The article states these tools "analyze questions to identify solution steps, required mathematical skills, cognitive complexity, and potential student misconceptions". Features include number of solution steps, Bloom's taxonomy level, misconception count, expression nesting depth, abstract-to-concrete symbol ratio, units check, information gap, real-world context flag, distractor plausibility scores, and categorical one-hot encoded features such as knowledge dimension and problem archetype. Features were aggregated over multiple LLM runs for stability.

## Accounts
<!-- How each source describes or uses the method -->
- **LLM-extracted pedagogical feature set for mathematics questions**: A set of features extracted from question text using Google's Gemini models, intended to capture pedagogical signals typically assessed by human experts. The article states these tools "analyze questions to identify solution steps, required mathematical skills, cognitive complexity, and potential student misconceptions". Features include number of solution steps, Bloom's taxonomy level, misconception count, expression nesting depth, abstract-to-concrete symbol ratio, units check, information gap, real-world context flag, distractor plausibility scores, and categorical one-hot encoded features such as knowledge dimension and problem archetype. Features were aggregated over multiple LLM runs for stability. (Matías Hoyl (2026))

### Claims
- [Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features](../claims/llm-pedagogical-features-drive-difficulty-gain.md) [+M]

## Related Research Methods
-

## Key Sources
- Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. https://arxiv.org/abs/2602.00034
