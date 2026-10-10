---
type: claim
title: "LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust"
description: "LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust"
id: lora-rank-sensitivity-architecture-dependent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: john-maurice-gayed-2026
    resource: "https://arxiv.org/abs/2606.12801"
    title: "John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801"
    author: John Maurice Gayed
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`

## Subclaims
`q1 i?` During pilot experiments, raising LoRA rank above 64 caused LLaMA to return only a numeric score and omit the JSON reasoning field entirely, while Gemma maintained both scoring accuracy and feedback quality across the same rank range. [→ John Maurice Gayed 2026](#john-maurice-gayed-2026)

## Evidence

### John Maurice Gayed 2026

John Maurice Gayed. (2026). AiAWE: An Open-Source LLM Automated Writing Evaluation System Using LoRA-Adapted Instruction-Tuned Models. A PREPRINT. https://arxiv.org/abs/2606.12801

`q1 · i?` · `causal · r1`

Qualitative observation from the authors' pilot experiments during fine-tuning, not a controlled benchmark. The article reports that "increasing LoRA rank above 64 caused the LLaMA model to lose its ability to produce qualitative rubric-referenced feedback."

> "Specifically, during pilot experiments we observed that increasing LoRA rank above 64 caused the LLaMA model to lose its ability to produce qualitative rubric-referenced feedback: it would return a numeric score but omit the JSON reasoning field entirely, effectively “forgetting” how to follow the part of the instruction that required structured narrative output."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Three LLMs fine-tuned on teacher-validated feedback reach reported training losses with qualitative teacher validation](aicofe-llm-finetuning-training-results.md) — related
- [LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring](lora-parameter-efficiency-drawing-scoring.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
