---
type: claim
title: Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters
description: Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters
id: lora-rank-diminishing-parameter-efficiency-returns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shaowen-lu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.13918"
    title: "Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918 [doi:10.48550/arxiv.2609.13918](https://doi.org/10.48550/arxiv.2609.13918)"
    author: Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: shaowen-lu-2026-2
    resource: "https://arxiv.org/abs/2609.13918"
    title: "Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918"
    author: Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` r=16 produced the largest absolute ROUGE-L gain at both model sizes but was less parameter-efficient than r=4 and r=8. [→ Shaowen Lu 2026](#shaowen-lu-2026)
`q2 i?` Higher LoRA ranks produced lower validation losses at both model sizes, indicating greater adaptation capacity improved fit to course reference answers. [→ Shaowen Lu 2026 (2)](#shaowen-lu-2026-2)

## Evidence

### Shaowen Lu 2026

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918 [doi:10.48550/arxiv.2609.13918](https://doi.org/10.48550/arxiv.2609.13918)

`q2 · i?` · `design · r2`

Parameter-efficiency analysis defining efficiency as ROUGE-L improvement per million adapter parameters (Table 7, Fig. 6). The article reports "r= 16 produced the largest absolute ROUGE-L gain at both model sizes but was less parameter- efficient thanr= 4 andr= 8"; for 7B, gain was +0.0726 at r=8 (0.0144 per million) versus +0.0874 at r=16 (0.0087 per million).

> "Table 7 shows thatr= 16 produced the largest absolute ROUGE-L gain at both model sizes but was less parameter- efficient thanr= 4 andr= 8 ."

### Shaowen Lu 2026 (2)

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918

`q2 · i?` · `design · r2`

Training and validation analysis across six experiments (Table 6, Fig. 2). The article reports the 3B best validation loss decreased from 0.8830 at r=4 to 0.8080 at r=16, and the 7B from 0.7992 to 0.7330, with validation-token accuracy increasing with rank.

> "The best validation loss of the 3B model decreased from 0.8830 at r= 4 to 0.8080 at r= 16 . For the 7B model, it decreased from 0.7992 at r= 4 to 0.7330 at r= 16 ."

## Discussion


## Related Claims
- [Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement](bootstrap-stability-lora-gains-7b-r4-rouge1.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model](lora-improves-structured-instructional-output-stability.md) — related
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](model-size-and-lora-rank-joint-effects.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
