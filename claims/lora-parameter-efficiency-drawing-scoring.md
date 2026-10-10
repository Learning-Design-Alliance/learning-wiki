---
type: claim
title: LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring
description: LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring
id: lora-parameter-efficiency-drawing-scoring
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: fang-2026
    resource: "https://arxiv.org/abs/2606.20264"
    title: "Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264"
    author: Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` LoRA updates only a small subset of parameters: 0.6M trainable parameters on the fixed 86.4M ViT backbone, while confidence-aware variants add no further trainable parameters. [→ Fang 2026](#fang-2026)

## Evidence

### Fang 2026

Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264

`q2 · i?` · `design · r2`

Model complexity analysis (Table 3): all approaches share the same 86.4M ViT backbone, so "performance differences are not attributable to model capacity"; confidence-aware scoring raises inference latency to about 20.5 ms versus about 1.03 ms.

> "LoRA introduces only 0.6M additional trainable parameters while keeping the backbone fixed, and the confidence-aware variants add no further trainable parameters."

## Discussion


## Related Claims
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
