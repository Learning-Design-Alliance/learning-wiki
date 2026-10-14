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
> **Evidence** · 11 claims (4 for, 7 mixed) · 7 studies (4 associational, 1 causal, 1 review, 1 design), `q2`–`q3` · 0 of 7 report an effect size · 11 claims rest on one study

## Description
The article proposes an analysis framework in which "Essays are first evaluated by LLMs to produce both predicted scores and textual feedback." Essay-level features (length, Flesch Reading Ease readability, and LanguageTool error counts) and feedback-derived signals (trait-specific praise and criticism via aspect-based sentiment analysis with a DeBERTa-v3 ABSA model, confidence above 0.9) are then extracted and related to the scores. The framework was applied to GPT-3.5, GPT-4.1, GPT-5-mini, and Llama 2, 3, and 4 models on the ASAP and DREsS datasets to compare LLM scores with human ratings and examine how feedback sentiment and essay characteristics relate to assigned scores.

## Accounts
<!-- How each source describes or uses the method -->
- **Framework combining LLM scoring, generated feedback, and essay-feature analysis**: The article proposes an analysis framework in which "Essays are first evaluated by LLMs to produce both predicted scores and textual feedback." Essay-level features (length, Flesch Reading Ease readability, and LanguageTool error counts) and feedback-derived signals (trait-specific praise and criticism via aspect-based sentiment analysis with a DeBERTa-v3 ABSA model, confidence above 0.9) are then extracted and related to the scores. The framework was applied to GPT-3.5, GPT-4.1, GPT-5-mini, and Llama 2, 3, and 4 models on the ASAP and DREsS datasets to compare LLM scores with human ratings and examine how feedback sentiment and essay characteristics relate to assigned scores. (Jerin George Mathew et al. (2026))
- **Three-layered assessment framework for evaluating LLMs in essay assessment**: A framework the article operationalizes to evaluate LLM essay scoring along three layers: consistency and reliability evaluation, human-LLM alignment analysis, and causal discovery analysis. Consistency assesses whether a model "maintains stable relative rankings of essay quality across repeated runs using identical prompts", while reliability captures absolute agreement of numeric outputs across runs; alignment serves as a measure of external validity against expert judgments; and causal discovery identifies "causal relationships between linguistic features and predicted scores". The article applies it to five LLMs scoring 60 higher-education essays. (Tongxi Liu et al. (2026))

### Claims

- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](../claims/llm-feedback-sentiment-tracks-scores.md) [+M] — (also cited [~W])
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](../claims/llm-essay-scoring-weak-human-agreement.md) [+M]
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](../claims/llama-strongest-human-llm-alignment-claude-weakest.md) [+M]
- [Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity](../claims/llm-causal-feature-dependencies-lexical-versus-syntactic.md) [+M]
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](../claims/gpt4-essay-score-inflation.md) [~W]
- [Implicit demographic conditioning inflates AES scores in some models, with Llama-70B scores rising 1.57 points over its own default, while GPT models remain stable](../claims/implicit-conditioning-inflates-aes-scores-llama-70b.md) [~W]
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](../claims/llm-high-consensus-agreement-circularity-risk.md) [~W]
- [ML-based scoring approaches more often overestimated expert-assigned scores, whereas LLM-based approaches more often underestimated them](../claims/ml-overestimates-llm-underestimates-pattern.md) [~W]
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](../claims/full-scale-llms-outperform-mini-nano-grading.md) [~W]
- [Teachers systematically assign higher grades than all evaluated LLM grading models](../claims/teachers-grade-higher-than-all-llm-models.md) [~W]
- [Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences](../claims/sliding-window-controls-document-length-effects.md) [~W]

## Related Research Methods
-

## Key Sources
- Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714
- Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565
