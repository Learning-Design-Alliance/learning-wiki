---
type: claim
title: Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging
description: Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging
id: rec-cbm-ablation-components-complementary
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chengshuai-zhao-2025
    resource: "https://github.com/scott-f-zhang/REC-CBM"
    title: "Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM"
    author: Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Dropping RACE is the most damaging single removal, consistent with per-rubric concept queries carrying most of the discriminative evidence. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Ablation results showing RACE removal is the most damaging single-component removal, with OPCC or LCEC removal yielding smaller but consistent declines. Double-removal variants sit between single-removal variants and Vanilla CBM, producing a monotone trend.

> "Among single removals, dropping RACE is the most damaging, consistent with the claim in §4.1 that per-rubric concept queries carry most of the discriminative evidence; removing OPCC or LCEC yields smaller but consistent declines."

## Discussion


## Related Claims
- [Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact](proprl-ablation-components-contribute.md) — related
- [REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines](rec-cbm-best-task-accuracy-f1-every-backbone.md) — related
- [Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable](rec-cbm-intervention-faithfulness-asymmetry.md) — related
