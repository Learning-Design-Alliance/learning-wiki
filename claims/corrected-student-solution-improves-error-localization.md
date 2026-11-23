---
type: claim
title: Supplying an LLM-generated corrected student solution improves first-error localization over the gold solution, especially for more capable models
description: Supplying an LLM-generated corrected student solution improves first-error localization over the gold solution, especially for more capable models
id: corrected-student-solution-improves-error-localization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
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

# Supplying an LLM-generated corrected student solution improves first-error localization over the gold solution, especially for more capable models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The corrected student solution prompt setting (w-Cor) yields the highest accuracy across most models on both datasets, improving over the gold-solution setting. [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `causal · r2`

Benchmark experiment across six LLMs on VtG and PRM800K; Table 1 shows w-Cor accuracies such as Llama3.1-405B at 64.77% (VtG) and 47.86% (PRM800K), where "The corrected solution (w-Cor) improves performance over w-GS".

> "The corrected solution (w-Cor) improves performance over w-GS and yields the highest accuracy across most models for both datasets (see RQ2)."

## Discussion


## Related Claims
- [Qwen2.5-72B-Math, tuned for problem solving rather than critique, drops in accuracy with gold and corrected solutions and often fails to rectify the first error in its corrections](qwen-math-hallucinates-corrections-error-localization.md) — reports the opposite
- [State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution](llms-struggle-first-error-localization-with-gold-solution.md) — related
