---
type: claim
title: Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization
description: Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization
id: quantization-aware-finetuning-recovers-accuracy
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

# Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Quantization-aware fine-tuning reduces the FP16-to-4-bit accuracy gap from 4.2 to 1.7 percentage points for Qwen-7B and from 2.9 to 1.2 percentage points for DeepSeek-MoE. [→ Shen X 2026](#shen-x-2026)

## Evidence

### Shen X 2026

Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444

`q2 · i?` · `design · r2`

Results section analysis of Table 3 accuracy data (n = 300 queries) comparing FP16, standard 4-bit, and quantization-aware fine-tuned variants of both model families. The article reports the gap reduction "from 4.2 pp. to 1.7 pp. for Qwen-7B". No standardized effect size is printed.

> "Our quantization-aware fine-tuning reduces the FP16-to-4-bit accuracy gap from 4.2 pp. to 1.7 pp. for Qwen-7B, and from 2.9 pp. to 1.2 pp. for DeepSeek-MoE (see Figure 2)"

## Discussion


## Related Claims
- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — related
- [Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning](quantization-raises-hallucination-rate-finetuning-mitigates.md) — related
