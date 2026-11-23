---
type: claim
title: LLM problem-solving ability has little bearing on error localization accuracy
description: LLM problem-solving ability has little bearing on error localization accuracy
id: problem-solving-ability-weakly-correlated-error-localization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kv-aditya-srivatsa-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.553"
    title: "KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)"
    author: KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM problem-solving ability has little bearing on error localization accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A chi-squared test finds error localization and problem-solving accuracy only weakly correlated across models and prompts. [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `causal · r2`

Chi-squared test on a 2×2 contingency table across models, datasets, and prompt types, reported in §4.2 and §C.3; the article states the two are "weakly correlated (p > 0.01; ϕ < 0.2)".

> "A chi-squared test for independence confirms that error localization and problem-solving accuracy are weakly correlated (p > 0.01; ϕ < 0.2) across models and prompts"

## Discussion


## Learner Variables
- [Problem Solving](../learner-variables/problem-solving.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)](model-capability-negatively-correlates-sfs.md) — related
