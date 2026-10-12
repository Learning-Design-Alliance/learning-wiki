---
type: research-method
id: harmogen-r-a-two-stage-hybrid-framework-for-ai-rubric-generation-with-reasoning-enhanced-g
title: "HARMOGEN-R: a two-stage hybrid framework for AI rubric generation with reasoning-enhanced generation and low-temperature synthesis"
description: HARMOGEN-R (Hybrid Assessment Rubric Model Generation with Reasoning) is a two-stage rubric generation pipeline.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# HARMOGEN-R: a two-stage hybrid framework for AI rubric generation with reasoning-enhanced generation and low-temperature synthesis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
HARMOGEN-R (Hybrid Assessment Rubric Model Generation with Reasoning) is a two-stage rubric generation pipeline. In stage one, reasoning-capable LLMs generate several candidate rubrics under a high temperature setting "to promote variation in criterion formulation and scoring structure"; in stage two, a synthesis model from the same provider family consolidates the candidates into a single rubric at low temperature (T = 1.0 for generation, T = 0.1 for synthesis). It supports a structured mode, in which predefined criteria and point allocations from the human baseline are supplied, and a free-form mode, in which the model defines criteria autonomously. Implemented with OpenAI (o3-mini, GPT-4o) and DeepSeek (deepseek-r1-distill-llama-70b, deepseek-chat) families, it produced four AI rubric variants per assessment for comparison against a human-created baseline.

## Accounts
<!-- How each source describes or uses the method -->
- **HARMOGEN-R: a two-stage hybrid framework for AI rubric generation with reasoning-enhanced generation and low-temperature synthesis**: HARMOGEN-R (Hybrid Assessment Rubric Model Generation with Reasoning) is a two-stage rubric generation pipeline. In stage one, reasoning-capable LLMs generate several candidate rubrics under a high temperature setting "to promote variation in criterion formulation and scoring structure"; in stage two, a synthesis model from the same provider family consolidates the candidates into a single rubric at low temperature (T = 1.0 for generation, T = 0.1 for synthesis). It supports a structured mode, in which predefined criteria and point allocations from the human baseline are supplied, and a free-form mode, in which the model defines criteria autonomously. Implemented with OpenAI (o3-mini, GPT-4o) and DeepSeek (deepseek-r1-distill-llama-70b, deepseek-chat) families, it produced four AI rubric variants per assessment for comparison against a human-created baseline. (Pedro C. Mendonça et al. (2026))

### Claims
- [When applied by human evaluators, all four AI-generated rubrics met pooled scoring equivalence with a human-created baseline within a ±5-point margin](../claims/ai-rubrics-pooled-equivalence-human-evaluators.md) [+M]
- [Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form](../claims/open-weight-proprietary-rubric-equivalence.md) [+M]

## Related Research Methods
-

## Key Sources
- Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663
