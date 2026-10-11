---
type: claim
title: REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines
description: REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines
id: rec-cbm-best-task-accuracy-f1-every-backbone
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

# REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` REC-CBM attains the best T-Acc and T-F1 within every backbone block across three datasets and five backbones. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Benchmark evaluation on Mohler, ASAP 2.0, and MOCHA datasets with five PLM backbones and three baseline classes (fine-tuned PLMs, prompted LLMs, SOTA CBMs). The article reports REC-CBM "attains the best T-Acc and T-F1 within every backbone block" and best C-F1 in 14 of 15 scenarios.

> "Across three datasets and five backbones, REC-CBM at-tains the best T-Acc and T-F1 within every backbone block, and the best C-F1 in 14 of 15 scenarios, improving the bottleneck alongside the final grade."

## Discussion


## Related Claims
- [REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa](rec-cbm-lifts-cf1-over-vanilla-cbm-roberta.md) — related
- [Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging](rec-cbm-ablation-components-complementary.md) — related
- [Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable](rec-cbm-intervention-faithfulness-asymmetry.md) — related
- [REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck](rec-cbm-decision-trace-reconstructible-bottleneck.md) — related
