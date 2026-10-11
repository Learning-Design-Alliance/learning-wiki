---
type: claim
title: REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa
description: REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa
id: rec-cbm-lifts-cf1-over-vanilla-cbm-roberta
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

# REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On RoBERTa, REC-CBM lifts C-F1 by +3.5/+4.6/+1.4 points over Vanilla CBM on the three datasets while delivering matching task-side gains. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Main results comparison on RoBERTa backbone across Mohler, ASAP 2.0, and MOCHA. The article reports REC-CBM lifts C-F1 by +3.5/+4.6/+1.4 points over Vanilla CBM while delivering matching task-side gains, showing accuracy and interpretability move together.

> "on RoBERTa, REC-CBM lifts C-F1 by +3.5/+4.6/+1.4points over Vanilla CBM on the three datasets while delivering matching task-side gains."

## Discussion


## Related Claims
- [REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines](rec-cbm-best-task-accuracy-f1-every-backbone.md) — related
- [Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable](rec-cbm-intervention-faithfulness-asymmetry.md) — related
- [REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck](rec-cbm-decision-trace-reconstructible-bottleneck.md) — related
