---
type: claim
title: Modern SLMs around 3B parameters match or exceed earlier-generation LLMs on the MMLU benchmark, including STEM subjects
description: Modern SLMs around 3B parameters match or exceed earlier-generation LLMs on the MMLU benchmark, including STEM subjects
id: slms-match-legacy-llms-mmlu
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: asghar-ghorbani-2025
    resource: "https://doi.org/10.1364/opn.36.9.000028"
    title: "Asghar Ghorbani, Hanieh Fattahi. (2025). Bridging the Digital Divide: Small Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions. arXiv. [doi:10.1364/opn.36.9.000028](https://doi.org/10.1364/opn.36.9.000028)"
    author: Asghar Ghorbani, Hanieh Fattahi
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Modern SLMs around 3B parameters match or exceed earlier-generation LLMs on the MMLU benchmark, including STEM subjects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Recent SLMs such as Qwen2.5 and DeepSeekMath outperform many legacy LLMs on MMLU while remaining deployable on edge devices; Qwen2.5-3B exceeds a score of 65. [→ Asghar Ghorbani 2025](#asghar-ghorbani-2025)

## Evidence

### Asghar Ghorbani 2025

Asghar Ghorbani, Hanieh Fattahi. (2025). Bridging the Digital Divide: Small Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions. arXiv. [doi:10.1364/opn.36.9.000028](https://doi.org/10.1364/opn.36.9.000028)

`q2 · i?` · `theoretical · r2`

Benchmark evaluation on MMLU, a 57-subject multiple-choice benchmark including mathematics, physics, and chemistry (Fig. 7), shows "well optimized Small Language Models (SLMs) such as Qwen 2.5 and DeepSeekMath outperform many legacy large language models (LLMs)"; Qwen2.5-3B exceeds a score of 65.

> "well optimized Small Language Models (SLMs) such as Qwen 2.5 and DeepSeekMath outperform many legacy large language models (LLMs) while remaining lightweight enough for deployment on edge devices"

## Discussion


## Related Claims
- [At 30K and 60K data scales, AgenticMath outperforms all compared baselines across four base models on six math benchmarks](agenticmath-sota-at-small-data-scales.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
