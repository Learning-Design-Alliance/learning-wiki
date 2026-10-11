---
type: claim
title: "DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set"
description: "DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set"
id: deepseek-moe-ours-strongest-accuracy-balance
status: draft
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

# DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The quantization-aware fine-tuned DeepSeek-MoE configuration achieves 78.6% overall accuracy and 81.2% multi-hop reasoning accuracy, significantly better than the RAG no-fine-tuning baseline (66.6%). [→ Shen X 2026](#shen-x-2026)

## Evidence

### Shen X 2026

Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444

`q2 · i?` · `design · r2`

Benchmark comparison on the study's n = 300 OER-derived query evaluation set (105 factual recall, 135 concept explanation, 60 multi-hop), with McNemar's test against the RAG no-fine-tuning baseline and Holm–Bonferroni correction. The article reports "DeepSeek-MoE (Ours) reaches 78.6% (+12.0 pp., p < 0.001)". No standardized effect size is printed.

> "the RAG (no fine-tuning) baseline achieves 66.6% overall accuracy, while Qwen-7B (Ours) reaches 69.8% (+3.2 pp., p = 0.031) and DeepSeek-MoE (Ours) reaches 78.6% (+12.0 pp., p < 0.001)"

## Discussion


## Related Claims
- [Quantization-aware fine-tuning narrows the FP16-to-4-bit accuracy gap and partially recovers accuracy lost to standard 4-bit quantization](quantization-aware-finetuning-recovers-accuracy.md) — related
- [Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning](quantization-raises-hallucination-rate-finetuning-mitigates.md) — related
- [The most energy-efficient tested configuration consumes 1.8 mWh per query, a 43.8% reduction relative to the Qwen-7B FP16 baseline](energy-efficient-configuration-1-8-mwh-per-query.md) — related
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline](retrieval-augmentation-essential-local-llm-below-tfidf.md) — related
