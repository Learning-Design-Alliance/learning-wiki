---
type: claim
title: Qwen2.5-72B-Math, tuned for problem solving rather than critique, drops in accuracy with gold and corrected solutions and often fails to rectify the first error in its corrections
description: Qwen2.5-72B-Math, tuned for problem solving rather than critique, drops in accuracy with gold and corrected solutions and often fails to rectify the first error in its corrections
id: qwen-math-hallucinates-corrections-error-localization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: mixed
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

# Qwen2.5-72B-Math, tuned for problem solving rather than critique, drops in accuracy with gold and corrected solutions and often fails to rectify the first error in its corrections

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qwen2.5-72B-Math records the lowest localization accuracies overall and even drops in w-GS and w-Cor compared to w/o-S, despite high problem-solving scores. [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `causal · r2`

Benchmark results in §4.1 and Table 1 (e.g., VtG w/o-S 45.01% vs w-Cor 19.10%) show Qwen2.5-72B-Math "records the lowest accuracies overall" while scoring highly in problem-solving.

> "In sharp contrast, Qwen2.5-72B-Math—tuned for problem solving rather than critique—records the lowest accuracies overall and even drops in both w-GS and w-Cor compared to w/o-S, while scoring highly in problem-solving on both datasets"

## Discussion


## Related Claims
- [Supplying an LLM-generated corrected student solution improves first-error localization over the gold solution, especially for more capable models](corrected-student-solution-improves-error-localization.md) — reports the opposite
- [State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution](llms-struggle-first-error-localization-with-gold-solution.md) — a broader claim this one bears on
