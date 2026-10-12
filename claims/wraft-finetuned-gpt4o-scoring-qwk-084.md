---
type: claim
title: Fine-tuned GPT-4o achieves state-of-the-art scoring of TOEFL argumentative essays with QWK 0.84 and RMSE 0.44 against official scores
description: Fine-tuned GPT-4o achieves state-of-the-art scoring of TOEFL argumentative essays with QWK 0.84 and RMSE 0.44 against official scores
id: wraft-finetuned-gpt4o-scoring-qwk-084
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: adnan-labib-2026
    resource: "https://arxiv.org/abs/2607.14524"
    title: "Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524"
    author: Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned GPT-4o achieves state-of-the-art scoring of TOEFL argumentative essays with QWK 0.84 and RMSE 0.44 against official scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On a 360-essay test subset, the fine-tuned GPT-4o model scored essays with QWK 0.84 and RMSE 0.44 on the 0-5 scale, outperforming fine-tuned LLaMA-3.3-70B and the Wang and Gayed (2024) baseline. [→ Adnan Labib 2026](#adnan-labib-2026)

## Evidence

### Adnan Labib 2026

Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524

`q2 · i?` · `design · r2`

Benchmark evaluation of two fine-tuned models (GPT-4o, LLaMA-3.3-70B-Instruct) on the 360-essay test subset, using RMSE, QWK and percentage agreement. Table 5 reports GPT-4o at "0.84" QWK and 0.44 RMSE, exceeding the ETS 0.7 QWK benchmark for e-rater.

> "Results indicate SOTA performance of our two fine-tuned models in scoring accuracy and reliability, with GPT-4o consistently performing the best across all three evaluation metrics."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
