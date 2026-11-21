---
type: claim
title: "MLLM performance on image-based conceptual physics tasks varies widely, from 81.5% (GPT-5) down to 21% (Gemma 3-4b)"
description: "MLLM performance on image-based conceptual physics tasks varies widely, from 81.5% (GPT-5) down to 21% (Gemma 3-4b)"
id: mllm-physics-visual-performance-range-21-81-5
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: giulia-polverini-and-bor-gregorcic-2025
    resource: "https://doi.org/10.1088/1361-6404/ae03f8"
    title: "Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)"
    author: Giulia Polverini and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MLLM performance on image-based conceptual physics tasks varies widely, from 81.5% (GPT-5) down to 21% (Gemma 3-4b)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 15 models and 102 items, total benchmark accuracy spanned more than 60 percentage points, with GPT-5 highest at 81.5% and Gemma 3-4b lowest at 21.0%. [→ Giulia Polverini and Bor Gregorcic 2025](#giulia-polverini-and-bor-gregorcic-2025)

## Evidence

### Giulia Polverini and Bor Gregorcic 2025

Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)

`q2 · i?` · `design · r2`

Benchmark evaluation in which each of 102 screenshot items was submitted 10 times per model via APIs; results in Table 3 show "substantial variation in performance across models. GPT-5 was the best performing model (81.5%)" with Gemma 3-4b at 21.0%.

> "Overall, there is substantial variation in performance across models. GPT-5 was the best performing model (81.5%)."

## Discussion


## Related Claims
- [Freely available Gemma models occupy the bottom of the performance scale (21.0–35.5%) and are not competitive for physics visual tasks](free-gemma-models-not-competitive-physics-visual.md) — a narrower finding that bears on this claim
- [ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail](chatgpt-poor-image-inference-scientific-graphs.md) — related
