---
type: research-method
id: two-stage-llm-misconception-identification-pipeline
title: Two-stage LLM misconception identification pipeline
description: "A pipeline combining quantitative quiz analysis with two LLM stages: GPT-4 (gpt-4o-2024-08-06, temperature 0.3) generates hypothesized misconceptions from structured question representations, most common incorrect answers, and Whisper-transcribed lecture transcripts; Gemini 2.0 Flash (temperature 0)"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Two-stage LLM misconception identification pipeline

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A pipeline combining quantitative quiz analysis with two LLM stages: GPT-4 (gpt-4o-2024-08-06, temperature 0.3) generates hypothesized misconceptions from structured question representations, most common incorrect answers, and Whisper-transcribed lecture transcripts; Gemini 2.0 Flash (temperature 0) creates topic synopses from titles and transcripts for instructors. The total LLM cost was minimal, "with the misconceptions work requiring only approximately one dollar and the topic synopsis work requiring one cent". The pipeline ran on an ordinary laptop via cloud APIs.

## Accounts
<!-- How each source describes or uses the method -->
- **Two-stage LLM misconception identification pipeline (GPT-4 misconception analysis plus Gemini topic synopses)**: A pipeline combining quantitative quiz analysis with two LLM stages: GPT-4 (gpt-4o-2024-08-06, temperature 0.3) generates hypothesized misconceptions from structured question representations, most common incorrect answers, and Whisper-transcribed lecture transcripts; Gemini 2.0 Flash (temperature 0) creates topic synopses from titles and transcripts for instructors. The total LLM cost was minimal, "with the misconceptions work requiring only approximately one dollar and the topic synopsis work requiring one cent". The pipeline ran on an ordinary laptop via cloud APIs. (Parker et al. (2025))

### Claims

- [LLM-generated misconceptions grounded in quiz content, response patterns, and lecture transcripts are rated excellent by subject matter experts](../claims/llm-misconceptions-rated-excellent-by-experts.md) [+M]
- [LLM misconception analysis that ties student errors to instructional content reveals insights not apparent from performance data alone](../claims/llm-misconception-analysis-reveals-insights-beyond-performance-data.md) [+W]

## Related Research Methods
-

## Key Sources
- Parker, M. J., & Zavala-Cerna, M. G. (2025). What Don't You Understand? Using Large Language Models to Identify and Characterize Student Misconceptions About Challenging Topics. https://arxiv.org/abs/2507.09875. [doi:10.48550/arxiv.2605.00294](https://doi.org/10.48550/arxiv.2605.00294)
