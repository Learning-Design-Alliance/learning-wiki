---
type: claim
title: "Combining human and LLM-generated responses at a 1:1 ratio yields more accurate educational item calibration"
description: "Combining human and LLM-generated responses at a 1:1 ratio yields more accurate educational item calibration"
id: human-synthetic-1to1-mix-improves-item-calibration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: luis-marquez-carpintero-2025
    resource: "https://arxiv.org/abs/2511.06078"
    title: "Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078"
    author: Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Combining human and LLM-generated responses at a 1:1 ratio yields more accurate educational item calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`

## Subclaims
`q2 i?` An IRT-based study found that mixing human and synthetic responses at a 1:1 ratio produced more accurate item calibration than synthetic responses alone, though high-performing LLMs showed narrower zones of ZPD limiting reflection of human variability. [→ Luis Marquez-Carpintero 2025](#luis-marquez-carpintero-2025)

## Evidence

### Luis Marquez-Carpintero 2025

Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078

`q2 · i?` · `review · r2`

The review reports an Item Response Theory study by Liu et al. [2025] testing six LLMs (GPT-3.5, GPT-4, LLaMA 2, LLaMA 3, Gemini-Pro, Cohere Command R Plus) on 20 university-level algebra questions, comparing estimated model ability against real students. No effect size is printed.

> "However, combining human and synthetic responses at a 1:1 ratio resulted in more accurate item calibration, suggesting that LLMs can serve as an effective complement in educational assessment."

## Discussion


## Related Claims
- [Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation](iea-ba-reduce-difficulty-estimate-bias.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — related
