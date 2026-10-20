---
type: claim
title: LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model
description: LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model
id: lora-improves-structured-instructional-output-stability
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
    kind: causal
    rigour: 2
  - id: shaowen-lu-2026-2
    resource: "https://arxiv.org/abs/2609.13918"
    title: "Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918"
    author: Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` LoRA fine-tuning substantially increased coverage of the Solution and Method structural markers relative to base models. [→ Shaowen Lu 2026](#shaowen-lu-2026)
`q2 i?` Improvements in Teaching Points coverage varied with model size, with wider intervals and lower stability for some 3B settings and more pronounced improvements for 7B models. [→ Shaowen Lu 2026 (2)](#shaowen-lu-2026-2)

## Evidence

### Shaowen Lu 2026

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918 [doi:10.48550/arxiv.2609.13918](https://doi.org/10.48550/arxiv.2609.13918)

`q2 · i?` · `causal · r2`

Structured-output analysis of generated responses on the 54-item test set, measuring has_solution, has_method, and has_teaching_points coverage rates. The article reports 3B base Solution coverage was 0 and Method coverage 0.13, and "Both reached 1.00 at r= 8 and r= 16 ."

> "For the 3B base model, Solution coverage was 0 and Method coverage was only 0.13. Both reached 1.00 at r= 8 and r= 16 ."

### Shaowen Lu 2026 (2)

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918

`q2 · i?` · `causal · r2`

Paired bootstrap analysis of Teaching Points coverage gains (Fig. 5). The article reports that "Improvements in Teaching Points coverage varied with model size," with some 3B settings less stable than 7B settings.

> "Improvements in Teaching Points coverage varied with model size. Some 3B settings had wider confidence intervals and lower stability, whereas improvements were more pronounced for the 7B models."

## Discussion


## Related Claims
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters](lora-rank-diminishing-parameter-efficiency-returns.md) — related
- [Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement](bootstrap-stability-lora-gains-7b-r4-rouge1.md) — related
