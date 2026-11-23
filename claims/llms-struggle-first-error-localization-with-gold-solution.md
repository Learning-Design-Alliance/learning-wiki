---
type: claim
title: State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution
description: State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution
id: llms-struggle-first-error-localization-with-gold-solution
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

# State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Providing the gold solution increases first-error-step localization accuracy over using only the problem and student solution, but most models still fail to pinpoint the exact error step. [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `causal · r2`

Benchmark experiment on VtG and PRM800K with six LLMs under three prompt settings; Table 1 reports accuracies such as Llama3.1-405B at 62.38% on VtG and 39.54% on PRM800K with the gold solution, showing "most models still struggle to pinpoint the exact error step".

> "Although providing the gold solution (w-GS) increases accuracy, most models still struggle to pinpoint the exact error step (see RQ1)."

## Discussion


## Related Claims
- [Supplying an LLM-generated corrected student solution improves first-error localization over the gold solution, especially for more capable models](corrected-student-solution-improves-error-localization.md) — related
- [Providing official reference solutions consistently reduces LLM marking error on structured physics questions](official-solutions-reduce-llm-marking-error.md) — related
- [Qwen2.5-72B-Math, tuned for problem solving rather than critique, drops in accuracy with gold and corrected solutions and often fails to rectify the first error in its corrections](qwen-math-hallucinates-corrections-error-localization.md) — a narrower finding that bears on this claim
