---
type: claim
title: "Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement"
description: "Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement"
id: bootstrap-stability-lora-gains-7b-r4-rouge1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
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
---

# Bootstrap stability of LoRA gains is not uniform: the ROUGE-1 confidence interval crossed zero at 7B-r4, so that increase is a trend rather than a stable improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The paired bootstrap 95% confidence interval for ROUGE-1 improvement crossed zero at 7B-r4, unlike most other settings. [→ Shaowen Lu 2026](#shaowen-lu-2026)

## Evidence

### Shaowen Lu 2026

Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918 [doi:10.48550/arxiv.2609.13918](https://doi.org/10.48550/arxiv.2609.13918)

`q2 · i?` · `causal · r2`

Paired bootstrap robustness analysis (B=10,000 resamples of the 54-item test set; Fig. 4). The article reports the ROUGE-1 interval crossed zero at 7B-r4 while 7B intervals for all three ROUGE metrics were above zero at r=8 and r=16.

> "In contrast, the confidence interval for ∆ROUGE-1 crossed zero at 7B-r4. The ROUGE-1 increase at that setting should therefore be interpreted as a trend and was less stable than the improvements under the other settings."

## Discussion


## Related Claims
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](model-size-and-lora-rank-joint-effects.md) — related
- [Increasing LoRA rank raises absolute ROUGE-L gains but produces diminishing returns in performance per million adapter parameters](lora-rank-diminishing-parameter-efficiency-returns.md) — related
- [LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model](lora-improves-structured-instructional-output-stability.md) — related
