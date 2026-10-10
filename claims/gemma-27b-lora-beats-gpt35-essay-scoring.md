---
type: claim
title: A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics
description: A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics
id: gemma-27b-lora-beats-gpt35-essay-scoring
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
    kind: design
    rigour: 2
---

# A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the same 360-essay held-out test set, the fine-tuned Gemma model achieves RMSE 0.474, QWK 0.828, and 90.56% agreement within ±0.5, surpassing the fine-tuned GPT-3.5 baseline (RMSE 0.573, QWK 0.78, agreement 84.72%). [→ John Maurice Gayed 2026](#john-maurice-gayed-2026)

## Evidence

### John Maurice Gayed 2026

John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801

`q2 · i?` · `design · r2`

Evaluation on the 360-essay held-out test set of the ETS TOEFL Independent Writing corpus, with both open-weight models fine-tuned on the same 120 essays under identical LoRA hyperparameters. The Gemma model shows "RMSE of 0.474 represents a 17.2% reduction relative to the GPT-3.5 baseline (0.573)" and QWK 0.828 vs 0.78.

> "The fine-tuned Gemma model achieves the best performance across all metrics. Its RMSE of 0.474 represents a 17.2% reduction relative to the GPT-3.5 baseline (0.573), and its QWK of 0.828 exceeds the 0.78 reported by Wang and Gayed [2024] for the same GPT-3.5 fine-tuning approach on the same dataset."

## Discussion


## Related Claims
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
