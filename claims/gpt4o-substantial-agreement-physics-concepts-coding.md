---
type: claim
title: "GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization"
description: "GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization"
id: gpt4o-substantial-agreement-physics-concepts-coding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After optimizing model hyperparameters and prompts, GPT-4o coded the domain-specific Physics Concepts theme with Cohen's κ = 0.7, showing remarkable agreement with human raters coding to consensus. [→ Nikhil Sanjay Borse 2025](#nikhil-sanjay-borse-2025)

## Evidence

### Nikhil Sanjay Borse 2025

Nikhil Sanjay Borse, Ravishankar Chatta Subramaniam, and N. Sanjay Rebello. (2025). Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis. arXiv:2508.14764. [doi:10.1119/perc.2025.pr.borse](https://doi.org/10.1119/perc.2025.pr.borse)

`q2 · i?` · `design · r2`

Reliability study comparing GPT-4o and GPT-4.5 coding of 204 text segments from 14 student-group transcripts against two human raters coding to consensus, using Cohen's κ. For the Physics Concepts theme the optimized model reached "Cohen's κ = 0.7", which the authors attribute to the objective clarity of the PC criteria.

> "For PC, Cohen's κ = 0.7, which showed remarkable agreement with human raters. This can be due to the objective clarity of the PC criteria, making them easier to rate for both LLMs and human raters [34]."

## Discussion


## Related Claims
- [Prompt polishing and hyperparameter optimization significantly increased LLM–human agreement across all four themes](llm-optimization-increases-inter-rater-reliability.md) — a broader claim this one bears on
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) — related
- [Optimal LLM hyperparameter settings peaked at Temperature = 1.1 and top-p = 0.8, with domain-specific themes favoring lower values](hyperparameter-optima-vary-by-theme.md) — related
- [GPT-4o performed best on domain-specific themes (PC, MC) while GPT-4.5 performed better on Engineering Design](model-choice-moderates-llm-coding-agreement.md) — related
- [An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).](llm-grader-substantial-agreement-human-consensus.md) — related
- [The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting](gradeopt-substantial-agreement-pck-outperforms-baselines.md) — related
- [LLMs reached only moderate agreement with human raters on Metacognitive Thinking, a non-domain-specific theme](llms-moderate-only-metacognitive-thinking.md) — related
