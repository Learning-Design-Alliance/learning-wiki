---
type: claim
title: Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning
description: Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning
id: quantization-raises-hallucination-rate-finetuning-mitigates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shen-x-2026
    title: Shen X 2026
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Hallucination rate rises from 8.6% to 12.3% for Qwen-7B and from 7.2% to 10.4% for DeepSeek-MoE under 4-bit quantization; fine-tuned versions score 9.8% and 8.1%. [→ Shen X 2026](#shen-x-2026)

## Evidence

### Shen X 2026

Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444

`q2 · i?` · `design · r2`

Hallucination rates (Section 5.2, Table 5) measured via a two-stage NLI procedure over the full n = 300 evaluation set, calibrated on a 50-response pilot at κ = 0.76. The article reports rates rising "from 8.6 to 12.3%" for Qwen-7B. No standardized effect size is printed.

> "hallucination rate increases under quantization (Qwen-7B: 8.6 to 12.3%; DeepSeek-MoE: 7.2–10.4%), with fine-tuning substantially mitigating this risk (Qwen-7B Ours: 9.8%; DeepSeek-MoE Ours: 8.1%)"

## Discussion


## Related Claims
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — related
- [Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization](quantization-aware-finetuning-recovers-accuracy.md) — related
