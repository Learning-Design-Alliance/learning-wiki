---
type: claim
title: JointBDOE achieves accuracy comparable to MEBOW at faster processing speed under the same baseline detection framework
description: JointBDOE achieves accuracy comparable to MEBOW at faster processing speed under the same baseline detection framework
id: jointbdoe-comparable-accuracy-faster-speed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: chen-yuqing-2025
    resource: "https://doi.org/10.3390/s25206421"
    title: "Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421"
    author: Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# JointBDOE achieves accuracy comparable to MEBOW at faster processing speed under the same baseline detection framework

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under the same detection baseline, JointBDOE matched MEBOW's estimation accuracy while running faster, and its single-stage design avoids the two-stage pipeline's extra computational overhead and error accumulation. [→ Chen Yuqing 2025](#chen-yuqing-2025)

## Evidence

### Chen Yuqing 2025

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Qualitative-plus-quantitative comparison (Figure 8 and Table 4) of the one-stage JointBDOE workflow against the two-stage MEBOW pipeline, with Params/FLOPs reported per model. JointBDOE "achieves comparable estimation accuracy to MEBOW while operating at a faster processing speed". No effect size is printed.

> "The scatter plot in the upper right corner further confirms that, under the same baseline detection framework, JointBDOE achieves comparable estimation accuracy to MEBOW while operating at a faster processing speed."

## Discussion


## Related Claims
- [The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset](jointbdoe-decoupled-yolov11x-mebow-performance.md) — a narrower finding that bears on this claim
- [On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°](jointbdoe-robustness-reconstructed-mebow.md) — a narrower finding that bears on this claim
