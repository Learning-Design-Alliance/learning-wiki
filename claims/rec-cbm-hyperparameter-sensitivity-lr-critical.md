---
type: claim
title: Task F1 saturates by K≈4 concepts and is insensitive to hidden dimension once d≥384, while learning rate forms a sharp inverted-U with collapse at LR≥10−3
description: Task F1 saturates by K≈4 concepts and is insensitive to hidden dimension once d≥384, while learning rate forms a sharp inverted-U with collapse at LR≥10−3
id: rec-cbm-hyperparameter-sensitivity-lr-critical
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
  - id: chengshuai-zhao-2025-2
    resource: "https://github.com/scott-f-zhang/REC-CBM"
    title: "Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM"
    author: Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Task F1 saturates by K≈4 concepts and is insensitive to hidden dimension once d≥384, while learning rate forms a sharp inverted-U with collapse at LR≥10−3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Task F1 saturates by K≈4 on every dataset and is insensitive to d once d≥384, so neither rubric cardinality nor encoder width requires backbone-specific tuning. [→ Chengshuai Zhao 2025](#chengshuai-zhao-2025)
`q2 i?` The learning rate is the only stability-critical knob, forming a sharp inverted-U with a peak in [10−5,10−4] and uniform collapse to near-zero F1 once LR≥10−3. [→ Chengshuai Zhao 2025 (2)](#chengshuai-zhao-2025-2)

## Evidence

### Chengshuai Zhao 2025

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Parameter analysis sweeping number of concepts K, hidden dimension d, and learning rate across four backbones on all three datasets, reporting task F1 in Fig. 4. The article reports task F1 saturates by K≈4 and is insensitive to d once d≥384.

> "task F1 saturates byK≈4on every dataset and is insen-sitive todonced≥384, so neither the rubric cardinal-ity nor the encoder width requires backbone-specific tuning."

### Chengshuai Zhao 2025 (2)

Chengshuai Zhao, Fan Zhang, Kumar Satvik Chaudhary, Yiwen Li, Lo Pang-Yun Ting, Ying-Chih Chen, Huan Liu. (2025). REC-CBM: Rubric-Aware Error-Correction Concept Bottleneck Models for Trustworthy Open-Ended Grading. https://github.com/scott-f-zhang/REC-CBM

`q2 · i?` · `design · r2`

Parameter analysis across backbones showing learning rate forms a sharp inverted-U with peak in [10−5,10−4] and uniform collapse to near-zero F1 once LR≥10−3. The article attributes this to Stage I jointly updating encoder, queries, and concept classifiers.

> "The learning rate is the only stability-critical knob, form-ing a sharp inverted-U across backbones with a peak in[10−5,10−4]and a uniform collapse to near-zero F1 onceLR≥10 −3."

## Discussion


## Related Claims
- [ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit](proprl-hyperparameter-sensitivity.md) — related
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related
