---
type: claim
title: Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict
description: Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict
id: score-wise-bias-regression-to-mean-awe
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

# Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both models over-predict low scores (positive bias at 1.0–2.5) and underpredict high scores (negative bias at 3.5–5.0), a pattern the authors link to class imbalance; error increases monotonically above score 3.0, with Gemma RMSE 0.671 and LLaMA 0.781 at score 5.0. [→ John Maurice Gayed 2026](#john-maurice-gayed-2026)

## Evidence

### John Maurice Gayed 2026

John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801

`q2 · i?` · `design · r2`

Score-wise error analysis (RMSE, MAE, mean signed bias per ETS score level) on the 360-essay held-out set, reported in Table 5. The article notes the pattern "is exacerbated by class imbalance, scores of 1.0 and 1.5 together account for only 4 of the 360 test essays, while the 3.0 bin alone contains 103."

> "Both models exhibit the classic pattern expected in constrained regression tasks: they over-predict low scores (positive bias at 1.0–2.5) and underpredict high scores (negative bias at 3.5–5.0)."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies](counterfactual-fine-tuning-reduces-sentiment-bias.md) — related
- [Sentiment scores of LLM-generated replies differ significantly from human replies under both classifiers](llm-vs-human-sentiment-significant-difference.md) — related
