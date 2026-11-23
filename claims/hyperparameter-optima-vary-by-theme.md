---
type: claim
title: Optimal LLM hyperparameter settings peaked at Temperature = 1.1 and top-p = 0.8, with domain-specific themes favoring lower values
description: Optimal LLM hyperparameter settings peaked at Temperature = 1.1 and top-p = 0.8, with domain-specific themes favoring lower values
id: hyperparameter-optima-vary-by-theme
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
    kind: causal
    rigour: 1
---

# Optimal LLM hyperparameter settings peaked at Temperature = 1.1 and top-p = 0.8, with domain-specific themes favoring lower values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Trendlines of Cohen's κ averaged over 5 runs showed a clear peak at Temperature = 1.1 and top-p = 0.8; optimal settings were Temperature = top-p = 0.9 for the domain-specific themes PC and MC. [→ Nikhil Sanjay Borse 2025](#nikhil-sanjay-borse-2025)

## Evidence

### Nikhil Sanjay Borse 2025

Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. [doi:10.1119/perc.2025.pr.borse](https://doi.org/10.1119/perc.2025.pr.borse)

`q2 · i?` · `causal · r1`

Numerical hyperparameter sweep for the ED theme using GPT-4.5, with κ averaged over 5 runs per value; trendlines "show a clear peak at Temperature = 1.1 and top-p = 0.8". Table II lists Temperature = top-p = 0.9 for PC and MC.

> "Both distributions or trendlines show a clear peak at Temperature = 1.1 and top-p = 0.8, respectively. These values of Cohen'sκ were averaged over 5 runs for each hyperparameter value."

## Discussion


## Related Claims
- [GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization](gpt4o-substantial-agreement-physics-concepts-coding.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
- [Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes](llm-optimization-increases-inter-rater-reliability.md) — a broader claim this one bears on
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [GPT-4o performed best on domain-specific themes (PC, MC) while GPT-4.5 performed better on Engineering Design](model-choice-moderates-llm-coding-agreement.md) — related
