---
type: claim
title: Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes
description: Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes
id: llm-optimization-increases-inter-rater-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: nikhil-sanjay-borse-2025
    resource: "https://doi.org/10.1119/perc.2025.pr.borse"
    title: "Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. [doi:10.1119/perc.2025.pr.borse](https://doi.org/10.1119/perc.2025.pr.borse)"
    author: Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Compared with default OpenAI API settings, optimized settings and polished few-shot prompts increased the mean Cohen's κ of all themes by 0.14, a statistically significant increase (p < 0.02, Mann-Whitney test). [→ Nikhil Sanjay Borse 2025](#nikhil-sanjay-borse-2025)

## Evidence

### Nikhil Sanjay Borse 2025

Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. [doi:10.1119/perc.2025.pr.borse](https://doi.org/10.1119/perc.2025.pr.borse)

`q2 · i?` · `design · r2`

Five-run reliability analysis of LLM coding of 14 student-group transcripts, comparing default API settings with optimized settings and polished few-shot prompts. The article reports the average κ increase was "0.14" and statistically significant with "p < 0.02" by Mann-Whitney test.

> "The average increase in Cohen's κ of all themes was 0.14, which is a statistically significant increase (p < 0.02) using a Mann-Whitney test [48]."

## Discussion


## Related Claims
- [GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization](gpt4o-substantial-agreement-physics-concepts-coding.md) — a narrower finding that bears on this claim
- [Optimal LLM hyperparameter settings peaked at Temperature = 1.1 and top-p = 0.8, with domain-specific themes favoring lower values](hyperparameter-optima-vary-by-theme.md) — a narrower finding that bears on this claim
- [LLMs reached only moderate agreement with human raters on Metacognitive Thinking, a non-domain-specific theme](llms-moderate-only-metacognitive-thinking.md) — related
