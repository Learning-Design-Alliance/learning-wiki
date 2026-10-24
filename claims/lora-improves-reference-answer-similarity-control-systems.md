---
type: claim
title: LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes
description: LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes
id: lora-improves-reference-answer-similarity-control-systems
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
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

# LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` LoRA-fine-tuned Qwen2.5 models outperformed their corresponding base models on most ROUGE and BERTScore metrics on the 54-item test set. [→ Shaowen Lu 2026](#shaowen-lu-2026)
`q2 i?` Paired bootstrap 95% confidence intervals for ROUGE improvements lay entirely above zero at most settings, indicating stable gains. [→ Shaowen Lu 2026 (2)](#shaowen-lu-2026-2)

## Evidence

### Shaowen Lu 2026

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918 [doi:10.48550/arxiv.2609.13918](https://doi.org/10.48550/arxiv.2609.13918)

`q2 · i?` · `causal · r2`

Test-set comparison of base and LoRA-fine-tuned Qwen2.5-3B and 7B models on 54 unseen course questions under identical prompts and deterministic decoding, reported via ROUGE-1/2/L and BERTScore-F1. The article reports that "The LoRA-fine-tuned models outperformed their corresponding base models on most metrics."

> "The LoRA-fine-tuned models outperformed their corresponding base models on most metrics. Fine-tuning on course data therefore increased both lexical overlap and semantic proximity to the reference answers."

### Shaowen Lu 2026 (2)

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918

`q2 · i?` · `causal · r2`

Paired bootstrap resampling (B=10,000 iterations over the 54-item test set) of ROUGE gains of fine-tuned over base models. The article reports that for the 3B model "the confidence intervals for ROUGE-1, ROUGE-2, and ROUGE-L were above zero" at all three ranks.

> "For the 3B model, the confidence intervals for ROUGE-1, ROUGE-2, and ROUGE-L were above zero at r= 4 , r= 8 , and r= 16 ."

## Discussion


## Related Claims
- [Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement](bootstrap-stability-lora-gains-7b-r4-rouge1.md) — related
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](model-size-and-lora-rank-joint-effects.md) — related
- [LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model](lora-improves-structured-instructional-output-stability.md) — related
- [Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters](lora-rank-diminishing-parameter-efficiency-returns.md) — related
- Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline — related
- [Adaptation gains grow monotonically with model capacity under the same LoRA recipe, though three data points cannot establish a scaling law](adaptation-gains-grow-with-model-capacity.md) — related
- [LoRA adaptation significantly increases closed-book accuracy on the PhysicsMate test set at all three Qwen3 scales](lora-adaptation-raises-bengali-physics-qa-accuracy-all-scales.md) — related
- [Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)](manova-cluster-effect-text-metrics.md) — related
