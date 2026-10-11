---
type: claim
title: "Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1"
description: "Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1"
id: model-size-and-lora-rank-joint-effects
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shaowen-lu-2026
    resource: "https://arxiv.org/abs/2609.13918"
    title: "Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918"
    author: Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: shaowen-lu-2026-2
    resource: "https://arxiv.org/abs/2609.13918"
    title: "Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918"
    author: Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`

## Subclaims
`q2 i?` After LoRA fine-tuning at r=16, the 7B model's advantage increased on ROUGE-2 and ROUGE-L while the ROUGE-1 gap narrowed in favor of the 3B model. [→ Shaowen Lu 2026](#shaowen-lu-2026)
`q2 i?` A smaller model with higher-rank LoRA adaptation can outperform a larger model with lower-rank adaptation on some metrics. [→ Shaowen Lu 2026 (2)](#shaowen-lu-2026-2)

## Evidence

### Shaowen Lu 2026

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918

`q2 · i?` · `causal · r1`

Direct comparison of base models and r=16 fine-tuned models on the 54-item test set (Section 5.5). The article reports the 3B model narrowed the ROUGE-1 gap while the 7B model gained more on ROUGE-2 and ROUGE-L under the same LoRA setting.

> "The ROUGE-1 difference decreased from +0.0263 to +0.0148, indicating that the 3B model narrowed the lexical-overlap gap through LoRA adaptation. In contrast, the ROUGE-2 difference increased from +0.0199 to +0.0318, and the ROUGE-L difference increased from +0.0207 to +0.0317."

### Shaowen Lu 2026 (2)

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918

`q2 · i?` · `causal · r2`

Cross-size comparison on the current test set (Section 5.5). The article reports 3B-r16 achieved ROUGE-L 0.3776 versus 0.3615 for 7B-r4, and BERTScore-F1 0.8606 versus 0.8579, which the authors note is relevant for local deployment under limited resources.

> "Its ROUGE-L score of 0.3776 exceeded the 0.3615 achieved by 7B-r4. Its BERTScore-F1 of 0.8606 likewise exceeded the 0.8579 of 7B-r4."

## Discussion


## Related Claims
- [Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement](bootstrap-stability-lora-gains-7b-r4-rouge1.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters](lora-rank-diminishing-parameter-efficiency-returns.md) — related
