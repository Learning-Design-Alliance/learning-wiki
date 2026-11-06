---
type: claim
title: "The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset"
description: "The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset"
id: jointbdoe-decoupled-yolov11x-mebow-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
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

# The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the original MEBOW benchmark, the decoupled YOLOv11x variant of JointBDOE achieved a mean absolute error of 10.631° and 48.7% accuracy within the 5° error range. [→ Chen Yuqing 2025](#chen-yuqing-2025)

## Evidence

### Chen Yuqing 2025

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Numerical benchmark evaluation on the original MEBOW dataset (54,007 annotated images) comparing decoupled-head YOLO variants. The article reports the Decoupled-YOLOv11x model "achieved even better performance", with MAE of 10.631° and 48.7% accuracy within 5°. No effect size is printed.

> "The results showed that the Decoupled-YOLOv11x model achieved even better performance, reducing the mean absolute error of direction estimation to 10.631° and increasing the accuracy within 5° error range to 48.7%."

## Discussion


## Related Claims
- [A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones](decoupled-head-improves-orientation-estimation.md) — related
- [JointBDOE achieves accuracy comparable to MEBOW at faster processing speed under the same baseline detection framework](jointbdoe-comparable-accuracy-faster-speed.md) — a broader claim this one bears on
- [On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°](jointbdoe-robustness-reconstructed-mebow.md) — related
