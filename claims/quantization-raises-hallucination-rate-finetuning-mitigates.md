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
newest_evidence: 2026
recheck_by: 2029
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
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

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
- [Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models](higher-bit-quantisation-preserves-semantic-structure-pidgin-llm.md) — related
- [A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible](quantized-local-teacher-llm-feasible.md) — related
