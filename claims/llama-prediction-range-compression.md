---
type: claim
title: "LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth"
description: "LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth"
id: llama-prediction-range-compression
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

# LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` LLaMA never predicts below 2.0 and assigns 85 essays a score of 4.0 but only 16 at 4.5 and 2 at 5.0, despite ground truth containing 46 and 25 essays at those levels; Gemma's prediction distribution more closely mirrors the ground truth. [→ John Maurice Gayed 2026](#john-maurice-gayed-2026)

## Evidence

### John Maurice Gayed 2026

John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801

`q2 · i?` · `design · r2`

Prediction frequency distribution analysis (Table 6) on the 360-essay held-out test set against the ETS ground-truth distribution. The article reports that "Gemma maintains a broader and more balanced prediction distribution that more closely mirrors the ground truth."

> "LLaMA’s prediction distribution reveals a notable compression of the upper score range: it assigns 85 essays a score of 4.0 but only 16 at 4.5 and just 2 at 5.0, despite the ground truth containing 46 and 25 essays at those levels respectively."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring](lora-parameter-efficiency-drawing-scoring.md) — related
