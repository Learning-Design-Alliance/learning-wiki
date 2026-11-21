---
type: claim
title: Practical on-device LLM deployment is limited to roughly 4-billion-parameter models because memory grows nearly linearly and generation speed drops sharply beyond that size
description: Practical on-device LLM deployment is limited to roughly 4-billion-parameter models because memory grows nearly linearly and generation speed drops sharply beyond that size
id: on-device-deployment-limited-4b-parameters
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

# Practical on-device LLM deployment is limited to roughly 4-billion-parameter models because memory grows nearly linearly and generation speed drops sharply beyond that size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under 8-bit quantization, peak inference memory rises nearly linearly with model size, and token generation speed declines sharply beyond the 4-billion-parameter threshold, leaving few model-device combinations above 10 tokens per second. [→ Asghar Ghorbani 2025](#asghar-ghorbani-2025)

## Evidence

### Asghar Ghorbani 2025

Asghar Ghorbani, Hanieh Fattahi. (2025). Bridging the Digital Divide: Small Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions. arXiv. [doi:10.1364/opn.36.9.000028](https://doi.org/10.1364/opn.36.9.000028)

`q2 · i?` · `theoretical · r2`

Benchmark analysis using AI Phone Leaderboard data (Figs. 3-4) shows "peak memory usage during inference increases nearly linearly with model size under 8-bit quantization"; the article adds that practical deployment is largely limited to models of roughly 4 billion parameters or fewer.

> "peak memory usage during inference increases nearly linearly with model size under 8-bit quantization"

## Discussion


## Related Claims
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — reports the opposite
- [A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible](quantized-local-teacher-llm-feasible.md) — reports the opposite
- [A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour](llmersion-feasibility-stack-pace-cost.md) — reports the opposite
- [LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance](llm-grading-performance-scales-with-parameters.md) — related
- [Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning](quantization-raises-hallucination-rate-finetuning-mitigates.md) — related
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
- [Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization](quantization-aware-finetuning-recovers-accuracy.md) — related
