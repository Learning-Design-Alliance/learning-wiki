---
type: claim
title: Qwen3.5-35B-A3B offered the best throughput and memory balance of three open-source LLMs benchmarked on consumer-grade hardware for translation
description: Qwen3.5-35B-A3B offered the best throughput and memory balance of three open-source LLMs benchmarked on consumer-grade hardware for translation
id: qwen-selected-optimal-throughput-memory-balance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: morris-2026
    resource: "https://doi.org/10.48550/arXiv.2609.35830"
    title: "Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. [doi:10.48550/arXiv.2609.35830](https://doi.org/10.48550/arXiv.2609.35830)"
    author: Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Qwen3.5-35B-A3B offered the best throughput and memory balance of three open-source LLMs benchmarked on consumer-grade hardware for translation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In local hardware benchmarks, Qwen3.5-35B-A3B ran at ~28 tokens/sec within ~13.4 GB VRAM, versus ~8 tokens/sec and >16 GB for Llama-3-70B and ~15 tokens/sec for DeepSeek-R1-32B, leading to its selection. [→ Morris 2026](#morris-2026)

## Evidence

### Morris 2026

Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. [doi:10.48550/arXiv.2609.35830](https://doi.org/10.48550/arXiv.2609.35830)

`q2 · i?` · `design · r2`

Benchmark study reported in the model-selection subsection, run on a single NVIDIA RTX 4070 Ti Super GPU (16 GB VRAM) with quantized models. Table 1 prints baseline accuracy ~80% for all three models and the throughputs quoted; the comparison is throughput and memory, not translation quality.

> "The Qwen3.5-35B-A3B model achieved the most optimal operational balance. This is due to its efficient attention architecture and native compatibility with low-bit frameworks (such as FlashAttention-2 [9] via llama.cpp [10]), it operated stably near the 16 GB VRAM ceiling (~13.4 GB) while maintaining a high throughput of ~28 tokens/sec."

## Discussion


## Related Claims
- [A complete four-skill open-model stack fits under 4 GB, runs at reading pace on the cheapest hardware by community measurements, and costs about one US cent of electricity per study hour](llmersion-feasibility-stack-pace-cost.md) — related
- [The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference](elevate-local-two-machine-low-latency-deployment.md) — related
- [Practical on-device LLM deployment is limited to roughly 4-billion-parameter models because memory grows nearly linearly and generation speed drops sharply beyond that size](on-device-deployment-limited-4b-parameters.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%](rag-llm-translation-accuracy-above-95-percent.md) — related
