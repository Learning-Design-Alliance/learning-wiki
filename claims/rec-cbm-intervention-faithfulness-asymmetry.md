---
type: claim
title: Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable
description: Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable
id: rec-cbm-intervention-faithfulness-asymmetry
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
    kind: causal
    rigour: 2
---

# Corrupting rubric evidence flips predicted grade while correcting it preserves or improves grade, demonstrating the bottleneck is actionable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Wrong and Random interventions degrade monotonically, losing 30–45 accuracy points at the largest k on every dataset, while Oracle matches or slightly exceeds None. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `causal · r2`

Human intervention simulation on top-k highest-confidence predicted concepts, replacing them with oracle, wrong, or random labels and re-evaluating the frozen Stage II head (Fig. 5). The article reports Wrong and Random lose 30–45 accuracy points at largest k while Oracle matches or slightly exceeds None.

> "Wrong and Random degrade monotonically, los-ing 30–45 accuracy points at the largestkon every dataset, while Oracle matches or slightly exceeds None. This asym-metry is the key faithfulness signal: corrupting rubric evi-dence flips the predicted grade, whereas correcting it pre-serves or improves the grade."

## Discussion


## Related Claims
- [REC-CBM attains the best task accuracy and macro-F1 within every backbone block across three datasets, improving grading performance over black-box and CBM baselines](rec-cbm-best-task-accuracy-f1-every-backbone.md) — related
- [REC-CBM produces a human-readable decision trace tied to named rubric dimensions, reconstructible from the bottleneck](rec-cbm-decision-trace-reconstructible-bottleneck.md) — related
- [Removing any single REC-CBM component degrades task accuracy on at least two of three datasets, with RACE removal most damaging](rec-cbm-ablation-components-complementary.md) — related
- [REC-CBM lifts concept-level F1 over Vanilla CBM while delivering matching task-side gains on RoBERTa](rec-cbm-lifts-cf1-over-vanilla-cbm-roberta.md) — related
