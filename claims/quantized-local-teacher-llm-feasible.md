---
type: claim
title: A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible
description: A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible
id: quantized-local-teacher-llm-feasible
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: hyeongdon-moon-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07040"
    title: "Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)"
    author: Hyeongdon Moon, Carolyn Rosé, and John Stamper
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` In this setup, the Teacher LLM generated and injected knowledge in the required format when guided by a carefully specified prompt, using a 4-bit quantized 27B local model rather than a large commercial API. [→ Hyeongdon Moon 2026](#hyeongdon-moon-2026)

## Evidence

### Hyeongdon Moon 2026

Hyeongdon Moon, Carolyn Rosé, and John Stamper. (2026). Cognitive Agent Compilation for Explicit Problem Solver Modeling. https://arxiv.org/abs/2605.07040 [doi:10.48550/arxiv.2605.07040](https://doi.org/10.48550/arxiv.2605.07040)

`q1 · i?` · `design · r2`

Authors' preliminary observation from the proof-of-concept setup (Section 5.2). The Teacher LLM was gemma-3-27b-it run locally with 4-bit quantization; the authors report it generated knowledge in the required format and note "further validation is required". No effect sizes are printed.

> "Notably, this was achieved using a 4-bit quantized 27B local model rather than a large commercial API. This observation suggests the possibility that similar pipelines could be implemented with relatively accessible resources, although further validation is required."

## Discussion


## Related Claims

- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — a broader claim this one bears on
- Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05 — related
- [Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models](higher-bit-quantisation-preserves-semantic-structure-pidgin-llm.md) — related
- [Model size defines a core trade-off: too-large SLMs answer without the cognitive structure while too-small SLMs break instruction-following coherence](curse-of-prior-knowledge-size-tradeoff.md)
- [An SLM executor under tight constraints can drive a Cognitive Agent through formatted outputs and logit-based action selection, yielding partial rather than full explainability](slm-executor-partial-explicit-control.md)
- [At the implementation checkpoint, several groups added an explicit human-approval step after encountering local-LLM structured-output reliability limitations](cp5-human-approval-step-added.md) — related
- [NF4 4-bit quantization reduces VRAM usage by 38.7% for Qwen-7B and 37.9% for DeepSeek-MoE while maintaining practical response times](nf4-quantization-vram-reduction.md) — related
- [Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning](quantization-raises-hallucination-rate-finetuning-mitigates.md) — related
