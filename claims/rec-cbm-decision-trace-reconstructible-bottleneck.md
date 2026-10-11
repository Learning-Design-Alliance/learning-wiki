---
type: claim
title: REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck
description: REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck
id: rec-cbm-decision-trace-reconstructible-bottleneck
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

# REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Every quantity in the decision trace is tied to a named rubric dimension, so the grade is reconstructible from the bottleneck and any dimension can be inspected or overridden. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Case study tracing a single Mohler short-answer grading decision by a BERT-backbone REC-CBM whose predicted grade matches the human label with high confidence (Fig. 7). The trace exposes rubric-aware token attention, per-concept ordinal scores with LCEC-corrected posteriors, and additive per-concept contributions.

> "Every quantity in the trace is tied to a named rubric dimension, so the grade is reconstructible from the bottleneck and any dimension can be inspected or overridden, realizing the inspect/verify/intervene workflow motivated in §1."

## Discussion


## Related Claims
- [REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines](rec-cbm-best-task-accuracy-f1-every-backbone.md) — related
- [Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable](rec-cbm-intervention-faithfulness-asymmetry.md) — related
- [REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa](rec-cbm-lifts-cf1-over-vanilla-cbm-roberta.md) — related
