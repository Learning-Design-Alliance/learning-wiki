---
type: claim
title: "The most energy-efficient tested configuration consumes 1.8 mWh per query, a 43.8% reduction relative to the Qwen-7B FP16 baseline"
description: "The most energy-efficient tested configuration consumes 1.8 mWh per query, a 43.8% reduction relative to the Qwen-7B FP16 baseline"
id: energy-efficient-configuration-1-8-mwh-per-query
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: shen-x-2026
    title: Shen X 2026
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The most energy-efficient tested configuration consumes 1.8 mWh per query, a 43.8% reduction relative to the Qwen-7B FP16 baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` DeepSeek-MoE (Ours) consumes 1.8 mWh per query (1.8 Wh per 1,000 queries), 43.8% less than the Qwen-7B FP16 baseline of 3.2 mWh/query. [→ Shen X 2026](#shen-x-2026)

## Evidence

### Shen X 2026

Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444

`q2 · i?` · `design · r2`

Energy efficiency analysis (Section 5.3) with GPU-level measurements at the device rail, idle power subtracted, 10 Hz sampling. The article reports "1.8 mWh per query" and the 43.8% reduction. No standardized effect size applies.

> "Our most energy-efficient configuration, DeepSeek-MoE (Ours), consumes 1.8 mWh per query, equivalent to 1.8 Wh per 1,000 queries, representing a 43.8% reduction relative to the Qwen-7B FP16 baseline (3.2 mWh/query)"

## Discussion


## Related Claims
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — related
- [The prototype maintains total end-to-end latency of 3-5 seconds between query completion and RAG-generated response delivery](hdr-vr-platform-3-5-second-latency.md) — related
- [Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review](round2-candidates-pass-speed-gate.md) — related
