---
type: claim
title: Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric
description: Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric
id: model-scale-not-predictor-lora-scoring
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: john-maurice-gayed-2026
    resource: "https://arxiv.org/abs/2606.12801"
    title: "John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801"
    author: John Maurice Gayed
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` With identical training data (120 essays) and identical LoRA hyperparameters, Gemma-3-27B achieves lower RMSE (0.474 vs. 0.512), lower MAE (0.335 vs. 0.379), higher QWK (0.828 vs. 0.777), and higher ±0.5 agreement (90.56% vs. 87.22%) than LLaMA-3.3-70B. [→ John Maurice Gayed 2026](#john-maurice-gayed-2026)

## Evidence

### John Maurice Gayed 2026

John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801

`q2 · i?` · `causal · r2`

Head-to-head comparison of the two LoRA-adapted open-weight models on the 360-essay held-out test set, both evaluated under the same Q4_K_M quantisation. The article reports that "the 27B-parameter Gemma model outperforms the 70B-parameter LLaMA model across every metric we computed."

> "Under identical training data (120 essays) and identical LoRA hyperparameters, the 27B-parameter Gemma model outperforms the 70B-parameter LLaMA model across every metric we computed: lower RMSE (0.474 vs. 0.512), lower MAE (0.335 vs. 0.379), higher QWK (0.828 vs. 0.777), and higher±0.5 agreement (90.56% vs. 87.22%)."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
