---
type: claim
title: GenAI personalised test allocation aligns better with a mathematical score-weighting model than with expert allocations, which it misses by a mean error of 1.81
description: GenAI personalised test allocation aligns better with a mathematical score-weighting model than with expert allocations, which it misses by a mean error of 1.81
id: genai-personalisation-mathematical-model-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: riya-gill-2025
    resource: "https://doi.org/10.1108/aiie-05-2025-0088"
    title: "Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)"
    author: Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: riya-gill-2025-2
    resource: "https://doi.org/10.1108/aiie-05-2025-0088"
    title: "Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)"
    author: Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GenAI personalised test allocation aligns better with a mathematical score-weighting model than with expert allocations, which it misses by a mean error of 1.81

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 50 simulated users, the platform's question allocation error was lower against the mathematical benchmark (mean 1.31) than against the expert benchmark (mean 1.81). [→ Riya Gill 2025](#riya-gill-2025)
`q2 i?` 48% of tests had allocation errors greater than 2 against the expert benchmark versus 34% against the mathematical model, indicating gaps in contextual prioritisation. [→ Riya Gill 2025 (2)](#riya-gill-2025-2)

## Evidence

### Riya Gill 2025

Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)

`q2 · i?` · `design · r2`

Simulation assessing personalised question distribution for 50 simulated users with different performance scores over three topics, benchmarked against a mathematical weighting model and an expert allocation using mean allocation error. The article reports "a mathematical model benchmark mean error of 1.31" versus 1.81 for the expert.

> "The results of the calculation showed a mathematical model benchmark mean error of 1.31 with a standard deviation of 0.96, and the expert benchmark mean error of 1.81, with a standard deviation of 1.18."

### Riya Gill 2025 (2)

Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)

`q2 · i?` · `design · r2`

Error distribution analysis from the same 50-simulated-user personalisation evaluation. The article reports "48% of tests had errors >2 against the expert, versus 34% against the model", attributing the gap to experts prioritising risk-critical topics while the GenAI relied solely on performance scores.

> "In addition, the error distribution showed that 48% of tests had errors >2 against the expert, versus 34% against the model, underscoring gaps in contextual prioritisation."

## Discussion


## Related Claims
- [GenAI-generated question-specific and overall test feedback is rated 98-99% positive, helpful, and accurate by both model and expert evaluators](genai-feedback-high-quality-ratings.md) — related
- [Students perceive personalised simulation with adaptive scenario complexity and targeted role allocation as supporting professional confidence and role development](personalised-simulation-confidence-role-development.md) — related
- [GenAI-generated driving theory questions show strong model-expert agreement on accuracy and relevancy, with the model slightly outperforming the expert on weighted average](genai-question-accuracy-relevancy-strong-agreement.md) — related
